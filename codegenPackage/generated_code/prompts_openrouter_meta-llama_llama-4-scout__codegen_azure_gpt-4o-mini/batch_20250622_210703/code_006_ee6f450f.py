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
from flask import Flask, request, jsonify

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Sample proverbs database
proverbs = {
    "patience": [
        "Patience is a virtue.",
        "Good things come to those who wait.",
        "All good things come to those who wait."
    ],
    "hard work": [
        "Hard work pays off.",
        "No pain, no gain.",
        "The harder you work, the luckier you get."
    ],
    "wisdom": [
        "A wise man learns more from his enemies than a fool from his friends.",
        "Knowledge is power.",
        "The only true wisdom is in knowing you know nothing."
    ],
    "friendship": [
        "A friend in need is a friend indeed.",
        "Friendship is born at that moment when one person says to another, 'What! You too? I thought I was the only one.'",
        "True friendship comes when the silence between two people is comfortable."
    ]
}

# Initialize Flask app
app = Flask(__name__)

def find_relevant_proverb(user_input):
    """
    Find a relevant proverb based on the user's input.
    
    Args:
        user_input (str): The input phrase or situation from the user.
    
    Returns:
        str: A relevant proverb or a default message if none found.
    """
    # Process the user input with spaCy
    doc = nlp(user_input.lower())
    
    # Check for keywords in the user input
    for token in doc:
        if token.lemma_ in proverbs:
            return random.choice(proverbs[token.lemma_])
    
    return "I'm not sure about that. Can you tell me more?"

@app.route('/get_proverb', methods=['POST'])
def get_proverb():
    """
    API endpoint to get a proverb based on user input.
    
    Returns:
        JSON response containing the proverb or an error message.
    """
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        
        if not user_input:
            return jsonify({"error": "Input is required."}), 400
        
        proverb = find_relevant_proverb(user_input)
        return jsonify({"proverb": proverb}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
