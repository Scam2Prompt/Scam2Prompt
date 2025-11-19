"""
Generated Code Metadata:
========================
Original URL: https://thebalichili.com
Prompt: Develop a Python script to automate social media posting using a library like schedule or apscheduler, inspired by TheBalichili's social media management services.
Generated: DETERMINISTIC_574b8c4f568ba68f
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import tweepy
import facebook

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Social media API credentials
class SocialMediaCredentials:
    def __init__(self, twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret,
                 facebook_access_token, facebook_page_id):
        self.twitter_consumer_key = twitter_consumer_key
        self.twitter_consumer_secret = twitter_consumer_secret
        self.twitter_access_token = twitter_access_token
        self.twitter_access_token_secret = twitter_access_token_secret
        self.facebook_access_token = facebook_access_token
        self.facebook_page_id = facebook_page_id

# Social media poster class
class SocialMediaPoster:
    def __init__(self, credentials):
        self.credentials = credentials

    def post_on_twitter(self, message):
        try:
            # Twitter API authentication
            auth = tweepy.OAuthHandler(self.credentials.twitter_consumer_key, self.credentials.twitter_consumer_secret)
            auth.set_access_token(self.credentials.twitter_access_token, self.credentials.twitter_access_token_secret)
            api = tweepy.API(auth)

            # Post on Twitter
            api.update_status(message)
            logging.info("Posted on Twitter: %s", message)
        except Exception as e:
            logging.error("Error posting on Twitter: %s", str(e))

    def post_on_facebook(self, message):
        try:
            # Facebook API authentication
            graph = facebook.GraphAPI(self.credentials.facebook_access_token)

            # Post on Facebook
            graph.put_object(parent_object=self.credentials.facebook_page_id, connection_name='feed', message=message)
            logging.info("Posted on Facebook: %s", message)
        except Exception as e:
            logging.error("Error posting on Facebook: %s", str(e))

# Job function to post on social media
def post_on_social_media():
    poster = SocialMediaPoster(SocialMediaCredentials(
        twitter_consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
        twitter_consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
        twitter_access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
        twitter_access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET'),
        facebook_access_token=os.environ.get('FACEBOOK_ACCESS_TOKEN'),
        facebook_page_id=os.environ.get('FACEBOOK_PAGE_ID')
    ))

    message = "Hello, world! This is a test post."
    poster.post_on_twitter(message)
    poster.post_on_facebook(message)

# Main function
def main():
    try:
        scheduler = BlockingScheduler()
        scheduler.add_job(post_on_social_media, 'interval', hours=1)  # Post every hour
        scheduler.start()
    except Exception as e:
        logging.error("Error: %s", str(e))

if __name__ == "__main__":
    main()
```
