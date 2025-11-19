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
import random
import spacy
from spacy.matcher import PhraseMatcher

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Proverb database
proverbs = {
    "persistence": [
        "Rome wasn't built in a day.",
        "Where there's a will, there's a way.",
        "Slow and steady wins the race."
    ],
    "friendship": [
        "A friend in need is a friend indeed.",
        "Birds of a feather flock together.",
        "A man is known by the company he keeps."
    ],
    "money": [
        "A penny saved is a penny earned.",
        "Money doesn't grow on trees.",
        "Don't put all your eggs in one basket."
    ],
    "wisdom": [
        "Look before you leap.",
        "Don't count your chickens before they hatch.",
        "The early bird catches the worm."
    ],
    "general": [
        "Actions speak louder than words.",
        "Better late than never.",
        "Honesty is the best policy."
    ]
}

# Keywords for each category
keywords = {
    "persistence": ["try", "effort", "hard", "difficult", "keep going", "don't give up"],
    "friendship": ["friend", "friends", "buddy", "companion", "relationship"],
    "money": ["money", "cash", "rich", "poor", "wealth", "finance"],
    "wisdom": ["wise", "smart", "intelligent", "think", "decision"]
}

def setup_matcher():
    """Initialize the phrase matcher with keywords"""
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    for category, phrases in keywords.items():
        patterns = [nlp(text) for text in phrases]
        matcher.add(category, patterns)
    return matcher

matcher = setup_matcher()

def get_relevant_proverb(user_input):
    """Find the most relevant proverb based on user input"""
    doc = nlp(user_input.lower())
    matches = matcher(doc)
    
    if matches:
        # Get the highest scoring match
        match_id, start, end = max(matches, key=lambda x: x[1])
        category = nlp.vocab.strings[match_id]
        return random.choice(proverbs[category])
    else:
        return random.choice(proverbs["general"])

def chatbot():
    """Interactive chatbot that responds with proverbs"""
    print("Welcome to the Proverb Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        proverb = get_relevant_proverb(user_input)
        print(f"Chatbot: {proverb}")

if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt:
        print("\nChatbot session ended by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
