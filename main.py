def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print_report(num_words, chars_dict)


def sort_on(dict):
    return dict["num"]


def print_report(num_words, chars_dict):
    char_list = []
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
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
