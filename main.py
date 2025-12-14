from stats import get_book_text, get_num_words

def main():
    
    word_count = get_num_words("./books/frankenstein.txt")
    print(f"Found {word_count} total words")

main()
