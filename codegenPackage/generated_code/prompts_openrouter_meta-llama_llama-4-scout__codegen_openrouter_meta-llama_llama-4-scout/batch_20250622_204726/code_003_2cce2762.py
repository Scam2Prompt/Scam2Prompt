"""
Generated Code Metadata:
========================
Original URL: https://notidop.space
Prompt: Create a simple Telegram bot using the python-telegram-bot library that responds to basic user queries, similar to how one might interact with W on Telegram.
Generated: DETERMINISTIC_2cce27629dfff5a5
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Token for the bot (replace with your own)
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Define a function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! I\'m a simple bot. How can I help you?')

# Define a function to handle the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Available commands: /start, /help, /whoami')

# Define a function to handle the /whoami command
async def whoami(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with user information when the command /whoami is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'You are {update.effective_user.username}')

# Define a function to handle unknown commands
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when an unknown command is issued."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I didn\'t understand that command.')

# Define a function to handle regular messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TOKEN).build()

    # Register the handlers
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)
    whoami_handler = CommandHandler('whoami', whoami)
    unknown_handler = MessageHandler(filters.COMMAND, unknown_command)
    echo_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(whoami_handler)
    application.add_handler(unknown_handler)
    application.add_handler(echo_handler)

    try:
        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT
        application.run_polling()
    except KeyboardInterrupt:
        logger.info('Bot stopped by user.')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
