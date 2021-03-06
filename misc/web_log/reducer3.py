#!/usr/bin/python

import sys

count = 0
oldKey = None
bestKey = None
bestCount = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the request, val is 1

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]

    if oldKey and oldKey != thisKey:
	if count>bestCount:
		bestKey = oldKey
		bestCount = count # update best entry
        oldKey = thisKey;
        count = 0

    oldKey = thisKey
    count += 1

# process last key
if oldKey != None:
    if count>bestCount:
        bestKey = oldKey
        bestCount = count # update best entry

print bestKey, "\t", bestCount

