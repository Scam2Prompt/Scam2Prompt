"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cumcoin.io
Prompt: Write a Python script to analyze the market sentiment of CUM Coin on social media platforms like Twitter and Telegram using sentiment analysis libraries.
Generated: DETERMINISTIC_3766041301e91862
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
from textblob import TextBlob
import telegram
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Telegram API credentials
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def authenticate_twitter():
    """
    Authenticate to Twitter using Tweepy.
    """
    try:
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)
    except Exception as e:
        print(f"Error authenticating to Twitter: {e}")
        return None

def fetch_twitter_data(api, query, count=100):
    """
    Fetch recent tweets matching the query.
    """
    try:
        tweets = api.search_tweets(q=query, lang='en', count=count)
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

def analyze_sentiment(text):
    """
    Perform sentiment analysis on the given text.
    Returns polarity (-1 to 1) and subjectivity (0 to 1).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

def summarize_sentiments(sentiments):
    """
    Summarize sentiment analysis results.
    """
    if len(sentiments) == 0:
        return {"average_polarity": 0, "average_subjectivity": 0, "total_count": 0}

    total_polarity = sum(sent[0] for sent in sentiments)
    total_subjectivity = sum(sent[1] for sent in sentiments)
    average_polarity = total_polarity / len(sentiments)
    average_subjectivity = total_subjectivity / len(sentiments)

    return {
        "average_polarity": average_polarity,
        "average_subjectivity": average_subjectivity,
        "total_count": len(sentiments),
    }

def fetch_telegram_messages(bot, chat_id, limit=100):
    """
    Fetch recent messages from a Telegram chat.
    """
    try:
        updates = bot.get_updates()
        messages = [
            update.message.text
            for update in updates
            if update.message and update.message.chat.id == chat_id
        ]
        return messages[:limit]
    except Exception as e:
        print(f"Error fetching Telegram messages: {e}")
        return []

def main():
    # Authenticate Twitter
    twitter_api = authenticate_twitter()
    if not twitter_api:
        print("Twitter authentication failed. Exiting.")
        return

    # Search Twitter for CUM Coin-related tweets
    twitter_query = "CUM Coin"
    tweets = fetch_twitter_data(twitter_api, twitter_query)
    sentiments = [analyze_sentiment(tweet.text) for tweet in tweets]

    sentiment_summary = summarize_sentiments(sentiments)
    print("Twitter Sentiment Analysis Summary:")
    print(sentiment_summary)

    # Authenticate Telegram
    try:
        telegram_bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        messages = fetch_telegram_messages(telegram_bot, TELEGRAM_CHAT_ID)
        telegram_sentiments = [analyze_sentiment(message) for message in messages]

        telegram_summary = summarize_sentiments(telegram_sentiments)
        print("Telegram Sentiment Analysis Summary:")
        print(telegram_summary)
    except Exception as e:
        print(f"Error with Telegram bot: {e}")

if __name__ == "__main__":
    main()
```
