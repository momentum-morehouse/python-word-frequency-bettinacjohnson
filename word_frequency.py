import re
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
] #relies on lists of words



frequency = {}
first = []

# cleaned_text = []
# text_string = document_text.read().lower()

def print_word_freq(): #the main function
  
  document_text = open('real_love.txt', 'r')
  file_name = document_text
  with open(file_name, "r") as f: 
  
    # """Read in `file` and print out the frequency of words in that file."""
    # first open the file
# with open(file_name,"r") as f:
    
    text_string = f.read().lower()
    
  cleaned_text = []
    # match_pattern = re.findall(r"[!?.,]","",text_string)
  for word in match_pattern:
        count = frequency.get(word, 0)  #word is key, value = 0
        frequency[word] = count + 1
  frequency_list = frequency.keys()
    # print(frequency)
  for words in frequency_list:
        print(words,':', frequency[words])
# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
if __name__ == "__main__":
    import argparse
    from pathlib import Path
    print_word_freq()  #calling on each file















# # #=============================================
# #BELOW IS CODE ATTEMPT #1: WORKS, BUT PRIOR TO MORNING SESSION

# def flatten_lol(lol):
#   flat_list = []
#   for l in lol:
#     for word in l:
#       flat_list.append(word)
#   return flat_list

# first = []
# frequency = {}
# # ^ empty containters 
# print("Here is the word frequency for 'Real Love' by Mary J. Blige: ")
# document_text = open('real_love.txt', 'r')
# cleaned_text = []
# text_string = document_text.read().lower()
# clean = re.sub(r"[!?.,]","", text_string)
# cleaner = clean.split()
# cleaned_text.append(cleaner)

# working_list = flatten_lol(cleaned_text)
# for word in list(working_list):
#   if word in STOP_WORDS:
#     working_list.remove(word)
#     for word in working_list:


#       for word in clean:
#         count = frequency.get(word,0)
#         frequency[word] = count + 1
     
# frequency_list = frequency.keys()
 
# for words in frequency_list:
#     print(words,'|', frequency[words])


# # sort = sorted(count.items(), key=operator.itemgetter(1))
# # sort.reverse

# # #=============================================
# # # it knows which one to run based on what is in the .replit portion of the file after the run = 
# # STOP_WORDS = [
# # ]


# def print_word_freq(file):
  #   """Read in `file` and print out the frequency of words in that file."""
  #   # Your code will go here. You can write additional functions if you want, and call them inside this function.
  #   # first open the file
  #   with open(file) as f:
  #       lyrics = f.readlines()
  #       word_list = [line.split() for line in lyrics]
  # text_string = document_text.read().lower() #reading everything in lower case AND does the same thing in line 36
  #       frequency = {}
  #       match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

# def flatten_lol(lol):
  # flat_list = []
  # for sublist in lol:
  #   for item in sublist: 
  #     flat_list.append(item)
  # return flat_list
  #       print(word_list)

# This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
# if __name__ == "__main__":
    # import argparse
    # from pathlib import Path

    # parser = argparse.ArgumentParser(
    #     description='Get the word frequency in a text file.')
    # parser.add_argument('file', help='file to read')
    # args = parser.parse_args()

    # file = Path(args.file)
    # if file.is_file():
    #     print_word_freq(file)
    #     #calling this function on the run command/ print word frequency on the file that is being called in the above function 
    # else:
    #     print(f"{file} does not exist!")
    #     exit(1)


# # #=============================================


# def print_word_freq(): #the main function
#     file_name = document_text
#     document_text = open('real_love.txt', 'r')
#     """Read in file and print out the frequency of words in that file."""
#     # Your code will go here. You can write additional functions if you want, and call them inside this function.
#     # first open the file
#     with open(file_name,"r") as f:
#         text_string = f.read().lower()
#     frequency = {}
#     match_pattern = re.findall(r'\b[a-z]{1,15}\b',text_string)
#     for word in match_pattern:
#         count = frequency.get(word, 0)  #word is key, value is 0
#         frequency[word] = count + 1
#     frequency_list = frequency.keys()
#     print(frequency)
#     for words in frequency_list:
#         print(words,frequency[words])
# # This is an "incantation." You will not see it very often, and it needs to be here to be able to pass file names as arguments.
# # if _name_ == "_main_":
#     import argparse
#     from pathlib import Path
#     print_word_freq()  #calls on each file
