import sys
from stats import count_words, list_of_dicts
from stats import character_frequency


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def sort_on(dict):
    return dict["num"]


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_of_words = count_words(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    frequency = character_frequency(get_book_text(filepath))
    list_of_dictionaries = list_of_dicts(frequency)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    for dictionary in list_of_dictionaries:
        if dictionary["name"].isalpha():
            print(f"{dictionary['name']}: {dictionary['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
