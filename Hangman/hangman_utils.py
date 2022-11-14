import random
from valid_hangman_words import words


def pick_up_word(lst_words):
    """Pick up random word from words poll"""
    len_lst = len(lst_words)
    rnd_word_index = random.randint(0, len_lst - 1)
    return lst_words[rnd_word_index]


def display_word(word: str):
    """Print random word for player"""
    first = word[0:1]
    last = word[len(word) - 1:len(word)]
    return first, last


print(display_word(pick_up_word(words)))