"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter-git-remove-any-collateral-withdrawal-wowcats.vercel.app
Prompt: Create a chatbot integration that allows users to "Talk to us" for support regarding the Jupiter Trade platform's features like Swap, Limit Order, DCA, and Bridge.
Generated: DETERMINISTIC_6ff2c5cc953cce5b
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API Key (Ensure this is securely stored in an environment variable in production)
OPENAI_API_KEY = "your_openai_api_key_here"
openai.api_key = OPENAI_API_KEY

# Function to send a message to OpenAI GPT and get a response
def get_chatbot_response(user_message):
    try:
        # Call OpenAI's GPT model
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a specific model; adjust if needed
            prompt=f"You are a support chatbot for the Jupiter Trade platform. Help users regarding Swap, Limit Order, DCA, and Bridge features. User: {user_message}",
            max_tokens=200,  # Adjust token limit as needed
            temperature=0.7,  # Control response randomness
            top_p=1,  # Use Top-p sampling for the response
            frequency_penalty=0,  # Adjust penalties as needed
            presence_penalty=0,  # Adjust penalties as needed
        )
        # Extract and return the text response
        return response.choices[0].text.strip()
    except Exception as e:
        # Log error and return a user-friendly error message
        print(f"Error in OpenAI API call: {e}")
        return "Sorry, I couldn't process your request at the moment. Please try again later."

# Route for chatbot interaction
@app.route('/talk-to-us', methods=['POST'])
def talk_to_us():
    try:
        # Parse the user's message from the request
        data = request.json
        user_message = data.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Get response from the chatbot
        chatbot_response = get_chatbot_response(user_message)

        # Return the chatbot's response
        return jsonify({"response": chatbot_response}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error in /talk-to-us endpoint: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Run the Flask app on port 5000 (adjust as necessary)
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Deployment Notes:
1. Replace `"your_openai_api_key_here"` with the actual OpenAI API key or use environment variables.
2. Remove `debug=False` for production deployment.
3. Use HTTPS for secure communication in production.
4. Ensure rate-limiting and authentication if deploying publicly.
