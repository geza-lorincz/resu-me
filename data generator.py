from nltk import sent_tokenize

# input raw text to be converted
punctuation = ['!', '–', '"', '$', '%', '&', ',', '(', ')', '*', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']

with open('text_import.txt', 'r') as f:
    raw_text = f.read()

print(raw_text)


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
            print(new_sent[:-1] + ",0")
    if len(new_sent) > 0:
        preprocessed_text.append(new_sent)


