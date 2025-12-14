def get_book_text(filepath):

    with open(filepath) as f:

        file_contents = f.read()

    return file_contents

def get_num_words(filepath):

    words = get_book_text(filepath).split()

    return len(words)
