"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Create a Telegram bot using Python that sends notifications to admins when a new scam report is submitted, similar to the bot mentioned in the website's news section.
Generated: DETERMINISTIC_1890874e6964af94
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define constants
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Telegram Bot Token from environment variable
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')  # Admin chat ID from environment variable

# Function to start the bot and provide instructions
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome! Please submit your scam report.')

# Function to handle incoming messages (scam reports)
def handle_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming messages and notify admins about scam reports."""
    scam_report = update.message.text
    logging.info(f"Received scam report: {scam_report}")

    # Notify admins
    try:
        context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"New scam report received:\n{scam_report}")
        update.message.reply_text('Thank you for your report! Admins have been notified.')
    except Exception as e:
        logging.error(f"Error sending message to admin: {e}")
        update.message.reply_text('There was an error processing your report. Please try again later.')

# Main function to run the bot
def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
```

Make sure to set the environment variables `TELEGRAM_BOT_TOKEN` and `ADMIN_CHAT_ID` before running the bot.
