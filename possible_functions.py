def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break
    #    can also do 'end with the project' in process_file

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    # Pseudo-code from professor in class:
    # 1. create a new list
    # 2. get the word and its freq from the given hist
        # if excluding_stopwords:
        # do nothing
    # 3. create tuple (freq, word)
    # 4. append the tuple to the list
    # 5. sort the list
   
    common_words = []
    for word, freq in hist.items():
        common_words.append(freq, word)

    common_words.sort(reverse=True)
    return common_words

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    print('The most common words are:')
    for freq, word in hist[0:num]:
        print(word, '\t', freq)


common words between file