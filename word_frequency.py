# import re
# import string


















#=============================================
#BELOW IS CODE ATTEMPT #1: WORKS, BUT PRIOR TO MORNING SESSION
frequency = {}
print("Here is the word frequency for 'Real Love' by Mary J. Blige: ")
document_text = open('real_love.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)
 
# for word in match_pattern:
#     count = frequency.get(word,0)
#     frequency[word] = count + 1
     
# frequency_list = frequency.keys()
 
# for words in frequency_list:
#     print(words, frequency[words])

# # sort = sorted(count.items(), key=operator.itemgetter(1))
# # sort.reverse

#=============================================
# it knows which one to run based on what is in the .replit portion of the file after the run = 
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # Your code will go here. You can write additional functions if you want, and call them inside this function.
    # first open the file
    with open(file) as f:
        lyrics = f.readlines()
        word_list = [line.split() for line in lyrics]
  text_string = document_text.read().lower() #reading everything in lower case AND does the same thing in line 36
        frequency = {}
        match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)


  def flatten_lol(lol):
  flat_list = []
  for sublist in lol:
    for item in sublist: 
      flat_list.append(item)
  return flat_list
        print(word_list)

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
        #calling this function on the run command/ print word frequency on the file that is being called in the above function 
    else:
        print(f"{file} does not exist!")
        exit(1)












