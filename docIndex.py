# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:46:48 2019

@author: Rogith
"""
import glob
import string
import re
import math
"""
# unit test: code that iterates through a directory of files file by file, line by line,
# word by word
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
"""

"""
#unit test: print contents of files without printing stopwords
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
#unit test: Create/print list of tuples
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

"""
# unit test: check membership of dictionary key
termIndex = dict()
termIndex['yo'] = 23
if 'yo' in termIndex:
    print('true')
if 'he' not in termIndex:
    print('true')
"""

"""
# unit test: append to listvalue of key-value pair 
termIndex = dict()
termIndex['ste'] = [ 1 , 1 ] 
print(termIndex['ste'])
termIndex['ste'].append(0)
print(termIndex['ste'])
"""

"""
# unit test: print each termInvertedIndex
for key in termIndex.items():
    print(key[0]+'->', end =" ")
    for lists in key[1]:
        print(lists)
        # print( '[' + str(lists[0]) + ', ' + str(lists[1]) + ']'  )

for key in docIndex.items():
    print("Doc #" + str(key[0]) + "-> numTerms: " + str(key[1]))
"""



# function that filters uwantwed characters
def filterSpecialChar(word):
    sChars = [ '\x00' ,'\x00\x00' , '\x00\x00\x00' ]

    if(word not in sChars):
        return True
    else:
        return False


# unit test: print each file to make sure there are no weird strings being encountred
# unit test: use regex search to replace a '-' witha ' ' and split two-word terms
# unit test: create a translator that converts punctuation to None or ""
# unit test: open stoplist.txt and store into a set
stop_words_set = set()
path = 'stoplist.txt'
with open(path) as fp:
    for line in fp:
        for word in line.split():
            stop_words_set.add(word.lower())

print(stop_words_set)




docIndex = dict()
dash = '-'
http = 'http'
translator = str.maketrans( '' , '' , string.punctuation)
filepath = 'cs172data/*.txt'
files = glob.glob(filepath)
fileID = 0
termList = list()
for name in files:
    fileID += 1
    with open(name) as fp:
        count = 0
        for line in fp:
            words = filter(filterSpecialChar , line.split())
            for word in words:
                word = word.lower()
                if word not in stop_words_set:
                    # check if '-' in word and 'http' not in word
                    if re.search(dash, word) and not re.search(http, word):
                        # replace dash with a space
                        wordSet = word.replace( "-" , " " )
                        # parse each word
                        for term in wordSet.split():
                            count += 1
                            filtered_term = term.translate(translator)
                            x = (filtered_term, fileID)
                            termList.append(x)
                    else:
                        count += 1
                        filtered_term = word.translate(translator)
                        x = (filtered_term, fileID)
                        termList.append(x)
        docIndex[fileID] = count

def update_term(item, termIndex):
    i = 0
    for listitem in termIndex[item[0]]:
        # if word_fileID == encountered_fileID
        if (item[1] == listitem[0]):
            listitem[1] += 1
            return
        else:
            i += 1
    termIndex[item[0]].append( [item[1] , 1] )
    return

# item = (term, fileID)
termIndex = dict()
for item in termList:
    if item[0] not in termIndex:
        # add term
        twoElemList = [item[1], 1]
        newlist = [twoElemList]
        termIndex[item[0]] = newlist
    else:
        # update term
        update_term(item, termIndex)



def display_term_data(termIndex, docIndex, term):
    print(term + '-> ')
    if term in termIndex:
        for postings in termIndex[term]:
            #what items to i need to compute tf, idf, & tf-idf?
            tf = postings[1]/docIndex[postings[0]] #num_occur/doc_size
            idf = math.log(20/len(termIndex[term]), 2)
            tf_idf = tf*idf
            print('for this posting, tf: ' + str(tf) + ', idf: ' + str(idf) + ', tf-idf: ' + str(tf_idf))
    else:
        print('Term not found')


            

term = 'phone'


s = input()
while s != 'sudoquit':
    print(s)
    display_term_data(termIndex, docIndex, s)
    s = input()




