import re
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
] #relies on lists of words
 #MY INITIAL CODE 

def print_word_freq(): #the main function
    file_name = document_text
    document_text = open('real_love.txt', 'r')
    """Read in file and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file_name,"r") as f:
        text_string = f.read().lower()
    frequency = {}
    match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string)
    for word in match_pattern:
        count = frequency.get(word, 0)  #word is key, value is 0
        frequency[word] = count + 1
    frequency_list = frequency.keys()
    print(frequency)
    for words in frequency_list:
        print(words,frequency[words])
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
# if _name_ == "_main_":
    import argparse
    from pathlib import Path
    print_word_freq()  #calls on each file

# END OF MY CODE============================================

#(STEVE'S CODE) STOP WORDS AND PUNCT========================
def flatten_lol(lol):
  flat_list = []
  for l in lol:
    for word in l:
      flat_list.append(word)
  return flat_list

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    
    first = []
    frequency = {}
    #empty contianers ^

    with open(file) as f:
      for items in f:
          first.append(items)
          # ^ grabbing the item/words out of the text file
      cleaned_text = []
      for w in first:
        clean = re.sub(r"[!?.,]","", w.lower())
        cleaner = clean.split()
        cleaned_text.append(cleaner)
        # ^ removing the punctuation from the text 
    
      working_list = flatten_lol(cleaned_text)
      # ^ running the cleaned text through my flatten function

      for word in list(working_list):  
          if word in STOP_WORDS:
           working_list.remove(word)
           for word in working_list:
             count = frequency.get(word,0)
             frequency[word] = count + 1
     
             frequency_list = frequency.keys()
 
             for words in frequency_list:
               # ^ counting words in text
              print(words, '|' ,frequency[words]) 
 
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
#(STEVE'S CODE) RUNS FOREVER=======================

#==========KIERANS CODE
# import re
# import string
# STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ] #relies on lists of words
# def print_word_freq(): #the main function
#     file_name = input("Enter a song")
#     """Read in `file` and print out the frequency of words in that file."""
#     # Your code will go here. You can write additional functions if you want, and call them inside this function.
#     # first open the file
#     with open(file_name,"r") as f:
#         text_string = f.read().lower()
#     frequency = {}
#     match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string)
#     for word in match_pattern:
#         count = frequency.get(word, 0)  #word is key, value = 0
#         frequency[word] = count + 1
#     frequency_list = frequency.keys()
#     print(frequency)
#     for words in frequency_list:
#         print(words,frequency[words])
# # This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path
#     print_word_freq()  #calling on each file
 #===========END OF KIERANS CODE





   



