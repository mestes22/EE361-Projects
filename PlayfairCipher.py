from collections import OrderedDict
#Keyword used in table
keyword = 'applecrisp'
#Eliminates any duplicates and places back in order
keyword = "".join(OrderedDict.fromkeys(keyword))
#Treats i=j condition
if 'j' in keyword:
    alphabet = 'abcdefghjklmnopqrstuvwxyz'
elif 'i' in keyword:
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
else:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 0
#Creates a string with keyword and alphabet values
while len(keyword) < 25:
    if alphabet[count] not in keyword:
        keyword += alphabet[count]
    count += 1
#Creates a 5x5 'table'
table = [keyword[i:i+5] for i in range(0,len(keyword),5)]
#Word to be encrypted
secret = 'pa'

#Encryption function
def encrypt(secret,table):
    past_letter = ''
    new_secret = ''
    #Adds x's to seperate duplicats and make length even
    for ind in range(len(secret)):
        letter = secret[ind]
        if ind != 0:
            past_letter = secret[ind-1]
        if letter == past_letter:
            new_secret += 'x'
        new_secret += secret[ind]
    if len(new_secret) % 2 != 0:
        new_secret += 'x'
    #Turns string into array to be indexed
    secret_arr = ([new_secret[i:i+1] for i in range(0,len(new_secret),1)])
    positions = ''
    #Gets row and column position for each letter in table
    for ind in range(len(secret_arr)):
        check_letters = secret_arr[ind]
        for ind3 in range(5):
            if check_letters in table[ind3]:
                positions += str(ind3) + str(table[ind3].index(check_letters))
    enc = ''
    #Encrypts the secret word/phrase
    for ind in range(len(positions)):
        if ind % 4 == 0:
            row1 = int(positions[ind])
            col1 = int(positions[ind + 1])
            row2 = int(positions[ind + 2])
            col2 = int(positions[ind + 3])
            #Same Column
            if col1 == col2:
                enc += table[row1-4][col1] + table[row2-4][col1]
            #Same Row
            elif positions[ind] == positions[ind+2]:
                enc += table[row2][col1-4] + table[row2][col2-4]
            #Box Method
            else:
                enc += table[row1][col2] + table[row2][col1]
    return enc

def decrypt(enc,table):
    #Creates array from encrypted values
    decrypt_arr = ([enc[i:i + 1] for i in range(0, len(enc), 1)])
    positions = ''
    #Gets row and column position for each letter in table
    for ind in range(len(decrypt_arr)):
        check_letters = decrypt_arr[ind]
        for ind3 in range(5):
            if check_letters in table[ind3]:
                positions += str(ind3) + str(table[ind3].index(check_letters))
    dec = ''
    #Decrypts encrypted word
    for ind in range(len(positions)):
        if ind % 4 == 0:
            row1 = int(positions[ind])
            col1 = int(positions[ind+1])
            row2 = int(positions[ind+2])
            col2 = int(positions[ind+3])
            #Same Col
            if col1 == col2:
                dec += table[row1-1][col1] + table[row2-1][col1]
            #Same Row
            elif positions[ind] == positions[ind+2]:
                dec += table[row2][col1-1] + table[row2][col2-1]
            #Box Method
            else:
                dec += table[row1][col2] + table[row2][col1]
    return dec

#Runs functions
enc = encrypt(secret, table)
dec = decrypt(enc,table)

#Displays output
print(enc,dec)

#Test Cases

#Keyword = applecrisp

#Test 1:
#Secret = the tea is very hot
#Encrypted = qkbycpsbyabvgqqy
#Decrypted = theteaisveryhotx

#Test 2:
#Secret = my ankle hurts
#Encrypted = kzrvhelkndqb
#Decrypted = myanklehurts

#Test 3:
#Secret = where did my laptop go
#Encrypted = xgabcbsrkzepeowiow
#Decrypted = wheredidmylaptopgo