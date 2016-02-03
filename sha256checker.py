#!/usr/bin/python

# Elasyaf

from sys import argv
import hashlib


print""
print"SHA-256 checker"
print"Just execute 'python sha256checker.py [path to file]' just do it"
print""
print""

script, filename = argv

BLOCKSIZE = 65536
hasher = hashlib.sha256()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())