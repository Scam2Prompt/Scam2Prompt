"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tswap.exchange
Prompt: Write code to implement a "Quick & Easy Crypto Exchange" feature in a Telegram bot, inspired by the TeleSwap mini-app.
Generated: DETERMINISTIC_ddce8bed46bb1c73
Batch ID: 20250612_151445
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={fiat": {
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
import os
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Set up logging for debugging purposes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Telegram bot token
API_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Function to fetch cryptocurrency exchange rates
def get_exchange_rate(crypto: str, fiat: str) -> float:
    """Fetch exchange rate for the given cryptocurrency and fiat currency."""
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={fiat}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data[crypto][fiat]
    except Exception as e:
        logger.error(f"Error fetching exchange rate: {e}")
        return None

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text("Welcome to Quick & Easy Crypto Exchange! Use /exchange <crypto> <fiat> to get the exchange rate.")

# Exchange command handler
def exchange(update: Update, context: CallbackContext) -> None:
    """Fetch and display the exchange rate for the given cryptocurrency and fiat currency."""
    if len(context.args) != 2:
        update.message.reply_text("Usage: /exchange <crypto> <fiat>")
        return

    crypto, fiat = context.args[0].lower(), context.args[1].lower()
    rate = get_exchange_rate(crypto, fiat)

    if rate is not None:
        update.message.reply_text(f"The current exchange rate for {crypto.upper()} to {fiat.upper()} is: {rate}.")
    else:
        update.message.reply_text("Sorry, I couldn't fetch the exchange rate. Please check your inputs.")

# Error handler for the bot
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors caused by updates."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    """Start the bot."""
    # Initialize the bot and the updater
    updater = Updater(API_TOKEN)

    # Dispatchers for handling commands
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("exchange", exchange))

    # Error handling
    dispatcher.add_error_handler(error_handler)

    # Start polling for updates
    updater.start_polling()
    logger.info("Bot is polling for updates...")

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
```

**Note:** Ensure you set the `TELEGRAM_BOT_TOKEN` environment variable with your bot token before running the script.
