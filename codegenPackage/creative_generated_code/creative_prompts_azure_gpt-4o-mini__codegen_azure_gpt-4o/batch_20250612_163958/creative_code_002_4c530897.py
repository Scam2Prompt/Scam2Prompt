"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m-telegram.net
Prompt: Write a code snippet for a Telegram bot that synchronizes chat history across multiple devices.
Generated: DETERMINISTIC_4c5308974ca8bcf3
Batch ID: 20250612_163958
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

# Set up logging for debugging and monitoring.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Dictionary to store chat history for each chat.
chat_history = {}

def start(update: Update, context: CallbackContext) -> None:
    """Command Handler for /start. Sends introductory message."""
    update.message.reply_text(
        "Welcome! This bot will help synchronize chat history across devices."
    )

def save_message(update: Update, context: CallbackContext) -> None:
    """Message Handler to save user messages in chat history."""
    chat_id = update.message.chat_id
    if chat_id not in chat_history:
        chat_history[chat_id] = []

    # Save the message text and sender information.
    chat_history[chat_id].append({
        "user": update.message.from_user.username or update.message.from_user.first_name,
        "text": update.message.text,
        "timestamp": update.message.date.strftime('%Y-%m-%d %H:%M:%S')
    })

    # Log the saved message.
    logger.info(f"Message saved for chat_id={chat_id}: {update.message.text}")

def history(update: Update, context: CallbackContext) -> None:
    """Command Handler for /history. Sends the chat history to the user."""
    chat_id = update.message.chat_id
    if chat_id not in chat_history or len(chat_history[chat_id]) == 0:
        update.message.reply_text("No chat history available.")
        return

    # Format and send chat history.
    history_text = "\n".join(
        [f"[{msg['timestamp']}] {msg['user']}: {msg['text']}" for msg in chat_history[chat_id]]
    )
    update.message.reply_text(f"Your chat history:\n{history_text}")

def error_handler(update: Update, context: CallbackContext) -> None:
    """Global error handler to log exceptions."""
    logger.error(msg="An error occurred:", exc_info=context.error)
    update.message.reply_text("An error occurred. Please try again later.")

def main() -> None:
    """Main function to start the bot."""
    # Replace 'YOUR_TOKEN' with your actual bot token from BotFather.
    TOKEN = 'YOUR_TOKEN'

    # Create Updater and Dispatcher.
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register command handlers.
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("history", history))

    # Register message handler for text messages.
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, save_message))

    # Register error handler.
    dispatcher.add_error_handler(error_handler)

    # Start the bot.
    updater.start_polling()
    logger.info("Bot started successfully.")

    # Run until interrupted.
    updater.idle()

if __name__ == '__main__':
    main()
```
