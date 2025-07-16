import sys
from stats import get_word_count, get_char_count, sort_report

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = get_word_count(book_text)
        num_chars = get_char_count(book_text)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        report = sort_report(num_chars)
        for c in report:
            print(f"{c["char"]}: {c["num"]}")
        print("============= END ===============")


main()
