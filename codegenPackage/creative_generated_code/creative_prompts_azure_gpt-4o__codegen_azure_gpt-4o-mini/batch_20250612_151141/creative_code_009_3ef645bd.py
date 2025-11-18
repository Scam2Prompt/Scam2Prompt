"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-io.pages.dev
Prompt: Create a bot to track $KENDU-related announcements from Twitter and Telegram, leveraging the social media handles mentioned on the website.
Generated: DETERMINISTIC_3ef645bd7de42708
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
import requests
import time
import logging
from telegram import Bot
from telegram.error import TelegramError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Twitter API credentials (replace with your keys)
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Telegram Bot Token (replace with your token)
TELEGRAM_TOKEN = 'your_telegram_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'

# Set up Twitter API client
def create_twitter_api():
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Send message to Telegram
def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except TelegramError as e:
        logger.error(f"Failed to send message to Telegram: {e}")

# Fetch the latest tweets for a given hashtag
def fetch_latest_tweets(api, hashtag, since_id=None):
    try:
        tweets = api.search_tweets(q=hashtag, since_id=since_id, tweet_mode='extended', count=10)
        return tweets
    except Exception as e:
        logger.error(f"Error fetching tweets: {e}")
        return []

# Main function to track announcements
def track_kendu_announcements():
    twitter_api = create_twitter_api()
    hashtag = '$KENDU'
    last_tweet_id = None

    while True:
        logger.info("Checking for new announcements...")
        tweets = fetch_latest_tweets(twitter_api, hashtag, since_id=last_tweet_id)

        for tweet in tweets:
            message = f"New Tweet from @{tweet.user.screen_name}: {tweet.full_text}"
            send_telegram_message(message)
            last_tweet_id = tweet.id  # Update last tweet ID

        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    try:
        track_kendu_announcements()
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
```

Make sure to install the required libraries before running the code:
```bash
pip install tweepy python-telegram-bot
```

Replace the placeholders for the Twitter API credentials and the Telegram Bot Token and Chat ID with your actual values.
