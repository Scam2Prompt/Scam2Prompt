"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a chatbot using Python and NLP libraries to answer common queries about Darul Raza's services, such as Istikhara, Taweezat, and online courses.
Generated: DETERMINISTIC_add23cc060bb51ae
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from typing import Dict, List, Optional
import spacy
from spacy.matcher import PhraseMatcher
from flask import Flask, request, jsonify

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize Flask app
app = Flask(__name__)

# Knowledge base for Darul Raza services
KNOWLEDGE_BASE = {
    "greetings": [
        "Hello! Welcome to Darul Raza. How can I assist you today?",
        "Assalamu Alaikum! How may I help you with Darul Raza services?",
        "Hi there! What would you like to know about Darul Raza?"
    ],
    "istikhara": [
        "Istikhara is a special prayer for seeking guidance from Allah. Darul Raza provides Istikhara services where our scholars perform this prayer on your behalf.",
        "Istikhara at Darul Raza is conducted by qualified scholars who follow proper Islamic guidelines to seek divine guidance for your matters."
    ],
    "taweezat": [
        "Taweezat are Islamic amulets containing Quranic verses or prayers. Darul Raza provides authentic Taweez prepared by qualified scholars after proper assessment.",
        "Our Taweezat service involves careful selection of appropriate Quranic verses and prayers based on your situation, prepared by certified scholars."
    ],
    "courses": [
        "Darul Raza offers various online courses including Quranic studies, Islamic jurisprudence, and spiritual development programs.",
        "We provide structured online courses taught by qualified scholars covering topics like Tafseer, Hadith, Fiqh, and more."
    ],
    "contact": [
        "You can contact Darul Raza through our website contact form, email at info@darulraza.org, or phone at +1234567890.",
        "For inquiries, please visit our website or call our office during working hours."
    ],
    "location": [
        "Darul Raza is located at 123 Islamic Center Road, but most of our services are available online through our website.",
        "Our physical center is in the Islamic District, but we primarily serve students and clients worldwide through our online platforms."
    ],
    "fallback": [
        "I'm sorry, I didn't understand that. Could you rephrase your question about Darul Raza services?",
        "I'm not sure I follow. Could you ask about our services like Istikhara, Taweezat, or courses?",
        "I specialize in Darul Raza services. Could you ask about Istikhara, Taweezat, or our online courses?"
    ]
}

# Initialize phrase matcher for intent detection
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
for intent, phrases in [
    ("greetings", ["hello", "hi", "salam", "assalamu alaikum"]),
    ("istikhara", ["istikhara", "guidance prayer", "prayer for decision"]),
    ("taweezat", ["taweez", "taweezat", "islamic amulet", "ruqyah"]),
    ("courses", ["courses", "online classes", "learn islam", "quran course"]),
    ("contact", ["contact", "email", "phone", "address"]),
    ("location", ["location", "where are you", "address"])
]:
    patterns = [nlp(text) for text in phrases]
    matcher.add(intent, patterns)

def get_intent(user_input: str) -> str:
    """Determine the intent of the user's message."""
    doc = nlp(user_input.lower())
    matches = matcher(doc)
    
    if matches:
        match_id, start, end = matches[0]
        intent = nlp.vocab.strings[match_id]
        return intent
    
    # Check for keywords if no phrase match
    for token in doc:
        if token.text in ["istikhara", "taweez", "course"]:
            return token.text
        
    return "fallback"

def get_response(intent: str) -> str:
    """Get a random response for the given intent."""
    responses = KNOWLEDGE_BASE.get(intent, KNOWLEDGE_BASE["fallback"])
    return random.choice(responses)

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests."""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({"response": "Please provide a message."}), 400
            
        intent = get_intent(user_message)
        response = get_response(intent)
        
        return jsonify({"response": response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
