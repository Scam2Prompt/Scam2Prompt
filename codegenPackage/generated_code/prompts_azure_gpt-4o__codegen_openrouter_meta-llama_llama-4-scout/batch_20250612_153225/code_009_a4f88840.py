"""
Generated Code Metadata:
========================
Original URL: https://theprintnan.app
Prompt: Develop a chatbot that uses AI to assist customers in choosing printing services and calculating costs for items like self-inking stamps, die-cut stickers, and product labels, based on ThePrintNan's offerings.
Generated: DETERMINISTIC_a4f88840b6f90b9c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import pickle
import string

# Load the chatbot model
try:
    model = load_model('chatbot_model.h5')
except Exception as e:
    print(f"Error loading model: {e}")

# Load the tokenizer and label encoder
try:
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
except Exception as e:
    print(f"Error loading tokenizer: {e}")

try:
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
except Exception as e:
    print(f"Error loading label encoder: {e}")

# Define a function to preprocess user input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input)
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.lower() not in stop_words and t not in string.punctuation]
    
    # Convert to lowercase
    tokens = [t.lower() for t in tokens]
    
    # Pad the sequence
    sequence = tokenizer.texts_to_sequences([tokens])[0]
    padded_sequence = pad_sequences([sequence], maxlen=20)[0]
    
    return padded_sequence

# Define a function to generate chatbot response
def generate_response(user_input):
    try:
        # Preprocess the input
        input_sequence = preprocess_input(user_input)
        
        # Make a prediction
        prediction = model.predict(np.array([input_sequence]))
        
        # Get the predicted label
        predicted_label = label_encoder.inverse_transform(np.argmax(prediction, axis=1))[0]
        
        # Define a dictionary of responses
        responses = {
            'greeting': 'Hello! How can I assist you today?',
            'printing_services': 'We offer self-inking stamps, die-cut stickers, and product labels. Which one are you interested in?',
            'self_inking_stamps': 'Our self-inking stamps are $5 each. Would you like to calculate the cost?',
            'die_cut_stickers': 'Our die-cut stickers start at $10 for a pack of 100. Would you like to calculate the cost?',
            'product_labels': 'Our product labels start at $20 for a pack of 500. Would you like to calculate the cost?',
            'calculate_cost': 'Please provide the quantity you would like to order, and I will calculate the cost for you.',
            'goodbye': 'Thank you for using our chatbot! Have a great day.'
        }
        
        # Return the response
        return responses.get(predicted_label, 'I didn\'t understand that. Can you please rephrase?')
    except Exception as e:
        print(f"Error generating response: {e}")
        return 'I didn\'t understand that. Can you please rephrase?'

# Define a function to calculate cost
def calculate_cost(item, quantity):
    try:
        # Define a dictionary of prices
        prices = {
            'self_inking_stamps': 5,
            'die_cut_stickers': 10,
            'product_labels': 20
        }
        
        # Calculate the cost
        cost = prices.get(item, 0) * quantity
        
        # Return the cost
        return f"The total cost is ${cost:.2f}."
    except Exception as e:
        print(f"Error calculating cost: {e}")
        return 'Error calculating cost. Please try again.'

# Define the main chatbot function
def chatbot():
    print("Welcome to ThePrintNan chatbot!")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'quit':
            print(generate_response(user_input))
            break
        
        response = generate_response(user_input)
        print("Chatbot:", response)
        
        if 'calculate cost' in response.lower():
            item = input("What item would you like to calculate the cost for? (self_inking_stamps, die_cut_stickers, product_labels): ")
            quantity = int(input("How many would you like to order? "))
            cost_response = calculate_cost(item, quantity)
            print("Chatbot:", cost_response)

# Run the chatbot
if __name__ == '__main__':
    chatbot()
```
