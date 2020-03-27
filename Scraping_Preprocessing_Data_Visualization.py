# !pip install newspaper3k
import newspaper
from newspaper import Article
import re, string, unicodedata
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import collections
import itertools
import pandas as pd
import nltk
from nltk.corpus import stopwords 

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

url = "https://jogja.tribunnews.com/2019/10/08/jadwal-pertandingan-timnas-senior-dan-u-23-indonesia-yang-disiarkan-langsung-rcti"
article = Article(url)
article.download()
article.parse()
txt = article.text
txt = txt.encode('ascii', 'ignore').decode("utf-8")
print(txt)

clean_txt = cleaning(txt)

wordcloud = WordCloud(max_font_size=45).generate(clean_txt)
plt.figure(figsize=(10,8))

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

words_in_article = clean_txt.split()
words_in_article

# Create counter
counts_no_urls = collections.Counter(words_in_article)
counts_no_urls.most_common(15)

df = pd.DataFrame(counts_no_urls.most_common(15),
                             columns=['words', 'count'])

df.head()

fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
df.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="blue")

ax.set_title("Common Words Found in Article (Including All Words)")

plt.show()

nltk.download('stopwords')

stop_words = set(stopwords.words('indonesian'))

# View a few words from the set
list(stop_words)[0:10]

new_word_list = [word for word in words_in_article if not word in stop_words]  
new_word_list



# Create counter
counts_no_urls = collections.Counter(new_word_list)

counts_no_urls.most_common(15)


df = pd.DataFrame(counts_no_urls.most_common(15),
                             columns=['words', 'count'])

df.head()

fig, ax = plt.subplots(figsize=(8, 8))

# Plot horizontal bar graph
df.sort_values(by='count').plot.barh(x='words',
                      y='count',
                      ax=ax,
                      color="red")

ax.set_title("Common Words Found in Article (After Removing Stopwords)")

plt.show()

urls = ["http://id.beritasatu.com/home/biayai-pembangunan-jalan-baru-tol-dan-jembatan/178885",
       "http://www.beritasatu.com/satu/506680-oktober-tol-pemalangbatang-jalani-uji-kelayakan.html",]

for url in urls:
    article = Article(url)
    article.download()
    article.parse()
    with open("news.txt","a+") as f:
        txt = article.text
        txt = txt.encode('ascii', 'ignore').decode("utf-8")
        f.write(txt + "\n\n")
        f.close()

"""
object n method
PreprocessUII

#rmNon_Ascii
#remove URLs
#remove punctuations
#remove digit from string
#remove digit or numbers
#to lowercase
#Remove additional white spaces

#remove stopwords
  #add stop words

#Stemming Indonesian
#wordcloud show
#counting
#plt frequency

import re, unicodedata
from nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

class PreprocessUII:

  # class attributes
  # stop_words = set(stopwords.words('stopwords_id'))
  
  def __init__(self, text): 
    self.text = text 
    self.rmNon_Ascii = self._rmNon_Ascii()
    self.rmURLs = self._rmURLs()
    self.rmPunc = self._rmPunc()
    self.rmDigit_string = self._rmDigit_string()
    self.rmDigitnumbers = self._rmDigitnumbers()
    self.lowercase = self._lowercase()
    self.rmAdditionalWs = self._rmAdditionalWs()

  def _rmNon_Ascii(self):
    return unicodedata.normalize('NFKD', self.text).encode('ascii', 'ignore').decode('utf-8', 'ignore')

  def _rmURLs(self):
    return re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', self.text)

  def _rmPunc(self):
    return re.sub(r'[^\w]|_',' ',self.text)

  def _rmDigit_string(self):
    return re.sub("\S*\d\S*", "", self.text).strip()

  def _rmDigitnumbers(self):
    return re.sub(r"\b\d+\b", " ", self.text)

  def _lowercase(self):
    return text.lower(self.text)

  def _rmAdditionalWs(self):
    return re.sub('[\s]+', ' ', self.text)

  def removeStopword(self):
    stop_words = set(stopwords.words('stopwords_id'))
    word_tokens = word_tokenize(self.text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    return ' '.join(filtered_sentence)

"""









