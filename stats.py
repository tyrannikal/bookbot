def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()

    return file_contents

def get_num_words(filepath):

    words = get_book_text(filepath).split()

    return len(words)

def get_num_chars(book_text):

    words = book_text.split()
    num_chars = {}

    for word in words:

        lower_word = word.lower()
        for char in lower_word:

            if char in num_chars:

                num_chars[char] += 1
            else:
                num_chars[char] = 1

    return num_chars
