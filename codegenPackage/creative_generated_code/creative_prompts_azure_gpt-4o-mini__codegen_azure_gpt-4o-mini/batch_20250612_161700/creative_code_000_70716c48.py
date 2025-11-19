"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paalai-io.web.app
Prompt: How can I create a personalized AI chatbot using PAAL AI that integrates with Telegram and Discord?
Generated: DETERMINISTIC_70716c4802af89bf
Batch ID: 20250612_161700
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
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from discord import Client, Intents
from discord.ext import commands

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask App
app = Flask(__name__)

# Initialize Telegram Bot
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
telegram_bot = Bot(token=TELEGRAM_TOKEN)

# Initialize Discord Client
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
discord_intents = Intents.default()
discord_client = Client(intents=discord_intents)

# Telegram Handler
def start_handler(update: Update, context: CallbackContext):
    """Handles the /start command for Telegram."""
    update.message.reply_text("Welcome to your personalized AI Chatbot!")

def message_handler(update: Update, context: CallbackContext):
    """Handles incoming messages from Telegram."""
    user_message = update.message.text
    response = get_ai_response(user_message)  # Placeholder for AI response
    update.message.reply_text(response)

# Discord Event Handlers
@discord_client.event
async def on_ready():
    """Runs when the Discord bot is ready."""
    logger.info(f'Logged in as {discord_client.user}')

@discord_client.event
async def on_message(message):
    """Handles incoming messages from Discord."""
    if message.author == discord_client.user:
        return  # Ignore messages from the bot itself

    user_message = message.content
    response = get_ai_response(user_message)  # Placeholder for AI response
    await message.channel.send(response)

def get_ai_response(user_message):
    """Placeholder function to get AI response from PAAL AI.
    
    Args:
        user_message (str): The user's message.

    Returns:
        str: The AI's response.
    """
    # Here, you'd integrate with the PAAL AI API to get a response
    # For now, we will return a dummy response
    return f"AI response to: {user_message}"

# Register handlers for Telegram
telegram_updater = telegram_bot.updater
telegram_updater.dispatcher.add_handler(CommandHandler('start', start_handler))
telegram_updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint for Telegram updates."""
    json_update = request.get_json()
    telegram_bot.process_new_updates([Update.de_json(json_update, telegram_bot)])
    return '', 200

if __name__ == "__main__":
    # Start the Flask app for Telegram
    telegram_bot.set_webhook(url=os.getenv('WEBHOOK_URL'))
    app.run(port=5000)

    # Start the Discord bot
    discord_client.run(DISCORD_TOKEN)
```

**Important:** Be sure to set the environment variables `TELEGRAM_TOKEN`, `DISCORD_TOKEN`, and `WEBHOOK_URL` before running this code. Additionally, ensure that you implement the actual integration with the PAAL AI API in the `get_ai_response` function. The logging and error handling can be enhanced based on production needs.
