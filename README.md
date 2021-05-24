# STAR_Voting
1) Goal: simulate STAR Voting Method (Single Winner). 

STAR voting is an electoral system for single-seat elections. The name (an allusion to star ratings) stands for "Score then Automatic Runoff", referring to the fact that this system is a combination of Score voting, to pick two finalists with the highest total scores, followed by a "virtual runoff" in which the finalist who is preferred on more ballots wins.

More info at: https://www.starvoting.us

Video: https://www.youtube.com/watch?v=3-mOeUXAkV0

Similar projects:
- https://star.vote
- Java Script https://starview.netlify.app ( https://github.com/Equal-Vote/star-core/tree/master/src )

Assumptions:
- STAR Votings can select a single winner and multi winner election / contest
- This Simulation is focused on a single winner (but it should leave room for future upgrade: multi winner).

2) Two program modes:
a) Random mode: generate random - candidates, voters, ballots (plus calculate results for each file, logging, etc)
b) Simulation mode: read TXT file and perform caluclations

Both modes share the logic to read the file and calculate the results.

3) File format:      
- folder name = election name, contest name (Mayer in City XYZ - election 2025)
- file name = results from a presinct, city, group (or a specific test scenario)
  in random mode - the file name is: time stamp (e.g. YYYYMMDD_HHMMSS_NNNNN.txt)
  in simulation mode - user can use files ending with TXT or CSV extentions
- first row - candidate names (default - one character: A, B, C, etc). 
- second (subsequent rows) - votes (comma seperated): 0 = worst, 5 = best

Subsequent rows should contain numbers (preferences) in the range 0-5 representing the score each voter gave each candidate.

Calculated Results are stored in a folder with a naming convention: add suffix - Time_stamp
File naming convention:
- original files remain in the main folder (contest)
- new files - naming conventions - add suffix:
- <time_stamp> - validation errors
- <time_stmap> - results - details
- <time_stamp> - results - summary
Example:
- test01.txt: test01_validation_errors.txt, test01_details.txt, test01_summary.txt
- test02.txt: test01_validation_errors.txt, test02_details.txt, test02_summary.txt
        
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

7) Calculating results
See link: 
