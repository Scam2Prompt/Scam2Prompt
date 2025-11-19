"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Develop a chatbot script to handle customer inquiries about wine tours, tastings, and events at a winery like Kadma Wine, using a natural language processing library like NLTK or spaCy."
Generated: DETERMINISTIC_ca813c373edab3ee
Batch ID: 20250622_210703
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
from nltk.tokenize import word_tokenize
import spacy
from spacy import displacy
import random

# Load the spacy model for natural language processing
nlp = spacy.load('en_core_web_sm')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define intents and responses
intents = {
    'greeting': {
        'patterns': ['hi', 'hello', 'hey'],
        'responses': ['Hello! Welcome to Kadma Wine.', 'Hi! How can I assist you today?', 'Hey! What brings you to our winery?']
    },
    'tours': {
        'patterns': ['tour', 'tours', 'wine tour'],
        'responses': ['We offer guided wine tours daily at 10am and 2pm. Would you like to book one?', 'Our wine tours last 1.5 hours and include a tasting.']
    },
    'tastings': {
        'patterns': ['tasting', 'wine tasting'],
        'responses': ['We have a variety of wine tastings available, including our popular flight of 5 wines.']
    },
    'events': {
        'patterns': ['events', 'wine events'],
        'responses': ['We host various events throughout the year, including wine and cheese pairings. Check our website for upcoming events.']
    },
    'hours': {
        'patterns': ['hours', 'winery hours'],
        'responses': ['Our winery is open daily from 10am-5pm.']
    },
    'default': {
        'patterns': [],
        'responses': ['Sorry, I didn\'t understand that. Can you please rephrase?', 'I\'m not sure I understand. Can you provide more context?']
    }
}

# Update default patterns to catch any unknown input
default_patterns = ['unknown', 'not sure', 'help']
intents['default']['patterns'].extend(default_patterns)

# Function to process user input
def process_input(user_input):
    try:
        # Tokenize and lemmatize user input
        doc = nlp(user_input.lower())
        tokens = [token.text for token in doc]
        lemmas = [lemmatizer.lemmatize(token) for token in tokens]

        # Check for matching intents
        for intent, data in intents.items():
            for pattern in data['patterns']:
                if pattern in lemmas:
                    return random.choice(data['responses'])

        # If no match found, return default response
        return random.choice(intents['default']['responses'])

    except Exception as e:
        # Log and handle any exceptions
        print(f"An error occurred: {e}")
        return "An error occurred. Please try again later."

# Main function to interact with the chatbot
def chatbot():
    print("Welcome to Kadma Wine Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = process_input(user_input)
        print("Chatbot: ", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
