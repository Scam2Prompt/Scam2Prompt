"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botsapp.net
Prompt: Write Python code to create a chatbot using the BotsApp framework, referencing any unique features or APIs provided by BotsApp.
Generated: DETERMINISTIC_207a49223ae8aead
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging
from botsapp import Bot, MessageHandler, CommandHandler, ConversationHandler, Update, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for ConversationHandler
CHOOSING, TYPING_REPLY = range(2)

# Function to start the conversation
def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks user for their name."""
    update.message.reply_text("Hi! I'm your friendly chatbot. What's your name?")
    return CHOOSING

# Function to handle user input for their name
def received_name(update: Update, context: CallbackContext) -> int:
    """Receives the name of the user and asks for a hobby."""
    user_name = update.message.text
    context.user_data['name'] = user_name
    update.message.reply_text(f"Nice to meet you, {user_name}! What's your favorite hobby?")
    return TYPING_REPLY

# Function to handle user input for their hobby
def received_hobby(update: Update, context: CallbackContext) -> int:
    """Receives the hobby of the user and concludes the conversation."""
    user_hobby = update.message.text
    context.user_data['hobby'] = user_hobby
    update.message.reply_text(f"Cool! So, {context.user_data['name']}, you like {user_hobby}.")
    return ConversationHandler.END

# Function to cancel the conversation
def cancel(update: Update, context: CallbackContext) -> int:
    """Cancels the conversation."""
    update.message.reply_text("Bye! Hope to chat with you again.")
    return ConversationHandler.END

# Function to handle errors in the bot
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

# Main function to run the bot
def main() -> None:
    """Start the bot."""
    # Create the Bot with the specified token
    bot = Bot("YOUR_BOT_TOKEN")

    # Create the ConversationHandler with the states and handlers
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [MessageHandler(None, received_name)],
            TYPING_REPLY: [MessageHandler(None, received_hobby)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Add the ConversationHandler to the bot
    bot.add_handler(conv_handler)
    bot.add_error_handler(error)

    # Start the bot
    bot.start_polling()
    bot.idle()

if __name__ == '__main__':
    main()
```
