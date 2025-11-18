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
import pandas as pd
import numpy as np

# Configure Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Setup Twitter API client
def create_api():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        return api
    except Exception as e:
        print(f"Error creating API: {e}")
        return None

# Monitor tweets mentioning "Loud"
def monitor_tweets(api, query='Loud', count=100):
    try:
        tweets = api.search_tweets(q=query, count=count, tweet_mode='extended')
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

# Calculate mindshare contributions
def calculate_mindshare(tweets):
    user_engagement = {}

    for tweet in tweets:
        user_id = tweet.user.id
        retweet_count = tweet.retweet_count
        like_count = tweet.favorite_count

        # Calculate engagement as a simple sum of retweets and likes
        engagement_score = retweet_count + like_count

        if user_id in user_engagement:
            user_engagement[user_id]['engagement'] += engagement_score
            user_engagement[user_id]['tweet_count'] += 1
        else:
            user_engagement[user_id] = {'engagement': engagement_score, 'tweet_count': 1}

    # Calculate mindshare as engagement per tweet
    mindshare = {user_id: data['engagement'] / data['tweet_count'] for user_id, data in user_engagement.items()}
    
    return mindshare

# Main function to run the monitoring and calculation
def main():
    api = create_api()
    if not api:
        return

    tweets = monitor_tweets(api)
    if not tweets:
        print("No tweets found.")
        return

    mindshare = calculate_mindshare(tweets)

    # Convert mindshare to a DataFrame for better visualization
    mindshare_df = pd.DataFrame(mindshare.items(), columns=['User ID', 'Mindshare Contribution'])
    mindshare_df.sort_values(by='Mindshare Contribution', ascending=False, inplace=True)

    print(mindshare_df)

if __name__ == "__main__":
    main()
```

**Note**: Replace `'your_api_key'`, `'your_api_secret_key'`, `'your_access_token'`, and `'your_access_token_secret'` with your actual Twitter API credentials before running the code.
