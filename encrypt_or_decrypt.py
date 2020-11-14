from string import ascii_lowercase as low
from string import ascii_uppercase as up


def index(letter):
    return up.index(letter) if letter.isupper() else low.index(letter)


def shift(letter, offset):
    new_index = (index(letter) + offset) % len(up)
    return up[new_index] if letter.isupper() else low[new_index]


def inverse(letter):
    new_index = (len(up) - index(letter)) % len(up)
    return up[new_index] if letter.isupper() else low[new_index]


def encrypt_caesar(text, key, decrypt=False):
    if decrypt:
        key = len(up) - key
    return ''.join(shift(letter, key) if letter.isalpha() else letter for letter in text)


def encrypt_vizhener(text, key, decrypt=False):
    if decrypt:
        key = ''.join(inverse(sym) for sym in key)
    new_text = ''
    for i, letter in enumerate(text):
        new_text += shift(letter, index(key[i % len(key)])) if letter.isalpha() else letter
    return new_text


def encrypt_vernam(text, key, decrypt=False):
    return encrypt_vizhener(text, key, decrypt)
