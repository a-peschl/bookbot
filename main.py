import sys
from stats import get_num_character, get_num_of_words, sort_on, sort_dictionary
from sys import argv


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_num_of_words(file_contents)
    char_count_dict = get_num_character(file_contents)
    sorted_char_list = sort_dictionary(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")  # Zugriff auf die Werte
    print("============= END ===============")

main()
