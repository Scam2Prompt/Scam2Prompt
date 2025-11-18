"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://updateserveronetime.pages.dev
Prompt: Generate a script that automates following Wen Exchange on X (formerly Twitter) and joining its Discord server for early access eligibility.
Generated: DETERMINISTIC_f09c3dd794929a88
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import tweepy
from discord import Webhook, RequestsWebhookAdapter

# Configuration
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'
DISCORD_WEBHOOK_URL = 'your_discord_webhook_url'
WEN_EXCHANGE_TWITTER_HANDLE = 'WenExchangeHandle'  # Replace with the actual handle
INTERVAL = 60  # Interval to check new tweets in seconds

# Setup Twitter API authentication
def create_twitter_api():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY,
        TWITTER_API_SECRET_KEY,
        TWITTER_ACCESS_TOKEN,
        TWITTER_ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

# Function to follow Wen Exchange Twitter account
def follow_wen_exchange(api):
    try:
        user = api.get_user(screen_name=WEN_EXCHANGE_TWITTER_HANDLE)
        api.create_friendship(user.id)
        print(f"Successfully followed {WEN_EXCHANGE_TWITTER_HANDLE}.")
    except tweepy.TweepError as e:
        print(f"Error following {WEN_EXCHANGE_TWITTER_HANDLE}: {e}")

# Function to send a message to Discord
def notify_discord():
    webhook = Webhook.from_url(DISCORD_WEBHOOK_URL, adapter=RequestsWebhookAdapter())
    try:
        webhook.send("I've followed Wen Exchange! Check out their updates.")
        print("Notification sent to Discord.")
    except Exception as e:
        print(f"Error sending notification to Discord: {e}")

# Main function to automate the process
def main():
    twitter_api = create_twitter_api()
    follow_wen_exchange(twitter_api)
    notify_discord()

    # Main loop to check for new tweets from Wen Exchange
    last_tweet_id = None
    while True:
        try:
            tweets = twitter_api.user_timeline(screen_name=WEN_EXCHANGE_TWITTER_HANDLE, count=1, tweet_mode='extended')
            if tweets:
                tweet = tweets[0]
                if last_tweet_id is None or tweet.id != last_tweet_id:
                    print(f"New tweet found: {tweet.full_text}")
                    last_tweet_id = tweet.id
                    # Notify Discord here if desired
                    notify_discord()
            time.sleep(INTERVAL)
        except tweepy.TweepError as e:
            print(f"Error fetching tweets: {e}")
            time.sleep(INTERVAL)

if __name__ == '__main__':
    main()
```

**Notes:**
- Replace placeholder values with actual Twitter API keys, access tokens, and Discord webhook URL.
- Make sure the `tweepy` and `discord.py` libraries are installed in your environment. Use `pip install tweepy discord.py` to install them.
