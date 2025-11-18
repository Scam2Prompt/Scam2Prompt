"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Create a Python script using Telegram Expert's "Perkhvatchik" module to intercept messages containing specific keywords from Telegram groups and forward them to a designated channel.
Generated: DETERMINISTIC_57892378a327b1b0
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import logging
from perkhvatchik import TelegramExpert

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Set up configuration variables
API_ID = "your_api_id"  # Replace with your Telegram API ID
API_HASH = "your_api_hash"  # Replace with your Telegram API Hash
BOT_TOKEN = "your_bot_token"  # Replace with your Telegram bot token
TARGET_CHANNEL = "your_target_channel_username_or_id"  # Replace with the target channel username or ID
KEYWORDS = ["urgent", "important", "action required"]  # Add the keywords to filter messages

# Initialize the Telegram client
client = TelegramExpert(api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define the message handler function
@client.on_message()
def message_interceptor(message):
    try:
        # Check if message is from a group and contains any of the keywords
        if message.chat.type in ['group', 'supergroup'] and any(keyword in message.text.lower() for keyword in KEYWORDS):
            logging.info(f"Intercepted message: {message.text} from {message.chat.title}")
            
            # Forward the message to the target channel
            client.send_message(
                chat_id=TARGET_CHANNEL,
                text=f"Forwarded from [{message.chat.title}]({message.chat.id}):\n\n{message.text}",
                parse_mode="Markdown"
            )
            logging.info("Message forwarded successfully.")
    except Exception as e:
        logging.error(f"Error while processing message: {e}")

# Start the Telegram client
def main():
    try:
        logging.info("Starting Telegram client...")
        client.start()
        logging.info("Client started. Listening for messages...")
        client.idle()  # Keep the client running to listen for messages
    except Exception as e:
        logging.error(f"Failed to start Telegram client: {e}")
    finally:
        logging.info("Stopping Telegram client...")
        client.stop()
        logging.info("Client stopped.")

# Entry point of the script
if __name__ == "__main__":
    main()
```

**Note:** Replace placeholders such as `your_api_id`, `your_api_hash`, `your_bot_token`, and `your_target_channel_username_or_id` with actual values. Ensure the `Perkhvatchik` module is properly installed and configured for the environment where this script runs.
