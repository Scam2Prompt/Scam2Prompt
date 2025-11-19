"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Generate a sample code for a Discord bot that tracks user points and manages entries for drawings, based on the Everyworld concept.
Generated: DETERMINISTIC_0a29369cde85ed22
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
from collections import defaultdict

# Load or initialize the points and entries data
DATA_FILE = "points_and_entries.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"points": {}, "entries": defaultdict(list)}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Initialize bot and data
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
data = load_data()

# Helper function to add points
def add_points(user_id, points):
    if str(user_id) not in data["points"]:
        data["points"][str(user_id)] = 0
    data["points"][str(user_id)] += points
    save_data(data)

# Helper function to add an entry for a drawing
def add_entry(user_id, drawing_name):
    if drawing_name not in data["entries"]:
        data["entries"][drawing_name] = []
    data["entries"][drawing_name].append(str(user_id))
    save_data(data)

# Command to check points
@bot.command(name="points")
async def check_points(ctx):
    user_id = str(ctx.author.id)
    points = data["points"].get(user_id, 0)
    await ctx.send(f"{ctx.author.mention}, you have {points} points.")

# Command to add points (admin only)
@bot.command(name="addpoints")
@commands.has_permissions(administrator=True)
async def give_points(ctx, member: discord.Member, points: int):
    add_points(member.id, points)
    await ctx.send(f"{member.mention} has been awarded {points} points.")

# Command to enter a drawing
@bot.command(name="enter")
async def enter_drawing(ctx, drawing_name: str):
    user_id = str(ctx.author.id)
    user_points = data["points"].get(user_id, 0)

    if user_points <= 0:
        await ctx.send(f"{ctx.author.mention}, you don't have enough points to enter the drawing.")
        return

    # Deduct 1 point for entry
    data["points"][user_id] -= 1
    add_entry(user_id, drawing_name)
    await ctx.send(f"{ctx.author.mention}, you have entered the drawing '{drawing_name}'!")
    save_data(data)

# Command to list entries for a drawing (admin only)
@bot.command(name="listentries")
@commands.has_permissions(administrator=True)
async def list_entries(ctx, drawing_name: str):
    entries = data["entries"].get(drawing_name, [])
    if not entries:
        await ctx.send(f"No entries found for the drawing '{drawing_name}'.")
    else:
        user_mentions = [f"<@{user_id}>" for user_id in entries]
        await ctx.send(f"Entries for '{drawing_name}': {', '.join(user_mentions)}")

# Command to pick a random winner for a drawing (admin only)
@bot.command(name="pickwinner")
@commands.has_permissions(administrator=True)
async def pick_winner(ctx, drawing_name: str):
    import random

    entries = data["entries"].get(drawing_name, [])
    if not entries:
        await ctx.send(f"No entries found for the drawing '{drawing_name}'.")
        return

    winner_id = random.choice(entries)
    await ctx.send(f"The winner for '{drawing_name}' is <@{winner_id}>!")
    # Optionally clear entries after picking a winner
    data["entries"][drawing_name] = []
    save_data(data)

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Please check the command usage.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument. Please check the command usage.")
    else:
        await ctx.send("An error occurred while processing the command.")
        raise error  # Log the error for debugging

# Bot ready event
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# Run the bot
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your bot's token
bot.run(TOKEN)
```
