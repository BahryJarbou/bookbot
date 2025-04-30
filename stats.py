def book_words_count(book_text):
  words = book_text.split()
  return len(words)


def report_creator(character_dict):
    dict_list = []
    for key,val in character_dict.items():
        dict_list.append({"char": key, "num": val })
    dict_list.sort(reverse=True, key= sort_on)

    for dic in dict_list:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}\n")
        

def sort_on(dict):
    return dict["num"]