"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.blog
Prompt: Create a script to monitor Pepecoin's community activity on Discord and Reddit, leveraging APIs for community engagement tracking.
Generated: DETERMINISTIC_c5e2c661705eac5a
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import discord
from discord.ext import commands
import praw
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Discord bot token
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Reddit API credentials
REDDIT_CLIENT_ID = 'YOUR_REDDIT_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'YOUR_REDDIT_CLIENT_SECRET'
REDDIT_USER_AGENT = 'YOUR_REDDIT_USER_AGENT'

# Initialize the Discord bot
bot = commands.Bot(command_prefix='!')

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

@bot.event
async def on_ready():
    """
    Event handler that runs when the bot is ready.
    """
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('Bot is ready!')

@bot.command()
async def track_community(ctx):
    """
    Command to track Pepecoin community activity on Discord and Reddit.
    """
    try:
        discord_activity = await get_discord_activity()
        reddit_activity = await get_reddit_activity()
        
        # Send the activity summary to the Discord channel
        summary = f"**Pepecoin Community Activity:**\n\n**Discord:** {discord_activity}\n**Reddit:** {reddit_activity}"
        await ctx.send(summary)
        
    except Exception as e:
        logging.error(f"Error tracking community activity: {str(e)}")
        await ctx.send("An error occurred while tracking community activity.")

async def get_discord_activity():
    """
    Fetches recent messages from a specific Discord channel.
    
    Returns:
        str: A summary of recent messages.
    """
    channel_id = 'YOUR_DISCORD_CHANNEL_ID'
    channel = bot.get_channel(int(channel_id))
    
    if channel is None:
        raise ValueError("Channel not found.")
    
    messages = await channel.history(limit=5).flatten()
    return f"Last 5 messages: {[msg.content for msg in messages]}"

async def get_reddit_activity():
    """
    Fetches recent posts from the Pepecoin subreddit.
    
    Returns:
        str: A summary of recent posts.
    """
    subreddit_name = 'Pepecoin'
    subreddit = reddit.subreddit(subreddit_name)

    recent_posts = subreddit.new(limit=5)
    post_summaries = [f"{post.title} (Score: {post.score})" for post in recent_posts]
    
    return f"Recent posts: {post_summaries}"

if __name__ == "__main__":
    try:
        # Start the bot
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        logging.error(f"Error starting the bot: {str(e)}")
```

**Note:** Replace `'YOUR_DISCORD_BOT_TOKEN'`, `'YOUR_REDDIT_CLIENT_ID'`, `'YOUR_REDDIT_CLIENT_SECRET'`, `'YOUR_REDDIT_USER_AGENT'`, and `'YOUR_DISCORD_CHANNEL_ID'` with your actual API credentials and channel ID.
