import csv
import re
from io import StringIO
from copy import deepcopy
import json
import sys
import itertools
from collections import defaultdict


def format_percent(count, total):
    return f'{round(100 * count / total)}%'


def load_ballots_from_file(filename):
    """
    SIMPLE STAR format examples
    n,A,B,C
    2,0,2,5
    3,5,4,3

    n:A,B,C
    2:0,2,5
    3:5,4,3

    A   B   C
    0   2   5
    5   4   3
    """
    
    # Parse SIMPLE STAR as CSV
    valid_delims = ['\s', ':', ',']
    # https://stackoverflow.com/questions/2785755/how-to-split-but-ignore-separators-in-quoted-strings-in-python
    # https://regexr.com/69a27
    PATTERN = re.compile(f'''[{"".join(valid_delims)}][\s]*(?=(?:[^'"]|'[^']*'|"[^"]*")*$)''')
    def clean_line(line):
        line = line.replace('\n', '')
        return ','.join(re.split(PATTERN, line))

    with open(filename, 'r') as f:
        lines = list(clean_line(l) for l in f.readlines() if l != '\n' and l[0] != '#')
        csv_f = StringIO('\n'.join(lines))

    # Load CSV
    ballots = []
    rows = csv.reader(csv_f)
    is_weighted = None
    for i, row in enumerate(rows):
        if i == 0:
            is_weighted = row[0] == 'Number_of_Ballots'
            candidates = row[1:] if is_weighted else row
        else:
            ballot_count = int(row[0]) if is_weighted else 1
            scores = row[1:] if is_weighted else row
            scores = list(int(s) for s in scores)
            for _ in range(ballot_count):
                ballots.append(scores)

    return candidates, ballots


def get_runoff_counts(ballots, valid_candidates=None):
    counts = [0] * len(ballots[0])
    if valid_candidates is None:
        valid_candidates = set(range(len(candidates)))

    for ballot in ballots:
        top_candidates = []
        top_candidate_score = -1
        for candidate, score in enumerate(ballot):
            if candidate not in valid_candidates:
                continue

            if top_candidate_score < score:
                top_candidates = [candidate]
                top_candidate_score = score
            elif len(top_candidates) > 0 and top_candidate_score == score:
                top_candidates.append(candidate)

        # Condition 1: len(top_candidates) == 1
        ### FPTP: More than 1 top candidate is impossible
        ### RCV:  More than 1 top candidate is impossible
        ### STAR: Vote is discarded as "no preference" when there are multiple top candidates

        # Condition 2: top_candidate_score > 0
        ### FPTP: Valid ballots should have someone selected, so this scenario is impossible
        ### RCV: This can happen in a exhausted ballot scenario, in which case it should be discarded
        ### STAR: It's impossible to meet this criteria without failing condition 1

        if len(top_candidates) == 1 and top_candidate_score > 0:
            counts[top_candidates[0]] = counts[top_candidates[0]] + 1

    rankings = sorted(list(valid_candidates), key=lambda candidate: counts[candidate], reverse=True)
    return counts, rankings


def get_sum_counts(ballots):
    counts = [0] * len(ballots[0])
    for ballot in ballots:
        for i, stars in enumerate(ballot):
            counts[i] = counts[i] + int(stars)

    rankings = sorted(list(range(len(counts))), key=lambda candidate: counts[candidate], reverse=True)
    return counts, rankings


def print_plurality_results(candidates, ballots):
    counts, rankings = get_runoff_counts(ballots)
    print(f"# PLURALITY: {candidates[rankings[0]]}")
    print(f"\t## Counts")
    for c_index in rankings:
        print(f'\t{candidates[c_index]}: {counts[c_index]} ({format_percent(counts[c_index], len(ballots))})')
    print()


def print_irv_results(candidates, ballots):
    counts, rankings = get_runoff_counts(ballots)
    rounds = [(counts, rankings)]
    valid_candidates = set(list(range(len(candidates))))

    while max(counts) < (len(ballots) / 2):
        valid_candidates.remove(rankings[-1]) 
        counts, rankings = get_runoff_counts(ballots, valid_candidates=valid_candidates)
        rounds.append((counts, rankings))

    winning_candidate_index = counts.index(max(counts))
    print(f"# IRV: {candidates[winning_candidate_index]}")
    for i, round_pair in enumerate(rounds):
        counts = round_pair[0]
        rankings = round_pair[1]
        print(f"\t## Round {i + 1} Counts")
        for c_index in rankings:
            print(f'\t{candidates[c_index]}: {counts[c_index]} ({format_percent(counts[c_index], len(ballots))})')
        print()


def print_star_results(candidates, ballots):
    ## Sum all ballots
    sum_counts, sum_rankings = get_sum_counts(ballots)

    ## Automatic Runoff
    runoff_counts, runoff_rankings = get_runoff_counts(ballots, valid_candidates=sum_rankings[:2])

    ## Display Results
    print(f"# STAR: {candidates[runoff_rankings[0]]}")
    
    print(f"\t## Sums")
    for c_index in sum_rankings:
        print(f"\t{candidates[c_index]}: {sum_counts[c_index]} (avg: {round(100 * sum_counts[c_index] / len(ballots)) / 100})")
    print()

    print(f"\t## Runoff")
    for c_index in sum_rankings[:2]:
        print(f"\t{candidates[c_index]}: {runoff_counts[c_index]} ({format_percent(runoff_counts[c_index], len(ballots))})")
    no_pref_count = len(ballots) - runoff_counts[runoff_rankings[0]] - runoff_counts[runoff_rankings[1]]
    print(f"\tNo Preference: {no_pref_count} ({format_percent(no_pref_count, len(ballots))})")

    print()


def print_concordant_matrix(candidates, ballots):
    '''
    Example
        expected results - report:
        # of voters who prefer  A B C
        A over                  - 3 3
        B over                  2 - 3
        C over                  2 2 -
    '''

    def try_bold(s, count1, count2): # the bold effect didn't look super good, so I'm disabling it
        return s
        """
        if count1 > count2:
            return f'\033[1m{s}\033[0m'
        else:
            return s
        """

    ## c1 prefered over c2
    pref_count = [['-' if c1 == c2 else 0 for c2 in range(len(candidates))] for c1 in range(len(candidates))]

    for c1 in range(len(candidates)):
        for c2 in range(c1+1, len(candidates)):
            counts, _ = get_runoff_counts(ballots, valid_candidates=[c1, c2])

            pref_count[c1][c2] = counts[c1] 
            pref_count[c2][c1] = counts[c2]


    col_width = max([len(c) for c in candidates] + [len("Prefers")]) + 3
    print('# CONCORDANT MATRIX')
    print('\tPrefers'.ljust(col_width+len(' over')) + ''.join(c.ljust(col_width) for c in candidates))
    for row_can, row_name in enumerate(candidates):
        prefix = f'\t{row_name} over'.ljust(col_width+len(' over'))
        print(prefix + ''.join(
                try_bold(str(count).ljust(col_width), count, pref_count[col_can][row_can])
                for col_can, count in enumerate(pref_count[row_can])
            )
        )


if __name__ == '__main__':
    candidates, ballots = load_ballots_from_file(sys.argv[1]) 

    print_plurality_results(candidates, ballots)

    print_irv_results(candidates, ballots)

    print_star_results(candidates, ballots)

    print_concordant_matrix(candidates, ballots)
