"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reward-yoracle.pages.dev
Prompt: Create a chatbot interface that connects to the $YAI Oracle API, allowing users to ask questions about current market trends, alpha opportunities, and sentiment analysis.
Generated: DETERMINISTIC_8fc429334953e361
Batch ID: 20250612_153420
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
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Fetch API key and endpoint from environment variables
API_KEY = os.getenv("YAI_ORACLE_API_KEY")
API_ENDPOINT = os.getenv("YAI_ORACLE_API_ENDPOINT")

# Error if environment variables are missing
if not API_KEY or not API_ENDPOINT:
    raise ValueError("Missing API_KEY or API_ENDPOINT in environment variables.")

def query_yai_oracle(question):
    """
    Send a question to the $YAI Oracle API and return the response.
    
    Args:
        question (str): The user's question about market trends, alpha opportunities, or sentiment analysis.
        
    Returns:
        dict: JSON response from the $YAI Oracle API.
    """
    try:
        # Prepare headers and payload for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        payload = {
            "question": question
        }
        
        # Make the API request
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Parse and return the JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Handle specific request exceptions
        return {"error": f"An error occurred while querying the API: {str(e)}"}

@app.route('/chatbot', methods=['POST'])
def chatbot_interface():
    """
    Flask route to handle chatbot queries.
    
    Expected input:
        JSON payload with a "question" field.
        
    Returns:
        JSON response from the $YAI Oracle API or an error message.
    """
    try:
        # Extract the question from the request payload
        data = request.get_json()
        if not data or "question" not in data:
            return jsonify({"error": "Invalid request. Please provide a 'question' field."}), 400
        
        question = data["question"]
        
        # Query the $YAI Oracle API
        api_response = query_yai_oracle(question)
        
        # Return the API response to the client
        return jsonify(api_response)
    
    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """
    Healthcheck route to verify the server is running.
    
    Returns:
        JSON response indicating the server's health status.
    """
    return jsonify({"status": "ok", "message": "Chatbot server is running."})

if __name__ == '__main__':
    # Run Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
```
