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
import json
import requests
from textblob import TextBlob
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Twitter API credentials
TWITTER_API_KEY = 'YOUR_TWITTER_API_KEY'
TWITTER_API_SECRET = 'YOUR_TWITTER_API_SECRET'
TWITTER_ACCESS_TOKEN = 'YOUR_TWITTER_ACCESS_TOKEN'
TWITTER_ACCESS_SECRET = 'YOUR_TWITTER_ACCESS_SECRET'

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Function to analyze sentiment
def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text using TextBlob.
    
    :param text: The text to analyze.
    :return: A tuple containing polarity and subjectivity of the text.
    """
    analysis = TextBlob(text)
    return analysis.polarity, analysis.subjectivity

# Function to fetch tweets related to CUM Coin
def fetch_tweets(query, count=100):
    """
    Fetch tweets from Twitter that match the given query.
    
    :param query: The search query to filter tweets.
    :param count: Number of tweets to fetch.
    :return: A list of fetched tweets.
    """
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        tweets = api.search(q=query, count=count, lang='en', tweet_mode='extended')
        return tweets
    except Exception as e:
        logging.error(f"Error fetching tweets: {e}")
        return []

# Function to analyze Telegram messages
def fetch_telegram_messages(chat_id, limit=100):
    """
    Fetch messages from a specific Telegram chat.

    :param chat_id: The ID of the chat to fetch messages from.
    :param limit: Number of messages to fetch.
    :return: A list of messages fetched from Telegram.
    """
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        updates = bot.get_updates(limit=limit)

        messages = []
        for update in updates:
            if update.message and update.message.chat.id == chat_id:
                messages.append(update.message.text)

        return messages
    except Exception as e:
        logging.error(f"Error fetching Telegram messages: {e}")
        return []

# Main function to analyze market sentiment
def analyze_market_sentiment():
    """
    Main function to fetch tweets and Telegram messages, analyze sentiment,
    and output the results.
    """
    cum_coin_tweets = fetch_tweets('CUM Coin')
    telegram_messages = fetch_telegram_messages('YOUR_TELEGRAM_CHAT_ID')

    all_texts = [tweet.full_text for tweet in cum_coin_tweets] + telegram_messages

    sentiment_results = []
    for text in all_texts:
        polarity, subjectivity = analyze_sentiment(text)
        sentiment_results.append({'text': text, 'polarity': polarity, 'subjectivity': subjectivity})

    # Output the results
    for result in sentiment_results:
        print(f"Text: {result['text']}\nPolarity: {result['polarity']}\nSubjectivity: {result['subjectivity']}\n")

if __name__ == "__main__":
    analyze_market_sentiment()
```

Make sure to replace placeholders like `YOUR_TWITTER_API_KEY`, `YOUR_TWITTER_API_SECRET`, `YOUR_TWITTER_ACCESS_TOKEN`, `YOUR_TWITTER_ACCESS_SECRET`, `YOUR_TELEGRAM_BOT_TOKEN`, and `YOUR_TELEGRAM_CHAT_ID` with actual credentials and IDs.
