"""
Generate a dconf locks file from file or stdin
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

section = None
for line in f:
    match = re.match(r"^\[(.+)\]$", line)
    if match:
        section = "/{}".format(match.group(1))
        continue
    match = re.match(r"^(.+)=.+$", line)
    if match:
        print "{}/{}".format(section, match.group(1))
        continue
    print
