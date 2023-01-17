

import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import Dense
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

from gensim.models import word2vec, FastText, Word2Vec
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import csv
import numpy as np

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

# load the labels from the csv file
labels = []
with open("data.csv") as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        labels.append(row[1])


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


# tokenize data and create sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(processed_data)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(processed_data)
sequences = pad_sequences(sequences)

# load labels in numpy array
processed_labels = np.array(labels, dtype=int)

print(sequences)
print(processed_labels)

# build the model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32))
model.add(LSTM(units=32))
model.add(Dense(1, activation='sigmoid'))
#model.summary()

# compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train the model
model.fit(sequences, processed_labels, epochs=5)

#w2v = Word2Vec(sentences=sequences, min_count=1, vector_size=5)

#words = list(w2v.wv.key_to_index)
#print(words)
#print(w2v.wv["environment"])






