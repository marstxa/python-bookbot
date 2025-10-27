# Data analysis functions for main.py

def count_words(book):
    # Get the total number of letters in a book and print the result to the terminal
    
    list_of_words = book.split()
    count = 0

    for num in list_of_words:
        count += 1
    
    return count

def character_count(book):
    dictionary_of_characters = {}

    for character in book:

        character = character.lower()

        if character in dictionary_of_characters:
            dictionary_of_characters[character] += 1
        else:
            dictionary_of_characters[character] = 1


    return dictionary_of_characters

def sort_dict(dictionary):
    sorted_items = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_items

def display_data(dictionary, book, word_count):
    
    #Sort dictionary
    sorted_dictionary = sort_dict(dictionary)

    #Print functions to display data:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")    

    #print dict keys and values in order
    for value in sorted_dictionary: 
        if value.isalpha():
            print(f"{value}: {sorted_dictionary[value]}") 

    return sorted_dictionary