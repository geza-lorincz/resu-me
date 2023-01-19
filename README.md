ResuMe

Welcome to the AI prototype of ResuMe.

The goal of this project, which was done in the context of TechLabs, is to automatically extract keywords from job descriptions.

Please keep in mind that this is a very early version prototype.

How to use:
1. Make sure the Python environment has all the required libraries. These can be found in the first lines of code in "model.py", which is the main code that should be used.
2. Copy & paste a job description into "text_import.txt". The program will automatically read all text from here, and try to find keywords. Please note, that while you can paste in any job description, this is an early prototype, and certain characters and structures in the text can break the program. For best results, use a job description from "job descriptions for testing.txt". These are real job descriptions that have been tested and are formatted in a way that make sure the program can understand them.
3. Run "model.py", and the program will take care of the rest. After the model finishes working, the keywords will be printed out in the console.

Notes:
- The model currently is not able to handle expressions that consist of two separate words, such as "computer science", or "bachelor's degree", but these can be considered as important requirements. In these cases, the model will simply output one word as a keyword, such as "computer" for computer science.
- As this is a proof of concept prototype, the model was trained on a small, limited amount of data. The data (which can be found in "data.csv") was job advertisements in the tech sector, therefore the model is best at finding tech related keywords.
- More data can be added, which can be automatically generated using "data generator.py". This will also take input from text_inport, and will convert the job description into data that can be copy & pasted in the dataset. When doing so, always check that the data is formatted correctly. To label the new data, change the 0 in the second column into a 1 for keywords.
- If the model is outputting too many or too few keywords, play around with the "keyword_sensitivity" variable.

