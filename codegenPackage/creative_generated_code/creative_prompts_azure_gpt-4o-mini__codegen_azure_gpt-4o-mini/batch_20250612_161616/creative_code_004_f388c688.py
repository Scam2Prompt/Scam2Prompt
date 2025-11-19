"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milli-dog.vercel.app
Prompt: Illustrate how to integrate a Telegram bot for community updates regarding $MILLI token listings and announcements.
Generated: DETERMINISTIC_f388c6882fbf0c56
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define the bot token and chat ID
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome to the $MILLI token updates bot!')

def send_token_update(message: str) -> None:
    """Send an update message to the specified Telegram chat.

    Args:
        message (str): The update message to be sent.
    """
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
        payload = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'  # Use HTML format for rich text
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        logging.info('Update sent successfully.')
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to send update: {e}')
        
def send_listing_update(update: str) -> None:
    """Notify the community about new token listings.

    Args:
        update (str): The details of the token listing.
    """
    message = f'📈 New $MILLI Token Listing:\n{update}'
    send_token_update(message)

def send_announcement(announcement: str) -> None:
    """Notify the community about important announcements.

    Args:
        announcement (str): The announcement details.
    """
    message = f'📢 Announcement regarding $MILLI Token:\n{announcement}'
    send_token_update(message)

def main() -> None:
    """Start the bot and set up the command handlers."""
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Registering the command handler for /start
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Start polling for updates
    updater.start_polling()
    logging.info('Bot is polling for updates...')
    
    # Run the bot until you send a signal to stop (e.g., Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
```
