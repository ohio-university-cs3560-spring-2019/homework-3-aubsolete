#
#   Name: Aubree Dix
#   Date: 2/26/19
#   Assignment: HW #5
#

import os

# Initialize the tracker for words, lines, and chars in all files.
total_words = 0;
total_chars = 0;
total_lines = 0;

# Obtain the current working directory
path = os.getcwd();

# Use CWD to access its files
for files in os.listdir(path):
    # Try provides a safety net against hidden non-files such as .git
    try:
        with open(files) as a_file:
            # for loop for lines
            for a_line in a_file:
                # for loop for words within lines
                for words in a_line:
                    if words.find(" "):
                        total_words += 1;
                total_chars += len(a_line.split());
                if a_line.find("\n"):
                    total_lines += 1;
    except:
        print("Not an accessible file.");

# Output
print("Total lines in CWD: ");
print(total_lines);
print("Total words in CWD: ");
print(total_words);
print("Total characters in CWD: ");
print(total_chars);
