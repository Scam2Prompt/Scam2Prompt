"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apiym.com
Prompt: What are the steps to build a Telegram automatic messaging tool as described on apiym.com?
Generated: DETERMINISTIC_953b513e7854956c
Batch ID: 20250612_163149
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
import time
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to start the bot
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome! I am your automatic messaging bot.')

# Define a function to handle messages
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

# Define a function to send scheduled messages
def scheduled_message(context: CallbackContext) -> None:
    """Send a scheduled message."""
    context.bot.send_message(chat_id=context.job.context, text='This is a scheduled message!')

# Define a function to set a timer for scheduled messages
def set_timer(update: Update, context: CallbackContext) -> None:
    """Set a timer for scheduled messages."""
    try:
        # Get timer duration from command arguments
        due = int(context.args[0])
        chat_id = update.message.chat_id
        
        # Schedule the job
        context.job_queue.run_once(scheduled_message, due, context=chat_id)
        update.message.reply_text(f'Timer set for {due} seconds!')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set_timer <seconds>')

# Define the main function to run the bot
def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(os.getenv('TELEGRAM_BOT_TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set_timer", set_timer))

    # Register message handler for echoing messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    # Run the main function
    main()
```
