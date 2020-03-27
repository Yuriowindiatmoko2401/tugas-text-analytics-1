!pip install newspaper3k

import newspaper
from newspaper import Article

url = "https://jogja.tribunnews.com/2019/10/08/jadwal-pertandingan-timnas-senior-dan-u-23-indonesia-yang-disiarkan-langsung-rcti"
article = Article(url)
article.download()
article.parse()
txt = article.text
txt = txt.encode('ascii', 'ignore').decode("utf-8")
print(txt)

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

clean_txt = cleaning(txt)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(max_font_size=45).generate(clean_txt)
plt.figure(figsize=(10,8))

'''plot wordcloud in matplotlib'''

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

words_in_article = clean_txt.split()
words_in_article

import collections
import itertools

# Create counter
counts_no_urls = collections.Counter(words_in_article)

counts_no_urls.most_common(15)

import pandas as pd

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

import nltk
from nltk.corpus import stopwords 
nltk.download('stopwords')

stop_words = set(stopwords.words('indonesian'))

# View a few words from the set
list(stop_words)[0:10]

new_word_list = [word for word in words_in_article if not word in stop_words]  
new_word_list

import collections
import itertools

# Create counter
counts_no_urls = collections.Counter(new_word_list)

counts_no_urls.most_common(15)

import pandas as pd

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


