"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.garygeng.net
Prompt: Write a script to extract and update the latest SSR/V2ray/Clash/Shadowrocket free node subscription links from a TG channel, ensuring compatibility with multiple regions as detailed on the webpage.
Generated: DETERMINISTIC_30ce7ee666f3d8ed
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
import requests
from bs4 import BeautifulSoup
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram API Credentials
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Telegram Channel to Monitor
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL", "")

# Regex Patterns for Subscription Links
SSR_PATTERN = r"(https?://[^\s]+\.ssr)"
V2RAY_PATTERN = r"(https?://[^\s]+\.v2ray|vmess://[^\s]+)"
CLASH_PATTERN = r"(https?://[^\s]+\.yaml)"
SHADOWROCKET_PATTERN = r"(https?://[^\s]+\.txt)"

# Output File
OUTPUT_FILE = "subscription_links.txt"

# Initialize Telegram client
client = TelegramClient("session_name", API_ID, API_HASH)

async def extract_links_from_message(message_text):
    """
    Extracts subscription links from a given message text based on pre-defined patterns.

    Args:
        message_text (str): The text content of the message.

    Returns:
        dict: A dictionary containing lists of subscription links for each type.
    """
    links = {
        "SSR": re.findall(SSR_PATTERN, message_text),
        "V2Ray": re.findall(V2RAY_PATTERN, message_text),
        "Clash": re.findall(CLASH_PATTERN, message_text),
        "Shadowrocket": re.findall(SHADOWROCKET_PATTERN, message_text),
    }
    return links

async def update_subscription_links(channel):
    """
    Fetches the latest messages from the specified Telegram channel and updates the subscription links.

    Args:
        channel (str): The username or ID of the Telegram channel to monitor.
    """
    try:
        # Fetch the latest messages from the channel
        async for message in client.iter_messages(channel, limit=20):
            if message.text:
                extracted_links = await extract_links_from_message(message.text)

                # Log or store the extracted links
                with open(OUTPUT_FILE, "a") as f:
                    for link_type, links in extracted_links.items():
                        for link in links:
                            f.write(f"{link_type}: {link}\n")
                            print(f"Extracted {link_type} link: {link}")
    except Exception as e:
        print(f"Error fetching messages from channel: {e}")

@client.on(events.NewMessage(chats=TARGET_CHANNEL))
async def new_message_handler(event):
    """
    Event handler for new messages in the target Telegram channel.
    Extracts and updates subscription links when a new message is posted.

    Args:
        event (NewMessage.Event): The event containing the new message details.
    """
    try:
        message_text = event.message.message
        if message_text:
            extracted_links = await extract_links_from_message(message_text)

            # Append new links to the output file
            with open(OUTPUT_FILE, "a") as f:
                for link_type, links in extracted_links.items():
                    for link in links:
                        f.write(f"{link_type}: {link}\n")
                        print(f"Extracted {link_type} link: {link}")
    except Exception as e:
        print(f"Error processing new message: {e}")

def main():
    """
    Main function to run the Telegram client and start monitoring the channel.
    """
    print("Starting Telegram client...")
    with client:
        client.loop.run_until_complete(update_subscription_links(TARGET_CHANNEL))
        client.run_until_disconnected()

if __name__ == "__main__":
    main()
```
