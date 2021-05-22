# STAR_Voting
Goal: simulate STAR Voting Method (Single Winner) - see details at https://www.starvoting.us,  https://star.vote and https://starview.netlify.app 

Two program modes:
a) Random mode: generate random - candidates, voters, ballots (plus calculate results for each file, logging, etc)
b) Simulation mode: read TXT file and perform caluclations

Both modes share the logic to read the file and calculate the results.

File format:
- file name is the "Poll_ID" (election name)
  in random mode - file name is: time stamp (e.g. YYYYMMDD_HHMMSS_NNNNN.txt)
  in simulation mode - user can use files ending with TXT or CSV extentions
- first row - candidate names (one character: A, B, C, etc)
- second (subsequent rows) - votes (comma seperated): 0 = worst, 5 = best

Calculated Results are stored in a file with the same name - with a sufix - "_results".

High Level Steps:
- read the file (or, all the files in a directory if specified as an argument)
- parse the file(s)
- calucalte results
- produce a log for each step in caluclation in each file

=Input File Format - Specification=
These files are provided to test file parsing and test expected error messages (negatived test cases).

"Input File Format - Positive Test Cases (well formated files)
Positive test cases: Format_P1.txt, Format_P2.txt, etc.

"Input File" format - negative test cases (incorrect file formating and expected error messages): Format_N1.txt, Format_N2.txt, etc

=Expected Results - Unit Test Cases=
Expected results: input file and output files (caluclated results)
test01.txt, test01_results; test02.txt, test02_results.txt
