def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    print(f"{num_word} words found in the document.")
    num_letter = get_num_letters(text)
    print(f"Number of letter occurences: {num_letter}")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lowered_text = text.lower()
    num_letters = {}
    for c in lowered_text:
        if c in num_letters:
            num_letters[c] += 1
        else:
            num_letters[c]= 1
    return num_letters

main()