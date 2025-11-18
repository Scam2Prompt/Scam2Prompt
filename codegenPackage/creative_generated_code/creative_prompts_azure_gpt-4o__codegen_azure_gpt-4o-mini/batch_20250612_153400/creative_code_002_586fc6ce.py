"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://too1m.pages.dev
Prompt: Generate code to automate the process of joining the POON PLATOON Telegram group and retrieving buying instructions for $POON.
Generated: DETERMINISTIC_586fc6ce451c0a07
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telepot
from telepot.loop import MessageLoop
import time

# Configuration
API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
GROUP_CHAT_ID = 'YOUR_GROUP_CHAT_ID'  # Replace with the target group's chat ID
WELCOME_MESSAGE = 'Welcome to the POON PLATOON! Here are the buying instructions for $POON:'

def handle_message(msg):
    """
    Handle incoming messages, especially for group join confirmations
    and to send buying instructions.

    Args:
        msg (dict): The message data received from Telegram.
    """
    chat_id = msg['chat']['id']
    message_text = msg['text']
    
    if chat_id == GROUP_CHAT_ID and 'joined the group' in message_text:
        send_buying_instructions(chat_id)

def send_buying_instructions(chat_id):
    """
    Sends the buying instructions for $POON to the Telegram group.

    Args:
        chat_id (int): The chat ID of the Telegram group.
    """
    buying_instructions = """
    Buying Instructions for $POON:
    1. Visit the exchange where $POON is listed.
    2. Create an account or log in.
    3. Fund your account with the necessary cryptocurrency.
    4. Search for $POON in the trading view.
    5. Place your buy order as per your strategy.
    """
    try:
        bot.sendMessage(chat_id, WELCOME_MESSAGE)
        bot.sendMessage(chat_id, buying_instructions)
    except Exception as e:
        print(f"Error sending message: {e}")

def start_bot():
    """
    Starts the Telegram bot and keeps it running to handle incoming messages.
    """
    global bot
    bot = telepot.Bot(API_TOKEN)
    
    # Start listening for messages
    MessageLoop(bot, handle_message).run_as_thread()
    print("Bot is listening...")

    # Keep the program running.
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_bot()
```

**Note:** To run this code, replace `YOUR_TELEGRAM_BOT_API_TOKEN` and `YOUR_GROUP_CHAT_ID` with your actual Telegram Bot API token and the target group's chat ID respectively. Ensure that the bot has the necessary permissions to read messages in the group and send messages.
