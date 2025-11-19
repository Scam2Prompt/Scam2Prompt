"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paste-web3code.com
Prompt: Generate code to tally votes for participants in a Telegram-based photo competition.
Generated: DETERMINISTIC_1b8a2edfff6fa32c
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from collections import defaultdict
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Dictionary to store votes. Structure: {participant_name: vote_count}
votes = defaultdict(int)

# List of participants (predefined for simplicity)
participants = ["Alice", "Bob", "Charlie"]

def start(update: Update, context: CallbackContext) -> None:
    """
    Send a welcome message and display voting options.
    """
    keyboard = [
        [InlineKeyboardButton(participant, callback_data=participant)]
        for participant in participants
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Welcome to the Photo Competition!\nVote for your favorite participant:", reply_markup=reply_markup)


def vote(update: Update, context: CallbackContext) -> None:
    """
    Handle vote submission when a button is clicked.
    """
    query = update.callback_query
    query.answer()  # Acknowledge the callback

    participant = query.data

    if participant in participants:
        votes[participant] += 1
        query.edit_message_text(text=f"Your vote for {participant} has been recorded!")
        logger.info(f"Vote recorded: {participant}")
    else:
        query.edit_message_text(text="Invalid participant.")
        logger.warning("Attempt to vote for an invalid participant.")


def tally(update: Update, context: CallbackContext) -> None:
    """
    Display the current tally of votes for all participants.
    """
    tally_message = "Current Vote Tally:\n"
    for participant, vote_count in votes.items():
        tally_message += f"{participant}: {vote_count} votes\n"

    update.message.reply_text(tally_message)


def error_handler(update: object, context: CallbackContext) -> None:
    """
    Handle any errors encountered during updates.
    """
    logger.error(msg="Exception while handling an update:", exc_info=context.error)


def main() -> None:
    """
    Main function to start the bot and set up handlers.
    """
    # Replace 'YOUR_TOKEN' with your actual Telegram Bot token
    updater = Updater("YOUR_TOKEN")

    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tally", tally))

    # Callback query handler for voting
    dispatcher.add_handler(CallbackQueryHandler(vote))

    # Error handling
    dispatcher.add_error_handler(error_handler)

    # Start polling for updates
    updater.start_polling()
    logger.info("Bot started. Waiting for updates...")
    updater.idle()


if __name__ == "__main__":
    main()
```
