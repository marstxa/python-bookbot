from stats import count_words
from stats import character_count

def get_book_text(file_path="books/frankenstein.txt"):
    with open(file_path) as book:
        file_contents = book.read()
        return file_contents

def main():
    count_words(get_book_text())
    character_count(get_book_text())

main()
