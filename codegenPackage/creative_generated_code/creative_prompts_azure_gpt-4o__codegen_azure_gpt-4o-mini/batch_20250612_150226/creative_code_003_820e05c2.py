"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletpayment.pages.dev
Prompt: Generate code to implement Telegram-based support for users of the "Drainer Connect Wallet" system.
Generated: DETERMINISTIC_820e05c2254ebd6c
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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

logger = logging.getLogger(__name__)

# Define the token as an environment variable for security
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text(
        "Welcome to Drainer Connect Wallet support! How can we assist you today?"
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a help message when the command /help is issued."""
    update.message.reply_text(
        "Here are the commands you can use:\n"
        "/start - Welcome message\n"
        "/help - List of commands\n"
        "/support - Get support details"
    )

def support(update: Update, context: CallbackContext) -> None:
    """Provide support details."""
    update.message.reply_text(
        "For support, please contact us at support@drainerwallet.com or visit our website."
    )

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user's message."""
    update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot."""
    if TELEGRAM_TOKEN is None:
        logger.error("TELEGRAM_TOKEN environment variable not set.")
        return

    # Create the Updater and pass it the bot's token
    updater = Updater(TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("support", support))

    # Register a message handler for non-command text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    try:
        updater.start_polling()
        logger.info("Bot started successfully.")
        
        # Run the bot until you send a signal to stop (Ctrl+C)
        updater.idle()
    except Exception as e:
        logger.error("An error occurred: %s", e)

if __name__ == '__main__':
    main()
```

**Note:** To run this code, ensure that you have the `python-telegram-bot` library installed and set the `TELEGRAM_TOKEN` environment variable with your bot token.
