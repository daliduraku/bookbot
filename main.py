def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    char_count = count_chr(text)
    word_count = count_words(text)
    report(char_count, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())
        
def count_chr(text):
    char_map = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
    
    lowered_string = text.lower()
    
    for char in lowered_string:
        if char in char_map:
            char_map[char] += 1
    
    return char_map          
            

def report(char_count, word_count):
    '''
    count_chr (dict): Dictionary with characters as keys and their counts as values.
    count_words (int): Count number of words in the document.
    
    '''
    
    # convert dict to list
    char_list = [{"character": k, "num": v} for k, v in char_count.items() if k.isalpha()]
    
    # sort the list
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    # Print the report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")    
    
    # Iterate through the sorted list
    
    
    
    for item in char_list:
        print(f"The '{item['character']}' character was found {item['num']} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()


