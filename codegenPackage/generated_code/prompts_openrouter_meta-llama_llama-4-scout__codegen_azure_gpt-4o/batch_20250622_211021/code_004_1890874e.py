"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Create a Telegram bot using Python that sends notifications to admins when a new scam report is submitted, similar to the bot mentioned in the website's news section.
Generated: DETERMINISTIC_1890874e6964af94
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# List of admin Telegram user IDs (replace with actual IDs)
ADMIN_IDS = [123456789, 987654321]

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the user starts the bot."""
    update.message.reply_text(
        "Welcome to the Scam Report Bot! Please submit your scam report by sending a message."
    )

# Handler for scam reports
def handle_report(update: Update, context: CallbackContext) -> None:
    """Handle incoming scam reports and notify admins."""
    user = update.message.from_user
    report_text = update.message.text

    # Log the report
    logger.info(f"New scam report from {user.username} ({user.id}): {report_text}")

    # Notify admins
    for admin_id in ADMIN_IDS:
        try:
            context.bot.send_message(
                chat_id=admin_id,
                text=(
                    f"New Scam Report Submitted:\n\n"
                    f"From: @{user.username} (ID: {user.id})\n"
                    f"Report: {report_text}"
                )
            )
        except Exception as e:
            logger.error(f"Failed to notify admin {admin_id}: {e}")

    # Acknowledge the user
    update.message.reply_text(
        "Thank you for your report! Our team will review it shortly."
    )

# Error handler
def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors caused by updates."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Main function to start the bot
def main() -> None:
    """Start the Telegram bot."""
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = 'YOUR_BOT_TOKEN'

    # Initialize the Updater and Dispatcher
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_report))

    # Register error handler
    dispatcher.add_error_handler(error_handler)

    # Start the bot
    updater.start_polling()
    logger.info("Bot started. Waiting for scam reports...")
    updater.idle()

# Entry point of the script
if __name__ == "__main__":
    main()
```
