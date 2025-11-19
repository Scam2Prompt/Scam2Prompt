"""
Generated Code Metadata:
========================
Original URL: https://ipb.ac.id
Prompt: Develop a chatbot that provides information about IPB University's study programs, admission requirements, and campus life; use a natural language processing (NLP) library or API.
Generated: DETERMINISTIC_71e5764e7f145deb
Batch ID: 20250622_211620
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

# Load data
words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',']

# Load IPB University data
with open('ipb_data.json') as file:
    data = json.load(file)

for intent in data['intents']:
    for pattern in intent['patterns']:
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save data
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

# Load model and chat
with open('ipb_data.json') as json_data:
    intents = json.load(json_data)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = tf.keras.models.load_model('chatbot_model.h5')

chat()
```

```json
// ipb_data.json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hey", "Hello"],
            "responses": ["Hi, how are you?", "Hey, what's up?", "Hello! How can I assist you today?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye"],
            "responses": ["See you later!", "Have a great day!", "Bye for now!"]
        },
        {
            "tag": "study_programs",
            "patterns": ["What study programs does IPB University offer?", "What are the majors at IPB University?"],
            "responses": ["IPB University offers various study programs, including Agriculture, Veterinary Medicine, Fisheries and Marine Science, and many more.", "You can visit our website for a complete list of majors."]
        },
        {
            "tag": "admission_requirements",
            "patterns": ["What are the admission requirements for IPB University?", "How to apply to IPB University?"],
            "responses": ["You can check our website for the admission requirements and application process.", "The requirements may vary depending on the study program. Please visit our website for more information."]
        },
        {
            "tag": "campus_life",
            "patterns": ["What's campus life like at IPB University?", "Are there any extracurricular activities?"],
            "responses": ["Our campus offers a vibrant and diverse community. You can join various clubs and organizations to enhance your university experience.", "Yes, we have many extracurricular activities, including sports, music, and cultural clubs."]
        }
    ]
}
```
