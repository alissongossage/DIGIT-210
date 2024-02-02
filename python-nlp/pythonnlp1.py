import spacy
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

chatgptresults = open('chatgpt-results.txt', 'r', encoding='utf8')
words = chatgptresults.read()
wordstrings = str(words)
print(wordstrings)

