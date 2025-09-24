def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    result = {}
    for char in book_text:
        char = char.lower()
        if result.get(char) != None:
            result[char] += 1
        else:
            result[char] = 1
    return result

def return_num_key(dict):
    return dict["num"]

def sort_values(char_list):
    clean_list = []
    
    for i in char_list:
        char_element = { }
        char_element["char"] =  i
        char_element["num"] = char_list[i]
        clean_list.append(char_element)
    
    clean_list.sort(reverse=True, key=return_num_key)
    return clean_list

    #print(dict.sort(key=return_num))

