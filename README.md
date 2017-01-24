# Linesum

Have you ever needed to compare two files on two disconnected computers, when your only option is doing by eyeball? Then read on.

`linesum.py` is a short script that prints each line of a file, along with 4 digits of has output fot that line. This makes it much easier to spot (and correct) lines that differ between two copies. The script only requires Python 2.x and it's short enough to type out by hand. Then run it like so

```
$ python linesum.py < linesum.py 
11b7 import fileinput
3b3e import hashlib
01ba 
6e61 for line in fileinput.input():
df17     print '%s %s' % (hashlib.sha256(line).hexdigest()[:4], line),
```

## Why not use `diff`?

If the files you are comparing can both be reached on ome system then you should use `diff`. `linesum` is for those situations where there is an airgap, and you cannot get the files togther in order to run a diff.

## Why not just do it by eye?

If you can print out the files, or overlay them on the same screen then you eyes have a good chance of spotting any differences. This technique is know as *blink diff* and it's long been used by astronomers to find planets and asteroids. If you cannot get the files on the same screen, then `linesum.py` will be more reliable.

## Could you add feature <x>?

Maybe, but having a very low character count is a major feature - people sometimes have to type this in by hand. `linesum.py` reaches parts that `pip install` can't.
