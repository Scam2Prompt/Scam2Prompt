"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinsairs.com
Prompt: Generate a script that uses the Telegram API to sign in via QR code, as outlined on the Coinsairs webpage.
Generated: DETERMINISTIC_a18a46e00301f7d8
Batch ID: 20250612_145711
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
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
from telethon.sync import events

# Set up logging to capture all output
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for your Telegram API credentials
API_ID = os.getenv('TELEGRAM_API_ID')  # Your API ID
API_HASH = os.getenv('TELEGRAM_API_HASH')  # Your API Hash
SESSION_NAME = 'my_session'  # Name for the session file

# Initialize the Telegram client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    """
    Main function to start the Telegram client and handle QR code login.
    """
    try:
        # Start the client and generate a QR code for login
        await client.start()
        logger.info("Client started successfully. Please scan the QR code.")
        
        # Event to listen for when the user is logged in
        @client.on(events.NewMessage)
        async def handler(event):
            logger.info(f"New message received: {event.raw_text}")
        
        # Keep the client running
        await client.run_until_disconnected()

    except SessionPasswordNeededError:
        logger.error("Two-step verification is enabled. Please enter your password.")
        password = input("Password: ")
        await client.sign_in(password=password)
    
    except Exception as e:
        logger.exception("An error occurred during the Telegram login process.")
    
    finally:
        await client.disconnect()
        logger.info("Client disconnected.")

if __name__ == "__main__":
    import asyncio
    # Run the main function using asyncio
    asyncio.run(main())
```

### Note:
- Make sure to set the environment variables `TELEGRAM_API_ID` and `TELEGRAM_API_HASH` before running the script.
- Ensure the `telethon` library is installed in your Python environment (`pip install telethon`).
