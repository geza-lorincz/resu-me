

import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

from gensim.models import word2vec, FastText, Word2Vec
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import csv

# testing text, irrelevant
text = "We are looking for an enthusiastic junior software developer to join our experienced software design team. You will report directly to the development manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers. To ensure success as a junior software developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills. Junior Software Developer Responsibilities: Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings. Learning the codebase and improving your coding skills. Writing and maintaining code. Working on minor bug fixes. Monitoring the technical performance of internal systems. Responding to requests from the development team. Gathering information from consumers about program functionality. Writing reports. Conducting development tests. Junior Software Developer Requirements:  Bachelor’s degree in Computer Science or Computer Engineering. Knowledge of basic coding languages including C++, HTML5, and JavaScript. Basic programming experience. Knowledge of databases and operating systems. Good working knowledge of email systems and Microsoft Office software. Ability to learn new software and technologies quickly. Ability to follow instructions and work in a team environment. Detail-oriented."

# load the data from the csv file
data = []

with open("data.csv") as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        data.append(row[0])
print(data)
train_label = []
test_data = []
test_label = []

geci_test = []

stop_words = ['more', 'isn', 'into', 'which', 'but', 'and', 'he', 'being', 'i', 'didn', 'haven', 'what', 'me', 'their', 'be', 'after', 'to', 'ain', 'when', 'or', 'ourselves', 'with', 'between', 'then', 'before', 'through', 'here', 'of', "weren't", 'against', 'been', 'myself', 'mustn', 'can', "needn't", 'shan', 'its', 'aren', 'himself', 'at', 'down', 'yours', "don't", 'it', 'hadn', 're', 'most', 'both', 'than', 's', "haven't", 'the', 'above', 'that', 'from', 'some', 'was', 'won', 'these', 'we', 'out', 'each', "that'll", 'your', 'further', 'nor', "she's", 'because', 'theirs', 'over', "isn't", 'd', 'hers', 'mightn', 'o', 'wouldn', 'll', 'now', 'am', 'is', "wasn't", 'does', 'by', 'doing', 'on', 'off', 'under', 'who', "doesn't", 'shouldn', "you'll", "aren't", 'don', 't', 'too', 'if', 'has', 'those', 'all', "should've", 'such', 'yourselves', 'should', 'my', 'so', 'her', 'whom', 'again', 'wasn', 'themselves', 'had', 'them', 'did', 'weren', 'yourself', "mustn't", "you're", 'only', 'y', 'have', 'during', 've', 'no', 'having', "didn't", "hadn't", 'as', 'herself', 'this', "it's", 'any', 'you', "you'd", 'few', "shan't", "you've", 'below', 'are', 'where', 'own', 'an', 'needn', 'up', 'ma', 'they', 'just', 'itself', 'were', "mightn't", 'how', "won't", 'will', 'doesn', 'do', 'other', 'not', 'while', 'about', 'once', "hasn't", 'hasn', 'she', 'him', 'same', "wouldn't", "couldn't", 'for', 'm', 'his', "shouldn't", 'why', 'couldn', 'a', 'very', 'ours', 'until', 'our', 'there', 'in']
punctuation = ['!', '"', '$', '%', '&', ',', '(', ')', '*', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']

# split text by sentences and words REDUNDANT
# preprocessed_text = []
# text = sent_tokenize(text)
# for sent in text:
#     new_sent = []
#     sent = sent.split()
#     for word in sent:
#         new_word = word.lower()
#         if new_word[-1] in punctuation:
#             new_word = new_word[:-1]
#         if new_word[0] not in punctuation:
#             new_sent.append(new_word)
#     if len(new_sent) > 0:
#         preprocessed_text.append(new_sent)


# split sentences in the data into words
processed_data = []
for sent in data:
    sent = sent.split()
    processed_data.append(sent)

print(processed_data)

# tokenize text and create sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(processed_data)
word_index = tokenizer.word_index
print(word_index)
sequences = tokenizer.texts_to_sequences(processed_data)
print(sequences)
sequences = pad_sequences(sequences)
print(sequences)






#w2v = Word2Vec(sentences=sequences, min_count=1, vector_size=5)

#words = list(w2v.wv.key_to_index)
#print(words)
#print(w2v.wv["environment"])






