#!/usr/bin/env python
# coding: utf-8
import sys
itemCount = {}
support = 2

# Define a list of stop words
stop_words = ["the", "and", "of", "a", "in", "to", "is", "it", "that", "for",
              "with", "on", "at", "as", "my", "was", "me", "this", "i", "from",
              "also", "about", "their", "you", "will", "are", "an", "your", "our"]

for line in sys.stdin:
    line = line.strip()
    #parse the key,value from mapper
    item, count = line.split('\t',1)
    #convert count from string to int
    try:
        count = int(count)
    except ValueError:
        #if count is not a number, ignore this line
        continue
    if item not in stop_words:
      #if item already in the dictionary, add the count
      if item in itemCount:
        itemCount[item] = itemCount[item]+count
      #otherwise, create a new key,value in dictionary
      else:
        itemCount[item] = count
#output the desired items
for item in itemCount.keys():
    if itemCount[item] >= support:
        print('%s\t%s' % (item, itemCount[item]))