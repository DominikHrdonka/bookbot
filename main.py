def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_word = get_num_words(text)
    chars_dict = get_num_letters(text)
    chars_sorted_list = char_dict_to_sort_list(chars_dict)

    print(f"---This is report of {book_path}---")
    print(f"{num_word} words found in the document")
    num_letter = get_num_letters(text)
    print()

    for item in chars_sorted_list:
        if not item ["char"].isalpha():
            continue
        print(f"The {item["char"]} was found {item["num"]} times")
    print("---End report---")


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

def sort_on(d):
    return d["num"]

def char_dict_to_sort_list(num_letter):
    sorted_list = []
    for ch in num_letter:
        sorted_list.append({"char":ch, "num":num_letter[ch]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list


main()