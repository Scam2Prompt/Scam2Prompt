"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hulashxcore.org
Prompt: Create a chatbot using Smartsupp or similar platforms to provide 24/7 customer support for users of hulashxcore.org, focusing on investment plan inquiries and withdrawal processes.
Generated: DETERMINISTIC_eff966966a04b386
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a simple structure for the chatbot responses
chatbot_responses = {
    "investment": {
        "info": "We offer various investment plans tailored to your needs. Please visit our investment plans page for more details.",
        "withdrawal": "To withdraw your funds, please follow the instructions in your account dashboard."
    },
    "withdrawal": {
        "info": "You can request a withdrawal at any time through your account dashboard.",
        "status": "Withdrawal requests typically take 1-3 business days to process."
    },
    "default": "I'm sorry, I didn't understand that. Please ask about our investment plans or withdrawal processes."
}

# Endpoint to handle incoming chat messages
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Extract user message from the request
        user_message = request.json.get('message', '').lower()

        # Determine the appropriate response based on keywords in the user message
        if 'investment' in user_message:
            response = chatbot_responses['investment']['info']
        elif 'withdrawal' in user_message:
            response = chatbot_responses['withdrawal']['info']
        else:
            response = chatbot_responses['default']

        return jsonify({"response": response}), 200

    except Exception as e:
        # Log the error message for debugging
        print(f"Error processing the chat message: {e}")
        return jsonify({"error": "An error occurred, please try again later."}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Instructions for Deployment:
1. Ensure that you have Flask installed in your environment. You can install it using pip:
   ```bash
   pip install Flask
   ```
2. Save the above code in a file named `chatbot.py`.
3. Run the chatbot server using the command:
   ```bash
   python chatbot.py
   ```
4. Set up a Smartsupp or similar widget to send requests to the `/chat` endpoint for handling user inquiries.
