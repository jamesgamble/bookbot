import sys
from stats import count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    text = get_book_text(filepath)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_characters = sort_characters(char_counts)
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

