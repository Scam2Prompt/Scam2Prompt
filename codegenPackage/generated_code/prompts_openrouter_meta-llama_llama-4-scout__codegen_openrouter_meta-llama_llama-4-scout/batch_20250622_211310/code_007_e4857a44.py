"""
Generated Code Metadata:
========================
Original URL: https://immediatecodeai.io
Prompt: Develop a chatbot that provides investment education and answers frequently asked questions about investment topics, using a natural language processing library such as NLTK or spaCy.
Generated: DETERMINISTIC_e4857a44cf004400
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
from nltk.tokenize import word_tokenize
import spacy
from spacy import displacy
import random

# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define a class for the investment chatbot
class InvestmentChatbot:
    def __init__(self):
        # Initialize a dictionary of intents and responses
        self.intents = {
            'greeting': {
                'patterns': ['hi', 'hello', 'hey'],
                'responses': ['Hello! How can I help you with investment education today?', 
                               'Hi! What\'s on your mind about investing?']
            },
            'investment_types': {
                'patterns': ['what are the types of investments', 'investment types'],
                'responses': ['There are several types of investments, including stocks, bonds, ETFs, mutual funds, and real estate.',
                               'Investment types include stocks, bonds, ETFs, mutual funds, and real estate.']
            },
            'risk_management': {
                'patterns': ['how to manage risk', 'risk management'],
                'responses': ['To manage risk, consider diversifying your portfolio, setting stop-loss orders, and conducting thorough research.',
                               'Risk management strategies include diversification, stop-loss orders, and thorough research.']
            }
        }

    def process_input(self, input_text):
        # Tokenize the input text
        tokens = word_tokenize(input_text)

        # Lemmatize the tokens
        lemmatizer = WordNetLemmatizer()
        lemmas = [lemmatizer.lemmatize(token.lower()) for token in tokens]

        # Process the input text using spaCy
        doc = nlp(input_text)

        # Determine the intent of the input text
        intent = self.determine_intent(lemmas)

        # Generate a response based on the intent
        response = self.generate_response(intent)

        return response

    def determine_intent(self, lemmas):
        # Iterate over the intents and check for matching patterns
        for intent, patterns_responses in self.intents.items():
            for pattern in patterns_responses['patterns']:
                pattern_lemmas = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(pattern)]
                if set(pattern_lemmas).issubset(set(lemmas)):
                    return intent

        # Default intent if no match is found
        return 'unknown'

    def generate_response(self, intent):
        if intent in self.intents:
            return random.choice(self.intents[intent]['responses'])
        else:
            return 'I\'m not sure I understand your question. Can you please rephrase?'

def main():
    chatbot = InvestmentChatbot()

    while True:
        user_input = input('User: ')
        if user_input.lower() == 'quit':
            break
        response = chatbot.process_input(user_input)
        print('Chatbot: ', response)

if __name__ == '__main__':
    main()
```
