#!/usr/bin/env python
# coding: utf-8
import sys
import re

# Define a list of stop words
stop_words = ["the", "and", "of", "a", "in", "to", "is", "it", "that", "for",
              "with", "on", "at", "as", "my", "was", "me", "this", "i", "from",
              "also", "about", "their", "you", "will", "are", "an", "your", "our"]

#get all lines from stdin
for line in sys.stdin:
  #remove leading and trailing whitespace
  line = line.strip()
  line = line.lower()
  line = re.sub(r'[^\w\s]', '', line)
  #split the line into items
  items = line.split()
  #output (item,1) in tab-delimited format
  for item in items:
    if item not in stop_words:
      print('%s\t%s' % (item,1))