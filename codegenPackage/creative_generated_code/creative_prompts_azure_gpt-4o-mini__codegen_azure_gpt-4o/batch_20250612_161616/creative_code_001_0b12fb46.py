"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-token.pages.dev
Prompt: Write a Python script that integrates with Discord to allow users to earn points through watching videos and participating in environmental initiatives, as described on the Everyworld platform.
Generated: DETERMINISTIC_0b12fb46056b507c
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import logging

# Set up logging for debugging and monitoring
logging.basicConfig(level=logging.INFO)

# Bot token (replace with your actual bot token from Discord Developer Portal)
BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Prefix for bot commands
COMMAND_PREFIX = '!'

# Initialize the bot
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

# Points database stored in memory for simplicity (consider using a persistent database in production)
user_points = {}

# Define the points system
WATCH_VIDEO_POINTS = 10
ENVIRONMENTAL_INITIATIVE_POINTS = 20


def add_points(user_id, points):
    """Adds points to the user's account."""
    if user_id not in user_points:
        user_points[user_id] = 0
    user_points[user_id] += points


def get_points(user_id):
    """Retrieves points for the user."""
    return user_points.get(user_id, 0)


@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    logging.info(f'{bot.user} has connected to Discord!')
    logging.info('Bot is ready to accept commands.')


@bot.command(name='watch_video')
async def watch_video(ctx):
    """
    Command to earn points by watching a video.
    Example: !watch_video
    """
    user_id = ctx.author.id
    add_points(user_id, WATCH_VIDEO_POINTS)
    await ctx.send(f"{ctx.author.mention}, you earned {WATCH_VIDEO_POINTS} points for watching a video! "
                   f"Your total points: {get_points(user_id)}")


@bot.command(name='participate')
async def participate(ctx):
    """
    Command to earn points by participating in environmental initiatives.
    Example: !participate
    """
    user_id = ctx.author.id
    add_points(user_id, ENVIRONMENTAL_INITIATIVE_POINTS)
    await ctx.send(f"{ctx.author.mention}, you earned {ENVIRONMENTAL_INITIATIVE_POINTS} points for participating in "
                   f"an environmental initiative! Your total points: {get_points(user_id)}")


@bot.command(name='points')
async def points(ctx):
    """
    Command to check the user's current points.
    Example: !points
    """
    user_id = ctx.author.id
    await ctx.send(f"{ctx.author.mention}, your total points: {get_points(user_id)}")


@bot.command(name='leaderboard')
async def leaderboard(ctx):
    """
    Command to display a leaderboard of top users by points.
    Example: !leaderboard
    """
    if not user_points:
        await ctx.send("No points have been earned yet!")
        return

    # Sort users by points in descending order
    sorted_users = sorted(user_points.items(), key=lambda item: item[1], reverse=True)
    leaderboard_message = "🏆 **Leaderboard** 🏆\n"
    for i, (user_id, points) in enumerate(sorted_users[:10], start=1):
        user = bot.get_user(user_id)
        username = user.name if user else f"User {user_id}"
        leaderboard_message += f"{i}. {username} - {points} points\n"
    await ctx.send(leaderboard_message)


@bot.event
async def on_command_error(ctx, error):
    """Global error handler for commands."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please use a valid command.")
    else:
        logging.error(f"Error occurred: {error}")
        await ctx.send("An error occurred while processing your command. Please try again later.")


# Run the bot
try:
    bot.run(BOT_TOKEN)
except Exception as e:
    logging.error(f"Failed to start the bot: {e}")
```
