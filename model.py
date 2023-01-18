

import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Embedding
from keras.layers import Dense
from keras.layers import LSTM
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences

from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import csv
import numpy as np

# parameters to configure
maximum_length = 50         # the maximum length of sentences that the model can take as input, measured in words
training_portion = .8       # what portion of the data should be used for training (the leftover is used for validation)
keyword_sensitivity = .45    # the value at which the predictor deems a word a keyword

train = False               # put true if you want to train the model, false if you want to extract keywords

punctuation = ['!', '–', '"', '$', '%', '&', ',', '(', ')', '*', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']


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
error = 0
with open("data.csv") as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    for row in reader:
        labels.append(row[1])



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
sequences = pad_sequences(sequences, maxlen=maximum_length)


# KEYWORD EXTRACTION - ANALYSE JOB DESCRIPTION AND PRINT KEYWORDS

if not train:
    # load model
    model = keras.models.load_model('model.h5')

    # load text from text_import.txt
    with open('text_import.txt', 'r') as f:
        raw_text = f.read()

    # split text by sentences and words
    preprocessed_text = []
    text = sent_tokenize(raw_text)
    for sent in text:
        new_sent = ""
        sent = sent.split()
        for word in sent:
            new_word = word.lower()
            if new_word[-1] in punctuation:
                new_word = new_word[:-1]
            if new_word[0] not in punctuation:
                new_sent = new_sent + new_word + " "
                preprocessed_text.append(new_sent[:-1])
        #if len(new_sent) > 0:
            #preprocessed_text.append(new_sent)
    print(preprocessed_text)

    # loop through the input data and print out keywords
    keywords = ""
    for sent in preprocessed_text:
        words = sent.split()
        processed_sent = []
        sent = sent.split()
        processed_sent.append(sent)

        # turn into sequence and pre-pad
        input_seq = tokenizer.texts_to_sequences(processed_sent)
        input_seq = pad_sequences(input_seq, maxlen=maximum_length)

        prediction = model.predict(input_seq)

        if prediction[0] >= keyword_sensitivity:
            keywords = keywords + " " + words[-1]

    print(keywords)

# MODEL TRAINING
if train:
    # load labels in numpy array
    processed_labels = np.array(labels, dtype=int)

    # split data into training and validation
    training_size = int(len(sequences) * training_portion)
    training_data = sequences[0: training_size]
    training_labels = processed_labels[0: training_size]
    validation_data = sequences[training_size:]
    validation_labels = processed_labels[training_size:]

    # build the model
    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32))
    model.add(LSTM(units=32))
    model.add(Dense(1, activation='sigmoid'))
    # model.summary()

    # compile the model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # train the model
    model.fit(training_data, training_labels, epochs=5, validation_data=(validation_data, validation_labels))

    # save the model
    model.save('model.h5')

    # testing purposes only
    testing_text = ["you should be a team"]
    testing_sequence = tokenizer.texts_to_sequences(testing_text)
    testing_sequence = pad_sequences(testing_sequence, maxlen=maximum_length)

    prediction = model.predict(testing_sequence)
    print(prediction)


