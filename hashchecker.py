#!/usr/bin/python

# Licence

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                  Version 2, December 2004 

# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 

#  0. You just DO WHAT THE FUCK YOU WANT TO.


from sys import argv
import hashlib

script, filename = argv


# Checking MD5 hash
BLOCKSIZE = 65536
hasher = hashlib.md5()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print"MD5 = ",(hasher.hexdigest())

# Checking SHA-1 hash
BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print"SHA-1 = ",(hasher.hexdigest())


# Checking SHA-256 hash
BLOCKSIZE = 65536
hasher = hashlib.sha256()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print"SHA-256 = ", (hasher.hexdigest())


# Checking SHA-384 hash
BLOCKSIZE = 65536
hasher = hashlib.sha384()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print"SHA-384 = ",(hasher.hexdigest())

# Checking SHA-512 hash
BLOCKSIZE = 65536
hasher = hashlib.sha512()
with open(filename, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print"SHA-512 = ",(hasher.hexdigest())