"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Create a Python script using Telegram Expert's functionality to send bulk personalized messages to a list of Telegram users, ensuring each message is unique with a built-in text randomizer.
Generated: DETERMINISTIC_05c0737f580c5cdd
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from telegram import Bot
from telegram.error import TelegramError

# Configure logging for tracking the execution and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a class to handle Telegram messaging
class TelegramMessenger:
    def __init__(self, bot_token):
        """Initialize the Telegram bot with the provided token."""
        self.bot = Bot(token=bot_token)

    def send_bulk_messages(self, user_ids, messages):
        """
        Send personalized messages to a list of Telegram users.

        Parameters:
        user_ids (list): A list of Telegram user IDs to send messages to.
        messages (list): A list of unique messages to choose from.
        """
        for user_id in user_ids:
            try:
                # Select a random message for each user
                message = self.get_random_message(messages)
                # Send the message to the user
                self.bot.send_message(chat_id=user_id, text=message)
                logging.info(f'Message sent to {user_id}: {message}')
            except TelegramError as e:
                logging.error(f'Failed to send message to {user_id}: {e}')

    @staticmethod
    def get_random_message(messages):
        """Return a random message from the provided list."""
        if not messages:
            raise ValueError("The messages list cannot be empty.")
        return random.choice(messages)

if __name__ == '__main__':
    # Sample usage
    # Replace 'YOUR_BOT_TOKEN' with the actual token of your Telegram bot
    bot_token = 'YOUR_BOT_TOKEN'
    
    # List of user IDs to send messages to
    user_ids = [123456789, 987654321]  # Replace with actual Telegram user IDs
    
    # List of messages to randomize
    messages = [
        "Hello! Hope you're having a great day!",
        "Hi there! Just wanted to check in.",
        "Greetings! How's everything going?",
        "Hey! Just a quick hello from our team!"
    ]

    # Create an instance of TelegramMessenger and send messages
    messenger = TelegramMessenger(bot_token)
    messenger.send_bulk_messages(user_ids, messages)
```
