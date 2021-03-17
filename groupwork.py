import urllib.request
import analyze_book
import string
import nltk

keys = ["Pride and Prejudice.txt", "Sense and Sensibility.txt", "Northanger Abbey.txt", "Mansfield Park.txt"]

def download_books():
    """
    downloads four Jane Austen books from Project Gutenberg 
    """
    values = ['http://www.gutenberg.org/files/1342/1342-0.txt', 'http://www.gutenberg.org/files/161/161-0.txt', 'http://www.gutenberg.org/files/121/121-0.txt', 'http://www.gutenberg.org/files/141/141-0.txt']
    books = dict(zip(keys, values))
    names = []
    for key in books.keys(): 
        names.append(key) 
    order = 0
    
    # download the books and store them as txt files
    for i in books.values():
        response = urllib.request.urlopen(i)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')
        with open(names[order],"w", encoding="utf-8") as fout:
            fout.write(text)
        order += 1

def text_books():
    """
    store each book as a string variable for future methods
    """
    text1 = open(keys[0], "r", encoding="utf-8").read()
    text2 = open(keys[1], "r", encoding="utf-8").read()
    text3 = open(keys[2], "r", encoding="utf-8").read()
    text4 = open(keys[3], "r", encoding="utf-8").read()

    return text1, text2, text3, text4


def process_books():
    """
    processes all four books into dictionaries where the keys are words that appear and the values are frequencies of words in the text
    """
    book1 = analyze_book.process_file(keys[0],skip_header=True)
    book2 = analyze_book.process_file(keys[1],skip_header=True)
    book3 = analyze_book.process_file(keys[2],skip_header=True)
    book4 = analyze_book.process_file(keys[3],skip_header=True)
    
    return book1, book2, book3, book4


def common_words(book1, book2, book3, book4):
    """
    prints top 20 common words for each of the four books
    """  
    books = [book1, book2, book3, book4]

    x = 0
    for i in books:
        t = analyze_book.most_common(i)
        print("\nThe most common words in", keys[x], "are:")
        for freq, word in t[0:20]:
            print(word, '\t', freq)
        x += 1


def common_words_wo_stopwords(text1, text2, text3, text4):
    """
    prints top 20 common words without stopwords for each of the four books
    """
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from collections import Counter

    # get rid of stopwords, punctuations, and digits
    added_list = ['“','”',"‘","’"]
    stop_words = set(stopwords.words("english") + list(string.punctuation) + list(string.digits) + added_list)
    texts = [text1.lower(), text2.lower(), text3.lower(), text4.lower()]
    x = 0
    for i in texts:
        word_tokens = word_tokenize(i)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]  
        filtered_sentence = []
        for w in word_tokens:  
            if w not in stop_words:  
                filtered_sentence.append(w)
        output = Counter(filtered_sentence)
        common = output.most_common(20)
        print("\nThe most common words without stopwords in", keys[x], "are:", "\n", common)
        x += 1


def summary_stats(book1, book2, book3, book4):
    """
    prints a table of summary stats about these four books, including: total number of words, total number 
    of unique words, and the percentage of unique words in each text
    """
    from tabulate import tabulate
    books = [book1, book2, book3, book4]
    num_words = []
    num_unique = []
    percentage = []

    # populate each list
    for i in range(4):
        num_words.append(analyze_book.total_words(books[i]))
        num_unique.append(analyze_book.different_words(books[i]))
        percentage.append(num_unique[i]/num_words[i]*100)

    # prints table
    data = [[keys[0], num_words[0], num_unique[0], percentage[0]],
    [keys[1], num_words[1], num_unique[1], percentage[1]],
    [keys[2], num_words[2], num_unique[2], percentage[2]],
    [keys[3], num_words[3], num_unique[3], percentage[3]]] 
    print("\n\nSummary Stats of these four books:\n")
    print(tabulate(data, headers=["Text", "# of Total Words", "# of Unique Words", "Percentage of Unique Words(%)"]))


def main():
    download_books()

    b1,b2,b3,b4 = process_books()
    common_words(b1,b2,b3,b4)

    t1,t2,t3,t4 = text_books()
    common_words_wo_stopwords(t1,t2,t3,t4)

    summary_stats(b1,b2,b3,b4)


if __name__ == '__main__':
    main()