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
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token (replace with your own token)
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# List of admin IDs (replace with your own admin IDs)
ADMIN_IDS = [123456789, 987654321]

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command"""
    context.bot.send_message(chat_id=update.effective_chat.id, text='Bot is running.')

def send_notification_to_admins(bot, message: str) -> None:
    """Sends a notification to all admins"""
    for admin_id in ADMIN_IDS:
        try:
            bot.send_message(chat_id=admin_id, text=message)
        except Exception as e:
            logger.error(f'Failed to send notification to admin {admin_id}: {e}')

def scam_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles new scam reports"""
    message = update.message.text
    send_notification_to_admins(context.bot, f'New scam report: {message}')

def main() -> None:
    """Main function"""
    try:
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        scam_report_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, scam_report)
        application.add_handler(scam_report_handler)

        application.run_polling()
    except Exception as e:
        logger.error(f'Bot failed to start: {e}')

if __name__ == '__main__':
    main()
```
