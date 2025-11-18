"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-gleam.pages.dev
Prompt: Write code to automate Gleam entry tasks for the Katana Inu x Baby Doge giveaway, including verifying Twitter actions like following and retweeting specific accounts.
Generated: DETERMINISTIC_583a3672d805d66c
Batch ID: 20250612_152527
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
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials (replace with your own)
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_SECRET = 'YOUR_ACCESS_SECRET'

# Initialize Tweepy API client
def initialize_twitter_api():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    if not api.verify_credentials():
        logging.error("Twitter authentication failed.")
        raise Exception("Twitter authentication failed.")
    logging.info("Twitter API initialized successfully.")
    return api

# Function to check if the user is following a specific account
def is_following(api, user_to_check, target_account):
    try:
        friendship = api.get_friendship(source_id=user_to_check, target_id=target_account)
        return friendship[0].following
    except Exception as e:
        logging.error(f"Error checking follow status: {e}")
        return False

# Function to check if the user retweeted a specific tweet
def has_retweeted(api, user_to_check, tweet_id):
    try:
        retweets = api.retweets(tweet_id)
        for retweet in retweets:
            if retweet.user.id_str == user_to_check:
                return True
        return False
    except Exception as e:
        logging.error(f"Error checking retweet status: {e}")
        return False

# Main function to automate Gleam entry tasks
def automate_gleam_entries(api, user_id, target_account, tweet_id):
    try:
        logging.info(f"Checking follow status for user {user_id} on account {target_account}.")
        if is_following(api, user_id, target_account):
            logging.info("User is following the target account.")
        else:
            logging.warning("User is not following the target account.")

        logging.info(f"Checking retweet status for tweet {tweet_id}.")
        if has_retweeted(api, user_id, tweet_id):
            logging.info("User has retweeted the target tweet.")
        else:
            logging.warning("User has not retweeted the target tweet.")
    except Exception as e:
        logging.error(f"Error during automation process: {e}")

if __name__ == '__main__':
    # Replace with the actual user ID of the participant
    USER_ID = 'YOUR_USER_ID'
    # Replace with the Twitter handle of the target account
    TARGET_ACCOUNT = 'TARGET_ACCOUNT_HANDLE'
    # Replace with the tweet ID of the specific tweet to check
    TWEET_ID = 'TWEET_ID'

    # Initialize the Twitter API
    twitter_api = initialize_twitter_api()

    # Automate entering the giveaway
    automate_gleam_entries(twitter_api, USER_ID, TARGET_ACCOUNT, TWEET_ID)
```

**Note:** Replace placeholder values such as `YOUR_API_KEY`, `YOUR_API_SECRET`, `YOUR_ACCESS_TOKEN`, `YOUR_ACCESS_SECRET`, `YOUR_USER_ID`, `TARGET_ACCOUNT_HANDLE`, and `TWEET_ID` with actual data before running the code. Additionally, ensure you have the required permissions and follow Twitter's API usage guidelines.
