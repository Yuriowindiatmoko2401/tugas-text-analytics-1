import re, string, unicodedata
import nltk
import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = replace_contractions(text)
    return text

def removeStopword(str):
    stop_words = set(stopwords.words('stopwords_id'))
    word_tokens = word_tokenize(str)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return ' '.join(filtered_sentence)

def stemming(str):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(str)

def cleaning(str):

    #remove non-ascii
    str = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore').decode('utf-8', 'ignore')

    #remove URLs
    str = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', str)

    #remove punctuations
    str = re.sub(r'[^\w]|_',' ',str)

    #remove digit from string
    str = re.sub("\S*\d\S*", "", str).strip()

    #remove digit or numbers
    str = re.sub(r"\b\d+\b", " ", str)

    #to lowercase
    str = str.lower()

    #Remove additional white spaces
    str = re.sub('[\s]+', ' ', str)
       
    return str

def preprocessing(str):
    str = denoise_text(str)
    str = cleaning(str)
    str = removeStopword(str)
    str = stemming(str)
    
    return str

#test the code
str = "Saya membeli buku dengan Copyright © 2008 John Wiley & Sons, Ltd."
print(preprocessing(str))


if __name__ == "__main__":
    fo = open("news.txt","r")
    fw = open("clean_data.txt","a")
    for f in fo:
        str = preprocessing(f)
        fw.write(str+'\n')

