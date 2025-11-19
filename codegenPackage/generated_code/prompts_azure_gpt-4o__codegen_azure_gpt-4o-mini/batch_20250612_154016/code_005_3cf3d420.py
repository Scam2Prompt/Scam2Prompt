"""
Generated Code Metadata:
========================
Original URL: https://suifox.online
Prompt: Develop a bot for Telegram that integrates with the SuiFOX ecosystem, allowing users to check token prices, transaction history, and participate in community-driven activities like meme competitions.
Generated: DETERMINISTIC_3cf3d420ebe26dec
Batch ID: 20250612_154016
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.suifox.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for the SuiFOX API
SUIFOX_API_BASE_URL = "https://api.suifox.com"  # Replace with the actual SuiFOX API base URL

# Function to start the bot and provide a welcome message
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the SuiFOX Bot. Use /help to see available commands.",
        reply_markup=ForceReply(selective=True),
    )

# Function to provide help information
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Available commands:\n"
        "/price - Check token prices\n"
        "/history - Check transaction history\n"
        "/meme - Participate in meme competitions"
    )

# Function to fetch token prices from the SuiFOX API
def get_token_price() -> str:
    """Fetch the current token price from the SuiFOX API."""
    try:
        response = requests.get(f"{SUIFOX_API_BASE_URL}/token/price")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return f"Current token price: {data['price']} {data['currency']}"
    except requests.RequestException as e:
        logger.error(f"Error fetching token price: {e}")
        return "Failed to fetch token price. Please try again later."

# Function to check transaction history
def get_transaction_history(user_id: str) -> str:
    """Fetch the transaction history for a user from the SuiFOX API."""
    try:
        response = requests.get(f"{SUIFOX_API_BASE_URL}/user/{user_id}/transactions")
        response.raise_for_status()
        data = response.json()
        if data['transactions']:
            return "\n".join([f"Transaction ID: {tx['id']} - Amount: {tx['amount']}" for tx in data['transactions']])
        else:
            return "No transaction history found."
    except requests.RequestException as e:
        logger.error(f"Error fetching transaction history: {e}")
        return "Failed to fetch transaction history. Please try again later."

# Function to handle the /price command
def price(update: Update, context: CallbackContext) -> None:
    """Send the current token price when the command /price is issued."""
    price_info = get_token_price()
    update.message.reply_text(price_info)

# Function to handle the /history command
def history(update: Update, context: CallbackContext) -> None:
    """Send the transaction history when the command /history is issued."""
    user_id = update.effective_user.id
    history_info = get_transaction_history(user_id)
    update.message.reply_text(history_info)

# Function to handle the /meme command
def meme(update: Update, context: CallbackContext) -> None:
    """Send a message to participate in meme competitions."""
    update.message.reply_text("Join our meme competition! Share your best memes with us!")

# Main function to start the bot
def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")  # Replace with your bot's token

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("price", price))
    dispatcher.add_handler(CommandHandler("history", history))
    dispatcher.add_handler(CommandHandler("meme", meme))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
```

Make sure to replace `"YOUR_TELEGRAM_BOT_TOKEN"` with your actual Telegram bot token and update the `SUIFOX_API_BASE_URL` with the correct API endpoint for SuiFOX.
