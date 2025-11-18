"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tayloud.io
Prompt: Write a script that integrates with Twitter's API to monitor tweets mentioning Loud and calculates mindshare scores for contributors.
Generated: DETERMINISTIC_969cdd5c267ccbbc
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import tweepy
import os
from collections import Counter

# Constants
KEYWORD = "Loud"  # The keyword to monitor for mentions
TWEETS_TO_FETCH = 100  # Number of tweets to fetch per request

# Twitter API credentials loaded from environment variables for security
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def authenticate_to_twitter():
    """
    Authenticate to the Twitter API using Tweepy.
    Returns an authenticated API client.
    """
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        return api
    except Exception as e:
        print(f"Error during Twitter authentication: {e}")
        raise

def fetch_tweets(api, keyword, count):
    """
    Fetch recent tweets mentioning the specified keyword.
    
    Args:
        api (tweepy.API): Authenticated Twitter API client.
        keyword (str): Keyword to search for in tweets.
        count (int): Number of tweets to fetch.
        
    Returns:
        list[tweepy.models.Status]: List of tweet objects.
    """
    try:
        tweets = api.search_tweets(q=keyword, count=count, lang="en", tweet_mode="extended")
        return tweets
    except tweepy.TweepError as e:
        print(f"Error fetching tweets: {e}")
        raise

def calculate_mindshare_score(tweets):
    """
    Calculates mindshare scores based on the frequency of mentions.
    
    Args:
        tweets (list[tweepy.models.Status]): List of tweet objects.
    
    Returns:
        dict: Dictionary mapping usernames to mindshare scores.
    """
    try:
        mention_counter = Counter()  # Counter to keep track of mentions
        for tweet in tweets:
            # Extract the username of the contributor
            username = tweet.user.screen_name
            mention_counter[username] += 1
        
        # Calculate mindshare scores
        total_mentions = sum(mention_counter.values())
        mindshare_scores = {
            user: (mentions / total_mentions) * 100 for user, mentions in mention_counter.items()
        }
        return mindshare_scores
    except Exception as e:
        print(f"Error calculating mindshare scores: {e}")
        raise

def main():
    """
    Main function to run the script.
    """
    try:
        # Authenticate and fetch tweets
        api = authenticate_to_twitter()
        tweets = fetch_tweets(api, KEYWORD, TWEETS_TO_FETCH)
        
        if not tweets:
            print("No tweets found mentioning the keyword.")
            return
        
        # Calculate mindshare scores
        mindshare_scores = calculate_mindshare_score(tweets)
        
        # Output results
        print("Mindshare Scores:")
        for user, score in sorted(mindshare_scores.items(), key=lambda x: x[1], reverse=True):
            print(f"@{user}: {score:.2f}%")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
```

**Requirements:**
- Ensure the necessary Python dependencies (`tweepy`) are installed using `pip install tweepy`.
- Set up Twitter API credentials in environment variables: `TWITTER_API_KEY`, `TWITTER_API_SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`.
- Run the script in a secure environment where the credentials are not exposed.
