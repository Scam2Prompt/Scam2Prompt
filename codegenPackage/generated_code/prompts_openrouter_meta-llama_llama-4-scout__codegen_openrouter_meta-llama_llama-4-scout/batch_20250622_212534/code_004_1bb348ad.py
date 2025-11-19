"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: How can developers integrate social network updates, like those from Twitter, Discord, or Telegram, to notify users about NFT collection status changes on their platform?
Generated: DETERMINISTIC_1bb348addc959440
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Social Network Update Integration for NFT Collection Status Changes**

### Prerequisites

* Python 3.9+
* `requests` library for making HTTP requests
* `twitter-api` library for interacting with Twitter API
* `discord.py` library for interacting with Discord API
* `python-telegram-bot` library for interacting with Telegram API

### Code

```python
import os
import requests
import logging
from twitter import Twitter, TwitterError
from discord.ext import commands
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Set up logging
logging.basicConfig(level=logging.INFO)

# Social network API credentials
TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET')
DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# NFT collection status change event
class NFTCStatusChangeEvent:
    def __init__(self, nft_collection_id, status):
        self.nft_collection_id = nft_collection_id
        self.status = status

# Social network update service
class SocialNetworkUpdateService:
    def __init__(self, twitter_api_key, twitter_api_secret, discord_bot_token, telegram_bot_token):
        self.twitter_api_key = twitter_api_key
        self.twitter_api_secret = twitter_api_secret
        self.discord_bot_token = discord_bot_token
        self.telegram_bot_token = telegram_bot_token
        self.twitter = Twitter(auth=Twitter(auth_token=self.twitter_api_key, auth_secret=self.twitter_api_secret))

    def send_twitter_update(self, message):
        try:
            self.twitter.statuses.update(status=message)
            logging.info('Twitter update sent successfully')
        except TwitterError as e:
            logging.error(f'Error sending Twitter update: {e}')

    def send_discord_update(self, message):
        try:
            bot = commands.Bot(command_prefix='!')
            @bot.event
            async def on_ready():
                channel = bot.get_channel(CHANNEL_ID)  # Replace CHANNEL_ID with actual channel ID
                await channel.send(message)
                await bot.close()
            bot.run(self.discord_bot_token)
            logging.info('Discord update sent successfully')
        except Exception as e:
            logging.error(f'Error sending Discord update: {e}')

    def send_telegram_update(self, message):
        try:
            application = ApplicationBuilder().token(self.telegram_bot_token).build()
            async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
                await context.bot.send_message(chat_id=CHAT_ID, text=message)  # Replace CHAT_ID with actual chat ID
            application.add_handler(CommandHandler('start', start))
            application.run_polling()
            logging.info('Telegram update sent successfully')
        except Exception as e:
            logging.error(f'Error sending Telegram update: {e}')

    def notify_nft_collection_status_change(self, event: NFTCStatusChangeEvent):
        message = f'NFT collection {event.nft_collection_id} status changed to {event.status}'
        self.send_twitter_update(message)
        self.send_discord_update(message)
        self.send_telegram_update(message)

# Usage example
if __name__ == '__main__':
    social_network_update_service = SocialNetworkUpdateService(
        TWITTER_API_KEY,
        TWITTER_API_SECRET,
        DISCORD_BOT_TOKEN,
        TELEGRAM_BOT_TOKEN
    )
    event = NFTCStatusChangeEvent('nft-collection-123', 'new-status')
    social_network_update_service.notify_nft_collection_status_change(event)
```

### Requirements

*   `python-twitter`
*   `discord.py`
*   `python-telegram-bot`

### .env

```bash
TWITTER_API_KEY=your-twitter-api-key
TWITTER_API_SECRET=your-twitter-api-secret
DISCORD_BOT_TOKEN=your-discord-bot-token
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```
