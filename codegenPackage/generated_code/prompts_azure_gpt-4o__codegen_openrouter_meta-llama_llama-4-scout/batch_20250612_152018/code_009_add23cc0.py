"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a chatbot using Python and NLP libraries to answer common queries about Darul Raza's services, such as Istikhara, Taweezat, and online courses.
Generated: DETERMINISTIC_add23cc060bb51ae
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import tflearn
import tensorflow as tf
import tflearn
import random
import json
import pickle

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load data
with open('intents.json') as file:
    data = json.load(file)

try:
    with open('words.pkl', 'rb') as f:
        words = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent['tag'])

            if intent['tag'] not in labels:
                labels.append(intent['tag'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    pickle.dump(words, open('words.pkl', 'wb'))
    pickle.dump(labels, open('labels.pkl', 'wb'))

try:
    with open('training.pkl', 'rb') as f:
        training = pickle.load(f)
except:
    training = []
    output_empty = [0] * len(labels)

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [lemmatizer.lemmatize(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = list(output_empty)
        output_row[labels.index(docs_y[x])] = 1

        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:,0])
    train_y = list(training[:,1])
    print("Training data created")

    pickle.dump(training, open('training.pkl', 'wb'))

# Create and train model
model = tflearn.DNN([ 
    {"type": "input", "name": "input", "shape": [len(train_x[0])]},
    {"type": "dense", "units": 8, "activation": "relu"},
    {"type": "dropout", "dropout": 0.1},
    {"type": "dense", "units": 8, "activation": "relu"},
    {"type": "dropout", "dropout": 0.1},
    {"type": "dense", "units": len(train_y[0]), "activation": "softmax"}
])

model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

# Create bag of words
def bag_of_words(s, words):
    bag = [0]*len(words)

    s_words = nltk.word_tokenize(s)
    s_words = [lemmatizer.lemmatize(word.lower()) for word in s_words]

    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return(np.array(bag))

# Create chat function
def chat():
    print("Welcome to Darul Raza's chatbot! Type quit to exit.")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        p = bag_of_words(inp, words)
        res = model.predict([p])[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD] 

        results.sort(key=lambda x: x[1], reverse=True) 
        tag = labels[results[0][0]]
        print(tag)

        for tg in data["intents"]:
            if(tg['tag']== tag):
                responses= tg['responses']

        print(random.choice(responses))

chat()
```

```json
// intents.json
{
    "intents": [
        {
            "tag": "istikhara",
            "patterns": ["What is Istikhara?", "Istikhara meaning", "Istikhara"],
            "responses": ["Istikhara is a prayer of guidance in Islam.", "It helps you make a decision by seeking Allah's guidance."]
        },
        {
            "tag": "taweezat",
            "patterns": ["What are Taweezat?", "Taweezat meaning", "Taweezat"],
            "responses": ["Taweezat are Islamic prayers or verses written on a piece of paper or cloth.", "They are used for protection or guidance."]
        },
        {
            "tag": "online_courses",
            "patterns": ["What online courses do you offer?", "Courses", "Online courses"],
            "responses": ["We offer various online courses on Islamic studies.", "You can visit our website for more information."]
        }
    ]
}
```
