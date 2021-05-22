# STAR_Voting
1) Goal: simulate STAR Voting Method (Single Winner) - see details at https://www.starvoting.us,  https://star.vote and https://starview.netlify.app, https://github.com/Equal-Vote/star-core/tree/master/src

Assumptions:
- STAR Votings can use two ???: single winner and multi winner.
2) Two program modes:
a) Random mode: generate random - candidates, voters, ballots (plus calculate results for each file, logging, etc)
b) Simulation mode: read TXT file and perform caluclations

Both modes share the logic to read the file and calculate the results.

3) File format:
- file name - election name
  in random mode - file name is: time stamp (e.g. YYYYMMDD_HHMMSS_NNNNN.txt)
  in simulation mode - user can use files ending with TXT or CSV extentions
- first row - candidate names (one character: A, B, C, etc)
- second (subsequent rows) - votes (comma seperated): 0 = worst, 5 = best

Calculated Results are stored in a file with the same name - with a sufix - "_results".

4) High Level Steps:
- read the file (or, all the files in a directory if specified as an argument)
- parse the file(s)
- calucalte results
- produce a log for each step in caluclation in each file

5) Input File Format - Specification=
These files are provided to test file parsing and test expected error messages (negatived test cases).

5.1) Input File Format - Positive Test Cases (well formated files)
Positive test cases - file parsing should be sucessful: 
- P1.txt, 
- P2.txt, etc.

5.2) Input File format - Negative Test Cases (files incorrectly formated and expected error messages): 
- N1.txt, N1_errors.txt 
- N2.txt, N2_errors.txt

6) Expected Results - Unit Test Cases
Expected results: input file and output files (caluclated results)
- test01.txt, test01_results.txt
- test02.txt, test02_results.txt
