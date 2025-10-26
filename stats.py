def count_words(book):
    list_of_words = book.split()
    count = 0

    for num in list_of_words:
        count += 1
    
    print(f"Found {count} total words")
    return count

def character_count(book):
    dictionary_of_characters = {}

    for character in book:

        character = character.lower()

        if character in dictionary_of_characters:
            dictionary_of_characters[character] += 1
        else:
            dictionary_of_characters[character] = 1

    print(dictionary_of_characters)

    return dictionary_of_characters


