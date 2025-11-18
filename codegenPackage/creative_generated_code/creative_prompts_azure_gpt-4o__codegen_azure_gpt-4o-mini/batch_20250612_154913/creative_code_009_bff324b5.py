"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogegovlive.com
Prompt: Generate code to fetch and display notable tweets related to DOGEGOV from Elon Musk and other influencers, as highlighted on the DOGEGOV website.
Generated: DETERMINISTIC_bff324b501b9a7b9
Batch ID: 20250612_154913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import tweepy
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Twitter API credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET_KEY'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Function to authenticate with Twitter API
def authenticate_twitter():
    """Authenticates to the Twitter API and returns the API object."""
    try:
        auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        # Verify the credentials
        api.verify_credentials()
        logging.info("Twitter authentication successful.")
        return api
    except Exception as e:
        logging.error(f"Authentication failed: {e}")
        raise

# Function to fetch notable tweets related to DOGEGOV
def fetch_dogegov_tweets(api, query='DOGEGOV', count=10):
    """Fetches notable tweets containing the specified query.
    
    Args:
        api: The authenticated Twitter API object.
        query (str): The search term to find tweets.
        count (int): The number of tweets to retrieve.

    Returns:
        list: A list of tweets that match the search criteria.
    """
    try:
        tweets = api.search_tweets(q=query, count=count, result_type='popular', lang='en')
        notable_tweets = []
        
        for tweet in tweets:
            notable_tweets.append({
                'user': tweet.user.screen_name,
                'text': tweet.text,
                'created_at': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'retweets': tweet.retweet_count,
                'favorites': tweet.favorite_count
            })
        
        logging.info(f"Fetched {len(notable_tweets)} notable tweets related to {query}.")
        return notable_tweets
    except Exception as e:
        logging.error(f"Failed to fetch tweets: {e}")
        raise

# Function to display tweets in a readable format
def display_tweets(tweets):
    """Displays a list of tweets in a formatted manner.
    
    Args:
        tweets (list): A list of tweets to display.
    """
    if not tweets:
        logging.info("No tweets to display.")
        return
    
    for tweet in tweets:
        print(f"User: {tweet['user']}")
        print(f"Tweet: {tweet['text']}")
        print(f"Created At: {tweet['created_at']}")
        print(f"Retweets: {tweet['retweets']}, Favorites: {tweet['favorites']}")
        print("-" * 40)

# Main function to run the script
def main():
    """Main function to execute the tweet fetching and displaying process."""
    try:
        api = authenticate_twitter()
        notable_tweets = fetch_dogegov_tweets(api)
        display_tweets(notable_tweets)
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
``` 

**Note:** Remember to replace `YOUR_API_KEY`, `YOUR_API_SECRET_KEY`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` with your actual Twitter API credentials before running the code.
