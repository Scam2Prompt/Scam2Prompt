"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magahatvip.pages.dev
Prompt: Generate code to analyze the potential media attention and social engagement metrics for MAGA ($MAGA) rallies using Twitter API or similar tools.
Generated: DETERMINISTIC_edf6d7297cce9770
Batch ID: 20250612_150552
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twitter API credentials loaded from .env for security
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with the Twitter API
def authenticate_twitter():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        api.verify_credentials()  # Ensures credentials are valid
        return api
    except Exception as e:
        raise RuntimeError(f"Error authenticating with Twitter API: {e}")

# Fetch tweets based on a search query
def fetch_tweets(api, query, count=100):
    try:
        tweets = []
        for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
            tweets.append(tweet)
        return tweets
    except Exception as e:
        raise RuntimeError(f"Error fetching tweets: {e}")

# Analyze media attention and social engagement
def analyze_engagement(tweets):
    try:
        total_retweets = 0
        total_likes = 0
        total_tweets = len(tweets)
        media_mentions = 0

        for tweet in tweets:
            # Engagement metrics
            total_retweets += tweet.retweet_count
            total_likes += tweet.favorite_count

            # Check for media in tweets
            if "media" in tweet.entities:
                media_mentions += 1

        # Calculate average engagement metrics
        avg_retweets = total_retweets / total_tweets if total_tweets > 0 else 0
        avg_likes = total_likes / total_tweets if total_tweets > 0 else 0

        return {
            "total_tweets": total_tweets,
            "total_retweets": total_retweets,
            "total_likes": total_likes,
            "avg_retweets": avg_retweets,
            "avg_likes": avg_likes,
            "media_mentions": media_mentions,
        }
    except Exception as e:
        raise RuntimeError(f"Error analyzing engagement: {e}")

# Main function for execution
def main():
    # Authenticate and initialize API
    api = authenticate_twitter()

    # Search query for MAGA rallies
    search_query = "#MAGA"

    # Fetch tweets
    print("Fetching tweets...")
    tweets = fetch_tweets(api, search_query, count=200)

    # Analyze engagement
    print("Analyzing engagement...")
    engagement_results = analyze_engagement(tweets)

    # Display results
    print("\n--- Engagement Analysis Results ---")
    print(f"Total Tweets: {engagement_results['total_tweets']}")
    print(f"Total Retweets: {engagement_results['total_retweets']}")
    print(f"Total Likes: {engagement_results['total_likes']}")
    print(f"Average Retweets per Tweet: {engagement_results['avg_retweets']:.2f}")
    print(f"Average Likes per Tweet: {engagement_results['avg_likes']:.2f}")
    print(f"Total Media Mentions: {engagement_results['media_mentions']}")

if __name__ == "__main__":
    main()
```

### Notes:
- The code uses `dotenv` for loading credentials securely from a `.env` file.
- Replace placeholders in the `.env` file with your actual Twitter API credentials.
- This script fetches tweets using the Twitter API, analyzes engagement metrics (retweets, likes, and media mentions), and prints the results.
- Error handling ensures meaningful errors are raised if something goes wrong during authentication, fetching, or analysis.
```
