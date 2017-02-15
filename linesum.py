import fileinput
import hashlib

h = hashlib.sha256()
for line in fileinput.input():
    h.update(line)
    print h.hexdigest()[:4], line,
