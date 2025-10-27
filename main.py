import sys
from stats import count_words
from stats import character_count
from stats import display_data


def get_book_text():
    
    #get arguments 
    arguments = sys.argv
    print(arguments)

    if len(arguments) >= 2:
        path_to_file = arguments[1] #get path to file
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) #exit program

    with open(path_to_file) as book:
        file_contents = book.read()
        return file_contents, path_to_file

def main():
    book, path = get_book_text()
    word_count = count_words(book)
    char_count = character_count(book)
    display_data(char_count, path, word_count) 
main()
