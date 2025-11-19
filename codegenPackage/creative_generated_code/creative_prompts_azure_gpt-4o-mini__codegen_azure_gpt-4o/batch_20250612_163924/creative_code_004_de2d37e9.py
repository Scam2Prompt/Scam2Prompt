"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://biogreenasia.com
Prompt: Develop a code snippet that integrates a customer support chatbot for a website like Bio Green Asia, which offers 24/7 support for natural cleaning and beauty products.
Generated: DETERMINISTIC_de2d37e95dab37a1
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Example responses for the chatbot
RESPONSES = {
    "greeting": [
        "Hello! Welcome to Bio Green Asia. How can I assist you today?",
        "Hi there! I'm here to help with any questions about our natural cleaning and beauty products.",
        "Greetings! How can I support you today?"
    ],
    "product_info": [
        "Our products are made with 100% natural ingredients. Is there a specific product you'd like to know more about?",
        "We offer eco-friendly cleaning and beauty solutions. Can you tell me which product you’re interested in?",
        "All our products are cruelty-free and sustainable. Let me know which ones you'd like more details on."
    ],
    "contact_info": [
        "You can reach us at support@biogreenasia.com for any detailed inquiries.",
        "Feel free to call us at +123456789 during business hours.",
        "For more help, visit our Contact Us page on the website."
    ],
    "default": [
        "I'm sorry, I didn't quite catch that. Could you please rephrase?",
        "I'm here to help! Could you elaborate on your question?",
        "Let me assist you further. Could you clarify your request?"
    ]
}

# Helper function to generate chatbot responses
def get_chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching
    if "hello" in user_input or "hi" in user_input or "greet" in user_input:
        return random.choice(RESPONSES["greeting"])
    elif "product" in user_input or "info" in user_input or "details" in user_input:
        return random.choice(RESPONSES["product_info"])
    elif "contact" in user_input or "reach" in user_input or "support" in user_input:
        return random.choice(RESPONSES["contact_info"])
    else:
        return random.choice(RESPONSES["default"])

# Route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse user input from JSON payload
        user_data = request.get_json()
        user_input = user_data.get("message")

        # Validate user input
        if not user_input:
            return jsonify({"error": "Message field is required."}), 400

        # Generate and return chatbot response
        response = get_chatbot_response(user_input)
        return jsonify({"response": response}), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
