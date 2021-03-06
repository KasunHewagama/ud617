#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want element 4 (cost), we use the line number as a key
# We need to write them out to standard output, separated by a tab

import sys

count_line = 1 # line number
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(count_line, cost)
    count_line += 1

