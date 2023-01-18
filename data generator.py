from nltk import sent_tokenize

# input raw text to be converted
raw_text = "Required Skills: 2-4 years of programming experience required! Strong desire to learn and grow required! Previous professional experience in Java mandate. Previous 1-3 years' experience in SQL required. Must be open to relocation after the training. What We Offer: Rapid career growth, with focused and intensive training. Paid training for 8 weeks. Compensation in line with industry forms. Excellent medical, dental, and vision benefits. Relocation assistance, if required for client assignment. Mentorship and support throughout the program. Networking opportunities within your industry with peers and industry leader. About Pyramid Consulting: GenSpark is a division of Pyramid Consulting, a $310M IT Consulting firm. Pyramid Consulting is among the Top 100 largest minority and privately owned IT Consulting firms in the U.S.. The success of our clients is facilitated through our ability to provide full-spectrum support via our development centers – from a single consultant under their management, at their site, to full turnkey solutions onsite and offshore."
punctuation = ['!', '"', '$', '%', '&', ',', '(', ')', '*', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']



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
            print(new_sent + ",0")
    if len(new_sent) > 0:
        preprocessed_text.append(new_sent)

print(preprocessed_text)

#for line in preprocessed_text
with open('data_export.txt', 'a') as f:
    f.writelines(new_sent + ",0 \n")
