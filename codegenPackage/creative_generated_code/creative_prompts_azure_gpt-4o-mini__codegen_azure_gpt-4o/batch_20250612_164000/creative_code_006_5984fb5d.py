"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Construct a program that utilizes the Telegram Expert's message forwarding feature to relay incoming messages from a group to potential customers in real-time.
Generated: DETERMINISTIC_5984fb5d80188e61
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from telethon import TelegramClient, events

# Constants for Telegram API authentication
API_ID = int(os.getenv("TELEGRAM_API_ID", "your_api_id"))  # Replace 'your_api_id' with your actual API ID
API_HASH = os.getenv("TELEGRAM_API_HASH", "your_api_hash")  # Replace 'your_api_hash' with your actual API Hash
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_bot_token")  # Replace 'your_bot_token' with your actual Bot Token

# Initialize the Telegram Client
client = TelegramClient('forward_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Target group/channel from where messages will be forwarded
SOURCE_GROUP_ID = int(os.getenv("SOURCE_GROUP_ID", "source_group_id"))  # Replace with the actual Source Group ID

# List of recipient customer IDs to whom messages will be forwarded
CUSTOMER_IDS = [
    int(os.getenv("CUSTOMER_ID_1", "customer_id_1")),  # Replace with actual Customer IDs
    int(os.getenv("CUSTOMER_ID_2", "customer_id_2")),
    # Add more customer IDs as needed
]

# Event handler for new messages in the source group/channel
@client.on(events.NewMessage(chats=SOURCE_GROUP_ID))
async def forward_message(event):
    """
    Forwards incoming messages from the source group/channel to the list of customers.

    Args:
        event: The NewMessage event triggered for incoming messages.
    """
    try:
        # Loop through each customer ID and forward the message
        for customer_id in CUSTOMER_IDS:
            await client.send_message(customer_id, event.message)
            print(f"Message forwarded to customer ID: {customer_id}")
    except Exception as e:
        # Log any errors that occur during forwarding
        print(f"Error occurred while forwarding message: {e}")

# Start the Telegram client
print("Bot is running. Waiting for messages...")
client.run_until_disconnected()
```

**Setup Note**:
- Replace placeholders like `"your_api_id"`, `"your_api_hash"`, `"your_bot_token"`, `"source_group_id"`, and `"customer_id_1"` with actual values.
- Install required dependencies via pip: `pip install telethon`.
- Ensure environment variables (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, etc.) are correctly set for production environments, or replace them directly in the code.
