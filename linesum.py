import fileinput
import hashlib

h = hashlib.sha256()
for line in fileinput.input():
    h.update(line)
    print '%s %s' % (h.hexdigest()[:4], line),
