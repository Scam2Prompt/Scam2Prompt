"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Develop a Telegram bot using Python's `python-telegram-bot` library that mimics the Hamster Kombat game mechanics, including coin collection, level progression, and bonus rewards for premium users.
Generated: DETERMINISTIC_1c61d15c6250f620
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
import random

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for the conversation
CHOOSING, PLAYING, COLLECTING, LEVEL_UP = range(4)

# Define user data
user_data = {}

# Game settings
COIN_COLLECTION_MAX = 10
LEVEL_UP_THRESHOLD = 3
PREMIUM_BONUS = 5


def start(update: Update, context: CallbackContext) -> int:
    """Start the game and initialize user data."""
    user_id = update.effective_user.id
    user_data[user_id] = {'level': 1, 'coins': 0, 'is_premium': False}
    update.message.reply_text(
        "Welcome to Hamster Kombat! Type /play to start playing.")
    return CHOOSING


def play(update: Update, context: CallbackContext) -> int:
    """Start the game session by allowing users to play."""
    user_id = update.effective_user.id
    level = user_data[user_id]['level']
    coins = user_data[user_id]['coins']
    
    update.message.reply_text(
        f"Level: {level}\nCoins: {coins}\nType /collect to collect coins.")
    return PLAYING


def collect(update: Update, context: CallbackContext) -> int:
    """Collect coins based on random outcome."""
    user_id = update.effective_user.id
    if user_id not in user_data:
        update.message.reply_text("Please start the game with /start.")
        return CHOOSING

    coins_collected = random.randint(1, COIN_COLLECTION_MAX)
    user_data[user_id]['coins'] += coins_collected

    update.message.reply_text(
        f"You collected {coins_collected} coins! Total coins: {user_data[user_id]['coins']}")
    
    # Check for level up
    if user_data[user_id]['coins'] >= LEVEL_UP_THRESHOLD:
        user_data[user_id]['level'] += 1
        user_data[user_id]['coins'] = 0  # Reset coins after level up
        update.message.reply_text(
            f"Congratulations! You've leveled up to Level {user_data[user_id]['level']}!")
    
    return PLAYING


def toggle_premium(update: Update, context: CallbackContext) -> int:
    """Toggle premium status for the user."""
    user_id = update.effective_user.id
    user_data[user_id]['is_premium'] = not user_data[user_id]['is_premium']
    
    if user_data[user_id]['is_premium']:
        update.message.reply_text("You've been upgraded to a premium user! Enjoy your bonus coins!")
        user_data[user_id]['coins'] += PREMIUM_BONUS
    else:
        update.message.reply_text("You've been downgraded from premium status.")
    
    return PLAYING


def help_command(update: Update, context: CallbackContext) -> None:
    """Provide help information to the user."""
    update.message.reply_text(
        "Commands:\n/start - Start the game\n/play - Play the game\n/collect - Collect coins\n/toggle_premium - Toggle premium status\n/help - Show this message")


def cancel(update: Update, context: CallbackContext) -> int:
    """Cancel the current conversation."""
    update.message.reply_text("Game has been cancelled.")
    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    bot_token = 'YOUR_BOT_TOKEN'  # Replace with your bot token
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Define the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [CommandHandler('play', play)],
            PLAYING: [
                CommandHandler('collect', collect),
                CommandHandler('toggle_premium', toggle_premium),
                CommandHandler('help', help_command),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    logger.info("Bot is running...")

    # Run the bot until you send a signal to stop it
    updater.idle()


if __name__ == '__main__':
    main()
```
