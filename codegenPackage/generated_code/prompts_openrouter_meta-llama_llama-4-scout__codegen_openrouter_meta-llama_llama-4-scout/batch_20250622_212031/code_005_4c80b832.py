"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Create a digital banking chatbot, inspired by Grand Chase's customer support, that can assist users with common queries, using a natural language processing (NLP) library or framework.
Generated: DETERMINISTIC_4c80b8326cb3cd16
Batch ID: 20250622_212031
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
from tensorflow.keras import layers

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load data
words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',']

# Load JSON data
with open('intents.json') as file:
    data = json.load(file)

# Process data
for intent in data['intents']:
    for pattern in intent['patterns']:
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))

# Sort classes
classes = sorted(list(set(classes)))

# Save words and classes
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Shuffle data
random.shuffle(training)
training = np.array(training)

# Split data
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Create model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

# Save model
model.save('chatbot_model.h5', hist)

# Create bag of words
def bag_of_words(s, words):
    bag = [0] * len(words)

    s_words = nltk.word_tokenize(s)
    s_words = [lemmatizer.lemmatize(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)

# Create chat function
def chat():
    print("Start talking with the bot! (type quit to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        p = bag_of_words(inp, words)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD] 

        results.sort(key=lambda x: x[1], reverse=True) 
        tag = classes[results[0][0]]
        for tg in data["intents"]:
            if(tg['tag']== tag):
                responses= tg['responses']

        print(random.choice(responses))

# Run chat function
chat()
```

```json
// intents.json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["hi", "hey", "hello"],
            "responses": ["Hi there!", "Hey! How are you?", "Hello! What's up?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["bye", "see you later", "goodbye"],
            "responses": ["See you later!", "Bye for now!", "Goodbye!"]
        },
        {
            "tag": "thanks",
            "patterns": ["thanks", "thank you", "appreciate it"],
            "responses": ["You're welcome!", "No problem!", "Thanks for using our service!"]
        },
        {
            "tag": "balance",
            "patterns": ["what's my balance", "balance", "account balance"],
            "responses": ["Your balance is $1000.", "You have $500 in your account.", "Your current balance is $2000."]
        }
    ]
}
```
