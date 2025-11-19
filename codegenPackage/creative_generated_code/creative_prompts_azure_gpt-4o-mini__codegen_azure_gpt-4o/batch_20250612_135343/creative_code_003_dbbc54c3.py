"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogemob.pages.dev
Prompt: Develop a community engagement tool using a Telegram bot that notifies users about DOGEMOB-related events and giveaways.
Generated: DETERMINISTIC_dbbc54c3e3f2c080
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configure logging for debugging and monitoring
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Replace with your bot's token from BotFather
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

# Global list to store subscribed users
subscribed_users = set()

# Command: Start
def start(update: Update, context: CallbackContext) -> None:
    """Handle the /start command. Sends a welcome message."""
    user = update.effective_user
    update.message.reply_text(
        f"Hello, {user.first_name}! Welcome to the DOGEMOB community bot.\n"
        f"Use /subscribe to receive event and giveaway notifications."
    )

# Command: Subscribe
def subscribe(update: Update, context: CallbackContext) -> None:
    """Handle the /subscribe command. Adds the user to the subscription list."""
    user_id = update.effective_user.id
    if user_id in subscribed_users:
        update.message.reply_text("You are already subscribed!")
    else:
        subscribed_users.add(user_id)
        update.message.reply_text("You have successfully subscribed to notifications!")

# Command: Unsubscribe
def unsubscribe(update: Update, context: CallbackContext) -> None:
    """Handle the /unsubscribe command. Removes the user from the subscription list."""
    user_id = update.effective_user.id
    if user_id in subscribed_users:
        subscribed_users.remove(user_id)
        update.message.reply_text("You have successfully unsubscribed!")
    else:
        update.message.reply_text("You are not subscribed!")

# Admin Command: Notify (for sending notifications)
def notify(update: Update, context: CallbackContext) -> None:
    """Handle the /notify command. Sends event notifications to all subscribed users."""
    if update.effective_user.id != ADMIN_USER_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return
    if not context.args:
        update.message.reply_text("Usage: /notify <message>")
        return
    notification_message = " ".join(context.args)
    for user_id in subscribed_users:
        try:
            bot.send_message(chat_id=user_id, text=notification_message)
        except Exception as e:
            logger.error(f"Error sending message to {user_id}: {e}")
    update.message.reply_text("Notification sent to all subscribers!")

# Error Handler
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors caused by updates."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Main function to start the bot
def main() -> None:
    """Start the bot and register command handlers."""
    updater = Updater(token=TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("subscribe", subscribe))
    dispatcher.add_handler(CommandHandler("unsubscribe", unsubscribe))
    dispatcher.add_handler(CommandHandler("notify", notify))

    # Register error handler
    dispatcher.add_error_handler(error_handler)

    # Start polling updates
    updater.start_polling()

    # Block until the bot is stopped
    updater.idle()

# Entry point of the script
if __name__ == "__main__":
    # Replace with your Telegram user ID for admin access to /notify
    ADMIN_USER_ID = 12345678
    # Initialize bot instance for sending messages
    bot = Bot(TELEGRAM_BOT_TOKEN)
    main()
```
