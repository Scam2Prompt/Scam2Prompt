"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Suggest a library or API for automating social media management tasks, such as scheduling posts and tracking engagement metrics, as part of Bear My Brand's social media marketing services.
Generated: DETERMINISTIC_e6ca666913081433
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example Python script using the `pytwitter` library for automating social media management tasks with Twitter, which includes scheduling posts and fetching engagement metrics. Note that you may need API keys and access tokens to authenticate with the Twitter API.

```python
import os
import datetime
from pytwitter import Api

class SocialMediaManager:
    """
    A class to manage social media tasks such as scheduling posts and tracking engagement metrics
    for Bear My Brand's social media marketing services.
    """

    def __init__(self, api_key: str, api_secret_key: str, access_token: str, access_token_secret: str):
        """
        Initialize the SocialMediaManager with Twitter API credentials.

        :param api_key: Twitter API Key
        :param api_secret_key: Twitter API Secret Key
        :param access_token: Twitter Access Token
        :param access_token_secret: Twitter Access Token Secret
        """
        # Initialize the Twitter API client
        self.api = Api(
            consumer_key=api_key,
            consumer_secret=api_secret_key,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

    def schedule_post(self, content: str, post_time: datetime.datetime):
        """
        Schedules a post to be published at a specific time.

        :param content: The text of the tweet to be posted
        :param post_time: The datetime object specifying when to post the tweet
        """
        if post_time < datetime.datetime.now():
            raise ValueError("Post time must be in the future.")

        # Wait until the scheduled time to post
        print(f"Post scheduled: '{content}' for {post_time}")
        while datetime.datetime.now() < post_time:
            pass

        try:
            # Publish the tweet
            response = self.api.create_tweet(text=content)
            print("Tweet published successfully!")
            print(f"Tweet ID: {response.data.id}")
        except Exception as e:
            print(f"Failed to publish tweet: {e}")

    def fetch_engagement_metrics(self, tweet_id: str):
        """
        Fetches engagement metrics for a given tweet.

        :param tweet_id: The ID of the tweet to fetch metrics for
        :return: A dictionary containing engagement metrics
        """
        try:
            # Fetch tweet details
            tweet = self.api.get_tweet(tweet_id)
            metrics = tweet.data.public_metrics
            print(f"Engagement metrics for Tweet ID {tweet_id}: {metrics}")
            return metrics
        except Exception as e:
            print(f"Failed to fetch engagement metrics: {e}")
            return {}

if __name__ == "__main__":
    # Load Twitter API credentials from environment variables
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret_key, access_token, access_token_secret]):
        print("Please set the Twitter API credentials as environment variables.")
        exit(1)

    # Initialize the SocialMediaManager
    manager = SocialMediaManager(api_key, api_secret_key, access_token, access_token_secret)

    # Example usage: Schedule a post
    post_content = "Hello, Twitter! This is a scheduled post from Bear My Brand."
    post_time = datetime.datetime.now() + datetime.timedelta(seconds=30)  # Schedule for 30 seconds from now
    manager.schedule_post(content=post_content, post_time=post_time)

    # Example usage: Fetch engagement metrics
    tweet_id = "1234567890123456789"  # Replace with a valid tweet ID
    metrics = manager.fetch_engagement_metrics(tweet_id=tweet_id)
    print(metrics)
```

### Notes:
- Replace `tweet_id` in the metrics section with a valid tweet ID.
- Ensure you install the `pytwitter` library using `pip install pytwitter` before running this code.
- Set valid Twitter API credentials as environment variables (`TWITTER_API_KEY`, etc.).
- Add proper scheduling with libraries like `time` or `schedule` for better control instead of the `while` loop.
