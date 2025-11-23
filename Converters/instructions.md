# How to Use the STAR Voting Converter

This Python script converts ranked ballots (e.g., A>B) into STAR Voting scores (0-5).
## Input Syntax
Define your ballots using a simple text string.

### Ranks
Use greater than **>** to separate candidates. Example: Alice > Bob > Carol

### Ties
Use equal character **=** to indicate a tie (requires strict=False).
Example: Alice = Bob > Carol

### Multipliers
Prefix a line with N: to count it N times. Example: 5: Alice > Bob (This counts as 5 ballots)

### Comments
Use # for notes / comments.

Example: A > B # This is a comment

### Compressed option
You can set compressed=True to aggregate identical ballots in the output.

## How to Run
The script currently runs test cases defined at the bottom of the file.

Open star_ballot_converter.py.

Scroll to the bottom if __name__ == "__main__": section.

Create a variable with your ballot data:
```
my_ballots = """
A > B > C
5: C > B > A
"""
```

run_example("My Election", my_ballots, strict=True, rule='High', compressed=True)


Run the script in your terminal:

python star_ballot_converter.py


## Output Options

**Compressed Output** (compressed=True):

Aggregates identical ballots and scores using the N: prefix.

Useful for large datasets or summarizing results.

Note: Comments from the input are not preserved in the reconstructed "Ranks" display when compressed mode is active.

**Standard Output (compressed=False)**: echoes the input exactly as provided (including comments).

Lists every score row individually.

**Scoring Logic** (Top-Anchored)
```
1st Rank: 5 points
2nd Rank: 4 points
...
6th Rank and lower: 0 points
Unranked candidates: 0 points
```