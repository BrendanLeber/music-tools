#!/usr/bin/python

# Copyright (C) 2014 Brendan Leber <brendan@brendanleber.com>
#
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar.
#
# See http://www.wtfpl.net/ for more details.

__version__ = "0.1.0"


import argparse
import glob
import pprint
import re


parser = argparse.ArgumentParser(description='Fix track numbers in .tags files.')
parser.add_argument('total', type=int, help='The total number of tracks in the album.')
parser.add_argument('files', nargs='*', help='The files to fix.')
args = parser.parse_args()

#pp = pprint.PrettyPrinter(indent=4)

repl = "\\1\\3/{}\\4".format(args.total)
#pp.pprint(repl)

all_files = []
for f in args.files:
    all_files.extend(glob.glob(f))
#pp.pprint(all_files)

for f in all_files:
    #pp.pprint(f)
    with open (f, 'r') as myfile:
        data = myfile.readlines()

    new_lines = []
    for l in data:
        #pp.pprint(l)
        nl = re.sub('^(TRACKNUMBER=)(0*)(\d+)(\s*)$', repl, l) #, flags=re.DEBUG)
        #pp.pprint(nl)
        new_lines.append(nl)

    #pp.pprint(new_lines)

    #pp.pprint(f)
    with open (f, 'w') as myfile:
        myfile.writelines(new_lines)
