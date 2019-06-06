import re


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

    #revmove all STOP_WORDS
    for word in querywords:
        if word not in STOP_WORDS:
            word_list += str(word)+" "
    
    #create a split lit
    word_list = word_list.split() 

    #create a dictionary
    master_list = {}

    #fill dictionary with words and word count
    for word in word_list:
        if master_list.get(word) == None:
            master_list[word] = 1
        else:
            master_list[word] += 1
    
    #create tuple from dictionary
    tuple_list = [(word, quantity) for word, quantity in master_list.items()] 
    
    def first_item(seq):
        return seq[0]
    
    #sort tuple alphabetically
    tuple_list = sorted(tuple_list, key=first_item)

    def second_item(seq):
        return seq[1]

    def top_ten(quantities):
        quantities = sorted(quantities, key=second_item, reverse=True)[0:10]
        return quantities
       
    #create final top 10 list
    final_list = top_ten(tuple_list)

    #print out top 10 words with * indicators
    for word, qty in final_list:
        print('{:>10}'.format(word), " | " , '{:<2}'.format(qty), '{:<1}'.format("*" * qty))


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

