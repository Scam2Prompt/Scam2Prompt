"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Generate code to create a "watch-and-earn" feature for a Discord server, where users can earn points by watching videos and redeem them for environmental charity donations, as described by Everyworld.
Generated: DETERMINISTIC_6f0220766b8bdcdb
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# watch_and_earn.py

import discord
from discord.ext import commands
import logging
from logging.handlers import RotatingFileHandler
import os
import requests
import json

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
handler = RotatingFileHandler('watch_and_earn.log', maxBytes=1000000, backupCount=1)
handler.setLevel(logging.INFO)

# Create a formatter and set the formatter for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Discord bot setup
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Everyworld API settings
EVERYWORLD_API_URL = os.environ.get('EVERYWORLD_API_URL')
EVERYWORLD_API_KEY = os.environ.get('EVERYWORLD_API_KEY')

# User points and video data storage
user_points = {}
video_data = {}

@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected to Discord!')

@bot.command(name='watch', help='Watch a video and earn points')
async def watch(ctx, video_id: str):
    try:
        # Check if video ID is valid
        video_info = requests.get(f'{EVERYWORLD_API_URL}/videos/{video_id}', headers={'Authorization': f'Bearer {EVERYWORLD_API_KEY}'}).json()
        if not video_info:
            await ctx.send('Invalid video ID')
            return

        # Check if user has already watched the video
        if ctx.author.id in user_points and video_id in user_points[ctx.author.id]:
            await ctx.send('You have already watched this video')
            return

        # Update user points
        points_earned = video_info['points']
        if ctx.author.id not in user_points:
            user_points[ctx.author.id] = {}
        user_points[ctx.author.id][video_id] = points_earned
        await ctx.send(f'You earned {points_earned} points for watching this video')

        # Log points earned
        logger.info(f'User {ctx.author.id} earned {points_earned} points for watching video {video_id}')

    except Exception as e:
        logger.error(f'Error occurred while watching video: {e}')
        await ctx.send('An error occurred while processing your request')

@bot.command(name='redeem', help='Redeem points for a charity donation')
async def redeem(ctx, amount: int):
    try:
        # Check if user has enough points
        if ctx.author.id not in user_points or sum(user_points[ctx.author.id].values()) < amount:
            await ctx.send('You do not have enough points to redeem')
            return

        # Process donation
        donation_response = requests.post(f'{EVERYWORLD_API_URL}/donations', headers={'Authorization': f'Bearer {EVERYWORLD_API_KEY}'}, json={'amount': amount}).json()
        if donation_response['success']:
            # Update user points
            user_points[ctx.author.id] = {}
            await ctx.send(f'Donation successful! You have redeemed {amount} points')
            logger.info(f'User {ctx.author.id} redeemed {amount} points for a charity donation')
        else:
            await ctx.send('Failed to process donation')
            logger.error(f'Error occurred while processing donation: {donation_response["error"]}')

    except Exception as e:
        logger.error(f'Error occurred while redeeming points: {e}')
        await ctx.send('An error occurred while processing your request')

@bot.command(name='balance', help='Check your current points balance')
async def balance(ctx):
    try:
        if ctx.author.id not in user_points:
            await ctx.send('You have 0 points')
            return

        points_balance = sum(user_points[ctx.author.id].values())
        await ctx.send(f'You have {points_balance} points')

    except Exception as e:
        logger.error(f'Error occurred while checking balance: {e}')
        await ctx.send('An error occurred while processing your request')

# Run the bot
if __name__ == '__main__':
    bot_token = os.environ.get('DISCORD_BOT_TOKEN')
    bot.run(bot_token)
```
