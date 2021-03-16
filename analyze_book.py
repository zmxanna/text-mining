import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    total = sum(hist.values())
    return total


def different_words(hist):
    """Returns the number of different words in a histogram."""
    unique =len(hist)
    return unique


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    # 1. create a new list
    # 2. get the word, frequency from given list
    # 3. create tuples (frequency, word)
    # 4. append the tuples to the list

    sorted_list = []
    for word, freq in hist.items():
        t = (freq, word)
        sorted_list.append(t)
    sorted_list = sorted(sorted_list,reverse=True)

    return sorted_list


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    print('The most common words are:')
    for freq, word in hist[0:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    d = dict()
    text = "not in dictionary"
    for i in d1:
        if i not in d2:
            d[i] = text
    return d
    

def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    # t = []
    # for word, freq in hist.items():
    #     t.extend([word] * freq)
    # return random.choice(t)

    text = []
    freq_final = 0
    for word, freq in hist.item():
        text.append[word]
        freq_final += freq
    ran = random.randint(1,freq_final)
    # perform bisection search
    # return text[ran]

def main():
    hist = process_file('data/gatsby.txt', skip_header=True)
    # print(hist)
    # print('Total number of words:', total_words(hist))
    # print('Number of different words:', different_words(hist))

    # t = most_common(hist, excluding_stopwords=True)
    # print('The most common words are:')
    # for freq, word in t[0:20]:
    #     print(word, '\t', freq)

    # print_most_common(most_common(hist, excluding_stopwords=True))
    
    # words = process_file('data/words.txt', skip_header=False)
    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()