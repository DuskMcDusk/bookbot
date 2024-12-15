def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    num_characters = count_characters(text)
    print_report(book_path)
    return None

def get_book(file_path):
    with open(file_path) as f:
        return f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def dict_to_list(dict):
    result = []
    for key in dict:
        result.append({"character": key, "count": dict[key]})
    return result

def sort_on(dict):
    return dict["count"]

def print_report(book_path):
    text = get_book(book_path)
    words = count_words(text)
    characters = count_characters(text)
    characters_dict = dict_to_list(characters)
    characters_dict.sort(reverse=True, key = sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")

    for entry in characters_dict:
        if entry["character"].isalpha() :
            print(f"char '{entry['character']}' found {entry['count']} times")

    print("--- end report ---")
main()