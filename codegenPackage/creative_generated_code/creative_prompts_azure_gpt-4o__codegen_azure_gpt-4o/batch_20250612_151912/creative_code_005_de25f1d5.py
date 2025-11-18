"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bettermost.net
Prompt: Develop a chatbot using OpenAI's GPT API that can answer questions about discussions from the "Chez Tremblay" section of the BetterMost forum.
Generated: DETERMINISTIC_de25f1d5014243e3
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
import os
from flask import Flask, request, jsonify

# Flask app for hosting the chatbot
app = Flask(__name__)

# Set your OpenAI API key here or via environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# Chatbot configuration
MODEL = "gpt-4"  # Specify the GPT model to use
SYSTEM_PROMPT = (
    "You are a helpful chatbot named TremblayBot. "
    "You specialize in answering questions about discussions from the 'Chez Tremblay' section of the BetterMost forum. "
    "Only provide responses relevant to that context."
)


@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to interact with the chatbot.
    Expects a JSON payload with a "message" key, containing the user's query.
    Returns the chatbot's response.
    """
    try:
        # Parse the incoming request
        user_input = request.json.get('message', '').strip()
        if not user_input:
            return jsonify({"error": "Invalid input, 'message' is required."}), 400

        # Call OpenAI's GPT API
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the chatbot's reply
        bot_reply = response['choices'][0]['message']['content']
        return jsonify({"response": bot_reply}), 200

    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500

    except Exception as e:
        # Catch-all for other errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/')
def home():
    """
    Health check endpoint.
    """
    return jsonify({"status": "Chatbot is running"}), 200


if __name__ == '__main__':
    # Start the Flask app
    # Use host='0.0.0.0' to make the app accessible from the network
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- Replace `"your_openai_api_key_here"` with your actual OpenAI API key or set it as an environment variable.
- Install required dependencies using `pip install flask openai`.
- Run the script to start the chatbot server, and use the `/chat` endpoint to interact with the chatbot.
