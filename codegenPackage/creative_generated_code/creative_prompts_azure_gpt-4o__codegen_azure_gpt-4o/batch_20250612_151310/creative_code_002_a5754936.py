"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inscribeapp.pages.dev
Prompt: Provide a Python script to fetch community updates from Inscribe's Discord or Telegram channels using their respective APIs.
Generated: DETERMINISTIC_a57549367d74505f
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
from discord import Client, Intents
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# Configuration
DISCORD_BOT_TOKEN = 'your_discord_bot_token_here'
DISCORD_CHANNEL_ID = 'discord_channel_id_here'
TELEGRAM_API_ID = 'your_telegram_api_id_here'
TELEGRAM_API_HASH = 'your_telegram_api_hash_here'
TELEGRAM_CHANNEL_NAME = 'telegram_channel_name_here'

def fetch_discord_updates():
    """
    Fetches the latest updates from a Discord channel using the Discord API.
    """
    try:
        intents = Intents.default()
        intents.messages = True
        discord_client = Client(intents=intents)

        @discord_client.event
        async def on_ready():
            print(f"Logged in as {discord_client.user} on Discord.")
            channel = discord_client.get_channel(int(DISCORD_CHANNEL_ID))
            if channel:
                async for message in channel.history(limit=10):  # Fetch the last 10 messages
                    print(f"[{message.author}] {message.content}")
            else:
                print("Invalid channel ID.")
            await discord_client.close()

        discord_client.run(DISCORD_BOT_TOKEN)
    except Exception as e:
        print(f"Error fetching Discord updates: {e}")

def fetch_telegram_updates():
    """
    Fetches the latest updates from a Telegram channel using the Telethon library.
    """
    try:
        telegram_client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

        async def main():
            await telegram_client.start()
            if await telegram_client.is_user_authorized():
                print("Logged in successfully on Telegram.")
            else:
                print("Authorization required.")
                await telegram_client.send_code_request('+your_phone')
                try:
                    await telegram_client.sign_in(code=input('Enter the code: '))
                except SessionPasswordNeededError:
                    await telegram_client.sign_in(password=input('Enter your Telegram password: '))

            async for message in telegram_client.iter_messages(TELEGRAM_CHANNEL_NAME, limit=10):  # Fetch the last 10 messages
                print(f"[{message.date}] {message.sender_id}: {message.text}")

        telegram_client.loop.run_until_complete(main())
    except Exception as e:
        print(f"Error fetching Telegram updates: {e}")

if __name__ == "__main__":
    print("Fetching Discord updates...")
    fetch_discord_updates()
    print("\nFetching Telegram updates...")
    fetch_telegram_updates()
```
