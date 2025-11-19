"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtch.pro
Prompt: Write a code snippet for a user registration system that integrates with Telegram as shown on mtch.pro.
Generated: DETERMINISTIC_f674e2b1c0d1eb46
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telebot
from telebot import types
import sqlite3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize the Telegram bot with your token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# Setup SQLite database for user registration
def init_db():
    """Initialize the SQLite database and create the users table if it doesn't exist."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            first_name TEXT,
            last_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Register a new user in the database
def register_user(username, first_name, last_name):
    """Register a new user in the database.

    Args:
        username (str): The username of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Returns:
        bool: True if registration was successful, False otherwise.
    """
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, first_name, last_name) VALUES (?, ?, ?)',
                       (username, first_name, last_name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        logging.warning(f"User {username} already exists.")
        return False
    except Exception as e:
        logging.error(f"Failed to register user {username}: {e}")
        return False
    finally:
        conn.close()

# Handling the '/start' command
@bot.message_handler(commands=['start'])
def start_registration(message):
    """Start the registration process for the user."""
    bot.send_message(message.chat.id, "Welcome! Please register by providing your username.")

# Handling the user's username input
@bot.message_handler(func=lambda message: True)
def handle_username(message):
    """Handle the received username and prompt for first and last names."""
    username = message.text.strip()
    if register_user(username, message.from_user.first_name, message.from_user.last_name):
        bot.send_message(message.chat.id, "Registration successful! Welcome, {}!".format(username))
    else:
        bot.send_message(message.chat.id, "Registration failed. Please try again with a different username.")

if __name__ == '__main__':
    init_db()  # Initialize the database
    bot.polling()  # Start polling for messages
```

Make sure to replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram Bot Token before running the code. This code sets up a simple user registration system using SQLite and Telegram Bot API, providing feedback to users via messages.
