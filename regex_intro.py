
# read in a file and search each line for string
# rstrip() is a string method to remove trailing characters/spaces
#
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

# now similar search as above using Regular Expressions

import re

hand = open('mbox-short.txt')
for line in hand:
    #line = line.rstrip()
    # the caret ^ character indicates the match the From at start of line
    #if re.search('^From:', line):
    #    print(line)

    # caret means start of line, dot is any character, asterisk is other characters 0 or more times
    # if re.search('^X.*:', line):
    #     print(line)

    # the characters, \S+ mean to match any non-whitespace char 1 or more times
    if re.search('^X-D\S+:', line):
        print(line)

