"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Develop a simple chatbot using natural language processing (NLP) to provide basic support and guidance for individuals seeking marriage counseling.
Generated: DETERMINISTIC_ec4fa4c51bc5ea70
Batch ID: 20250622_212850
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
with open('marriage_counseling_chatbot_data.json') as file:
    data = json.load(file)

# Preprocess data
for intent in data['intents']:
    for pattern in intent['patterns']:
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize words
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(list(set(words)))

# Sort classes
classes = sorted(list(set(classes)))

# Save words and classes to pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Create training and output data
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        if word in word_patterns:
            bag.append(1)
        else:
            bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1

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
model.save('marriage_counseling_chatbot_model.h5', hist)

# Function to clean up sentence
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# Function to bag words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for se in sentence_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return np.array(bag)

# Function to predict class
def predict_class(sentence):
    p = bag_of_words(sentence)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Function to get response
def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents_tag = intents_json['intents']
    result = None
    for i in list_of_intents_tag:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Function to chat
def chat():
    print("Marriage Counseling Chatbot: I'm here to help. How can I assist you today?")
    while True:
        message = input("You: ")
        if not message:
            print("Marriage Counseling Chatbot: Please enter a message.")
            continue

        ints = predict_class(message)
        response = get_response(ints, data)
        print("Marriage Counseling Chatbot: ", response)

# Run chat function
if __name__ == '__main__':
    chat()
```

**marriage_counseling_chatbot_data.json**
```json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hey", "Hello"],
            "responses": ["Hi, I'm here to help. How can I assist you today?", "Hello! What's on your mind?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later", "Goodbye"],
            "responses": ["It was nice chatting with you. Goodbye!", "See you later!"]
        },
        {
            "tag": "marriage_problems",
            "patterns": ["I'm having problems in my marriage", "My marriage is struggling"],
            "responses": ["I'm sorry to hear that. Can you tell me more about what's going on?", "That sounds tough. What seems to be the issue?"]
        },
        {
            "tag": "communication_issues",
            "patterns": ["We don't communicate well", "Communication is a problem"],
            "responses": ["Effective communication is key to a healthy marriage. Have you tried active listening?", "That's a common issue. Have you considered couples therapy?"]
        }
    ]
}
```
