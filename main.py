from stats import get_num_words
from stats import get_num_letters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    word_count = get_num_words(get_book_text("books/frankenstein.txt"))
    letter_count = get_num_letters("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(letter_count)

main()