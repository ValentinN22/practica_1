import dictionar as dc
import random as rd
import time

def get_data_from_file():
    try:
        with open('cuvinte_de_verificat.txt', 'r', encoding='utf-8-sig') as data_file:
            all_lines = data_file.read().splitlines()

        ids = [x for x in range(1,len(all_lines)+1)]
        data_set = {x:[] for x in ids}

        for line in all_lines:
            line_list = line.split(';')
            data_set[int(line_list[0])].append(line_list[1])
            data_set[int(line_list[0])].append(line_list[2])

        return data_set

    except ValueError:
        print("Id-ul nu este un numar intreg!!")


def get_data_from_word(word):
    patterns = dc.check_for_patterns(word)
    letters = dc.check_for_letters(word)
    first_letter =''
    last_letter = ''
    if word[0] != '*':
        first_letter = word[0]
    if word[-1] != '*':
        last_letter = word[-1]
    return patterns,first_letter,last_letter,letters



def solving(start_word, solutie):
    incercari_corecte = []
    incercari_gresite = []

    print("Cuvantul de start:",start_word)

    while True:
        if start_word == solutie:
            break
        
        date_cuvant = get_data_from_word(start_word)
        similar_words = dc.similar_words(len(start_word),date_cuvant[0], incercari_gresite, date_cuvant[1], date_cuvant[2])
        alfabet_optimizat = dc.freq_of_letter(similar_words,date_cuvant[3], incercari_gresite)
        for letter in alfabet_optimizat[:1:]:
            incercare_corecta = False
            for i in range(0, len(solutie)):
                if letter == solutie[i]:
                    incercare_corecta = True
                    start_word = start_word[:i:] + solutie[i] + start_word[i+1::]
            if incercare_corecta == False:
                incercari_gresite.append(letter)
                print(f"Litera {letter} este incorecta!")
            else:
                incercari_corecte.append(letter)
                print(f"Litera {letter} este corecta! Noul cuvant este: {start_word}")

    print(f"c:{incercari_corecte}, g:{incercari_gresite}")
    return len(incercari_corecte), len(incercari_gresite)

    

def start_game(data_set):
    numar_incercari_corecte = 0
    numar_incercari_gresite = 0
    numar_incercari = 0
    while(True):
        if(len(data_set) == 0):
            break
        # cautam un joc random
        keys = list(data_set.keys())
        id = rd.choice(keys)

        start_word= data_set[id][0]
        solutie = data_set[id][1]

        del data_set[id]

        # automatizare hangman
        feedback_cuvant = solving(start_word, solutie)
        numar_incercari_corecte += feedback_cuvant[0]
        numar_incercari_gresite += feedback_cuvant[1]
        numar_incercari = ( numar_incercari_corecte + numar_incercari_gresite)
        print()
        print(f"Incercari corecte = {numar_incercari_corecte}, Incercari_gresite= {numar_incercari_gresite}, Total Incercari={numar_incercari}")
        print()
    return numar_incercari



if __name__ == '__main__':
    data_set = get_data_from_file()
    start_time = time.time()
    start_game(data_set)
    end_time = time.time()
    print('Timp rulare:', end_time-start_time)