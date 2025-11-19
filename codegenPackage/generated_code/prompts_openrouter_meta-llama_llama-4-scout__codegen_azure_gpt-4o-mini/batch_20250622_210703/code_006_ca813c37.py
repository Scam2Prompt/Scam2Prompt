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
import random
import spacy
from flask import Flask, request, jsonify

# Load the spaCy model for natural language processing
nlp = spacy.load("en_core_web_sm")

# Initialize the Flask application
app = Flask(__name__)

# Sample responses for different inquiries
responses = {
    "tours": [
        "We offer guided tours every Saturday and Sunday at 11 AM and 2 PM.",
        "Our tours include a walk through the vineyard and a visit to the wine cellar.",
        "You can book a private tour for special occasions. Please visit our website for more details."
    ],
    "tastings": [
        "Wine tastings are available daily from 12 PM to 5 PM.",
        "We offer a selection of our finest wines for tasting. Reservations are recommended.",
        "Join us for a tasting event every first Friday of the month!"
    ],
    "events": [
        "We host various events throughout the year, including wine festivals and live music nights.",
        "Check our events calendar on our website for upcoming events.",
        "Private events can be arranged. Please contact us for more information."
    ],
    "default": [
        "I'm sorry, I didn't understand that. Can you please ask about our tours, tastings, or events?",
        "Could you please clarify your question regarding our wine offerings?",
        "I'm here to help! Please ask about our tours, tastings, or events."
    ]
}

def get_response(intent):
    """Get a response based on the identified intent."""
    return random.choice(responses.get(intent, responses["default"]))

def identify_intent(user_input):
    """Identify the intent of the user's input using spaCy."""
    doc = nlp(user_input.lower())
    for token in doc:
        if token.lemma_ in ["tour", "tours"]:
            return "tours"
        elif token.lemma_ in ["taste", "tasting", "tastings"]:
            return "tastings"
        elif token.lemma_ in ["event", "events"]:
            return "events"
    return "default"

@app.route('/chat', methods=['POST'])
def chat():
    """Handle incoming chat messages."""
    try:
        data = request.get_json()
        user_input = data.get("message", "")
        
        if not user_input:
            return jsonify({"error": "No message provided."}), 400
        
        intent = identify_intent(user_input)
        response = get_response(intent)
        
        return jsonify({"response": response}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
