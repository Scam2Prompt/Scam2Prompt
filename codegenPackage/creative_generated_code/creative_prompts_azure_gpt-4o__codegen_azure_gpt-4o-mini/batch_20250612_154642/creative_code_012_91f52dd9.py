"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syntera.pro
Prompt: Generate a Python script to integrate Syntera's AI manager with Instagram and Telegram for handling customer inquiries and appointment scheduling.
Generated: DETERMINISTIC_91f52dd9852ea185
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask, request, jsonify

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Environment variables for sensitive information
INSTAGRAM_TOKEN = os.getenv("INSTAGRAM_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SYNTERA_API_URL = os.getenv("SYNTERA_API_URL")

# Error handling for missing environment variables
if not INSTAGRAM_TOKEN or not TELEGRAM_TOKEN or not SYNTERA_API_URL:
    logger.error("Environment variables are not set. Please set INSTAGRAM_TOKEN, TELEGRAM_TOKEN, and SYNTERA_API_URL.")
    raise EnvironmentError("Missing required environment variables.")

# Function to handle customer inquiries
def handle_customer_inquiry(message, chat_id):
    try:
        # Send the message to Syntera's AI manager
        response = requests.post(
            f"{SYNTERA_API_URL}/inquiries",
            json={"message": message}
        )
        response.raise_for_status()

        # Forward the response back to the user
        bot.send_message(chat_id=chat_id, text=response.json().get('reply', 'Sorry, I could not process your request.'))
    except requests.exceptions.RequestException as e:
        logger.error(f"Error during request to Syntera API: {e}")
        bot.send_message(chat_id=chat_id, text="There was an error processing your inquiry. Please try again later.")

# Telegram bot command to start interaction
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! How can I assist you today?")

# Message handler for customer inquiries
def handle_message(update: Update, context: CallbackContext):
    message = update.message.text
    chat_id = update.message.chat_id
    handle_customer_inquiry(message, chat_id)

# Function to set up Telegram bot
def setup_telegram_bot():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    # Define command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start polling for updates
    updater.start_polling()
    updater.idle()

# Flask route to handle Instagram webhook
@app.route('/instagram/webhook', methods=['POST'])
def instagram_webhook():
    data = request.json
    logger.info(f"Received Instagram data: {data}")
    
    # Here you should add logic to handle Instagram messages/inquiries
    # This is a placeholder for further implementation
    return jsonify(status="received"), 200

# Main entry point for the application
if __name__ == '__main__':
    # Start the Telegram bot in a separate thread
    from threading import Thread
    telegram_thread = Thread(target=setup_telegram_bot)
    telegram_thread.start()

    # Run the Flask app
    app.run(port=5000)
```

### Note
Make sure to set the following environment variables before running the script:
- `INSTAGRAM_TOKEN`: Token for Instagram API
- `TELEGRAM_TOKEN`: Token for Telegram Bot API
- `SYNTERA_API_URL`: Base URL for Syntera's AI manager API

Ensure you also have the required libraries installed:
```bash
pip install python-telegram-bot Flask requests
```
