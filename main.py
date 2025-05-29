from stats import count_words, count_chars, sort_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    book_path = str(sys.argv[1])
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_chars = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path_string):
    with open(path_string) as f:
        file_contents = f.read()
    return (file_contents)

if __name__ == "__main__":
    main()
