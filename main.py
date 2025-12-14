from stats import get_book_text, get_num_words, get_num_chars

def main():
   
    filepath = "./books/frankenstein.txt"

    word_count = get_num_words(filepath)
    print(f"Found {word_count} total words")

    char_count = get_num_chars(get_book_text(filepath))
    print(char_count)

main()
