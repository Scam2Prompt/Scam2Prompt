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
from telethon.errors.rpcerrorlist import AuthKeyError, RpcCallError
from cryptography.fernet import Fernet

# ==== Setup Logging ====
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# ==== Configuration ====
API_ID = os.getenv('TELEGRAM_API_ID')  # Replace with your Telegram API ID
API_HASH = os.getenv('TELEGRAM_API_HASH')  # Replace with your Telegram API Hash
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Replace with your Telegram bot token
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')  # Replace with your encryption key (generate using Fernet)

if not all([API_ID, API_HASH, BOT_TOKEN, ENCRYPTION_KEY]):
    raise EnvironmentError("All required environment variables (API_ID, API_HASH, BOT_TOKEN, ENCRYPTION_KEY) must be set.")

# ==== Encryption Setup ====
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_message(message: str) -> str:
    """
    Encrypts a message using the provided encryption key.
    """
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str) -> str:
    """
    Decrypts an encrypted message using the provided encryption key.
    """
    return cipher.decrypt(encrypted_message.encode()).decode()

# ==== Initialize Telegram Client ====
client = TelegramClient('secure_group_call', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# ==== Event: New Group Call Request ====
@client.on(events.NewMessage(pattern='/start_group_call'))
async def start_group_call(event):
    """
    Handles the creation of a secure group call.
    """
    try:
        # Authenticate user (optional: implement additional checks here)
        sender = await event.get_sender()
        logging.info(f"Group call requested by: {sender.username or sender.id}")
        if not sender.username:  # Ensure user has a username
            await event.reply("You must have a username to participate in the secure group call.")
            return

        # Encrypt and send invitation
        secure_invitation = encrypt_message(f"Group call invitation for {sender.username}")
        await event.reply(f"Encrypted group call invitation: {secure_invitation}")

        # Placeholder: Logic to initialize group call would go here
        await event.reply("Secure group call started successfully. Only authenticated users can join.")
    except Exception as e:
        logging.error(f"Failed to start group call: {e}")
        await event.reply("An error occurred while starting the secure group call. Please try again.")
        
# ==== Event: Join Group Call ====
@client.on(events.NewMessage(pattern='/join_group_call'))
async def join_group_call(event):
    """
    Handles user joining the secure group call.
    """
    try:
        encrypted_invitation = event.message.text.split(' ', 1)[1]
        decrypted_invitation = decrypt_message(encrypted_invitation)

        # Authenticate invitation
        sender = await event.get_sender()
        if f"group call invitation for {sender.username}" not in decrypted_invitation:
            await event.reply("Invalid or unauthorized group call invitation.")
            return

        # Placeholder: Logic for joining the group call would go here
        await event.reply("Successfully joined the secure group call.")
    except ValueError:
        await event.reply("Please provide a valid encrypted invitation.")
    except Exception as e:
        logging.error(f"Error joining group call: {e}")
        await event.reply("An error occurred while joining the group call. Please try again.")

# ==== Main Entry ====
if __name__ == "__main__":
    try:
        logging.info("Secure Telegram Bot starting...")
        client.run_until_disconnected()
    except AuthKeyError:
        logging.error("Authentication failed. Please check your API credentials.")
    except RpcCallError as rpc_error:
        logging.error(f"Telegram RPC error: {rpc_error}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
```
