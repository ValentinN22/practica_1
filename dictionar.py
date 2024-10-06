import re

def similar_words(word_length, letters_and_patterns, wrong_letters=[], first_letter='',last_letter=''):
    words = []
    dictionar = {x:[] for x in range(4,25)}
    with open('dex.txt', 'r', encoding='utf-8-sig') as file:
        cuvinte = file.read().splitlines()
    for cuvant in cuvinte:
        try:
            dictionar[len(cuvant)].append(cuvant)
        except KeyError:
            pass
    for cuvant in dictionar[word_length]:
        good_word = True
        # elimina cuvintele care nu au literele din cuvantul de completat
        for letter_or_pattern in letters_and_patterns:
            if letter_or_pattern not in cuvant:
                good_word = False
                break
        # elimina cuvintele care au litere gresite incercate deja
        if good_word == True:
            if len(wrong_letters) != 0:
                for letter in wrong_letters:
                    if letter in cuvant:
                        good_word = False
                        break
        # elimina cuvintele care nu incep cu litera de inceput
        if first_letter != '':
            if cuvant[0] != first_letter:
                good_word = False
        
        # elimina cuvintele care nu se termina cu litera de final
        if last_letter != '':
            if cuvant[-1] != last_letter:
                good_word = False        

        # elimina cuvintele care nu au un pattern de litere din cuvantul de completat
        if good_word == True:
            words.append(cuvant)
    # print(words) # -- debug
    return words


def freq_of_letter(words, letters ,wrong_letters = None):
    if wrong_letters is not None:
        letters += wrong_letters
    alfabet = 'AĂÂBCDEFGHIÎJKLMNOPRSȘTȚUVWXYZ'
    for letter in letters:
        if letter in alfabet:
            alfabet = alfabet.replace(letter,'')
    freq_counter = {letter:0 for letter in alfabet}
    alfabet_optimizat = ''
    for word in words:
        for letter in alfabet:
            freq_counter[letter] += word.count(letter)
    sorted_by_freq = sorted(freq_counter.items(),key=lambda x:x[1])
    sorted_by_freq = sorted_by_freq[::-1]
    for i in range(len(sorted_by_freq)):
        alfabet_optimizat += sorted_by_freq[i][0]
    return alfabet_optimizat


def check_for_patterns(word):
    patterns = re.findall(r'[A-ZÂĂÎȘȚ]+', word)
    return patterns

def check_for_letters(word):
    letters = []
    for letter in word:
        if letter.isalpha():
            letters.append(letter)
    return letters


if __name__ == '__main__':
    pass
    


        