# STAR_Voting
Goal: simulate STAR Voting Method (Single Winner) - see details at https://www.starvoting.us and https://starview.netlify.app

Two program modes:
a) Random mode: generate random candidates, random voters and random ballots (plus calculate results, logging, etc)
b) Simulation mode: read the file and perform caluclations

The same calculation are performed in both modes.

File format:
- file name is the "Poll_ID" (election name)
  in random mode - file name is: time stamp (e.g. YYYYMMDD_HHMMSS_NNNNN.txt)
  in simulation mode - user can use files ending with TXT or CSV extentions
- first row - candidate names (one character: A, B, C, etc)
- second (subsequent rows) - votes (comma seperated): 0 = worst, 5 = best

Results are stored in a file with the same name - with sufix - "results".

Example file format (three candidates, four voting ballots)
A,B,C
0,5,4
2,5,5
5,0,5
1,2,2

High Level Steps:
- read file (all the files if a directory is provided as argument)
- parse the file(s)
- calucalte results
- produce a log for each step in caluclation in each file
