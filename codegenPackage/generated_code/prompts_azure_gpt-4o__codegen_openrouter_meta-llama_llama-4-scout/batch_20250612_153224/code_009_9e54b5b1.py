"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Write code for a chatbot that provides information about multidisciplinary therapy services, including ABA-based approaches, logopedia, and physiotherapy, inspired by Centro Abakadabra's offerings.
Generated: DETERMINISTIC_9e54b5b1b7bf24a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class TherapyService:
    """Base class for therapy services"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_info(self):
        return f"{self.name}: {self.description}"

class ABATherapy(TherapyService):
    """ABA-based therapy service"""
    def __init__(self):
        super().__init__("ABA-based Therapy", "Applied Behavior Analysis (ABA) is a scientific approach to understanding behavior.")

class Logopedia(TherapyService):
    """Logopedia therapy service"""
    def __init__(self):
        super().__init__("Logopedia", "Logopedia is a therapeutic approach that focuses on the assessment, diagnosis, and treatment of communication disorders.")

class Physiotherapy(TherapyService):
    """Physiotherapy service"""
    def __init__(self):
        super().__init__("Physiotherapy", "Physiotherapy is a healthcare profession that focuses on the prevention, diagnosis, and treatment of disorders and injuries affecting physical function.")

class Chatbot:
    """Multidisciplinary therapy services chatbot"""
    def __init__(self):
        self.services = {
            "aba": ABATherapy(),
            "logopedia": Logopedia(),
            "physiotherapy": Physiotherapy()
        }

    def get_service_info(self, service_name):
        try:
            service = self.services[service_name.lower()]
            return service.get_info()
        except KeyError:
            return f"Sorry, we don't have information about {service_name} therapy service."

    def handle_user_input(self, user_input):
        try:
            user_input = json.loads(user_input)
            if "service" in user_input:
                return self.get_service_info(user_input["service"])
            else:
                return "Please provide a service name."
        except json.JSONDecodeError:
            return "Invalid input format. Please use JSON."

def main():
    chatbot = Chatbot()
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.handle_user_input(user_input)
        print("Chatbot: ", response)

if __name__ == "__main__":
    main()
```

```python
# Alternatively, if you want a more advanced chatbot using Natural Language Processing (NLP)
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

with open('intents.json') as file:
    data = json.load(file)

for intent in data['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []

    w = doc[0]
    w = [lemmatizer.lemmatize(word.lower()) for word in w]
    for se in w:
        if se in words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)

model.save('chatbot_model.h5', hist)

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np

from keras.models import load_model

model = load_model('chatbot_model.h5')
import nltk
nltk.download('punkt')

with open('intents.json') as file:
    data = json.load(file)

try:
    model = load_model('chatbot_model.h5')
except:
    pass

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)  
    for se in sentence_words:
        for i,w in enumerate(words):
            if w == se: 
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
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
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
    res = get_response(ints, data)
    return res

def main():
    print("Welcome to the chatbot! Type quit to exit.")
    while True:
        inp = input("User: ")
        if inp.lower() == "quit":
            break
        response = chatbot_response(inp)
        print("Chatbot: ", response)

if __name__ == "__main__":
    main()
```
