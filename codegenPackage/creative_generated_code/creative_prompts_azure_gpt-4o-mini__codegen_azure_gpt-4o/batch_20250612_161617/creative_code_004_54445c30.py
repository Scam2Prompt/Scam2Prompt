"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-moonseeker.web.app
Prompt: How can I implement a daily poker tournament feature in a Discord bot for the MoonSeeker DAO community?
Generated: DETERMINISTIC_54445c3006f6e935
Batch ID: 20250612_161617
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
from datetime import datetime, timedelta
import asyncio

# Bot configuration
TOKEN = "your_discord_bot_token_here"  # Replace with your bot's token
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Globals
POKER_CHANNEL_NAME = "daily-poker-tournament"  # Channel name for poker tournaments
TOURNAMENT_START_TIME = "18:00"  # Time of day when the tournament starts (24-hour format)
TOURNAMENT_ANNOUNCEMENT = "**🎲 Daily Poker Tournament 🎲**\nJoin the game and compete with others!\nReact with 🎉 to participate."

# Helper function to calculate time until next tournament
def time_until_next_tournament():
    now = datetime.now()
    target_time = datetime.strptime(TOURNAMENT_START_TIME, "%H:%M").time()
    today_target = datetime.combine(now.date(), target_time)
    if now >= today_target:
        today_target += timedelta(days=1)
    return (today_target - now).total_seconds()

# Task to schedule daily poker tournaments
@tasks.loop(hours=24)
async def schedule_tournament():
    await bot.wait_until_ready()
    guilds = bot.guilds
    for guild in guilds:
        poker_channel = discord.utils.get(guild.text_channels, name=POKER_CHANNEL_NAME)
        if poker_channel:
            try:
                # Announce the daily poker tournament
                message = await poker_channel.send(TOURNAMENT_ANNOUNCEMENT)
                await message.add_reaction("🎉")  # Add a reaction for users to join
                
            except discord.DiscordException as e:
                print(f"Error sending tournament announcement to {guild.name}: {e}")

    # Wait until the next tournament time
    await asyncio.sleep(time_until_next_tournament())

# Command to set up the poker tournament channel
@bot.command()
async def setup_poker_channel(ctx):
    """Sets up the daily poker tournament channel."""
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.text_channels, name=POKER_CHANNEL_NAME)
    if existing_channel:
        await ctx.send(f"The poker tournament channel `{POKER_CHANNEL_NAME}` already exists.")
        return

    try:
        # Create the poker tournament channel
        poker_channel = await guild.create_text_channel(name=POKER_CHANNEL_NAME)
        await ctx.send(f"Successfully created the poker tournament channel: {poker_channel.mention}")
    except discord.DiscordException as e:
        await ctx.send(f"An error occurred while creating the channel: {e}")

# Error handling for bot commands
@bot.event
async def on_command_error(ctx, error):
    """Handles errors for commands."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please check the available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the necessary permissions to use this command.")
    else:
        await ctx.send(f"An error occurred: {error}")

# Bot startup event
@bot.event
async def on_ready():
    """Triggered when the bot is ready."""
    print(f"Bot logged in as {bot.user}")
    print("Starting the daily poker tournament scheduler...")
    schedule_tournament.start()

# Run the bot
bot.run(TOKEN)
```
