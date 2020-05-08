import re

def readFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as wells:
        return wells.read()

def text_formatting(plain_text, cipher_text):
    plain_text = re.sub(r'[^a-zA-Z]'," ",plain_text)
    cipher_text = re.sub(r'[^a-zA-Z]'," ",cipher_text)
    plain_text = re.sub(' +', ' ', plain_text)
    plain_text = plain_text.split(' ')
    cipher_text = cipher_text.split(' ')
    return plain_text, cipher_text

def normalized_alphabet(plain_text, cipher_text):
    plain_num = [len(i) for i in plain_text]
    cipher_num = [len(i) for i in cipher_text]
    alphabet = 'abcdefghijkmnopqrstuvwxyz123456789'
    plain_alphabet = [alphabet[num] for num in plain_num]
    cipher_alphabet = [alphabet[num] for num in cipher_num]
    plain_string = ''
    for each in plain_alphabet:
        plain_string += each
    cipher_string = ''
    for each in cipher_alphabet:
        cipher_string += each
    return plain_string, cipher_string

def get_index(plain_string, cipher_string):
    contain = False
    x = len(cipher_string)
    while contain == False:
        contain = cipher_string[0:x] in plain_string
        if contain == True:
            idx = plain_string.find(cipher_string[0:x])
        x -= 10

    return plain_text[idx: idx + len(cipher_text) + 1]

plain_text = readFile('wells.txt')
cipher_text = readFile('cipherText2.txt')

plain_text, cipher_text = text_formatting(plain_text, cipher_text)
plain_string, cipher_string = normalized_alphabet(plain_text, cipher_text)

decrypted = get_index(plain_string, cipher_string)
print(cipher_text)
print(decrypted)