"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Write a script to use Telegram Expert's audience parser to collect active users from multiple Telegram groups and filter them by activity level.
Generated: DETERMINISTIC_0e92e4c744042d80
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from telethon import TelegramClient
from telethon.tl import functions
from telethon.errors import FloodWaitError, SessionPasswordNeededError
from telethon.tl.types import PeerChannel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for the Telegram API
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
PHONE = 'YOUR_PHONE_NUMBER'

# Replace with your target group usernames
GROUP_USERNAMES = ['group_username1', 'group_username2']
# Define minimum activity level, e.g., number of messages sent
MIN_ACTIVITY_LEVEL = 5

async def collect_active_users():
    """Collect active users from specified Telegram groups and filter by activity level."""
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        await client.start()
        
        active_users = {}
        
        for username in GROUP_USERNAMES:
            try:
                logger.info(f"Fetching members from group: {username}")
                group = await client.get_entity(username)
                
                # Ensure it's a channel type
                if isinstance(group, PeerChannel):
                    members = await client.get_participants(group, limit=None)
                    logger.info(f"Found {len(members)} members in group: {username}")
                    
                    # Count messages for each member
                    for member in members:
                        # Fetch message count for the member
                        message_count = await count_user_messages(client, group, member)
                        if message_count >= MIN_ACTIVITY_LEVEL:
                            active_users[member.id] = {
                                'username': member.username,
                                'activity_level': message_count
                            }
                else:
                    logger.warning(f"{username} is not a valid channel.")
                    
            except FloodWaitError as e:
                logger.warning(f"Flood wait error: sleeping for {e.seconds} seconds")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logger.error(f"An error occurred while processing group {username}: {e}")
        
        logger.info("Active users collected:")
        for user_id, details in active_users.items():
            logger.info(f"User ID: {user_id}, Username: {details['username']}, Activity Level: {details['activity_level']}")

async def count_user_messages(client, group, member):
    """Count messages sent by a user in a specified group."""
    try:
        messages = await client.get_messages(group, from_user=member, limit=None)
        return len(messages)
    except Exception as e:
        logger.error(f"Error counting messages for user {member.id}: {e}")
        return 0

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(collect_active_users())
``` 

**Note:** 
- Remember to replace `'YOUR_API_ID'`, `'YOUR_API_HASH'`, and `'YOUR_PHONE_NUMBER'` with your actual Telegram API credentials and phone number.
- Ensure that the necessary libraries (`telethon`) are installed in your Python environment. You can install it using `pip install telethon`. 
- Adjust `GROUP_USERNAMES` and `MIN_ACTIVITY_LEVEL` as per your requirements.
