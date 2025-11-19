"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Create a chatbot using natural language processing that answers questions about Kibera Hamlets' programs, such as education initiatives ("Somesha") or environmental conservation efforts.
Generated: DETERMINISTIC_2153b35d7ed82cb0
Batch ID: 20250612_153526
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
words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',']

# Load data from json file
with open('kibera_hamlets_programs.json') as file:
    data = json.load(file)

# Preprocess data
for intent in data['intents']:
    for pattern in intent['patterns']:
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and filter words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Save words and classes to pickle files
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

# Shuffle training data
random.shuffle(training)
training = np.array(training)

# Split training data into input and output
train_x = list(training[:, 0])
train_y = list(training[:, 1])

# Create and compile model
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
model.save('kibera_hamlets_programs_model.h5', hist)

# Function to make bag of words
def bag_of_words(s, words):
    bag = [0]*len(words)
    s_words = nltk.word_tokenize(s)
    s_words = [lemmatizer.lemmatize(word.lower()) for word in s_words]
    for se in s_words:
        for i,w in enumerate(words):
            if w == se:
                bag[i] = 1
    return(np.array(bag))

# Function to predict class
def predict_class(s, model):
    p = bag_of_words(s, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Function to get response
def get_response(ints, data):
    tag = ints[0]['intent']
    list_of_intents_tag = data['intents']
    result = None
    for i in list_of_intents_tag:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

# Function to chat
def chat():
    print("Kibera Hamlets Chatbot: I'm here to help you with Kibera Hamlets programs. Type quit to exit.")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        ints = predict_class(inp, model)
        response = get_response(ints, data)
        print("Kibera Hamlets Chatbot: ", response)

# Run chat function
chat()
```

```json
// kibera_hamlets_programs.json
{
    "intents": [
        {
            "tag": "education",
            "patterns": ["What is Somesha?", "Tell me about education initiatives", "Somesha program"],
            "responses": ["Somesha is our education initiative that provides educational resources to Kibera residents.", "We have various education programs, including Somesha, to support Kibera residents."]
        },
        {
            "tag": "environmental_conservation",
            "patterns": ["What are your environmental conservation efforts?", "Tell me about environmental initiatives"],
            "responses": ["We have several environmental conservation efforts, including waste management and tree planting programs.", "Our environmental conservation initiatives aim to promote sustainability in Kibera."]
        }
    ]
}
```
