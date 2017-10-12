import nltk
import py_scraper
scraper = py_scraper
url = "https://www.vice.com/en_us/article/gy5mp3/its-time-to-take-down-statues-of-conquistadors"
soup = scraper.scrape(url)

# sentence soup
sentence = " ".join(soup)


# Tokenize a sentence. turn each work AND punctuation mark into an item in a list.
def tokenize_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    print("RESULT = {}.".format(tokens))
    return tokens

# tokenize a sentence and identify part of speech for each token
def tag_sentence(sentence):
    tokens = tokenize_sentence(sentence)
    tagged = nltk.pos_tag(tokens)
    print("RESULT = {}.".format(tagged))
    return tagged

tokens = tag_sentence(sentence)
print(tokens)
