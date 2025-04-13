from stats import *
import sys

""" def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents """


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    try:
        print("========== BOOKBOT ==========")
        print(f"Analyzing book found at {sys.argv[1]}....")
        #print(count_words('books/frankenstein.txt'))
        print(count_words(sys.argv[1]))
        new_dict = count_letters(sys.argv[1])
        list_of_letters = dict_to_list(count_letters(sys.argv[1]))
        list_of_letters.sort(reverse=True, key=sort_on)
        print_list_of_letters(list_of_letters)

    except FileNotFoundError as e:
        print(e)

main()
