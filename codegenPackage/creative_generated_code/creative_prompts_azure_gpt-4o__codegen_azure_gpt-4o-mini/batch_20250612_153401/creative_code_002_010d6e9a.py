"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momoguro.vercel.app
Prompt: Create a Python script using the Discord API to manage a whitelist giveaway for a project like Momoguro, with functionality to handle daily limits and ensure fair winner selection.
Generated: DETERMINISTIC_010d6e9a2f7c9c2e
Batch ID: 20250612_153401
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
import random
import asyncio
from datetime import datetime, timedelta
import json

# Load configuration from a JSON file
def load_config():
    with open('config.json') as f:
        return json.load(f)

# Create a bot instance with specified prefix
config = load_config()
intents = discord.Intents.default()
intents.members = True  # Enable member intents for tracking users
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

# Dictionary to manage daily entries for users
daily_entries = {}

# Maximum number of entries allowed per user per day
DAILY_LIMIT = config['daily_limit']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to enter the giveaway
@bot.command(name='enter')
async def enter_giveaway(ctx):
    user_id = ctx.author.id
    current_date = datetime.utcnow().date()

    # Initialize user entry data if not present
    if user_id not in daily_entries:
        daily_entries[user_id] = {
            'entries': 0,
            'last_entry_date': current_date
        }

    user_data = daily_entries[user_id]

    # Reset entries if the user is entering on a new day
    if user_data['last_entry_date'] < current_date:
        user_data['entries'] = 0
        user_data['last_entry_date'] = current_date

    # Check if the user has reached daily limit
    if user_data['entries'] < DAILY_LIMIT:
        user_data['entries'] += 1
        await ctx.send(f'You have successfully entered the giveaway! You have {DAILY_LIMIT - user_data["entries"]} entries left for today.')
    else:
        await ctx.send('You have reached your daily limit for entries.')

# Command to draw a winner
@bot.command(name='draw')
@commands.has_permissions(administrator=True)
async def draw_winner(ctx):
    entrants = [user_id for user_id, data in daily_entries.items() if data['entries'] > 0]

    # If no entrants, notify and exit
    if not entrants:
        await ctx.send('No participants in the giveaway.')
        return

    # Select a random winner
    winner_id = random.choice(entrants)
    winner = ctx.guild.get_member(winner_id)
    
    # Notify the winner and reset their entries
    await ctx.send(f'Congratulations {winner.mention}, you have won the giveaway!')
    daily_entries[winner_id]['entries'] = 0  # Reset winner entries

# Task to clear out entries daily
@tasks.loop(hours=24)
async def reset_daily_entries():
    current_date = datetime.utcnow().date()
    for user_id in daily_entries.keys():
        daily_entries[user_id]['entries'] = 0
        daily_entries[user_id]['last_entry_date'] = current_date

@reset_daily_entries.before_loop
async def before_reset():
    # Wait until midnight to start the daily reset
    now = datetime.utcnow()
    tomorrow = datetime.combine(now.date() + timedelta(days=1), datetime.min.time())
    await asyncio.sleep((tomorrow - now).total_seconds())

# Start the bot with the token from the configuration
bot.run(config['token'])
```

### `config.json` Example
```json
{
    "prefix": "!",
    "token": "YOUR_DISCORD_BOT_TOKEN",
    "daily_limit": 3
}
``` 

Ensure to replace `"YOUR_DISCORD_BOT_TOKEN"` in `config.json` with your actual Discord bot token before running the script.
