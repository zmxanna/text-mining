import urllib.request

url = 'http://www.gutenberg.org/files/1342/1342-0.txt' #Pride and Prejudice
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing