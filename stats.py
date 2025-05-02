def get_num_words(words):
    word_list = words.split()
    return len(word_list)

def get_num_letters(book):
    with open(book) as f:
        letters_list = list(f.read())
    letter_count = {}
    for letter in letters_list:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:
            letter_count[letter.lower()] = 1
    return letter_count

def main():
    get_num_letters("books/frankenstein.txt")

main()