import urllib.request
import analyze_book

def download_books():
    keys = ["Pride and Prejudice", "Emma", "Sense and Sensibility", "Northanger Abbey", "Mansfield Park"]
    values = ['http://www.gutenberg.org/files/1342/1342-0.txt', 'http://www.gutenberg.org/files/158/158-0.txt', 'http://www.gutenberg.org/files/161/161-0.txt', 'http://www.gutenberg.org/files/121/121-0.txt', 'http://www.gutenberg.org/files/141/141-0.txt']
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

def main():
    download_books()


if __name__ == '__main__':
    main()