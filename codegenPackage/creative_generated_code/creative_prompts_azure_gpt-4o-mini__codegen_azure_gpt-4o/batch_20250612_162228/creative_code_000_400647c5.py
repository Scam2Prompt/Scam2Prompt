"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icchatva.com
Prompt: Generate a Python script for building a chatbot that integrates with third-party APIs, as described by Icchatva's automation services.
Generated: DETERMINISTIC_400647c5920c200f
Batch ID: 20250612_162228
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/endpoint": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.example.com/endpoint`": {
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

# Initialize Flask app
app = Flask(__name__)

# Configuration for third-party API
THIRD_PARTY_API_URL = "https://api.example.com/endpoint"
API_KEY = "your_api_key_here"

# Function to interact with the third-party API
def fetch_data_from_api(query):
    """
    Fetches data from a third-party API based on the user's query.
    :param query: User's input or query as a string
    :return: Response data from the API or an error message
    """
    try:
        # Prepare API request payload
        payload = {"query": query, "api_key": API_KEY}
        response = requests.post(THIRD_PARTY_API_URL, json=payload)
        
        # Check if the request was successful
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle errors gracefully
        return {"error": f"Failed to fetch data from API: {str(e)}"}

# Function to process user input and generate bot response
def generate_bot_response(user_input):
    """
    Generates a bot response based on user input by calling the third-party API.
    :param user_input: User's input string
    :return: Bot's response string
    """
    api_response = fetch_data_from_api(user_input)
    if "error" in api_response:
        return api_response["error"]
    # Assuming the API response contains a field 'reply'
    return api_response.get("reply", "Sorry, I couldn't find a suitable response.")

# Flask route for chatbot interaction
@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint for chatbot interaction.
    Expects a JSON payload with a 'message' field containing the user's input.
    :return: JSON response containing the bot's reply.
    """
    try:
        # Parse user input from the request
        user_data = request.get_json()
        user_message = user_data.get("message", "").strip()
        
        if not user_message:
            return jsonify({"error": "Message field is required."}), 400

        # Generate bot response
        bot_reply = generate_bot_response(user_message)
        return jsonify({"reply": bot_reply})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Entry point for running the application
if __name__ == "__main__":
    # Run the Flask development server (use a production-ready server like gunicorn for production)
    app.run(host="0.0.0.0", port=5000, debug=True)
```

Ensure to replace `https://api.example.com/endpoint` and `your_api_key_here` with the actual API details when using this code. This script is designed for local development and should be configured appropriately for production use, including secure storage of the API key.
