#!/usr/bin/env python
from random import SystemRandom
import sys
ran = SystemRandom()
words = [x.strip('\n') for x in open('word.list')]

try:
    cnt = int(sys.argv[1])
    num = int(sys.argv[2])
except IndexError:
    print "Usage: python dw.py <count> <length>"
    sys.exit(1)
for i in range(cnt):
    print ' '.join([words[ran.randrange(0,len(words))] for _ in range(num)])
