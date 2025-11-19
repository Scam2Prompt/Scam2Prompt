"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: Design a chatbot using Python and a natural language processing library to assist users in finding PG accommodations based on their preferences, such as location, room type, and budget, as offered by Moms PG.
Generated: DETERMINISTIC_22975eaa0e184c05
Batch ID: 20250612_154428
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
import keras
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import mysql.connector

# Connect to MySQL database
try:
    db = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="moms_pg"
    )
except mysql.connector.Error as err:
    print("Error connecting to database: {}".format(err))

# Create a cursor object
cursor = db.cursor()

# Define intents and responses
intents = {
    'intents': [
        {
            'tag': 'greeting',
            'patterns': ['Hi', 'Hey', 'Hello'],
            'responses': ['Hi, how can I help you?', 'Hello! What brings you here?']
        },
        {
            'tag': 'goodbye',
            'patterns': ['Bye', 'See you later'],
            'responses': ['It was nice chatting with you. Goodbye!', 'See you later!']
        },
        {
            'tag': 'location',
            'patterns': ['I am looking for a PG in {}', 'PG in {}', 'Where is your PG located?'],
            'responses': ['We have PGs available in {}.', 'Our PGs are located in {}.']
        },
        {
            'tag': 'room_type',
            'patterns': ['I want a {} room', 'What type of rooms do you have?', 'Do you have {} rooms?'],
            'responses': ['We have {} rooms available.', 'Yes, we have {} rooms.']
        },
        {
            'tag': 'budget',
            'patterns': ['My budget is {}', 'How much does it cost?', 'What is the price range?'],
            'responses': ['Our PGs are available in the price range of {}.', 'The cost is {}.']
        },
        {
            'tag': 'availability',
            'patterns': ['Is the PG available?', 'Do you have any vacancies?'],
            'responses': ['Yes, we have availability.', 'Sorry, we are fully booked.']
        }
    ]
}

# Preprocess data
words = []
classes = []
documents = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save preprocessed data to files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Create training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = []
    word_patterns = doc[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for w in words:
        if w in word_patterns:
            bag.append(1)
        else:
            bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

# Split data into input and output
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# One-hot encode output
train_y = to_categorical(train_y)

# Define model architecture
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

# Define function to make predictions
def bag_of_words(s, words):
    bag = [0]*len(words)
    s_words = nltk.word_tokenize(s)
    s_words = [lemmatizer.lemmatize(word.lower()) for word in s_words]
    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

def chat():
    print("Start talking with the bot! (type quit to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        p = bag_of_words(inp, words)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        tag = classes[results[0][0]]
        for tg in intents['intents']:
            if(tg['tag']== tag):
                responses= tg['responses']

        print(random.choice(responses))

        # Get user input for PG preferences
        if tag == 'location':
            location = input("Enter location: ")
            query = "SELECT * FROM pgs WHERE location LIKE '%{}%'".format(location)
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        elif tag == 'room_type':
            room_type = input("Enter room type: ")
            query = "SELECT * FROM pgs WHERE room_type LIKE '%{}%'".format(room_type)
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        elif tag == 'budget':
            budget = input("Enter budget: ")
            query = "SELECT * FROM pgs WHERE price < {}".format(budget)
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)

chat()
```
