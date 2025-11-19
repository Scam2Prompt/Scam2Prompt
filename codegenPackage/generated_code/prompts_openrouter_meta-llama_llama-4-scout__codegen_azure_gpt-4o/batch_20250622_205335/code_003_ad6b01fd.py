"""
Generated Code Metadata:
========================
Original URL: https://blur.gay
Prompt: Write a code snippet that showcases a bot project similar to the ones documented under the Projects section of Blur's website.
Generated: DETERMINISTIC_ad6b01fdd81c456e
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Bot configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in the environment variables.")

# Simulated bot logic
def process_message(message):
    """
    Process incoming messages and generate a response.
    :param message: str - The message sent by the user.
    :return: str - The bot's response.
    """
    if "hello" in message.lower():
        return "Hi there! How can I assist you today?"
    elif "bye" in message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Endpoint to handle incoming webhook requests.
    :return: JSON response with the bot's reply.
    """
    try:
        # Parse incoming JSON payload
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        user_message = data['message']
        logging.info(f"Received message: {user_message}")

        # Process the message and generate a response
        bot_response = process_message(user_message)
        logging.info(f"Bot response: {bot_response}")

        return jsonify({"response": bot_response}), 200

    except Exception as e:
        logging.error(f"Error processing webhook: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
```
