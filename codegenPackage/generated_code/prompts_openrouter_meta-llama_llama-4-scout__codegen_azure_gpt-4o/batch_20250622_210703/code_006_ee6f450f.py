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
import spacy
from spacy.matcher import PhraseMatcher

# Load the English language model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define a dictionary of situations/phrases and their corresponding proverbs
proverbs = {
    "hard work": "No pain, no gain.",
    "patience": "Good things come to those who wait.",
    "teamwork": "Many hands make light work.",
    "failure": "If at first you don't succeed, try, try again.",
    "opportunity": "Strike while the iron is hot.",
    "time": "Time and tide wait for no man.",
    "wisdom": "A stitch in time saves nine.",
    "money": "A penny saved is a penny earned.",
    "trust": "Don't put all your eggs in one basket.",
    "risk": "Fortune favors the bold."
}

# Preprocess the phrases for matching
phrase_patterns = [nlp.make_doc(key) for key in proverbs.keys()]
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ProverbMatcher", phrase_patterns)

def get_proverb(user_input):
    """
    Responds with a relevant proverb based on the user's input.

    Args:
        user_input (str): The situation or phrase provided by the user.

    Returns:
        str: A relevant proverb or a default message if no match is found.
    """
    try:
        # Process the user input
        doc = nlp(user_input.lower())
        
        # Match the input against the predefined phrases
        matches = matcher(doc)
        
        if matches:
            # Get the first match and return the corresponding proverb
            match_id, start, end = matches[0]
            matched_phrase = doc[start:end].text
            return proverbs[matched_phrase]
        else:
            # Default response if no match is found
            return "I'm sorry, I don't have a proverb for that situation."
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    print("Welcome to the Proverb Chatbot!")
    print("Type a situation or phrase, and I'll respond with a relevant proverb.")
    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = get_proverb(user_input)
        print(f"Chatbot: {response}")
```
