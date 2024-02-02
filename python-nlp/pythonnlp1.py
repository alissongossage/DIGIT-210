import spacy
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

chatgptresults = open('chatgpt-results.txt', 'r', encoding='utf8')
words = chatgptresults.read()
wordstrings = str(words)
print(wordstrings)

text = (wordstrings)
doc = nlp(text)
print()

print("Nouns:")
for token in doc:
    if token.pos_ == "NOUN":
        print (token.text)

print("Verb lemmas:")
sentence  = "In poetry, the heart may dwell, Expressing joy, embracing pain, A testament of life's refrain."
doc =nlp(sentence)
for token in doc:
    if token.pos_ == "VERB":
        print(token.lemma_)
