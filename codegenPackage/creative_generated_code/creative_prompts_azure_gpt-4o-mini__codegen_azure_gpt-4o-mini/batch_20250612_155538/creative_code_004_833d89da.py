"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.org
Prompt: Illustrate how to use the Telegram API for auto-translation of messages in channels, focusing on the implementation details provided in the recent updates.
Generated: DETERMINISTIC_833d89dad1abf1c1
Batch ID: 20250612_155538
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
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Set up logging to track events and errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Google Translator
translator = Translator()

# Define the translation function
def translate_text(text: str, dest_language: str) -> str:
    """Translate text to the specified destination language."""
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        logger.error(f"Error during translation: {e}")
        return "Translation failed."

# Define the /start command handler
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome! Send me a message and I will translate it.')

# Define the message handler for translation
def translate_message(update: Update, context: CallbackContext) -> None:
    """Translate the received message into the specified language."""
    user_text = update.message.text  # Get the user's message
    dest_language = context.args[0] if context.args else 'en'  # Default to English if no language is provided
    
    # Validate the destination language code
    if len(dest_language) != 2:
        update.message.reply_text("Invalid language code. Please use a valid 2-letter language code.")
        return

    # Translate the message
    translated_text = translate_text(user_text, dest_language)
    update.message.reply_text(translated_text)

def main() -> None:
    """Start the bot."""
    # Create the Updater object and pass your bot's token
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Ensure your Telegram bot token is set in the environment
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
```

**Note:** Make sure to set the `TELEGRAM_BOT_TOKEN` environment variable with your bot's token before running the script. Additionally, the `googletrans` library should be installed with `pip install googletrans==4.0.0-rc1`.
