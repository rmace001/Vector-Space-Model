# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:46:48 2019

@author: Rogith
"""
import glob



"""
unit test: code that iterates through a directory of files file by file, line by line,
word by word

filepath = 'cs172testdata/*.txt'
files = glob.glob(filepath)

for name in files:
    with open(name) as fp:
        for line in fp:
             for word in line.split():
                print(word)
"""

#open stoplist.txt and store into a set
stop_words_set = set()
filepath = 'stoplist.txt'
with open(filepath) as fp:
    for line in fp:
        for word in line.split():
            stop_words_set.add(word)

#unit test: print contents of files without printing stopwords
"""
filepath = 'cs172data/*.txt'
files = glob.glob(filepath)
fileID = 0
for name in files:
    fileID += 1
    print(fileID)
    with open(name) as fp:
        for line in fp:
             for word in line.split():
                if word not in stop_words_set:
                    print(word)
"""
         

