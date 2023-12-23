# NRIC Checksum Python Project
This Python project implements the NRIC checksum algorithm based on the specifications outlined in https://www.ngiam.net/NRIC/NRIC_numbers.ppt. The project consists of three main files: generator.py, validator.py, and bruteforce.py.

## Files
1. generator.py
This file generates a random NRIC number that matches the checksum. It includes a function for generating the checksum for both 'S'/'T' and 'F'/'G' prefixes.

2. validator.py
This file provides a function to validate a given NRIC number. It takes user input for an NRIC and checks its validity based on the checksum.

3. bruteforce.py
This file contains functions for generating all possible combinations of NRIC numbers given the last 4 digits. The results are written to an external text file called nric.txt.

## Usage
To use this project, run the respective Python scripts based on your needs:

Use generator.py to generate a random valid NRIC.
Use validator.py to validate a given NRIC.
Use bruteforce.py to find all valid NRIC combinations based on the last 4 digits.

## Watch the demo:
TBD

## Dependencies
This code requires Python and random. If you have Python and pip, you can get random via

    pip install random

## Issues and Contributions
If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository.

Happy coding!