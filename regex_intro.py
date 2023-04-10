
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
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
