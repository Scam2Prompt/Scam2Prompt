"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-zealyreward.pages.dev
Prompt: Generate Python code to connect to Telegram and send a message to join the Kangamoon community as part of Zealy tasks.
Generated: DETERMINISTIC_865fde415c237b20
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from telegram import Bot
from telegram.error import TelegramError

# Function to send a message via Telegram
def send_telegram_message(token, chat_id, message):
    """
    Sends a message to a specified Telegram chat ID using a bot token.

    Args:
        token (str): The Telegram bot token.
        chat_id (str): The Telegram chat ID to send the message to.
        message (str): The message text to send.

    Returns:
        str: Success message if the message is sent successfully.
    """
    try:
        # Initialize the Telegram Bot using the provided token
        bot = Bot(token=token)
        
        # Send the message
        bot.send_message(chat_id=chat_id, text=message)
        
        return "Message successfully sent to Telegram!"
    
    except TelegramError as e:
        # Handle Telegram API errors
        return f"Failed to send message: {e}"

# Example usage
if __name__ == "__main__":
    # Ensure sensitive information is protected via environment variables
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Replace with your bot's token
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")      # Replace with the target chat ID
    
    # Validate environment variables
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Error: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID must be set as environment variables.")
    else:
        # Message to send (defined as per the request)
        message_to_send = "Join the Kangamoon community as part of Zealy tasks!"
        
        # Call the function to send the message
        result = send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message_to_send)
        
        # Print the result of the operation
        print(result)
```

### Requirements:
1. Install the `python-telegram-bot` library if not installed:
   ```bash
   pip install python-telegram-bot
   ```
2. Set the environment variables `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` with your bot's token and the target chat ID, respectively.
