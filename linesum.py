import fileinput
import hashlib

for line in fileinput.input():
    print '%s %s' % (hashlib.sha256(line).hexdigest()[:4], line),
