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
from datetime import datetime, time
import asyncio

# Set up the bot with the required intents
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define constants
TOURNAMENT_CHANNEL_ID = 1234567890  # Replace with your channel ID
TOURNAMENT_START_TIME = time(20, 0)  # Tournament starts at 8:00 PM UTC

# Function to format the current time in a readable way
def current_time_formatted():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Background task that checks if it's time for the tournament
@tasks.loop(minutes=1)
async def tournament_timer():
    now = datetime.utcnow().time()
    channel = bot.get_channel(TOURNAMENT_CHANNEL_ID)
    
    # Check if current time matches tournament start time
    if now.hour == TOURNAMENT_START_TIME.hour and now.minute == TOURNAMENT_START_TIME.minute:
        try:
            await channel.send("🎉 A new daily poker tournament is starting now! Join the game! 🎉")
            # You can add more functionality here, such as storing participants, etc.
        except Exception as e:
            print(f"Error sending tournament message: {e}")

# Command to manually start the tournament (for testing)
@bot.command(name='start_tournament', help='Manually start the poker tournament (for testing purposes).')
async def start_tournament(ctx):
    if ctx.channel.id != TOURNAMENT_CHANNEL_ID:
        await ctx.send("This command can only be used in the designated tournament channel.")
        return

    try:
        await ctx.send("🎉 A poker tournament is starting now! Join the game! 🎉")
    except Exception as e:
        await ctx.send("An error occurred while starting the tournament.")
        print(f"Error starting tournament: {e}")

# Event to notify when the bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user} at {current_time_formatted()}')
    tournament_timer.start()

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please check the command and try again.")
    else:
        await ctx.send("An error occurred while processing your command.")
        print(f"Error: {error}")

# Run the bot with your token
if __name__ == "__main__":
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot token
    bot.run(TOKEN)
```
