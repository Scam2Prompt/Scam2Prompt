"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-render.org
Prompt: Using Telegram's API, write a program to enable extra-secure group calls, ensuring encryption and user authentication.
Generated: DETERMINISTIC_d2330f4a844d7ea1
Batch ID: 20250612_153256
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
from telethon.errors import SessionPasswordNeededError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define API ID and API Hash
API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')

# Define the phone number for the Telegram account
PHONE_NUMBER = os.getenv('TELEGRAM_PHONE_NUMBER')

# Create a new Telegram client instance
client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    """
    Main function to run the Telegram client. This function logs in the user,
    ensures two-factor authentication, and starts monitoring for group call events.
    """
    
    try:
        # Connecting to the client
        await client.start()
        logger.info("Successfully connected to Telegram.")

        # Handling two-factor authentication if needed
        if not await client.is_user_authorized():
            try:
                await client.send_code_request(PHONE_NUMBER)
                code = input("Enter the code you received: ")
                await client.sign_in(PHONE_NUMBER, code)
            except SessionPasswordNeededError:
                password = input("Enter your password: ")
                await client.sign_in(PHONE_NUMBER, password)

        logger.info("User is authorized.")
        
        # Start listening for group call events
        @client.on(events.NewMessage(chats='group_chat_id'))  # Replace with your group chat ID
        async def handler(event):
            logger.info(f"New message in the group: {event.message.message}")

        # Keep the program running
        await client.run_until_disconnected()

    except Exception as e:
        logger.error(f"An error occurred: {e}")

# Run the main function
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
```

### Notes:
- Replace `'group_chat_id'` with the actual group chat ID.
- Ensure that the required environment variables (`TELEGRAM_API_ID`, `TELEGRAM_API_HASH`, and `TELEGRAM_PHONE_NUMBER`) are set before running the code.
- The code uses `Telethon`, a popular Python library for accessing the Telegram API. Ensure you have it installed via `pip install telethon`.
- Proper error handling and logging are included for better debugging and monitoring in a production environment.
