def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text)
        
def count_chr(text):
    char_map = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        'o':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0
    }
    
    lowered_string = text.lower()
    
    for char in lowered_string:
        if char in char_map:
            char_map[char] += 1
    
    return char_map          
            
    


main()

