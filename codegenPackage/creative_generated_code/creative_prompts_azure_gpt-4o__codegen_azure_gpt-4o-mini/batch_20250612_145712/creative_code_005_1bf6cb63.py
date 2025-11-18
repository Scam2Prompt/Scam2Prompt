"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe.pages.dev
Prompt: Develop a chatbot that integrates with the MIND of Pepe AI agent to answer FAQs about staking, token claiming, and presale participation.
Generated: DETERMINISTIC_1bf6cb636110234d
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.INFO)

# Example FAQs for the chatbot
FAQs = {
    "staking": {
        "question": "What is staking?",
        "answer": "Staking is the process of actively participating in transaction validation (similar to mining) on a proof-of-stake (PoS) blockchain."
    },
    "token_claiming": {
        "question": "How do I claim my tokens?",
        "answer": "To claim your tokens, you need to connect your wallet and follow the instructions provided in the claiming portal."
    },
    "presale_participation": {
        "question": "How can I participate in the presale?",
        "answer": "To participate in the presale, ensure you have the required tokens in your wallet and follow the steps outlined on our presale page."
    },
}

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    """
    Endpoint to receive user queries and return responses based on FAQs.
    Expected JSON format:
    {
        "query": "User's question"
    }
    """
    try:
        # Get the query from the request
        data = request.get_json()
        query = data.get('query')

        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        # Search for the relevant FAQ
        response = find_faq_response(query)

        if response:
            return jsonify({"response": response}), 200
        else:
            return jsonify({"response": "I'm sorry, I don't have an answer for that question."}), 404

    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500

def find_faq_response(query):
    """
    Find and return a response based on the FAQ database.
    
    Args:
        query (str): User's question.
    
    Returns:
        str: The answer to the FAQ or None if not found.
    """
    for key, faq in FAQs.items():
        if key in query.lower():
            return faq['answer']
    return None

if __name__ == '__main__':
    # Run the Flask app
    # Use the environment variable for the port or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

Make sure to install the required packages with:
```bash
pip install Flask Flask-Cors
```

This code snippet sets up a simple chatbot using Flask, which responds to FAQs about staking, token claiming, and presale participation. It includes proper error handling and logging for robustness.
