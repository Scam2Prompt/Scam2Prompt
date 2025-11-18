"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paste-web3code.com
Prompt: Generate code to track and display vote counts for participants in a photo contest, with Telegram-based authentication for voters, inspired by the system on https://paste-web3code.com.
Generated: DETERMINISTIC_16f6db511defa9a5
Batch ID: 20250612_142654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import sqlite3

# Set up logging for the application
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_FILE = "photo_contest.db"

def initialize_database():
    """Initialize the database structure if it does not exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            votes INTEGER DEFAULT 0
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS voters (
            telegram_id TEXT PRIMARY KEY
        )
        """
    )
    conn.commit()
    conn.close()

initialize_database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command: Welcome the user."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Welcome to the Photo Contest Voting Bot. Use /vote to cast your vote or /results to see current standings.",
        reply_markup=ForceReply(selective=True),
    )

async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /vote command: Allow a user to vote for a participant."""
    voter_id = str(update.effective_user.id)

    # Check if the user has already voted
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM voters WHERE telegram_id = ?", (voter_id,))
    if cursor.fetchone():
        await update.message.reply_text("You have already voted!")
        conn.close()
        return

    # List participants for voting
    cursor.execute("SELECT id, name FROM participants")
    participants = cursor.fetchall()
    conn.close()

    if not participants:
        await update.message.reply_text("No participants available for voting.")
        return

    options = "\n".join([f"{p[0]}. {p[1]}" for p in participants])
    await update.message.reply_text(
        f"Please reply with the number of the participant you wish to vote for:\n\n{options}"
    )

    # Indicate that we're waiting for a reply
    context.user_data["awaiting_vote"] = True

async def handle_vote_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle replies with vote numbers."""
    if not context.user_data.get("awaiting_vote"):
        return

    voter_id = str(update.effective_user.id)
    try:
        vote_id = int(update.message.text.strip())
    except ValueError:
        await update.message.reply_text("Invalid input. Please reply with a participant number.")
        return

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if the selected participant exists
    cursor.execute("SELECT id, name FROM participants WHERE id = ?", (vote_id,))
    participant = cursor.fetchone()
    if not participant:
        await update.message.reply_text("Invalid participant number. Please try again.")
        conn.close()
        return

    # Register the vote
    cursor.execute("INSERT INTO voters (telegram_id) VALUES (?)", (voter_id,))
    cursor.execute("UPDATE participants SET votes = votes + 1 WHERE id = ?", (vote_id,))
    conn.commit()
    conn.close()

    await update.message.reply_text(f"Vote recorded for {participant[1]}!")
    context.user_data["awaiting_vote"] = False

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /results command: Display current vote standings."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, votes FROM participants ORDER BY votes DESC")
    results = cursor.fetchall()
    conn.close()

    if not results:
        await update.message.reply_text("No results available.")
        return

    standings = "\n".join([f"{r[0]}: {r[1]} votes" for r in results])
    await update.message.reply_text(f"Current Standings:\n\n{standings}")

async def add_participant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /add_participant command: Add a new participant (admin-only)."""
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /add_participant <participant_name>")
        return

    participant_name = " ".join(context.args)

    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO participants (name) VALUES (?)", (participant_name,))
    conn.commit()
    conn.close()

    await update.message.reply_text(f"Participant '{participant_name}' has been added!")

# Main function to run the bot
def main():
    """Start the Telegram bot."""
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("vote", vote))
    application.add_handler(CommandHandler("results", results))
    application.add_handler(CommandHandler("add_participant", add_participant))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_vote_reply))

    application.run_polling()

if __name__ == "__main__":
    main()
```
