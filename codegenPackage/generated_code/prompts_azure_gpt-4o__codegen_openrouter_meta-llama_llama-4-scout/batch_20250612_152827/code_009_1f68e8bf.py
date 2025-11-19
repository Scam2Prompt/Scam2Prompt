"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Generate code for a chatbot that can answer patient queries about laboratory tests, including "fosfata alcalina," "bilirrubina total," and "coprológico funcional," using natural language processing.
Generated: DETERMINISTIC_1f68e8bf8eacceb0
Batch ID: 20250612_152827
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
import tensorflow as tf
from tensorflow import keras

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load laboratory tests data
lab_tests_data = {
    "fosfata alcalina": "La fosfata alcalina es una enzima que se encuentra en la sangre y se utiliza para evaluar la función hepática y ósea.",
    "bilirrubina total": "La bilirrubina total es un pigmento amarillo que se produce durante la descomposición de la hemoglobina y se utiliza para evaluar la función hepática.",
    "coprológico funcional": "El coprológico funcional es un examen que evalúa la función digestiva y se utiliza para diagnosticar trastornos gastrointestinales."
}

# Load intents data
intents = {
    "intents": [
        {
            "tag": "fosfata_alcalina",
            "patterns": ["fosfata alcalina", "fosfata alcalina alta", "fosfata alcalina baja"],
            "responses": [lab_tests_data["fosfata alcalina"]]
        },
        {
            "tag": "bilirrubina_total",
            "patterns": ["bilirrubina total", "bilirrubina total alta", "bilirrubina total baja"],
            "responses": [lab_tests_data["bilirrubina total"]]
        },
        {
            "tag": "coprológico_funcional",
            "patterns": ["coprológico funcional", "examen coprológico"],
            "responses": [lab_tests_data["coprológico funcional"]]
        }
    ]
}

# Preprocess data
words = []
labels = []
docs_x = []
docs_y = []

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(labels, open("labels.pkl", "wb"))

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

train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Build chatbot model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save model
model.save("chatbot_model.h5", hist)

# Define functions for chatbot
def clean_up_sentence(sentence):
    sentence = nltk.word_tokenize(sentence)
    sentence = [lemmatizer.lemmatize(word.lower()) for word in sentence]
    return sentence

def bow(sentence, words, show_details=True):
    sentence = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD] 

    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = []
    for r in results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents_tag = intents_json['intents']
    for i in list_of_intents_tag:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = get_response(ints, intents)
    return res

# Test chatbot
while True:
    message = input("Patient: ")
    if message == "quit":
        break
    response = chatbot_response(message)
    print("Chatbot: ", response)
```
