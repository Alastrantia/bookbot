from stats import get_num_words, get_num_chars, sort_values
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def create_pretty_print(num_words, sorted_chars, path):
    pretty_print = ""
    pretty_print += "============ BOOKBOT ============\n"
    pretty_print += f"Analyzing book found at {path}...\n"
    pretty_print += "----------- Word Count ----------\n"
    pretty_print += f"Found {num_words} total words\n"
    pretty_print += "--------- Character Count -------\n"
    for element in sorted_chars:
        if not element["char"].isalpha(): continue
        line = element["char"] + ": " + str(element["num"]) + "\n"
        pretty_print += line
    pretty_print += "============= END ===============\n"
    return pretty_print
    

    
def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted_chars = sort_values(num_chars)
    print(create_pretty_print(num_words, sorted_chars, book_path))
    

main()
