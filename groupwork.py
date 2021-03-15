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

def main():
    download_books()
    book1,book2,book3,book4 = process_books()
    # print(book1,book2,book3,book4)
    print('Total number of words in book1:', analyze_book.total_words(book1))
    print('Total number of words in book2:', analyze_book.total_words(book2))
    print('Total number of words in book3:', analyze_book.total_words(book3))
    print('Total number of words in book4:', analyze_book.total_words(book4))

if __name__ == '__main__':
    main()