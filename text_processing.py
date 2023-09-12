from sklearn.base import BaseEstimator, TransformerMixin
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.corpus import stopwords


stemmer = PorterStemmer()
words = stopwords.words("english")

class processing_text(BaseEstimator, TransformerMixin):
    def __init__(self,remove_punctuation= True, strip_email=True, to_lowercase= True, replace_url= True, replace_number= True, stemming= True):
        self.remove_punctuation = remove_punctuation
        self.strip_email = strip_email
        self.to_lowercase = to_lowercase
        self.replace_number = replace_number
        self.replace_url = replace_url
        self.stemming = stemming
        self.stemmed_data = []
        self.punctuations = ['!', '.', ',','?', ]
    def fit(self , x, y= None,):
        return self
    def transform(self, x, y=None):
        self.stemmed_data = []
        for text in x:
            tokenize_x = word_tokenize(text)
            url_pattern = url_pattern = r'https?://\S+|www\.\S+'
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
            stemmed_sentence = []
            for word in tokenize_x:
                if self.remove_punctuation and word in self.punctuations:
                        continue
                if word in words:
                     continue
                if self.replace_url and re.match(url_pattern,word):
                    word = "URL"
                         
                if self.replace_number and re.match(r'\+?[0-9][0-9\-]+', word):
                     word = "NUMBER"
                     
                if self.strip_email and re.match(email_pattern,word):
                     continue    
                if self.to_lowercase:
                     word = word.lower()

                if self.stemming:
                    stemmed_word = stemmer.stem(word)
                    stemmed_sentence.append(stemmed_word)
                else:
                     stemmed_sentence.append(word)


            stemmed_text = ' '.join(stemmed_sentence)
            self.stemmed_data.append(stemmed_text)

        
        
        return self.stemmed_data

class bag_of_words(BaseEstimator, TransformerMixin):
    def __init__(self, top_words= 20):
        self.top_words = top_words
        self.vectorizer = CountVectorizer(max_features = self.top_words, binary=True, lowercase=False, stop_words= "english")
    def fit(self,X,y= None):
        self.vectorizer.fit(X)
        return self
    def transform(self,X,y=None):
        bag_of_words = self.vectorizer.transform(X).toarray()
        return bag_of_words
