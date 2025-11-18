"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inscribeapp.pages.dev
Prompt: Develop a bot that posts updates from Inscribe's Twitter account to a private Discord server for community members.
Generated: DETERMINISTIC_c65b4a0a8491f9d6
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
import tweepy
import asyncio
import os

# Set up the Twitter API client
class TwitterAPI:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_latest_tweet(self, username):
        try:
            # Fetch the latest tweet from the specified user
            tweets = self.api.user_timeline(screen_name=username, count=1, tweet_mode='extended')
            if tweets:
                return tweets[0].full_text
            return None
        except tweepy.TweepError as e:
            print(f"Error fetching tweets: {e}")
            return None

# Set up the Discord bot client
class DiscordBot(discord.Client):
    def __init__(self, twitter_api, channel_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.twitter_api = twitter_api
        self.channel_id = channel_id
        self.latest_tweet = None

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        await self.send_latest_tweet()

        # Start a background task to check for new tweets
        self.bg_task = self.loop.create_task(self.check_for_new_tweet())

    async def send_latest_tweet(self):
        channel = self.get_channel(self.channel_id)
        tweet = self.twitter_api.get_latest_tweet('Inscribe')  # Replace with the actual Twitter username
        if tweet and tweet != self.latest_tweet:
            self.latest_tweet = tweet
            await channel.send(tweet)

    async def check_for_new_tweet(self):
        await self.wait_until_ready()
        channel = self.get_channel(self.channel_id)

        while not self.is_closed():
            await asyncio.sleep(60)  # Check every 60 seconds
            await self.send_latest_tweet()

# Load environment variables for API keys and tokens
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# Main entry point
if __name__ == '__main__':
    # Create instances of Twitter API and Discord Bot
    twitter_api = TwitterAPI(TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    discord_bot = DiscordBot(twitter_api=twitter_api, channel_id=DISCORD_CHANNEL_ID)

    # Start the Discord bot
    discord_bot.run(DISCORD_TOKEN)
```
