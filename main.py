import sys
from stats import get_book_text, get_num_words, get_num_chars, create_report

def main():
 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    word_count = get_num_words(filepath)
    char_count = get_num_chars(get_book_text(filepath))
    sorted_report = create_report(char_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath + "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict_tmp in sorted_report:
        print(f"{dict_tmp["char"]}: {dict_tmp["num"]}")

    print("============= END ===============")

main()
