import csv
from copy import deepcopy
import json
import sys


def format_percent(count, total):
    return f'{round(100 * count / total)}%'


# filename = sys.argv[1]
''',A,B,C
2,0,2,5
3,5,4,3
'''

'''expected results - report:
# of voters who prefer  A B C
A over                  - 3 3
B over                  2 - 3
C over                  2 2 -
'''
# Load CSV
ballots = []
with open('file.txt', 'r') as f:
    rows = csv.reader(f)
    for i, row in enumerate(rows):
        if i == 0:
            candidates = row[1:]
        else:
            ballot_count = int(row[0])
            for _ in range(ballot_count):
                ballots.append(row[1:])
# Plurality
counts = [0] * len(candidates)
for ballot in ballots:
    top_candidate = ballot.index(max(ballot))
    counts[top_candidate] = counts[top_candidate] + 1
winning_candidate_index = counts.index(max(counts))
print(f"# PLURALITY: {candidates[winning_candidate_index]}")
total_votes = sum(counts)
print(f"\t## Counts")
for candidate, count in zip(candidates, counts):
    print(f'\t{candidate}: {count} ({format_percent(count, total_votes)})')
print()
# Instant Runoff
counts = [0] * len(candidates)
round_counts = []
counts = [0] * len(candidates)
for ballot in ballots:
    top_candidate = ballot.index(max(ballot))
    counts[top_candidate] = counts[top_candidate] + 1
round_counts.append(counts)
ballot_copies = deepcopy(ballots)
while max(counts) < (total_votes / 2):
    # clear min candidate
    bot_candidate = counts.index(min(counts))
    for ballot in ballot_copies:
        ballot[bot_candidate] = '0'  # I'm choosing string because they're read as string from the csv
    counts = [0] * len(candidates)
    for ballot in ballot_copies:
        top_candidate = ballot.index(max(ballot))
        counts[top_candidate] = counts[top_candidate] + 1
    round_counts.append(counts)
winning_candidate_index = counts.index(max(counts))
print(f"# IRV: {candidates[winning_candidate_index]}")
total_votes = sum(counts)
for i, counts in enumerate(round_counts):
    print(f"\t## Round {i + 1} Counts")
    for candidate, count in zip(candidates, counts):
        print(f'\t{candidate}: {count} ({format_percent(count, total_votes)})')
    print()

# Star
## Sum all ballots
counts = [0] * len(candidates)
for ballot in ballots:
    for i, stars in enumerate(ballot):
        counts[i] = counts[i] + int(stars)
## Get 2 highest (this approach is messy, I'm sure there's a better one)
highest = counts.index(max(counts))
t = counts[highest]
counts[highest] = 0  # removing highest, so that I can find next highest
next_highest = counts.index(max(counts))
counts[highest] = t  # adding highest count back
## Automatic Runoff
highest_count = 0
next_highest_count = 0
for ballot in ballots:
    if ballot[highest] > ballot[next_highest]:
        highest_count = highest_count + 1
    if ballot[highest] < ballot[next_highest]:
        next_highest_count = next_highest_count + 1
no_pref_count = total_votes - highest_count - next_highest_count
if highest_count > next_highest_count:
    winning_candidate_index = highest
else:
    winning_candidate_index = next_highest
print(f"# STAR: {candidates[winning_candidate_index]}")
print(f"\t## Runoff")
print(f"\t{candidates[highest]}: {highest_count} ({format_percent(highest_count, total_votes)})")
print(f"\t{candidates[next_highest]}: {next_highest_count} ({format_percent(next_highest_count, total_votes)})")
print(f"\tNo Preference: {no_pref_count} ({format_percent(no_pref_count, total_votes)})")
print()
print(f"\t## Sums")
for candidate, count in zip(candidates, counts):
    print(f"\t{candidate}: {count} (avg: {round(100 * count / total_votes) / 100})")