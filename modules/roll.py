#!/usr/bin/env python
"""
roll.py - Phenny random roll module
Copyright 2010 Dustin Ho
Licensed under the Eiffel Forum License 2.
"""

import random

def roll(phenny, input):
  """Returns a random number between 1 and the input. Defaults to 1-100"""
  roller = input.nick
  low = 1
  high = 100
  if input.group(2):
    try:
      high = int(input.group(2))
      if high < 1:
        high = 100
    except ValueError:
      high = 100
  num = random.randint(low, high)
  phenny.say(roller + ' rolled: ' + str(num) + ' (1-' + str(high) + ')')
roll.commands = ['roll']
roll.priority = 'high'
roll.example = '.roll'

if __name__ == '__main__':
   print __doc__.strip()
