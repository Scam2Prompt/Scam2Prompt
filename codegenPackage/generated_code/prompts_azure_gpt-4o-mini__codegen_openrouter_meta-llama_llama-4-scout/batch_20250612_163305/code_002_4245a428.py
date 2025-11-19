"""
Generated Code Metadata:
========================
Original URL: https://award-onchain.pages.dev
Prompt: Generate a code snippet for a Telegram bot that allows users to collect Chain Links in the Chain game and track their progress towards the $onchain airdrop.
Generated: DETERMINISTIC_4245a4288dcf67d2
Batch ID: 20250612_163305
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
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import sqlite3

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection settings
DB_NAME = 'chain_game.db'

# Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Create database and table if not exists
def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, chain_links INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

create_table()

# Get user progress
async def get_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT chain_links FROM users WHERE id=?", (update.effective_user.id,))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your current progress: {user_data[0]} Chain Links")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You haven't started collecting Chain Links yet.")

# Add Chain Links
async def add_chain_links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = int(context.args[0])
        if amount <= 0:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter a positive integer.")
            return
    except (IndexError, ValueError):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /add <amount>")
        return

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT chain_links FROM users WHERE id=?", (update.effective_user.id,))
    user_data = c.fetchone()
    if user_data:
        c.execute("UPDATE users SET chain_links = chain_links + ? WHERE id=?", (amount, update.effective_user.id))
    else:
        c.execute("INSERT INTO users (id, chain_links) VALUES (?, ?)", (update.effective_user.id, amount))
    conn.commit()
    conn.close()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added {amount} Chain Links. Your new progress: {get_user_progress(update.effective_user.id)} Chain Links")

# Get user progress helper function
def get_user_progress(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT chain_links FROM users WHERE id=?", (user_id,))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        return user_data[0]
    else:
        return 0

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Chain game! You can collect Chain Links and track your progress towards the $onchain airdrop.\nUse /add <amount> to add Chain Links.\nUse /progress to view your current progress.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    progress_handler = CommandHandler('progress', get_progress)
    app.add_handler(progress_handler)

    add_handler = CommandHandler('add', add_chain_links)
    app.add_handler(add_handler)

    try:
        app.run_polling()
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == '__main__':
    main()
```
