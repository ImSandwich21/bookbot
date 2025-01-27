def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    word_count = get_word_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    char_dict = get_char_count(text)
    char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    for c in char_dict:
        if c[0].isalpha():
            print(f"The '{c}' character was found {char_dict[c]} times")

    print("--- End report ---")


def sort_on(dict):
    return dict[1]

def get_char_count(text):
    char_dict = {}
    for w in text:
        for c in w.lower():
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()