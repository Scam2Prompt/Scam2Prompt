"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.org
Prompt: Develop a script using Telegram's API to organize channel messages into topic tabs for better navigation and categorization.
Generated: DETERMINISTIC_5fedf12d8ce83a13
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
from collections import defaultdict

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Dictionary to hold messages categorized by topics
topic_messages = defaultdict(list)

# Command to start the bot and show available topics
def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message and shows available topics."""
    keyboard = [
        [InlineKeyboardButton("View Topics", callback_data='view_topics')],
        [InlineKeyboardButton("Add Topic", callback_data='add_topic')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Topic Organizer Bot! Choose an option:', reply_markup=reply_markup)

# Callback function to handle button presses
def handle_button(update: Update, context: CallbackContext) -> None:
    """Handles button presses in inline keyboards."""
    query = update.callback_query
    query.answer()

    if query.data == 'view_topics':
        view_topics(update, context)
    elif query.data == 'add_topic':
        query.edit_message_text(text="Please send the topic name followed by the message.")

# Function to view all topics and their messages
def view_topics(update: Update, context: CallbackContext) -> None:
    """Displays all topics and their associated messages."""
    if not topic_messages:
        update.callback_query.edit_message_text(text="No topics available.")
        return

    text = "Available Topics:\n"
    for topic in topic_messages.keys():
        text += f"- {topic}\n"

    update.callback_query.edit_message_text(text=text)

# Function to handle incoming messages and categorize them by topics
def handle_message(update: Update, context: CallbackContext) -> None:
    """Categorizes incoming messages into specified topics."""
    # Expecting format: "Topic Name: Your message here"
    try:
        topic, message = update.message.text.split(':', 1)
        topic = topic.strip()
        message = message.strip()

        if topic and message:
            topic_messages[topic].append(message)
            update.message.reply_text(f"Message added to topic '{topic}'.")
        else:
            update.message.reply_text("Please provide a valid topic and message.")
    except ValueError:
        update.message.reply_text("Invalid format. Use: 'Topic Name: Your message here'.")

# Main function to start the bot
def main() -> None:
    """Start the Telegram bot."""
    # Replace 'YOUR_TOKEN_HERE' with your actual bot token
    updater = Updater("YOUR_TOKEN_HERE")
    
    # Register handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(handle_button))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start polling for updates
    updater.start_polling()

    # Run the bot until you send a signal (Ctrl + C)
    updater.idle()

if __name__ == '__main__':
    main()
```
