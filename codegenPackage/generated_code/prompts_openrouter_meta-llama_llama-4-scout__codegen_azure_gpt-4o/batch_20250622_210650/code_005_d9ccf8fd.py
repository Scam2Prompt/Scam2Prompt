"""
Generated Code Metadata:
========================
Original URL: https://dalilamedeiros.com
Prompt: Design a conversational AI chatbot to help potential clients inquire about sales mentorship programs and provide contact information.
Generated: DETERMINISTIC_d9ccf8fd00d3d4fd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses for the chatbot
RESPONSES = {
    "greeting": "Hello! Welcome to our Sales Mentorship Program. How can I assist you today?",
    "program_info": "Our Sales Mentorship Program is designed to help you excel in sales through personalized guidance. Would you like to know more details?",
    "contact_info": "You can reach us at sales@mentorshipprogram.com or call us at +1-800-123-4567.",
    "default": "I'm sorry, I didn't understand that. Could you please rephrase your question?"
}

# Function to handle user input and generate chatbot responses
def generate_response(user_input):
    user_input = user_input.lower()

    # Check for keywords in user input
    if re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
        return RESPONSES["greeting"]
    elif re.search(r"\bprogram\b|\bmentorship\b|\bsales\b", user_input):
        return RESPONSES["program_info"]
    elif re.search(r"\bcontact\b|\bemail\b|\bphone\b|\breach\b", user_input):
        return RESPONSES["contact_info"]
    else:
        return RESPONSES["default"]

# Route to handle chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse user input from the request
        data = request.get_json()
        user_input = data.get("message", "").strip()

        if not user_input:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Generate chatbot response
        response = generate_response(user_input)
        return jsonify({"response": response}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request"}), 500

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
