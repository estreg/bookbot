def main():
    books = get_book_list()

    while True:
        display_book_menu(books)
        try:
            choice = input("Enter the number of the book you want to analyze")
            book_index = int(choice) - 1

            if book_index < 0 or book_index >= len(books):
                print(f"Please enter a number between 1 and {len(books)}")
                continue


            book_path = f"books/{books[book_index]}"
            break

        except ValueError:
            print("Please enter a valid number")

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(num_words, chars_dict, books[book_index])


import os

def get_book_list(directory="books"):
    return os.listdir(directory)


def display_book_menu(books):
    for index, book in enumerate(books):
        print(f"{index + 1}) {book}")

def sort_on(dict):
    return dict["num"]


def print_report(num_words, chars_dict, book_name):
    char_list = []
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_name} ---")
    print(f"{num_words} words found in the document\n")

    for chars_dict in char_list:
        print(f"The '{chars_dict['char']}' character was found {chars_dict['num']} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in characters:
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
