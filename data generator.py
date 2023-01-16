from nltk import sent_tokenize

# input raw text to be converted
raw_text = "We are looking for an enthusiastic junior software developer to join our experienced software design team. You will report directly to the development manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers. To ensure success as a junior software developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills. Junior Software Developer Responsibilities: Assisting the development manager with all aspects of software design and coding. Attending and contributing to company development meetings. Learning the codebase and improving your coding skills. Writing and maintaining code. Working on minor bug fixes. Monitoring the technical performance of internal systems. Responding to requests from the development team. Gathering information from consumers about program functionality. Writing reports. Conducting development tests. Junior Software Developer Requirements:  Bachelor’s degree in Computer Science or Computer Engineering. Knowledge of basic coding languages including C++, HTML5, and JavaScript. Basic programming experience. Knowledge of databases and operating systems. Good working knowledge of email systems and Microsoft Office software. Ability to learn new software and technologies quickly. Ability to follow instructions and work in a team environment. Detail-oriented."
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
            new_sent = new_sent + " " + new_word
            print(new_sent + ",0")
    if len(new_sent) > 0:
        preprocessed_text.append(new_sent)

print(preprocessed_text)
