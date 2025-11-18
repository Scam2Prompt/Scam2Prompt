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
import os
import tweepy
import discord
from discord.ext import tasks
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twitter API credentials (use a Twitter developer account to generate these)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Discord bot token and channel ID
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))  # Ensure the channel ID is an integer

# Twitter handle to monitor (e.g., @Inscribe handle without "@")
TWITTER_HANDLE = "Inscribe"

# Set up Twitter API client
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)
twitter_api = tweepy.API(auth)

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# To track the most recent tweet ID
last_tweet_id = None

# Function to fetch the latest tweet from the Twitter handle
def fetch_latest_tweet():
    global last_tweet_id
    try:
        # Fetch recent tweets from the specified user
        tweets = twitter_api.user_timeline(
            screen_name=TWITTER_HANDLE, 
            count=1, 
            tweet_mode="extended"
        )
        if tweets:
            latest_tweet = tweets[0]
            if latest_tweet.id != last_tweet_id:  # Check if it's a new tweet
                last_tweet_id = latest_tweet.id
                return latest_tweet.full_text, latest_tweet.id
    except Exception as e:
        print(f"Error fetching tweets: {e}")
    return None, None

# Task to periodically check for new tweets
@tasks.loop(minutes=1)  # Check every 1 minute
async def post_twitter_updates():
    channel = client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        tweet_text, tweet_id = fetch_latest_tweet()
        if tweet_text:
            try:
                await channel.send(f"📢 New tweet from @{TWITTER_HANDLE}: {tweet_text}")
            except Exception as e:
                print(f"Error sending message to Discord: {e}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print("Bot is ready!")
    post_twitter_updates.start()  # Start the periodic task

# Run the Discord bot
try:
    client.run(DISCORD_BOT_TOKEN)
except Exception as e:
    print(f"Error running the Discord bot: {e}")
```
