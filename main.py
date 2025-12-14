def main():
    
    word_count = get_word_count("./books/frankenstein.txt")
    print(f"Found {word_count} total words")

def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()

    return file_contents

def get_word_count(filepath):

    words = get_book_text(filepath).split()

    return len(words)

main()
