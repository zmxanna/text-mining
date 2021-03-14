import urllib.request

url = 'http://www.gutenberg.org/files/1342/1342-0.txt' # Pride and Prejudice
url = 'http://www.gutenberg.org/files/158/158-0.txt' # Emma
url = 'http://www.gutenberg.org/files/161/161-0.txt' # Sense and Sensibility
url = 'http://www.gutenberg.org/ebooks/105.txt.utf-8'# Persuasion
url = 'http://www.gutenberg.org/files/121/121-0.txt' # Northanger Abbey
url = 'http://www.gutenberg.org/files/141/141-0.txt' # Mansfield Park

response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing