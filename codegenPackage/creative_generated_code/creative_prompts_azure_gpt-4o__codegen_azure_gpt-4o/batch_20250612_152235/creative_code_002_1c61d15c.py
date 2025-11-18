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
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants for game mechanics
INITIAL_COINS = 0
PREMIUM_BONUS = 10
LEVEL_UP_THRESHOLD = 50
MAX_LEVEL = 10

# Game state storage
user_data = {}

def start(update: Update, context: CallbackContext) -> None:
    """Start command handler to initialize game state."""
    user_id = update.effective_user.id
    if user_id not in user_data:
        user_data[user_id] = {
            'coins': INITIAL_COINS,
            'level': 1,
            'premium': False
        }
    update.message.reply_text(
        "Welcome to Hamster Kombat!\n"
        "You can collect coins, level up, and unlock rewards.\n"
        "Use /collect to collect coins, /level to check your progress, "
        "/premium to become a premium user."
    )

def collect(update: Update, context: CallbackContext) -> None:
    """Collect coins and handle level progression."""
    user_id = update.effective_user.id
    if user_id not in user_data:
        update.message.reply_text("Please start the game using /start.")
        return
    
    user_info = user_data[user_id]
    collected_coins = 5  # Default coin collection value
    if user_info['premium']:
        collected_coins += PREMIUM_BONUS
    
    user_info['coins'] += collected_coins
    
    # Check for level up
    if user_info['coins'] >= LEVEL_UP_THRESHOLD and user_info['level'] < MAX_LEVEL:
        user_info['level'] += 1
        user_info['coins'] -= LEVEL_UP_THRESHOLD
        update.message.reply_text(
            f"Congratulations! You leveled up to Level {user_info['level']}!"
        )
    else:
        update.message.reply_text(
            f"You collected {collected_coins} coins. "
            f"Total coins: {user_info['coins']}."
        )

def level(update: Update, context: CallbackContext) -> None:
    """Display the user's current level and coin status."""
    user_id = update.effective_user.id
    if user_id not in user_data:
        update.message.reply_text("Please start the game using /start.")
        return
    
    user_info = user_data[user_id]
    update.message.reply_text(
        f"Current Level: {user_info['level']}\n"
        f"Coins: {user_info['coins']}"
    )

def premium(update: Update, context: CallbackContext) -> None:
    """Allow the user to become a premium user."""
    user_id = update.effective_user.id
    if user_id not in user_data:
        update.message.reply_text("Please start the game using /start.")
        return
    
    user_info = user_data[user_id]
    user_info['premium'] = True
    update.message.reply_text(
        "You are now a Premium user! Enjoy extra bonuses when collecting coins."
    )

def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors caused by updates."""
    logger.error(msg="Exception while handling update:", exc_info=context.error)

def main() -> None:
    """Main function to run the bot."""
    # Replace 'TOKEN' with your actual bot token
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    
    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("collect", collect))
    dispatcher.add_handler(CommandHandler("level", level))
    dispatcher.add_handler(CommandHandler("premium", premium))
    
    # Error handler
    dispatcher.add_error_handler(error_handler)
    
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```
