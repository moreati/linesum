from __future__ import print_function
import fileinput, hashlib

h = hashlib.sha256()
for line in fileinput.input(mode='rb'):
    h.update(line)
    print(h.hexdigest()[:4], line.decode('utf-8'), end='')
