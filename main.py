from stats import count_words
from stats import count_characters
import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(count_words(sys.argv[1]))
    print("--------- Character Count -------")
    for char, count in count_characters(sys.argv[1]).items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()


    