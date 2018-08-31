#!/usr/bin/env python2
"""
Sort sections and key/value pairs in output from dconf dump to make comparing easier
"""

import os
import re
import select
import sys

if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
    f = open(sys.argv[1])
elif select.select([sys.stdin,], [], [], 0.0)[0]:
    f = sys.stdin
else:
    sys.exit("No input to read from")

dconf = {}
section = None
for line in f:
    match = re.match(r"^\[.+\]$", line)
    if match:
        section = match.group(0)
        dconf[section] = []
        continue
    match = re.match(r"^(.+)=.+$", line)
    if match:
        dconf[section].append(match.group(0))
        continue

sections = dconf.keys()
sections.sort()
for section in sections:
    print section
    pairs = dconf[section]
    pairs.sort()
    for pair in pairs:
        print pair
    print
