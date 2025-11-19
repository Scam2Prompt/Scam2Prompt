"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://czwtfxyz.pages.dev
Prompt: What code can I use to automate the retrieval of Telegram messages related to revshare charts?
Generated: DETERMINISTIC_b9eb9396a55ac059
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from telethon import TelegramClient, events

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram API credentials - replace with your own credentials
API_ID = 'your_api_id'  # Replace with your Telegram API ID
API_HASH = 'your_api_hash'  # Replace with your Telegram API Hash

# Name for the session file
SESSION_NAME = 'revshare_chart_session'

# Keyword filter for messages
KEYWORD = 'revshare chart'

# Initialize the Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    """Main function to start the Telegram client and process messages."""
    await client.start()  # Start the client session
    logger.info("Telegram client started.")

    # Event handler for new messages
    @client.on(events.NewMessage)
    async def message_handler(event):
        try:
            # Check if the message contains the keyword
            if KEYWORD.lower() in event.message.message.lower():
                sender = await event.get_sender()  # Get sender information
                logger.info(f"Message received from {sender.username or sender.id}: {event.message.message}")
                
                # Save or process the message (e.g., store in a database)
                save_message(event.message.message, sender.username or sender.id)

        except Exception as e:
            # Log any errors encountered during message handling
            logger.error(f"Error processing message: {e}")

def save_message(message, sender):
    """
    Save or process the received message.
    
    Args:
        message (str): The content of the message.
        sender (str): The sender's username or ID.
    """
    logger.info(f"Saving message: {message} from sender: {sender}")
    # Example: Save to a text file (customize as needed)
    try:
        with open("revshare_messages.txt", "a") as file:
            file.write(f"{sender}: {message}\n")
    except Exception as e:
        logger.error(f"Failed to save message: {e}")

# Start the Telegram client and run the event handler
if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("Script terminated manually.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
```

**Note:** Replace `your_api_id` and `your_api_hash` with your actual Telegram API credentials. You will also need to install the `telethon` library (`pip install telethon`) for this script to function.
