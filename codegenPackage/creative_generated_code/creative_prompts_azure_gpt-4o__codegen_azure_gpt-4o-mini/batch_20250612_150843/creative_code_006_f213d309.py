"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-bitwave.com
Prompt: Develop a chatbot using Python that answers FAQs about Immediate Bitwave, such as registration costs, supported countries, and the types of investment education offered.
Generated: DETERMINISTIC_f213d309a43dbc55
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, request, jsonify

# Initialize Flask application
app = Flask(__name__)

# Load FAQs from a JSON file
def load_faqs(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: The JSON file is not properly formatted.")
        return {}

# FAQs data
faq_data = load_faqs('faqs.json')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint for the chatbot to receive user messages and respond
    with appropriate FAQ answers.
    """
    try:
        # Get the user's message from the request
        user_message = request.json.get('message', '').lower()

        # Simple keyword matching to find an answer
        for question, answer in faq_data.items():
            if question.lower() in user_message:
                return jsonify({"response": answer})

        # If no matching question was found, provide a fallback response
        return jsonify({"response": "I'm sorry, I don't have an answer for that. Please check our website for more information."})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
```

```json
// faqs.json
{
    "What are the registration costs?": "The registration costs for Immediate Bitwave are $100.",
    "Which countries are supported?": "Immediate Bitwave supports users from over 50 countries, including the USA, Canada, and UK.",
    "What types of investment education are offered?": "We offer courses on cryptocurrency trading, risk management, and market analysis."
}
```
