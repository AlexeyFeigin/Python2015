#!/usr/bin/python2.7
from itertools import *
import sys

def main():
    ls = []
    for _, lines in groupby(open(sys.argv[1]),
                            lambda s:       s.startswith('sage:')
                                      or    s.startswith('...  ') ):
        lines = [
            '\n' if line == 'sage: #\n' else line
            for line in lines
        ]
        ls.append(''.join(lines))
    print '\n'.join(ls)

main()
