"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orchaii.web.app
Prompt: Create a script to connect to Orchai's Alert Hub Telegram bot and set up personalized notifications for market fluctuations and investment opportunities.
Generated: DETERMINISTIC_39cde5397a6e2f90
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import os
import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment variables for sensitive data
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Set your bot token here
ALERT_HUB_API_URL = os.getenv("ALERT_HUB_API_URL")  # Endpoint for Orchai's Alert Hub API
ALERT_HUB_API_KEY = os.getenv("ALERT_HUB_API_KEY")  # Authentication Key for Alert Hub API

# Error message constants
ERROR_TELEGRAM_TOKEN = "Telegram Bot Token is missing. Please set `TELEGRAM_BOT_TOKEN` in your environment variables."
ERROR_API_URL = "Alert Hub API URL is missing. Please set `ALERT_HUB_API_URL` in your environment variables."
ERROR_API_KEY = "Alert Hub API Key is missing. Please set `ALERT_HUB_API_KEY` in your environment variables."

# Ensure necessary environment variables are set
if not TELEGRAM_BOT_TOKEN:
    raise ValueError(ERROR_TELEGRAM_TOKEN)
if not ALERT_HUB_API_URL:
    raise ValueError(ERROR_API_URL)
if not ALERT_HUB_API_KEY:
    raise ValueError(ERROR_API_KEY)

# Command: Start
def start(update: Update, context):
    """Handles the /start command. Sends a welcome message."""
    user = update.effective_user
    welcome_message = (
        f"Hello {user.first_name}, welcome to Orchai's Alert Hub bot!\n"
        "Use /subscribe to set up personalized notifications for market fluctuations and investment opportunities.\n"
        "Use /unsubscribe to stop receiving notifications."
    )
    update.message.reply_text(welcome_message)

# Command: Subscribe
def subscribe(update: Update, context):
    """Handles the /subscribe command. Registers the user for notifications."""
    chat_id = update.message.chat_id

    try:
        # Register user with Alert Hub API
        response = requests.post(
            url=f"{ALERT_HUB_API_URL}/subscribe",
            headers={"Authorization": f"Bearer {ALERT_HUB_API_KEY}"},
            json={"telegram_chat_id": chat_id}
        )
        response.raise_for_status()
    except requests.RequestException as e:
        # Log the error and inform the user
        logger.error(f"Error while subscribing user {chat_id}: {e}")
        update.message.reply_text("Failed to subscribe. Please try again later.")
        return

    update.message.reply_text("Subscription successful! You'll now receive notifications.")

# Command: Unsubscribe
def unsubscribe(update: Update, context):
    """Handles the /unsubscribe command. Unregisters the user from notifications."""
    chat_id = update.message.chat_id

    try:
        # Unregister user with Alert Hub API
        response = requests.post(
            url=f"{ALERT_HUB_API_URL}/unsubscribe",
            headers={"Authorization": f"Bearer {ALERT_HUB_API_KEY}"},
            json={"telegram_chat_id": chat_id}
        )
        response.raise_for_status()
    except requests.RequestException as e:
        # Log the error and inform the user
        logger.error(f"Error while unsubscribing user {chat_id}: {e}")
        update.message.reply_text("Failed to unsubscribe. Please try again later.")
        return

    update.message.reply_text("You have successfully unsubscribed from notifications.")

# Error handler
def error(update: Update, context):
    """Logs errors and sends an error message to the user."""
    logger.error(f"Update {update} caused error {context.error}")
    update.message.reply_text("An unexpected error occurred. Please try again later.")

# Main function
def main():
    """Starts the bot and sets up command handlers."""
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))
    dispatcher.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Register error handler
    dispatcher.add_error_handler(error)

    # Start polling for updates from Telegram
    updater.start_polling()

    logger.info("Bot started successfully.")
    # Keep the bot running until interrupted
    updater.idle()

if __name__ == "__main__":
    # Entry point
    main()
```
