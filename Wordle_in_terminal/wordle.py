from valid_words import valid_words
import sys
import random

CHOSEN_WORD = random.choice(valid_words)
GUESSES_COUNT = 6


class Color:
    PREFIX = '\033'
    BASE = '\033[0m'
    GREY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'


class GuessWord:
    counter = 1
    wordles = []

    def __init__(self, w_str: str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    def jump_turn(self):
        GuessWord.counter += 1

    def is_valid(self):
        return self.w_str in valid_words

    def apply_greens(self):
        for i, _ in enumerate(self.w_chars):  # we use only i parameter
            actual_char = CHOSEN_WORD[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                colored_char = f'{Color.GREEN}{actual_char}{Color.BASE}'
                self.w_chars[i] = colored_char

    def apply_yellows(self):
        for i, _ in enumerate(self.w_chars):  # we use only i parameter
            guessed_char = self.w_chars[i]
            if guessed_char in CHOSEN_WORD:
                colored_char = f'{Color.YELLOW}{guessed_char}{Color.BASE}'
                self.w_chars[i] = colored_char

    def apply_guesses(self):
        self.apply_greens()
        self.apply_yellows()
        self.post_guess_w_str = ''.join(self.w_chars)
        GuessWord.wordles.append(self.post_guess_w_str)
        print(self.post_guess_w_str)

    def check_perfect_guess(self):
        if self.w_str == CHOSEN_WORD:
            print(f"Congratulation! You beat Wordle in {GuessWord.counter} guesses")
            for element in GuessWord.wordles:
                print(element)
            sys.exit(1)

    def check_game_loss(self):
        if GuessWord.counter == GUESSES_COUNT + 1:
            print(f"You lost the game. The word was {CHOSEN_WORD}")
            sys.exit(1)
