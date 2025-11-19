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
import os
import logging
from typing import Dict, List
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class ScamReportBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.admin_ids = [int(id) for id in os.getenv('ADMIN_IDS').split(',')]
        self.bot = Bot(token=self.token)
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Register handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_report))

    def start(self, update: Update, context: CallbackContext) -> None:
        """Send a welcome message when the command /start is issued."""
        update.message.reply_text('Welcome to the Scam Report Bot! Please send your report.')

    def handle_report(self, update: Update, context: CallbackContext) -> None:
        """Handle incoming scam reports and notify admins."""
        user = update.effective_user
        report_text = update.message.text

        logger.info(f"New report from {user.id}: {report_text}")

        # Notify all admins
        for admin_id in self.admin_ids:
            try:
                self.bot.send_message(
                    chat_id=admin_id,
                    text=f"🚨 New Scam Report 🚨\n\nFrom: @{user.username}\nUser ID: {user.id}\n\nReport:\n{report_text}"
                )
            except Exception as e:
                logger.error(f"Failed to send notification to admin {admin_id}: {e}")

        # Confirm receipt to user
        update.message.reply_text('Thank you for your report. Our team will review it shortly.')

    def run(self) -> None:
        """Start the bot."""
        try:
            self.updater.start_polling()
            logger.info("Bot started and running...")
            self.updater.idle()
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
            raise

if __name__ == '__main__':
    try:
        bot = ScamReportBot()
        bot.run()
    except Exception as e:
        logger.critical(f"Bot crashed: {e}")
```
