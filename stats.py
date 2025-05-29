def count_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return (word_count)

def count_chars(book_text):
    all_char_count = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in all_char_count:
            all_char_count[lower_char] = 1
        else:
            all_char_count[lower_char] += 1
    return all_char_count

def sort_chars(char_count):
    sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict