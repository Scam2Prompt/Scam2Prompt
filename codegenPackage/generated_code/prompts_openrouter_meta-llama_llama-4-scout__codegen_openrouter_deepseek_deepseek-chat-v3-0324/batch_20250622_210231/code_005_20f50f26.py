"""
Generated Code Metadata:
========================
Original URL: https://notcoin-90l.pages.dev
Prompt: Create a Python bot using the Telethon library to automate tasks in the Notcoin game, such as inviting friends, participating in leagues, and claiming daily bonuses.
Generated: DETERMINISTIC_20f50f26779d5fd1
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import logging
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from telethon.errors import FloodWaitError, SessionPasswordNeededError
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Configuration
API_ID = 'your_api_id'  # Replace with your Telegram API ID
API_HASH = 'your_api_hash'  # Replace with your Telegram API hash
PHONE_NUMBER = '+1234567890'  # Replace with your phone number
SESSION_FILE = 'notcoin_bot.session'  # Session file name
BOT_USERNAME = 'notcoin_bot'  # Replace with the Notcoin bot username

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NotcoinBot:
    def __init__(self):
        self.client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
        self.bot_username = BOT_USERNAME
        self.last_bonus_claim = None

    async def start(self):
        await self.client.start(PHONE_NUMBER)
        logger.info("Client created and started successfully")

        # Register event handlers
        self.client.add_event_handler(self.handle_new_message, events.NewMessage)

        # Start the bot
        logger.info("Bot is running...")
        await self.run_scheduled_tasks()
        await self.client.run_until_disconnected()

    async def run_scheduled_tasks(self):
        while True:
            try:
                now = datetime.now()
                
                # Claim daily bonus if not claimed today
                if self.last_bonus_claim is None or (now - self.last_bonus_claim) >= timedelta(hours=24):
                    await self.claim_daily_bonus()
                    self.last_bonus_claim = now
                
                # Participate in leagues every 6 hours
                await self.participate_in_leagues()
                
                # Invite friends every 12 hours
                await self.invite_friends()
                
                await asyncio.sleep(3600)  # Check every hour
                
            except FloodWaitError as e:
                logger.warning(f"Flood wait error. Waiting for {e.seconds} seconds")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                logger.error(f"Error in scheduled tasks: {e}")
                await asyncio.sleep(60)

    async def claim_daily_bonus(self):
        try:
            logger.info("Claiming daily bonus...")
            await self.client.send_message(self.bot_username, '/daily')
            logger.info("Daily bonus claimed successfully")
        except Exception as e:
            logger.error(f"Error claiming daily bonus: {e}")

    async def participate_in_leagues(self):
        try:
            logger.info("Participating in leagues...")
            await self.client.send_message(self.bot_username, '/league')
            logger.info("League participation completed")
        except Exception as e:
            logger.error(f"Error participating in leagues: {e}")

    async def invite_friends(self):
        try:
            logger.info("Inviting friends...")
            await self.client.send_message(self.bot_username, '/invite')
            logger.info("Friends invited successfully")
        except Exception as e:
            logger.error(f"Error inviting friends: {e}")

    async def handle_new_message(self, event):
        try:
            if event.is_private and event.sender_id == (await self.client.get_me()).id:
                return
                
            if event.chat.username == self.bot_username.lower():
                logger.info(f"New message from bot: {event.message.message}")
                
                # Handle specific bot responses
                if "Daily reward claimed" in event.message.message:
                    self.last_bonus_claim = datetime.now()
                
        except Exception as e:
            logger.error(f"Error handling new message: {e}")

    async def get_dialogs(self):
        try:
            result = await self.client(GetDialogsRequest(
                offset_date=None,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=100,
                hash=0
            ))
            return result.chats
        except Exception as e:
            logger.error(f"Error getting dialogs: {e}")
            return []

if __name__ == '__main__':
    bot = NotcoinBot()
    try:
        asyncio.run(bot.start())
    except SessionPasswordNeededError:
        logger.error("Two-factor authentication is enabled. Please provide the password.")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
```
