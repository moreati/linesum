# Linesum

`linesum.py` is a short script that prints each line of a file, plus a running digest. If a line differs between the two files, then that line's digest plus every following digest will also be different. This makes it much easier to spot (and correct) than by a purely visual comparison.

Have you ever needed to compare two files on disconnected computers, when your only option is doing by eyeball? Then read on.

`linesum.py` prints each line of a file, plus a running sha256 digest. If a line differs between the two files, then that line's digest plus every following digest will be different. This makes it much easier to spot any changes.

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
