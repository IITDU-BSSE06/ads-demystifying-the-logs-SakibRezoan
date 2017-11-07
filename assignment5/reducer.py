#!/usr/bin/python

import sys

urls = {}

for line in sys.stdin:
    if line in urls:
	urls[line] = urls[line]+1
    else:
	urls[line] = 1

print len(urls)
