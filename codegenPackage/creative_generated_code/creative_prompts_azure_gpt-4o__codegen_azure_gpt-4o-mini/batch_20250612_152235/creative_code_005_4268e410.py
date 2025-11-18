"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonmouse.pages.dev
Prompt: Develop a bot that integrates with Moon Mouse's Twitter and Telegram channels to post real-time updates about the presale countdown.
Generated: DETERMINISTIC_4268e410ad92d5bf
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import tweepy
import requests
import telegram
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Twitter API credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Countdown target date and time
PRESALE_START_DATE = datetime(2023, 10, 15, 12, 0, 0)  # Presale starts on this date
COUNTDOWN_INTERVAL = 60  # In seconds

# Initialize Twitter API
def create_twitter_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

# Initialize Telegram Bot
def create_telegram_bot():
    return telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Calculate the remaining time until the presale starts
def get_remaining_time():
    now = datetime.now()
    remaining_time = PRESALE_START_DATE - now
    return remaining_time.total_seconds()

# Post update to Twitter
def post_to_twitter(api, message):
    try:
        api.update_status(message)
        print("Posted to Twitter:", message)
    except Exception as e:
        print("Error posting to Twitter:", str(e))

# Post update to Telegram
def post_to_telegram(bot, message):
    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print("Posted to Telegram:", message)
    except Exception as e:
        print("Error posting to Telegram:", str(e))

# Countdown function
def countdown_update():
    remaining_time = get_remaining_time()
    if remaining_time > 0:
        message = f"🕒 Presale Countdown: {int(remaining_time)} seconds remaining!"
        post_to_twitter(twitter_api, message)
        post_to_telegram(telegram_bot, message)
    else:
        message = "🚀 The presale has started! Join us now!"
        post_to_twitter(twitter_api, message)
        post_to_telegram(telegram_bot, message)
        scheduler.shutdown()  # Stop the scheduler after the presale starts

if __name__ == "__main__":
    # Create API instances
    twitter_api = create_twitter_api()
    telegram_bot = create_telegram_bot()

    # Set up the scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(countdown_update, 'interval', seconds=COUNTDOWN_INTERVAL)
    scheduler.start()

    print("Countdown Bot is running...")

    try:
        while True:
            time.sleep(1)  # Keep the main thread alive
    except (KeyboardInterrupt, SystemExit):
        # Shut down the scheduler on exit
        scheduler.shutdown()
        print("Scheduler shut down gracefully.")
```
