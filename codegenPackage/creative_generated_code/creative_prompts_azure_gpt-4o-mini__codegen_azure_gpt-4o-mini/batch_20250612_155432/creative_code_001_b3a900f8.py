"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cn-telegram.cn
Prompt: How can I implement Telegram's open API to create a bot that responds to user messages in a chat?
Generated: DETERMINISTIC_b3a900f82f64dd29
Batch ID: 20250612_155432
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

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text('Hello! I am your bot. How can I help you today?')

# Define message handler for text messages
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message back."""
    update.message.reply_text(update.message.text)

# Define the main function that sets up the bot
def main() -> None:
    """Start the bot."""
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    updater = Updater("YOUR_TOKEN_HERE")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    try:
        updater.start_polling()
        logger.info("Bot is polling for updates...")
        updater.idle()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

# Entry point of the script
if __name__ == '__main__':
    main()
```
