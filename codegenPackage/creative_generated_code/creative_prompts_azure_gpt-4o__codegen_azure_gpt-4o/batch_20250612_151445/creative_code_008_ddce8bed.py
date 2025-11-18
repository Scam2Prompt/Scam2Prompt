"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tswap.exchange
Prompt: Write code to implement a "Quick & Easy Crypto Exchange" feature in a Telegram bot, inspired by the TeleSwap mini-app.
Generated: DETERMINISTIC_ddce8bed46bb1c73
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Mock crypto exchange rates (normally this would come from a live API)
EXCHANGE_RATES = {
    "BTC": {"ETH": 14.5, "USDT": 23000},
    "ETH": {"BTC": 0.069, "USDT": 1600},
    "USDT": {"BTC": 0.000043, "ETH": 0.000625},
}

# Button callbacks
CRYPTO_CHOICES = ["BTC", "ETH", "USDT"]

# In-memory user state (replace with database in production)
user_state: Dict[int, Dict[str, Optional[str]]] = {}


def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command and display the welcome message."""
    user = update.effective_user
    update.message.reply_text(
        f"Hi {user.first_name}! Welcome to Quick & Easy Crypto Exchange!\n"
        f"Use /exchange to start swapping crypto."
    )


def exchange(update: Update, context: CallbackContext) -> None:
    """Initiate the exchange process by selecting the source currency."""
    keyboard = [
        [InlineKeyboardButton(crypto, callback_data=f"source_{crypto}")]
        for crypto in CRYPTO_CHOICES
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Select the currency you want to exchange:", reply_markup=reply_markup
    )


def handle_source_currency(update: Update, context: CallbackContext) -> None:
    """Handle the selection of the source currency."""
    query = update.callback_query
    user_id = query.from_user.id
    source_currency = query.data.split("_")[1]

    # Update user state
    user_state[user_id] = {"source_currency": source_currency, "target_currency": None}
    query.answer()
    logger.info(f"User {user_id} selected source currency: {source_currency}")

    # Prompt for target currency
    keyboard = [
        [
            InlineKeyboardButton(
                crypto,
                callback_data=f"target_{crypto}",
            )
        ]
        for crypto in CRYPTO_CHOICES
        if crypto != source_currency
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        f"Source currency: {source_currency}\nSelect the target currency:",
        reply_markup=reply_markup,
    )


def handle_target_currency(update: Update, context: CallbackContext) -> None:
    """Handle the selection of the target currency."""
    query = update.callback_query
    user_id = query.from_user.id
    target_currency = query.data.split("_")[1]

    # Update user state
    user_state[user_id]["target_currency"] = target_currency
    query.answer()
    logger.info(f"User {user_id} selected target currency: {target_currency}")

    # Prompt for amount
    source_currency = user_state[user_id]["source_currency"]
    query.edit_message_text(
        f"Source currency: {source_currency}\nTarget currency: {target_currency}\n"
        f"Enter the amount of {source_currency} you want to exchange:"
    )


def handle_amount(update: Update, context: CallbackContext) -> None:
    """Handle the amount input and perform the exchange."""
    user_id = update.message.from_user.id
    user_data = user_state.get(user_id)

    # Ensure user has selected source and target currencies
    if not user_data or not user_data.get("source_currency") or not user_data.get(
        "target_currency"
    ):
        update.message.reply_text("Please start the exchange process using /exchange.")
        return

    try:
        amount = float(update.message.text)
        source_currency = user_data["source_currency"]
        target_currency = user_data["target_currency"]

        # Perform conversion based on mock exchange rates
        rate = EXCHANGE_RATES[source_currency][target_currency]
        converted_amount = amount * rate

        update.message.reply_text(
            f"{amount:.8f} {source_currency} = {converted_amount:.8f} {target_currency}\n"
            f"Exchange complete! Thank you for using Quick & Easy Crypto Exchange."
        )

        # Clear user state (optional, depending on desired UX)
        user_state.pop(user_id, None)

    except ValueError:
        update.message.reply_text("Invalid amount. Please enter a valid number.")
    except KeyError:
        update.message.reply_text(
            "An error occurred in processing the exchange. Please try again later."
        )
        logger.error(
            f"Exchange rate not found for {source_currency} to {target_currency}"
        )


def main() -> None:
    """Run the bot."""
    # Replace TOKEN with your Telegram Bot token
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    updater = Updater(TOKEN)

    # Command handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("exchange", exchange))

    # Callback query handlers for buttons
    updater.dispatcher.add_handler(
        CallbackQueryHandler(handle_source_currency, pattern="^source_")
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(handle_target_currency, pattern="^target_")
    )

    # Message handler for user input (amount)
    updater.dispatcher.add_handler(
        CommandHandler("handle_amount", handle_amount)
    )

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
```
