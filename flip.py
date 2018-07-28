#!/usr/bin/python
# coding: utf-8
import sys

def f(x):
    d = {
        'a': 'ɐ',
        'b': 'q',
        'c': 'ɔ',
        'd': 'p',
        'e': 'ǝ',
        'f': 'ɟ',
        'g': 'ƃ',
        'h': 'ɥ',
        'i': 'ᴉ',
        'j': 'ɾ',
        'k': 'ʞ',
        'l': 'ן',
        'm': 'ɯ',
        'n': 'u',
        'o': 'o',
        'p': 'd',
        'q': 'b',
        'r': 'ɹ',
        's': 's',
        't': 'ʇ',
        'u': 'n',
        'v': 'ʌ',
        'w': 'ʍ',
        'x': 'x',
        'y': 'ʎ',
        'z': 'z',
        '0': '0',
        '1': '⇂',
        '2': 'ᄅ',
        '3': 'Ɛ',
        '4': 'ㄣ',
        '5': 'ϛ',
        '6': '9',
        '7': 'ㄥ',
        '8': '8',
        '9': '6',
        '.': '˙',
        ',': '\'',
        '?': '¿',
        '!': '¡',
    }
    if x in d:
        return d[x]
    else:
        return x

if len(sys.argv) < 2:
    print "usage: flip.py [text]"
    sys.exit(0)

instr = sys.argv[1].lower()
res = ""
for i in instr:
    res += f(i)

print res.decode('utf8')[::-1].encode('utf8')
