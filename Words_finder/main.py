from helpers import *
import sys

if __name__ == '__main__':
    # This part allow us to run program from terminal
    try:
        str_to_find = sys.argv[1]
        find_word_in_files(str_to_find=str_to_find)
    except IndexError:
        print('Please provide argument in execution!\n'
              'Example: python main.py foo')
