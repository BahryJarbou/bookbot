def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  words_count = book_words_count(text)
  chars_counts = book_chars_counts(text)
  sorted_chars_counts = dict(sorted(chars_counts.items(), key = lambda item: item[1],reverse = True))
  print(sorted_chars_counts)
  print(f"--- Begin report of  {book_path} ---")
  print(f"{words_count} words found in the document")
  print("\n")
  for key in sorted_chars_counts:
    if key.isalpha():
      print(f"the {key} character was found {sorted_chars_counts[key]} times")
  
  print("--- End report ---")



def get_book_text(path):
  with open(path) as f:
    return f.read()


def book_words_count(book_text):
  words = book_text.split()
  return len(words)


def book_chars_counts(book_text):
  book_text_lowered = book_text.lower()
  results = {}
  for char in book_text_lowered:
    if char in results:
      results[char] +=1
    else:
      results[char] =1
  return results

  

main()
