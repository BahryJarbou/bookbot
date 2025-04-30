import sys

from stats import book_words_count, report_creator
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  
  words_count = book_words_count(text)
  chars_counts = book_chars_counts(text)
  #sorted_chars_counts = dict(sorted(chars_counts.items(), key = lambda item: item[1],reverse = True))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {words_count} total words")
  print("--------- Character Count -------")
  report_creator(chars_counts)
  print("============= END ===============")



def get_book_text(path):
  with open(path) as f:
    return f.read()


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
