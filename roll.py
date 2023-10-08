#!/usr/bin/python

import re
import sys

from  models.dice import Dice

if len(sys.argv) > 1:

    m = re.match(r'(\d?)d(\d+)', sys.argv[1])
    if m.groups()[1] == '':
        d = 6
    else:
        d = int(m.groups()[1])

    if m.groups()[0] == '':
        n = 1
    else:
        n = int(m.groups()[0])

    # print('n:', n, 'd:', d, m.groups())
    dice = Dice(d)
    print(dice.roll(n))
    sys.exit(0)


d = Dice(4)
print('d4  :', d.roll())

d = Dice(6)
print('d6  :', d.roll())

d = Dice(10)
print('d10 :', d.roll())

d = Dice(12)
print('d12 :', d.roll())

d = Dice(20)
print('d20 :', d.roll())

d = Dice(100)
print('d100:', d.roll(), "rolls: {}".format(d.rolls))

print()
d = Dice(6)
print('3d6 :', d.roll(3), "rolls: {}".format(d.rolls))

d = Dice(20)
print('5d20:', d.roll(5), "rolls: {}".format(d.rolls))

print()
print('dice:', d)

