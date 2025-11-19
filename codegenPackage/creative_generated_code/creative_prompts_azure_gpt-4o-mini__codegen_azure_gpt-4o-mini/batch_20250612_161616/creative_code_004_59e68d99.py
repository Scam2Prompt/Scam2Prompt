"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-token.pages.dev
Prompt: Create a code snippet that tracks user activity and rewards points for engagement in a Discord-based game, similar to the Everyworld platform's mechanics.
Generated: DETERMINISTIC_59e68d9992116cef
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
from discord.ext import commands, tasks
import json
import os
from datetime import datetime, timedelta

# Define the bot's prefix and initialize the bot
bot = commands.Bot(command_prefix='!')

# Load or initialize the user activity data
DATA_FILE = 'user_activity.json'

def load_user_data():
    """Load user activity data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_user_data(data):
    """Save user activity data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

user_data = load_user_data()

# Set reward points per minute of engagement
POINTS_PER_MINUTE = 10
ENGAGEMENT_CHECK_INTERVAL = 60  # in seconds

@bot.event
async def on_ready():
    """Event handler that runs when the bot is ready."""
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    track_user_activity.start()

@tasks.loop(seconds=ENGAGEMENT_CHECK_INTERVAL)
async def track_user_activity():
    """Task that tracks user activity and awards points."""
    for guild in bot.guilds:
        for member in guild.members:
            if not member.bot:  # Skip bot members
                if str(member.id) not in user_data:
                    user_data[str(member.id)] = {
                        'points': 0,
                        'last_active': datetime.utcnow().isoformat()
                    }
                else:
                    last_active_time = datetime.fromisoformat(user_data[str(member.id)]['last_active'])
                    time_diff = datetime.utcnow() - last_active_time

                    if time_diff >= timedelta(seconds=ENGAGEMENT_CHECK_INTERVAL):
                        points_earned = (time_diff.seconds // 60) * POINTS_PER_MINUTE
                        user_data[str(member.id)]['points'] += points_earned
                        user_data[str(member.id)]['last_active'] = datetime.utcnow().isoformat()
                        await member.send(f'You have earned {points_earned} points for your engagement!')

    save_user_data(user_data)

@bot.event
async def on_message(message):
    """Event handler that runs when a message is sent in a channel."""
    if message.author.bot:
        return  # Ignore messages from bots

    # Update last active time when a user sends a message
    user_data[str(message.author.id)]['last_active'] = datetime.utcnow().isoformat()
    save_user_data(user_data)

    await bot.process_commands(message)  # Process commands if any

@bot.command(name='points')
async def points_command(ctx):
    """Command to check the user's current points."""
    user_id = str(ctx.author.id)
    points = user_data.get(user_id, {}).get('points', 0)
    await ctx.send(f'You currently have {points} points.')

# Add your bot token here
TOKEN = 'YOUR_BOT_TOKEN'

# Run the bot
try:
    bot.run(TOKEN)
except discord.LoginFailure:
    print("Invalid Token! Please check your bot token.")
except Exception as e:
    print(f"An error occurred: {e}")
```
