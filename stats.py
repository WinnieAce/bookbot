def get_book_text(file_path) :
    try:
        with open(file_path, 'r') as file :
            return file.read()
    except FileNotFoundError:
        return 'File not found'
    except Exception as e:
        return f'An error occurred: {e}'    

def count_words(file_path) :
    text = get_book_text(file_path)
    return f'Found {len(text.split())} total words'

def count_characters(file_path) :
    text = get_book_text(file_path)
    character_dict = {}
    for char in text.lower() :
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))