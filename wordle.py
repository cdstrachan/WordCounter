from collections import Counter
import os, sys

words=[]
c=Counter()
d=Counter()
MAX_ELEMENTS=5

# read file into list
# Source: https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
filename = "source.txt"
with open(os.path.join(sys.path[0], filename)) as file:
    for line in file:
        words.append(line.strip())

print("########### WORDS COUNTED ################")
wordcount=len(words)
lettercount = wordcount * 5
print ("Word count: " + str(wordcount))
print ("Letter count: " + str(lettercount))

# most common letters - read the word as a set, and add to the counter (nifty python feature)
for word in words:
    c.update(set(word))  

print ("########### MOST COMMON LETTERS ###########")
commonletters=c.most_common(MAX_ELEMENTS)
for k in commonletters:
    # convert to percent and print
    print(k[0] + " {:.2f}".format(float(100*k[1])/lettercount) + "%")

# most common letters per position x
#print ("########### MOST COMMON LETTERS PER POSITION ###########")
for i in range(5):
    for word in words:
        d.update(set(word[i]))
    
    print ("########### Most popular in position: " + str(i+1) + " ###########")
    commonpositionletters=d.most_common(MAX_ELEMENTS)
    for k in commonpositionletters:
        # convert to percent and print
        print(k[0] + " {:.2f}".format(float(100*k[1])/wordcount) + "%")
    d.clear()
