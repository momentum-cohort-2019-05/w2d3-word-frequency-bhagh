import re
from collections import Counter


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    raw_string = open(file).read()
    clean_string = (re.sub("[^a-zA-Z0-9]+", ' ', raw_string))
    clean_string = clean_string.lower()
    querywords = clean_string.split()
    word_list = ""

    for word in querywords:
        if word not in STOP_WORDS:
            word_list += str(word)+" "
    
    word_list = word_list.split() 

    master_list = {}

    for word in word_list:
        if master_list.get(word) == None:
            master_list[word] = 1
        else:
            master_list[word] += 1
    
    list2 = [(word, quantity) for word, quantity in master_list.items()] 
    
    def first_item(seq):
        return seq[0]
    
    list2 = sorted(list2, key=first_item)

    def second_item(seq):
        return seq[1]

    def top_ten(quantities):
        quantities = sorted(quantities, key=second_item, reverse=True)[0:10]
        return quantities
        #for word, qty in quantities:
            #print(word, qty)
        
    final_list = top_ten(list2)

    for word, qty in final_list:
        print(word, qty)


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

