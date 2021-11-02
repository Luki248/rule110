#!/usr/bin/env python3

# rule110.py

NUMBER_OF_COLUMNS = 80
NUMBER_OF_ROWS = 100

print("Rule 110")

line = " "*(NUMBER_OF_COLUMNS - 1) + "*"

for i in range(NUMBER_OF_ROWS):
    print(line)
    next_line = " "
    for j in range(1, NUMBER_OF_COLUMNS-1):
        pattern = line[j-1] + line[j] + line[j+1]
        if pattern == "   ":
            next_line += " "
        elif pattern == "  *":
            next_line += "*"
        elif pattern == " * ":
            next_line += "*"
        elif pattern == " **":
            next_line += "*"
        elif pattern == "*  ":
            next_line += " "
        elif pattern == "* *":
            next_line += "*"
        elif pattern == "** ":
            next_line += "*"
        elif pattern == "***":
            next_line += " "
    next_line += " "
    line = next_line