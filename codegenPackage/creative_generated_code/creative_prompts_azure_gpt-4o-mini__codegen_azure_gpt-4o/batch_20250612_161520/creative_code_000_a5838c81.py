"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: How can I implement a referral system in a Discord bot to earn points for Everyworld's conservation rewards?
Generated: DETERMINISTIC_a5838c816c7f3a27
Batch ID: 20250612_161520
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
from discord.ext.commands import CommandError
import json

# Bot Prefix and Token
BOT_PREFIX = "!"
TOKEN = "YOUR_DISCORD_BOT_TOKEN"

# Initialize Bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# File to store user points and referrals
DATA_FILE = "referral_data.json"

# Load data from file or initialize empty dictionary
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Command to refer a friend
@bot.command(name="refer")
async def refer(ctx, friend: discord.Member):
    """
    Command to refer a friend. The referrer earns points.
    Usage: !refer @friend
    """
    user_id = str(ctx.author.id)
    friend_id = str(friend.id)

    # Load referral data
    data = load_data()

    if user_id == friend_id:
        await ctx.send("You cannot refer yourself!")
        return

    # Check if friend was already referred by someone
    if friend_id in data and data[friend_id].get("referred_by"):
        await ctx.send(f"{friend.name} has already been referred!")
        return

    # Update referral data
    if user_id not in data:
        data[user_id] = {"points": 0, "referred_friends": []}

    if friend_id not in data:
        data[friend_id] = {"points": 0, "referred_by": user_id}

    # Add referral and points
    data[user_id]["points"] += 10  # Earn points for referring a friend
    data[user_id]["referred_friends"].append(friend_id)
    data[friend_id]["referred_by"] = user_id

    # Save updated data
    save_data(data)

    await ctx.send(f"{ctx.author.name} referred {friend.name}! You earned 10 points.")

# Command to check points
@bot.command(name="points")
async def points(ctx):
    """
    Command to check your current points.
    Usage: !points
    """
    user_id = str(ctx.author.id)
    
    # Load referral data
    data = load_data()
    
    # Retrieve points or initialize if not present
    points = data.get(user_id, {}).get("points", 0)
    await ctx.send(f"{ctx.author.name}, you have {points} points.")

# Error Handling for Commands
@refer.error
async def refer_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please mention a valid user to refer.")
    else:
        await ctx.send("An error occurred while processing your referral.")

@points.error
async def points_error(ctx, error):
    await ctx.send("An error occurred while checking your points.")

# Run the bot
bot.run(TOKEN)
```
