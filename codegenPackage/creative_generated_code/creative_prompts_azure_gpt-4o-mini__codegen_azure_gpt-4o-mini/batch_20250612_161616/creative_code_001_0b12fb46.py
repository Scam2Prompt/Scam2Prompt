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
import os
import json
import requests

# Load bot token and other configurations from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
EVERYWORLD_API_URL = os.getenv('EVERYWORLD_API_URL')

# Define bot command prefix
bot = commands.Bot(command_prefix='!')

# Dictionary to keep track of user points
user_points = {}

# Load user points from a JSON file if it exists
def load_user_points():
    if os.path.exists('user_points.json'):
        with open('user_points.json', 'r') as file:
            return json.load(file)
    return {}

# Save user points to a JSON file
def save_user_points():
    with open('user_points.json', 'w') as file:
        json.dump(user_points, file)

# Fetch points from Everyworld platform
def fetch_points(user_id):
    try:
        response = requests.get(f"{EVERYWORLD_API_URL}/user/{user_id}/points")
        response.raise_for_status()
        return response.json().get('points', 0)
    except requests.RequestException as e:
        print(f"Error fetching points: {e}")
        return 0

# Command to display user points
@bot.command(name='points', help='Displays your current points.')
async def points(ctx):
    user_id = str(ctx.author.id)
    points = user_points.get(user_id, 0)
    await ctx.send(f"{ctx.author.mention}, you have {points} points!")

# Command to earn points by watching a video
@bot.command(name='watch', help='Earn points by watching a video. Usage: !watch <video_id>')
async def watch(ctx, video_id: str):
    user_id = str(ctx.author.id)
    points_earned = 10  # Fixed points for watching a video

    # Update user points
    user_points[user_id] = user_points.get(user_id, 0) + points_earned
    save_user_points()

    await ctx.send(f"{ctx.author.mention}, you've earned {points_earned} points for watching video {video_id}!")

# Command to earn points for participating in environmental initiatives
@bot.command(name='participate', help='Earn points for participating in an environmental initiative. Usage: !participate <initiative_id>')
async def participate(ctx, initiative_id: str):
    user_id = str(ctx.author.id)
    points_earned = 20  # Fixed points for participation in an initiative

    # Update user points
    user_points[user_id] = user_points.get(user_id, 0) + points_earned
    save_user_points()

    await ctx.send(f"{ctx.author.mention}, you've earned {points_earned} points for participating in initiative {initiative_id}!")

# Event to handle when the bot is ready
@bot.event
async def on_ready():
    global user_points
    user_points = load_user_points()
    print(f'Bot {bot.user} has connected!')

# Error handling for unknown commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I didn't understand that command.")

# Run the bot
if __name__ == "__main__":
    if DISCORD_TOKEN is None:
        print("Error: Discord token is not set in environment variables.")
    else:
        bot.run(DISCORD_TOKEN)
```
