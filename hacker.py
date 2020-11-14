from string import ascii_lowercase as low
from collections import OrderedDict
from scipy.spatial import distance
from encrypt_or_decrypt import encrypt_caesar


def text_comparator(freq_dict1, freq_dict2):
    return distance.cosine(list(freq_dict1.values()),
                           list(freq_dict2.values()))


def hacker_learning():
    text = open('text_for_hacker_learning', 'r')
    learn_text = text.read()
    dict_of_letters = OrderedDict()
    for letter in low:
        dict_of_letters[letter] = 0.0

    for letter in learn_text:
        if not letter.isalpha():
            continue
        else:
            temp_letter = letter.lower()
            dict_of_letters[temp_letter] += 1

    dict_of_letters = letter_percent_count(dict_of_letters)

    return dict_of_letters


def letter_percent_count(letter_dict):
    length = 0
    for value in letter_dict.values():
        length += value
    for key in letter_dict.keys():
        letter_dict[key] /= length

    return letter_dict


def hacker_func(text):
    learn_dict = hacker_learning()
    real_dict = OrderedDict()
    for letter in low:
        real_dict[letter] = 0.0
    for letter in text:
        if not letter.isalpha():
            continue
        else:
            temp_letter = letter.lower()
            real_dict[temp_letter] += 1

    real_dict = letter_percent_count(real_dict)
    min_length = 927
    step = 0
    key = 0
    while step <= 26:
        a_value = real_dict['a']
        for i in range(1, len(low)):
            real_dict[low[i - 1]] = real_dict[low[i]]
        real_dict['z'] = a_value
        temp_dif = text_comparator(real_dict, learn_dict)
        step += 1
        if min_length > temp_dif:
            key = step
            min_length = temp_dif

    decrypt = True
    return encrypt_caesar(text, key, decrypt)
