from stats import get_num_words
from stats import get_num_letters
from stats import letter_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(book_path):
    word_count = get_num_words(get_book_text(book_path))
    letter_count = get_num_letters(book_path)
    sorted_letters = letter_sort(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
#    print(f"{word_count} words found in the document")
#    print(letter_count)

# main()

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])