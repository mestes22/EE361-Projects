import operator
def sortWords(word_list, len_word):
    freq_word_list = {}
    for word in word_list:
        if len(word) == len_word:
            freq_word_list[word] = freq_word_list.get(word, 0) + 1
    return sorted(freq_word_list.items(),key=operator.itemgetter(1),reverse=True)