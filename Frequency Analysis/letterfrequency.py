from removematches import *
from checkword import *
from sortWords import *

def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as wells:
	    return wells.read()

def letterFrequency(text):
    text = text.lower()
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    text = removeMatches(text, nonLetters)
    lCount = {}
    total = len(text)
    for ch in text:    #count each letter's occurrence
        lCount[ch] = lCount.get(ch, 0) + 1
    for ch in lCount:  #calculate percentages
        lCount[ch] = lCount[ch] / total
    return lCount

def getFreq(t):
	 return t[1]    #return second item in the tuple 

def sortByLen(w):
	return len(w)

def maybeAdd(ch, toDict):
	if ch in 'abcdefghijklmnopqrstuvwxyz':
		toDict[ch] = toDict.setdefault(ch, 0) + 1
 
def neighborCount(text):
	nbDict = {}
	text = text.lower()
	for i in range(len(text) - 1):
		nbList = nbDict.setdefault(text[i], {})
		maybeAdd(text[i + 1], nbList)
		nbList = nbDict.setdefault(text[i + 1], {})
		maybeAdd(text[i], nbList)
	return nbDict

plain = readFile('wells.txt')
lf_plain = letterFrequency(plain)
cipher = readFile('cipherText2.txt')
lf_cipher = letterFrequency(cipher)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#1

#Take 4 highest letter frequencies from the plain text and cipher text
lf_plain_list = list(lf_plain.items())
lf_plain_list.sort(key=getFreq,reverse=True)
print('Plain letter frequency:', lf_plain_list[:4])
lf_cipher_list = list(lf_cipher.items())
lf_cipher_list.sort(key=getFreq,reverse=True)
print('Cipher letter frequency:', lf_cipher_list[:4])

#'e' 't' 'a' 'n' are most frequent in plain text
#'g' 'c' 's' 'y' are most frequent in cipher text

#2
pf_plain = neighborCount(plain)
pf_cipher = neighborCount(cipher)

plain_neighbor_list = []
plain_neighbor_list.append(['e: ', sum(pf_plain['e'].values())])
plain_neighbor_list.append(['t: ', sum(pf_plain['t'].values())])
plain_neighbor_list.append(['a: ', sum(pf_plain['a'].values())])
plain_neighbor_list.append(['n: ', sum(pf_plain['n'].values())])
print('\nPlain text neighbors:', plain_neighbor_list)

cipher_neighbor_list = []
cipher_neighbor_list.append(['g: ', sum(pf_plain['g'].values())])
cipher_neighbor_list.append(['c: ', sum(pf_plain['c'].values())])
cipher_neighbor_list.append(['s: ', sum(pf_plain['s'].values())])
cipher_neighbor_list.append(['y: ', sum(pf_plain['y'].values())])
print('Cipher text neighbors:', cipher_neighbor_list)

#E and C have high frequency and number of neighbors
cipher = cipher.replace('c','E')
alphabet = alphabet.replace('e','')

#3
cipher_words = cipher.split()
plain_words = plain.split()
wc_cipher = sortWords(cipher_words, 3)
wc_text = sortWords(plain_words, 3)
print('\nPlain word frequency:', wc_cipher)
print('Cipher word frequency:', wc_text,'\n')

#The is the most common word
#gsE has high frequency and is guessed to be THE
cipher = cipher.replace('g','T')
alphabet = alphabet.replace('t','')
cipher = cipher.replace('s','H')
alphabet = alphabet.replace('h','')

#By examining the list Tz was guessed to be TO
cipher = cipher.replace('z','O')
alphabet = alphabet.replace('o','')

#4

#Checked word list for potential matches

#Three
print(findLetters(alphabet,'THdEE'))
cipher = cipher.replace('d','R')
alphabet = alphabet.replace('r','')

#Towards
print(findLetters(alphabet,'TOmjRnf'))
cipher = cipher.replace('m','W')
alphabet = alphabet.replace('w','')
cipher = cipher.replace('j','A')
alphabet = alphabet.replace('a','')
cipher = cipher.replace('n','D')
alphabet = alphabet.replace('d','')
cipher = cipher.replace('f','S')
alphabet = alphabet.replace('s','')

#Neither
print(findLetters(alphabet,'yEtTHER'))
cipher = cipher.replace('y','N')
alphabet = alphabet.replace('n','')
cipher = cipher.replace('t','I')
alphabet = alphabet.replace('i','')

#Number
print(findLetters(alphabet,'NixoER'))
cipher = cipher.replace('i','U')
cipher = cipher.replace('o','B')
cipher = cipher.replace('x','M')

#Right
cipher = cipher.replace('e','G')

#Up
cipher = cipher.replace('a','P')

#Saying
cipher = cipher.replace('q','Y')

#Bless
cipher = cipher.replace('w','L')

#Count
cipher = cipher.replace('h','C')

#Of
cipher = cipher.replace('l','F')

#Breakfast
cipher = cipher.replace('v','K')

#Anchovies
cipher = cipher.replace('k','V')

#Cipher text completely deciphered
print('\n')
print(cipher)