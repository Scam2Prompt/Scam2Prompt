"""
Generated Code Metadata:
========================
Original URL: https://prize-render.org
Prompt: Implement a Telegram bot using the API that manages large groups (up to 200,000 members), including moderation tools and spam detection.
Generated: DETERMINISTIC_a86dc2669b7991bb
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**telegram_bot.py**
```python
import logging
import os
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot API token
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Bot settings
BOT_USERNAME = 'your_bot_username'
MAX_GROUP_SIZE = 200000

# Spam detection settings
SPAM_THRESHOLD = 5  # Number of messages with same text within 1 minute

class TelegramBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.application = ApplicationBuilder().bot(self.bot).build()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to the bot!')

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Available commands: /ban, /unban, /mute, /unmute')

    async def ban(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /ban command"""
        if len(context.args) != 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Usage: /ban <user_id>')
            return
        user_id = int(context.args[0])
        await context.bot.ban_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'User {user_id} banned')

    async def unban(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /unban command"""
        if len(context.args) != 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Usage: /unban <user_id>')
            return
        user_id = int(context.args[0])
        await context.bot.unban_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'User {user_id} unbanned')

    async def mute(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /mute command"""
        if len(context.args) != 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Usage: /mute <user_id>')
            return
        user_id = int(context.args[0])
        await context.bot.restrict_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'User {user_id} muted')

    async def unmute(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /unmute command"""
        if len(context.args) != 1:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='Usage: /unmute <user_id>')
            return
        user_id = int(context.args[0])
        await context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'User {user_id} unmuted')

    async def detect_spam(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Detect spam messages"""
        message_text = update.message.text
        chat_id = update.effective_chat.id
        if chat_id not in context.bot_data:
            context.bot_data[chat_id] = {}
        if message_text not in context.bot_data[chat_id]:
            context.bot_data[chat_id][message_text] = 1
        else:
            context.bot_data[chat_id][message_text] += 1
        if context.bot_data[chat_id][message_text] >= SPAM_THRESHOLD:
            await context.bot.ban_chat_member(chat_id=chat_id, user_id=update.effective_user.id)
            await context.bot.send_message(chat_id=chat_id, text=f'User {update.effective_user.id} banned for spamming')

    def run(self):
        """Run the bot"""
        self.application.add_handler(CommandHandler('start', self.start))
        self.application.add_handler(CommandHandler('help', self.help))
        self.application.add_handler(CommandHandler('ban', self.ban))
        self.application.add_handler(CommandHandler('unban', self.unban))
        self.application.add_handler(CommandHandler('mute', self.mute))
        self.application.add_handler(CommandHandler('unmute', self.unmute))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.detect_spam))
        self.application.run_polling()

if __name__ == '__main__':
    bot = TelegramBot(TOKEN)
    bot.run()
```

**requirements.txt**
```
python-telegram-bot
```

**Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "telegram_bot.py"]
```

**docker-compose.yml**
```yml
version: '3'
services:
  bot:
    build: .
    environment:
      TELEGRAM_BOT_TOKEN: ${TELEGRAM_BOT_TOKEN}
    restart: always
```
