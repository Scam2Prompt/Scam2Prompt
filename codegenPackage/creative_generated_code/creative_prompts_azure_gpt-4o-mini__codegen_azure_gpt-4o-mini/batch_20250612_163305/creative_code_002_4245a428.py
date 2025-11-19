"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-onchain.pages.dev
Prompt: Generate a code snippet for a Telegram bot that allows users to collect Chain Links in the Chain game and track their progress towards the $onchain airdrop.
Generated: DETERMINISTIC_4245a4288dcf67d2
Batch ID: 20250612_163305
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
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define a class to manage user progress
class UserProgress:
    def __init__(self):
        self.progress = {}

    def add_chain_link(self, user_id):
        if user_id not in self.progress:
            self.progress[user_id] = 0
        self.progress[user_id] += 1

    def get_progress(self, user_id):
        return self.progress.get(user_id, 0)

# Instantiate user progress tracker
user_progress = UserProgress()

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the Chain Links Tracker Bot.\n"
        "Use /collect to collect a Chain Link and track your progress towards the $onchain airdrop!",
        reply_markup=ForceReply(selective=True),
    )

# Command to collect a Chain Link
def collect(update: Update, context: CallbackContext) -> None:
    """Collect a Chain Link."""
    user_id = update.effective_user.id
    user_progress.add_chain_link(user_id)
    current_progress = user_progress.get_progress(user_id)
    update.message.reply_text(
        f"You have collected {current_progress} Chain Link(s). Keep going to reach the airdrop!"
    )

# Command to check progress
def progress(update: Update, context: CallbackContext) -> None:
    """Check the user's progress towards the airdrop."""
    user_id = update.effective_user.id
    current_progress = user_progress.get_progress(user_id)
    update.message.reply_text(
        f"You are currently at {current_progress} Chain Link(s)."
    )

# Command to stop the bot
def stop(update: Update, context: CallbackContext) -> None:
    """Stop the bot."""
    update.message.reply_text("Goodbye! Hope to see you again.")

# Error handling callback
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(os.getenv("TELEGRAM_BOT_TOKEN"))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("collect", collect))
    dispatcher.add_handler(CommandHandler("progress", progress))
    dispatcher.add_handler(CommandHandler("stop", stop))
    
    # Register error handler
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
```

**Note:** Make sure to set the environment variable `TELEGRAM_BOT_TOKEN` with your bot's token for this code to run successfully.
