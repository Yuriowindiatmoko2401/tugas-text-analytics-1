#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/fathanick/Data-Science-Talk-Workshop-Series-2/blob/master/Preprocessing.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ![picture](https://drive.google.com/uc?id=1-xuFvbmPE2Y8fTaRaBblI4ghFmRfG7Bs)

# In[2]:


get_ipython().system('pip install Sastrawi')


# In[ ]:


import nltk #import library nltk
from nltk.tokenize import word_tokenize #import word_tokenize for tokenizing text into words 
from nltk.tokenize import sent_tokenize #import sent_tokenize for tokenizing paragraph into sentences
from nltk.stem.porter import PorterStemmer #import Porter Stemmer Algorithm 
from nltk.stem import WordNetLemmatizer #import WordNet lemmatizer 
from nltk.corpus import stopwords #import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #import Indonesian Stemmer
import re #import regular expression


# In[5]:


nltk.download('punkt')


# In[6]:


text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
sent_tokenize(text_data)


# In[7]:


#sentence tokenization
def sentence_tokenization(s):
    sentences_list = sent_tokenize(s)
    
    return sentences_list

text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
sentence_tokenization(text_data)


# In[8]:


#word tokenization
def word_tokenization(s):
    tokens = word_tokenize(s)

    return tokens
    
text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
word_tokenization(text_data)


# In[9]:


#casefolding
def casefolding(s):
    new_str = s.lower()
    
    return new_str

text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
casefolding(text_data)


# In[10]:


#Stemming Indonesian
def stemmingIndo(str):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return stemmer.stem(str)

text_data = "Saya suka belajar. Karena ingin menjadi pintar. Selain itu, saya ingin membuat bahagia kedua orang tua."
stemmingIndo(text_data)


# In[11]:


#Stemming English
def stemmingEnglish(str):
    porter_stemmer = PorterStemmer()
    words = word_tokenize(str)
    result = list()
    for word in words:
        result.append(porter_stemmer.stem(word))
        
    return ' '.join(result)

text_data = "She had been with her father and sister when she was attacked and received first aid at the scene, an official said."
stemmingEnglish(text_data)


# In[12]:


porter_stemmer = PorterStemmer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#Next find the roots of the word
for w in nltk_tokens:
       print("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))


# In[14]:


#Lemmatization
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       print ("Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w)))


# In[15]:


#remove digit from string
def removeDigit(str):
    new_string =  re.sub(r"[0-9]", " ", str)
    return new_string

text_data = "saya lahir tanggal 1 Januari 2016"
removeDigit(text_data)


# In[17]:


#pos tagging
nltk.download('averaged_perceptron_tagger')
def postag(str):
    tok_sentence = nltk.word_tokenize(str)
    tagged_sentence = nltk.pos_tag(tok_sentence)
    return tagged_sentence

text_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
postag(text_data)


# In[ ]:


import re, string, unicodedata

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


# In[19]:


str = "Copyright © 2008 John Wiley & Sons, Ltd. adalah ini https://www.analyticsvidhya.com/blog/2015/10/6-practices-enhance-performance-text-classification-model/"
print(cleaning(str))


# In[ ]:




