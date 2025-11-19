"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Generate a Python script for building a chatbot that integrates with third-party APIs, as described by Icchatva's automation services.
Generated: DETERMINISTIC_400647c5920c200f
Batch ID: 20250612_162228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/chat": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuration for third-party API integration
API_URL = "https://api.example.com/chat"  # Replace with the actual API endpoint
API_KEY = "your_api_key_here"  # Replace with your API key

def get_chatbot_response(user_message):
    """
    Sends user message to the third-party API and retrieves the chatbot's response.

    Parameters:
    - user_message (str): The message input from the user.

    Returns:
    - str: The response from the chatbot.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": user_message
    }
    
    try:
        # Send POST request to the third-party API
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        response_data = response.json()  # Parse the JSON response

        # Extract and return the chatbot's reply
        return response_data.get("reply", "Sorry, I didn't understand that.")
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        return f"Error communicating with chatbot service: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat requests.

    Returns:
    - JSON response: The chatbot's reply to the user's message.
    """
    # Use try-except to handle potential JSON parsing errors
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Missing 'message' field."}), 400

        # Get response from the chatbot
        chatbot_reply = get_chatbot_response(user_message)

        # Return the chatbot's response as JSON
        return jsonify({"reply": chatbot_reply}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)  # Set debug=False for production
```

Make sure to replace the placeholder values for `API_URL` and `API_KEY` with actual values from the third-party service you are integrating with. Additionally, review the security practices when deploying the application in a production environment.
