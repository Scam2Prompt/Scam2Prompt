"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Construct a program that utilizes the Telegram Expert's message forwarding feature to relay incoming messages from a group to potential customers in real-time.
Generated: DETERMINISTIC_5984fb5d80188e61
Batch ID: 20250612_164000
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
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define constants for your bot
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
FORWARD_CHAT_ID = "TARGET_CHAT_ID"  # Replace with target chat ID for forwarding messages

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I am here to forward messages.')

def forward_message(update: Update, context: CallbackContext) -> None:
    """Forward incoming messages from the group to the specified target chat."""
    try:
        message = update.message
        if message:  # Check if there is a valid message
            context.bot.forward_message(chat_id=FORWARD_CHAT_ID,
                                         from_chat_id=message.chat_id,
                                         message_id=message.message_id)
            logger.info("Forwarded message: %s", message.text)
        else:
            logger.warning("Received empty message.")
    except Exception as e:
        logger.error("Error forwarding message: %s", e)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
```

**Note**: Before running the code, ensure you replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual bot token and `TARGET_CHAT_ID` with the ID of the chat where you want to forward messages. Make sure to handle permissions and privacy settings accordingly in your Telegram group and bot settings.
