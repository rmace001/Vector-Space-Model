# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:46:48 2019

@author: Rogith
"""
import glob
import string
import re


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

"""
#Initial testing on filtering characters
printable = set(string.printable)
with open('cs172data/file20.txt', 'r') as content_file:
    content = content_file.read()
    cleaned = filter(lambda x: x in printable, content)
    
for word in cleaned:
    print(word)
end test"""


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

"""
#Create/print list of tuples

filepath = 'cs172data/file06.txt'
files = glob.glob(filepath)
fileID = 0
termList = list()
for name in files:
    fileID += 1
    with open(name) as fp:
        for line in fp:
             for word in line.split():
                if word not in stop_words_set:
                    filtered_term = word.translate(translator)
                    x = (filtered_term, fileID)
                    termList.append(x)
                # end if
                    
for item in termList:
    #continue from here
    print(item)
"""


# unit test: print each file to make sure there are no weird strings being encountred
# unit test: use regex search to replace a '-' witha ' ' and split two-word terms
# unit test: create a translator that converts punctuation to None or ""
# function that filters uwantwed characters
def filterSpecialChar(word):
    sChars = [ '\x00' ,'\x00\x00' , '\x00\x00\x00' ]

    if(word not in sChars):
        return True
    else:
        return False

dash = '-'
http = 'http'
translator = str.maketrans( '' , '' , string.punctuation)
filepath = 'cs172data/file04.txt'
files = glob.glob(filepath)
fileID = 0
termList = list()
for name in files:
    fileID += 1
    with open(name) as fp:
        for line in fp:
            words = filter(filterSpecialChar , line.split())
            for word in words:
                if word not in stop_words_set:
                    # check if '-' in word and 'http' not in word
                    if re.search(dash, word) and not re.search(http, word):
                        # replace dash with a space
                        wordSet = word.replace( "-" , " " )
                        # parse each word
                        for term in wordSet.split():
                            filtered_term = term.translate(translator)
                            x = (filtered_term.lower(), fileID)
                            termList.append(x)
                    else:
                        filtered_term = word.translate(translator)
                        x = (filtered_term.lower(), fileID)
                        termList.append(x)
               # end if

for item in termList:
    #continue from here
    print(item)



"""
# unit test: use regex search to replace a '-' witha ' ' and split two-word terms
testword = 'word-test'

if re.search(dash, testword):
    print("test")
    #replace dash with a space
    wordSet = testword.replace( "-" , " " )
    
    #parse each word and add to tmplist
    tmplist = list()
    for term in wordSet.split():
        print(term)
"""




