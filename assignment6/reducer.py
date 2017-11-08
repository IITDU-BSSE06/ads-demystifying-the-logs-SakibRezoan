#!/usr/bin/python

import sys

hits= {}

for line in sys.stdin:
    year = line.strip().split("/")[2]
    
    if "2009" in year:
	hits[hit9] = hits[hit9]+1
    else:
	hits[hit9] = 1

    if "2010" in year:
	hits[hit10] = hits[hit10]+1
    else:
	hits[hit10] = 1

    if "2011" in year:
        hits[hit11] = hits[hit11]+1
    else:
	hits[hit11] = 1

print "2009" + len(hits[hit9])
print "2010" + len(hits[hit10])
print "2011" + len(hits[hit11])
