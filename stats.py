def count_words(path):
    with open(path) as f:
        file_contents = f.read()
    list_of_strings = file_contents.split()
    print("-------- Word Count --------")
    return f"Found {len(list_of_strings)} total words"


def count_letters(path):
    dictionary_of_wordcount = {}
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                'r','s','t','u','v','w','x','y','z',',','.','(',')']
    
    with open(path) as f:
        file_contents = f.read()
    for character in characters:
        num_occurrences = file_contents.lower().count(character)
        dictionary_of_wordcount[character] = num_occurrences
    #print(dictionary_of_wordcount)
    return dictionary_of_wordcount



def dict_to_list(dict):
    list_of_dicts = [{"key": k, "value": v} for k, v in dict.items()]
    return list_of_dicts

def sort_on(dict):
    return dict["value"]

def print_list_of_letters(lst):
    new_dict = {item['key']: item['value'] for item in lst}
    print("------ Character Count --------")
    for k, v in new_dict.items():
        print(f"{k}: {v}")

