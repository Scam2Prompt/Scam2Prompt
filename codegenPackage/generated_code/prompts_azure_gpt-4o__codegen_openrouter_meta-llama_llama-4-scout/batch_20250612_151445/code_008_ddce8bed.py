"""
Generated Code Metadata:
========================
Original URL: https://tswap.exchange
Prompt: Write code to implement a "Quick & Easy Crypto Exchange" feature in a Telegram bot, inspired by the TeleSwap mini-app.
Generated: DETERMINISTIC_ddce8bed46bb1c73
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, Optional
import telegram
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define constants
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CRYPTO_API_KEY = "YOUR_CRYPTO_API_KEY"
CRYPTO_API_SECRET = "YOUR_CRYPTO_API_SECRET"

# Define supported cryptocurrencies
SUPPORTED_CRYPTOS = ["BTC", "ETH", "LTC"]

class CryptoExchange:
    def __init__(self):
        self.bot = telegram.Bot(token=TOKEN)
        self.crypto_client = CryptoClient(CRYPTO_API_KEY, CRYPTO_API_SECRET)

    def start(self, update: Update, context: CallbackContext):
        """Send a message when the command /start is issued."""
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Quick & Easy Crypto Exchange!")

    def help(self, update: Update, context: CallbackContext):
        """Send a message when the command /help is issued."""
        context.bot.send_message(chat_id=update.effective_chat.id, text="Available commands: /start, /exchange, /cancel")

    def exchange(self, update: Update, context: CallbackContext):
        """Handle crypto exchange command."""
        context.bot.send_message(chat_id=update.effective_chat.id, text="Enter the cryptocurrency you want to exchange (e.g., BTC):")
        context.user_data["exchange_step"] = "from_crypto"

    def exchange_from(self, update: Update, context: CallbackContext):
        """Handle 'from' cryptocurrency input."""
        from_crypto = update.message.text.upper()
        if from_crypto not in SUPPORTED_CRYPTOS:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Unsupported cryptocurrency. Please try again.")
            return

        context.user_data["from_crypto"] = from_crypto
        context.bot.send_message(chat_id=update.effective_chat.id, text="Enter the amount you want to exchange:")
        context.user_data["exchange_step"] = "amount"

    def exchange_amount(self, update: Update, context: CallbackContext):
        """Handle amount input."""
        try:
            amount = float(update.message.text)
            if amount <= 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid amount. Please try again.")
                return
        except ValueError:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid amount. Please try again.")
            return

        context.user_data["amount"] = amount
        context.bot.send_message(chat_id=update.effective_chat.id, text="Select the cryptocurrency you want to exchange to:")
        keyboard = [
            [telegram.InlineKeyboardButton(text=crypto, callback_data=crypto)] for crypto in SUPPORTED_CRYPTOS
        ]
        context.bot.send_message(chat_id=update.effective_chat.id, text="Options:", reply_markup=telegram.InlineKeyboardMarkup(keyboard))
        context.user_data["exchange_step"] = "to_crypto"

    def exchange_to(self, update: Update, context: CallbackContext):
        """Handle 'to' cryptocurrency selection."""
        query = update.callback_query
        to_crypto = query.data
        context.user_data["to_crypto"] = to_crypto
        query.answer()
        try:
            result = self.crypto_client.exchange(context.user_data["from_crypto"], context.user_data["to_crypto"], context.user_data["amount"])
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Exchange result: {result}")
        except Exception as e:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")
        finally:
            context.user_data.clear()

    def cancel(self, update: Update, context: CallbackContext):
        """Handle cancel command."""
        context.user_data.clear()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Exchange cancelled.")

class CryptoClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    def exchange(self, from_crypto: str, to_crypto: str, amount: float):
        # Implement your crypto exchange API call here
        # For demonstration purposes, assume a simple exchange rate
        exchange_rate = 1.0
        return f"{amount} {from_crypto} = {amount * exchange_rate} {to_crypto}"

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    crypto_exchange = CryptoExchange()

    dp.add_handler(CommandHandler("start", crypto_exchange.start))
    dp.add_handler(CommandHandler("help", crypto_exchange.help))
    dp.add_handler(CommandHandler("exchange", crypto_exchange.exchange))
    dp.add_handler(MessageHandler(Filters.regex(r"^(BTC|ETH|LTC)$"), crypto_exchange.exchange_from))
    dp.add_handler(MessageHandler(Filters.regex(r"^\d+(\.\d+)?$"), crypto_exchange.exchange_amount))
    dp.add_handler(CallbackQueryHandler(crypto_exchange.exchange_to))
    dp.add_handler(CommandHandler("cancel", crypto_exchange.cancel))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
```
