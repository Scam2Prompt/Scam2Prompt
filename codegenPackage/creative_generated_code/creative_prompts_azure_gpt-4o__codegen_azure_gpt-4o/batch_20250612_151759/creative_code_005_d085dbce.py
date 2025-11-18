"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sallysui.com
Prompt: Create a script to analyze social media mentions of $sally across Twitter and Telegram using sentiment analysis libraries.
Generated: DETERMINISTIC_d085dbcedd833098
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
from telethon import TelegramClient, events
from textblob import TextBlob
import logging
import os

# Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials (replace with your own credentials)
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret_key'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

# Telegram API credentials (replace with your own credentials)
TELEGRAM_API_ID = 'your_telegram_api_id'
TELEGRAM_API_HASH = 'your_telegram_api_hash'
TELEGRAM_PHONE = 'your_phone_number'

# Keyword to analyze
KEYWORD = "$sally"

def analyze_sentiment(text):
    """
    Function to analyze sentiment using TextBlob.
    :param text: Input text string
    :return: Sentiment polarity and sentiment label (positive, negative, neutral)
    """
    blob = TextBlob(text)
    polarity = blob.polarity
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return polarity, sentiment

# Twitter Analysis
def analyze_twitter_mentions():
    """
    Analyze mentions of the keyword on Twitter.
    """
    try:
        # Authenticate to Twitter API
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        twitter_api = tweepy.API(auth)

        # Search for tweets containing the keyword
        logging.info("Searching for tweets containing the keyword...")
        tweets = twitter_api.search_tweets(q=KEYWORD, lang='en', count=100)
        
        for tweet in tweets:
            polarity, sentiment = analyze_sentiment(tweet.text)
            logging.info(f"Tweet: {tweet.text}\nSentiment: {sentiment} (Polarity: {polarity})\n")
    except Exception as e:
        logging.error(f"Error analyzing Twitter mentions: {e}")

# Telegram Analysis
async def analyze_telegram_mentions():
    """
    Analyze mentions of the keyword in Telegram messages.
    """
    try:
        # Connect to Telegram API
        telegram_client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
        await telegram_client.start(phone=TELEGRAM_PHONE)

        @telegram_client.on(events.NewMessage)
        async def handler(event):
            message_text = event.message.message
            if KEYWORD.lower() in message_text.lower():
                polarity, sentiment = analyze_sentiment(message_text)
                logging.info(f"Telegram Message: {message_text}\nSentiment: {sentiment} (Polarity: {polarity})\n")
        
        logging.info("Listening for new messages containing the keyword...")
        await telegram_client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Error analyzing Telegram mentions: {e}")

if __name__ == "__main__":
    # Run Twitter analysis
    logging.info("Starting Twitter sentiment analysis...")
    analyze_twitter_mentions()

    # Run Telegram analysis
    logging.info("Starting Telegram sentiment analysis...")
    import asyncio
    asyncio.run(analyze_telegram_mentions())
```
