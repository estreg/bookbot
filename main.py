def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    print(f"Word count: {word_count}")

main()
