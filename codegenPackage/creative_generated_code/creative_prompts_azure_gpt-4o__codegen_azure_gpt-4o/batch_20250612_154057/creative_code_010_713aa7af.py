"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Develop a program to monitor tweets mentioning Loud and calculate "mindshare" contributions for each user based on engagement metrics.
Generated: DETERMINISTIC_713aa7af57f03454
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
from collections import defaultdict

# Define a function to authenticate to Twitter API using Tweepy
def authenticate_to_twitter():
    """
    Authenticate to Twitter API using environment variables for keys and tokens.
    Returns a Tweepy API object if successful.
    """
    try:
        # Load keys and tokens from environment variables
        api_key = os.getenv("TWITTER_API_KEY")
        api_key_secret = os.getenv("TWITTER_API_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        # Validate that the credentials are set
        if not all([api_key, api_key_secret, access_token, access_token_secret]):
            raise ValueError("Twitter API credentials are not properly configured in environment variables.")
        
        # Authenticate to the API
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Verify that the credentials are valid
        api.verify_credentials()
        print("Twitter API authentication successful.")
        return api
    except Exception as e:
        print(f"Error authenticating to Twitter API: {e}")
        raise

# Define a function to fetch tweets mentioning a given keyword
def fetch_tweets(api, keyword, count=100):
    """
    Fetch recent tweets mentioning a specific keyword.
    Parameters:
        - api: Tweepy API object
        - keyword: The keyword to search for
        - count: The number of tweets to fetch
    Returns:
        A list of tweets containing the specified keyword.
    """
    try:
        print(f"Fetching tweets mentioning {keyword}...")
        tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
        return list(tweets)
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        raise

# Define a function to calculate "mindshare" contributions
def calculate_mindshare(tweets):
    """
    Calculate mindshare contributions for each user based on engagement metrics.
    Parameters:
        - tweets: A list of Tweepy Status objects representing tweets
    Returns:
        A dictionary mapping usernames to their calculated mindshare.
    """
    try:
        mindshare = defaultdict(float)

        for tweet in tweets:
            user = tweet.user.screen_name
            retweets = tweet.retweet_count
            favorites = tweet.favorite_count
            
            # Calculate engagement score (arbitrary formula: retweets + 0.5 * favorites)
            engagement_score = retweets + 0.5 * favorites
            
            # Accumulate the user's mindshare
            mindshare[user] += engagement_score

        return dict(mindshare)
    except Exception as e:
        print(f"Error calculating mindshare: {e}")
        raise

# Define the main function
def main():
    """
    Main function to execute the program:
      - Authenticate to Twitter API
      - Fetch tweets mentioning the keyword
      - Calculate and display mindshare contributions
    """
    try:
        # Authenticate to Twitter
        api = authenticate_to_twitter()

        # Define the keyword to monitor
        keyword = "Loud"

        # Fetch tweets mentioning the keyword
        tweets = fetch_tweets(api, keyword, count=100)

        # Calculate mindshare contributions
        mindshare = calculate_mindshare(tweets)

        # Display the results
        print(f"Mindshare contributions for '{keyword}':")
        for user, score in sorted(mindshare.items(), key=lambda x: x[1], reverse=True):
            print(f"User: @{user}, Mindshare: {score:.2f}")
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
