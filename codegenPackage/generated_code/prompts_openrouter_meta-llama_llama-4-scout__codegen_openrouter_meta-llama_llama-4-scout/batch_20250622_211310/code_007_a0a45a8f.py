"""
Generated Code Metadata:
========================
Original URL: https://immediate-elevate.com
Prompt: Develop a chatbot that answers user queries about investment education and provides resources from Immediate Elevate, using natural language processing (NLP) techniques.
Generated: DETERMINISTIC_a0a45a8fc6d7a060
Batch ID: 20250622_211310
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
import warnings
warnings.filterwarnings('ignore')

# Load Immediate Elevate resources
try:
    with open('immediate_elevate_resources.json') as f:
        immediate_elevate_resources = json.load(f)
except FileNotFoundError:
    print("Error: Immediate Elevate resources file not found.")
    exit()

# Load NLP data
try:
    with open('nltk_data.pkl', 'rb') as f:
        words, labels, training, output = pickle.load(f)
except FileNotFoundError:
    print("Error: NLP data file not found.")
    exit()

# Initialize NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Preprocess data
training = np.array(training)
output = np.array(output)

# Create chatbot model
model = Sequential()
model.add(Dense(128, input_shape=(len(training[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(output[0]), activation='softmax'))

# Compile model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train model
try:
    model.load_model('chatbot_model.h5')
except:
    model.fit(training, output, epochs=200, batch_size=5, verbose=1)
    model.save('chatbot_model.h5')

# Define functions
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                break
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = []
    for r in results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, immediate_elevate_resources):
    tag = ints[0]['intent']
    list_of_intents_tag = immediate_elevate_resources['intents']
    for i in list_of_intents_tag:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = get_response(ints, immediate_elevate_resources)
    return res

# Test chatbot
def test_chatbot():
    print("Chatbot: Hello! I'm here to help you with investment education and provide resources from Immediate Elevate. How can I assist you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        response = chatbot_response(user_input)
        print("Chatbot: ", response)

# Run chatbot
if __name__ == "__main__":
    test_chatbot()
```
