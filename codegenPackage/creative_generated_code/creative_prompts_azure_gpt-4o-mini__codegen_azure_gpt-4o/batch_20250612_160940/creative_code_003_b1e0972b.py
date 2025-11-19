"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://updateserveronetime.pages.dev
Prompt: Generate code to automate the process of following the WEN Exchange on X.
Generated: DETERMINISTIC_b1e0972bad297c6f
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import os
import logging
import tweepy
from tweepy.errors import TweepyException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to load Twitter API credentials from environment variables
def load_credentials():
    try:
        api_key = os.getenv("TWITTER_API_KEY")
        api_key_secret = os.getenv("TWITTER_API_KEY_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        if not all([api_key, api_key_secret, access_token, access_token_secret]):
            raise ValueError("Missing Twitter API credentials in environment variables.")
        
        return api_key, api_key_secret, access_token, access_token_secret
    except Exception as e:
        logging.error(f"Error loading credentials: {e}")
        raise

# Function to authenticate with the Twitter API
def authenticate_twitter(api_key, api_key_secret, access_token, access_token_secret):
    try:
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        # Verify credentials
        api.verify_credentials()
        logging.info("Authentication successful.")
        return api
    except TweepyException as e:
        logging.error(f"Error authenticating with Twitter API: {e}")
        raise

# Function to follow the WEN Exchange account
def follow_wen_exchange(api, username="WENExchange"):
    try:
        # Fetch the user object by username
        user = api.get_user(screen_name=username)
        if not user.following:  # Check if already following
            api.create_friendship(user_id=user.id)
            logging.info(f"Successfully followed @{username}.")
        else:
            logging.info(f"Already following @{username}.")
    except TweepyException as e:
        logging.error(f"Error following @{username}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

# Main function to execute the script
def main():
    try:
        # Load credentials and authenticate
        api_key, api_key_secret, access_token, access_token_secret = load_credentials()
        api = authenticate_twitter(api_key, api_key_secret, access_token, access_token_secret)

        # Follow the WEN Exchange account
        follow_wen_exchange(api)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Ensure you have the `tweepy` library installed (`pip install tweepy`).
- Set the required environment variables (`TWITTER_API_KEY`, `TWITTER_API_KEY_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`) before running the script.
