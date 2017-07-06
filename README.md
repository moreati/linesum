# Linesum

Have you ever needed to compare two files on two disconnected computers, and had to do it by eye? Then read on.

`linesum.py` is a short script that prints each line of a file, plus a running digest. If any line differs between the two files, then that line's digest plus every following digest will also be different. This makes it much easier to spot (and correct) typos than just by eyeball.

The script only requires Python 2.x. It's short enough to type out by hand. Then run a it like so

```
$ python linesum.py < linesum.py 
11b7 import fileinput
ca5b import hashlib
12e1 
2314 h = hashlib.sha256()
f1b3 for line in fileinput.input():
7b0f     h.update(line)
db6c     print h.hexdigest()[:4], line,
```

## Why not use `diff`?

If you can use `diff`, then you should. `linesum.py` is for those occasions you can't reach both the files from one system, e.g. when there's an airgap.

## Why not just do it by eye?

Spotting small differences side by side is slow and error prone. Spotting them with `linesum.py` is merely slow.

However, if you can superimpose the files and flick between them, then your eye is much better at locating differences. For this to work effectively it's important to

- display both files with the same version of your editor
- using the same fonts
- using the same highlighting
- using the same window size.

Quickly switch between each copy (e.g. using a keyboard shortcut). Alternatively you might print out the files, align each page and hold them up to a bright light.

This technique is known as [blink comparison](https://en.wikipedia.org/wiki/Blink_comparator). Historically it was used by astronomers to spot planets and comets.

## Could you add feature \<x\>?

Maybe, but `linesum.py` is designed to reach parts that `pip install` can't. Having a very low character count is a major feature - people sometimes have to type the script in by hand. If you have suggestions or requests, please file a bug or send a pull request.
