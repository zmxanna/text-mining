import urllib.request
import analyze_book

def download_books():
    keys = ["Pride and Prejudice", "Sense and Sensibility", "Northanger Abbey", "Mansfield Park"]
    values = ['http://www.gutenberg.org/files/1342/1342-0.txt', 'http://www.gutenberg.org/files/161/161-0.txt', 'http://www.gutenberg.org/files/121/121-0.txt', 'http://www.gutenberg.org/files/141/141-0.txt']
    books = dict(zip(keys, values))
    names = []
    for key in books.keys(): 
        names.append(key) 
    order = 0
    for i in books.values():
        response = urllib.request.urlopen(i)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')
        # print(text) # for testing
        with open(names[order],"w", encoding="utf-8") as fout:
            fout.write(text)
        order += 1

# fin = open("pride_and_prejudice.txt","r")
# print(fin.readlines())


def process_books():
    book1 = analyze_book.process_file("Pride and Prejudice",skip_header=True)
    book2 = analyze_book.process_file("Sense and Sensibility",skip_header=True)
    book3 = analyze_book.process_file("Northanger Abbey",skip_header=True)
    book4 = analyze_book.process_file("Mansfield Park",skip_header=True)
    return book1, book2, book3, book4

import sys
import random

# global variables
suffix_map = {} # map from prefixes to a list of suffixes
prefix = () # current tuple of words

def markov_process_file(filename, order=2):
    """Reads a file and performs Markov analysis.
    filename: string
    order: integer number of words in the prefix
    returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        if not line.startswith('*** END OF THIS PROJECT'):
            for word in line.rstrip().split():
                process_word(word, order)

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def process_word(word, order=2):
    """Processes each word.
    word: string
    order: integer
    During the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)

def random_text(n=100):
    """Generates random wordsfrom the analyzed text.
    Starts with a random prefix from the dictionary.
    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes is None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n - i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.
    t: tuple of strings
    word: string
    Returns: tuple of strings
    """
    return t[1:] + (word,)

def main(script, filename, n=50, order=2):
    try:
        n = int(n)
        order=int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else:
        markov_process_file(filename, order)
        random_text(n)
        print()

if __name__ == '__main__':
    download_books()
    book1,book2,book3,book4 = process_books()
    main(script, filename = book1, n=50, order=2)
    main(script, filename = book2, n=50, order=2)
    main(script, filename = book3, n=50, order=2)
    main(script, filename = book4, n=50, order=2)