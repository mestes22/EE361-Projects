import sys
#Takes in second argument from command line (Where filename goes)
file_name = sys.argv[1]
#Opens file as readable
file_object = open(file_name,'r')
#Reads file into variable and turns into a list
words = file_object.read()
words = words.replace('\n',' ')
#Put words into array for easy indexing
words = words.split(' ')
words = list(filter(None, words))
print(words)
#Initializes variable to be used in while loop
e='S'
#Dictionary chosen to store keywords with values
storage = {}
#List used to store multiple strings for the values in the dict
values = []

#Runs untill user enters Q
while e != 'Q':
     keyword = input('Enter Keyword: ')
     if keyword == 'Q':
         e = 'Q'
     else:
        #Finds all indexes of keyword in the list of words
        ind = [i for i, x in enumerate(words) if x == keyword]
        #Loops through each index/ appends on position to avoid indexing out of range
        for c in range(len(ind)):
            if ind[c] >= 2 and ind[c] <= len(words) - 3:
                values.append(words[ind[c]-2] + ' ' + words[ind[c]-1] + ' ' + words[ind[c]] + ' ' + words[ind[c]+1] + ' ' + words[ind[c]+2])
            elif ind[c] == 0:
                values.append(words[ind[c]] + ' ' + words[ind[c]+1] + ' ' + words[ind[c]+2])
            elif ind[c] == len(words) - 1:
                values.append(words[ind[c]-2] + ' ' + words[ind[c]-1] + ' ' + words[ind[c]])
            elif ind[c] == 1:
                values.append(words[ind[c]-1] + ' ' + words[ind[c]] + ' ' + words[ind[c]+1] + ' ' + words[ind[c]+2])
            else:
                values.append(words[ind[c]-2] + ' ' + words[ind[c]-1] + ' ' + words[ind[c]] + ' ' + words[ind[c]+1])
        #Only adds words that appeared in file values to dict
        if values:
            storage[keyword] = values
        #Outputs values per keyword
        for value in values:
            print(value)
        #Clears values
        values = []
#Outputs dict with each keyword mapped to its values
print(storage)

#Test Cases

#Test 1:
#File = testfile1.txt
#Keyword 1 = is
#This is a test
#Keyword 2 = the
#file for the project. Words
#output to the screen.
#Keyword 3 = This
#This is a

#Test 2:
#File = testfile2.txt
#Keyword 1 = of
#had heard of it before,
#Keyword 2 = he
#doorstep. There he saw something
#not even he could believe.
#Keyword 3 = different.
#something entirely different.

#Test 3:
#File = testfile3.txt
#Keyword 1 = slow
#The slow white fox
#Keyword 2 =sank
#white fox sank under the
#Keyword 3 = Q
#Program Terminates
