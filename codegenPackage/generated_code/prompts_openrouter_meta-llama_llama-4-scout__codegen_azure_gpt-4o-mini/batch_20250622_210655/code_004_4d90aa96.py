"""
Generated Code Metadata:
========================
Original URL: https://www.nkatandiinyom.com
Prompt: Create a chatbot that provides guidance on conflict resolution and leadership development for women in Igbo communities, using a knowledge base from Nkata ndi Inyom Igbo.
Generated: DETERMINISTIC_4d90aa96de926d07
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception("Knowledge base file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON from the knowledge base file.")

# Initialize the knowledge base
knowledge_base = load_knowledge_base('nkata_ndi_inyom_igbo.json')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages.
    Expects a JSON payload with a 'message' key.
    Returns a response based on the knowledge base.
    """
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Message is required."}), 400
        
        # Simple keyword matching for responses
        response = get_response(user_message)
        return jsonify({"response": response}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_response(user_message):
    """
    Generate a response based on the user's message.
    Uses keyword matching to find relevant information in the knowledge base.
    """
    user_message = user_message.lower()
    
    # Check for keywords in the user's message
    for topic, responses in knowledge_base.items():
        if topic in user_message:
            return random.choice(responses)
    
    return "I'm sorry, I don't have information on that topic. Can you ask something else?"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```

**Note:** Ensure you have a JSON file named `nkata_ndi_inyom_igbo.json` in the same directory as this script, containing a structured knowledge base. The structure should be a dictionary where keys are topics and values are lists of responses.
