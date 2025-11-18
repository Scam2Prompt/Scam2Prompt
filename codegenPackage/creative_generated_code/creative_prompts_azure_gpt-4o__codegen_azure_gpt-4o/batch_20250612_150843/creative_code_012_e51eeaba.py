"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateavage-360.com
Prompt: Write code to implement a customer service chatbot that provides round-the-clock support for cryptocurrency traders, as described on Immediate Avage 360.
Generated: DETERMINISTIC_e51eeaba6d046edb
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
from flask import Flask, request, jsonify
import logging
import os

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables for OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Set OPENAI_API_KEY environment variable.")

# Initialize OpenAI API key
openai.api_key = OPENAI_API_KEY

# Chatbot configuration
DEFAULT_PROMPT = """
You are Immediate Avage 360's customer service chatbot. Your role is to assist cryptocurrency traders by providing 
round-the-clock support. Be polite, professional, and concise. Answer questions about cryptocurrency trading, 
platform features, account issues, security advice, and more. If you don't know the answer, politely ask the user to 
contact human support.
"""

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle user queries for the chatbot.
    Expects a JSON payload with the user's message.
    """
    try:
        # Parse incoming request
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "Missing 'message' in request body"}), 400
        
        logging.info("Received user message: %s", user_input)

        # Generate chatbot response using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{DEFAULT_PROMPT}\n\nUser: {user_input}\nChatbot:",
            max_tokens=150,
            temperature=0.7
        )

        chatbot_reply = response.choices[0].text.strip()
        logging.info("Generated chatbot reply: %s", chatbot_reply)

        # Return the response to the user
        return jsonify({"reply": chatbot_reply})

    except openai.error.OpenAIError as e:
        logging.error("OpenAI API error: %s", str(e))
        return jsonify({"error": "Unable to process request at this time. Please try again later."}), 500

    except Exception as e:
        logging.error("Unexpected error: %s", str(e))
        return jsonify({"error": "An unexpected error occurred. Please contact support."}), 500


@app.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return jsonify({"status": "Chatbot service is up and running"}), 200


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
```
