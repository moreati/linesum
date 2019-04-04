# Linesum

Have you ever needed to compare two files on two disconnected computers, when your only option is doing by eyeball? Then read on.

`linesum.py` is a short script that prints each line of a file, plus a running digest. If a line differs between the two files, then that line's digest plus every following digest will also be different. This makes it much easier to spot (and correct) than by a purely visual comparison.

The script just needs Python 2.x or 3.x. It's short enough to type out by hand.

Run it like so

```
$ python linesum.py < linesum.py 
6aaa from __future__ import print_function
527c import fileinput, hashlib
907d 
10bf h = hashlib.sha256()
4f25 for line in fileinput.input(mode='rb'):
c18b     h.update(line)
e151     print(h.hexdigest()[:4], line.decode('utf-8'), end='')
```

## Why not use `diff`?

If the files you are comparing can both be reached on one system then you should use `diff`. `linesum` is for when there's an airgap, and you cannot get the files togther in order to run a diff.

## Why not just do it by eye?

If you can print out the files, or overlay them on the same screen then your eyes have a good chance of spotting any differences. This technique is know as *blink diff* and it's long been used by astronomers to find planets and asteroids. If you cannot get the files on the same screen, then `linesum.py` will be more reliable.

## Could you add feature \<x\>?

Maybe, but having a very low character count is a major feature - people sometimes have to type this in by hand. `linesum.py` reaches parts that `pip install` can't. Please file a bug or send a pull request with your ideas.
