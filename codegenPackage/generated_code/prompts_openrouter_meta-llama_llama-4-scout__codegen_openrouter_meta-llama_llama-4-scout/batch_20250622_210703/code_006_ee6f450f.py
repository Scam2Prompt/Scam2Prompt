"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Use the Learn English Simply's Proverb section to create a chatbot that responds with a relevant proverb when given a situation or phrase, using a library like NLTK or spaCy.
Generated: DETERMINISTIC_ee6f450fd1c4b819
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
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import spacy
import random

# Load the spacy model for natural language processing
nlp = spacy.load('en_core_web_sm')

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Define a dictionary of proverbs with their corresponding situations or phrases
proverbs = {
    "a bird in the hand is worth two in the bush": ["safety", "security", "caution", "opportunity cost"],
    "actions speak louder than words": ["actions", "inaction", "results", "effort"],
    "all's fair in love and war": ["love", "war", "conflict", "morality"],
    "an eye for an eye": ["revenge", "retribution", "punishment", "justice"],
    "blood is thicker than water": ["family", "loyalty", "obligation", "relationships"],
    # Add more proverbs here...
}

# Preprocess the proverbs and their situations/phrases
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Preprocess text by tokenizing, lemmatizing, and removing stop words"""
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return tokens

def get_proverb(situation):
    """Get a relevant proverb based on the given situation"""
    situation_tokens = preprocess_text(situation)
    situation = ' '.join(situation_tokens)

    best_match = None
    best_score = 0

    for proverb, keywords in proverbs.items():
        # Calculate the similarity between the situation and the proverb's keywords
        proverb_tokens = preprocess_text(' '.join(keywords))
        similarity = len(set(situation_tokens) & set(proverb_tokens)) / len(set(proverb_tokens))
        if similarity > best_score:
            best_score = similarity
            best_match = proverb

    return best_match

def chatbot_response(situation):
    """Generate a chatbot response with a relevant proverb"""
    proverb = get_proverb(situation)
    if proverb:
        return f"In that situation, remember that '{proverb}'."
    else:
        return "I'm not sure I have a proverb for that situation."

def main():
    # Test the chatbot
    while True:
        situation = input("Enter a situation or phrase: ")
        if situation.lower() == "quit":
            break
        print(chatbot_response(situation))

if __name__ == "__main__":
    main()
```
