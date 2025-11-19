"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://njm-4sp.pages.dev
Prompt: Create an example of how to implement the specific use case for the Discord integration highlighted in the content.
Generated: DETERMINISTIC_2f076a189a3dcc7b
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Discord Bot Example: Sending a message to a specific channel
# This script demonstrates how to set up a Discord bot and send a message 
# to a specific channel upon startup.

import discord
from discord.ext import commands
import os

# Load environment variables (for storing sensitive info like tokens)
from dotenv import load_dotenv

load_dotenv()

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN is not set in environment variables.")

# Define the bot and its intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Triggered when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f"Bot is logged in as {bot.user} and is ready!")

    # Replace with your specific channel ID
    channel_id = 123456789012345678  # Example: Replace with your actual channel ID
    channel = bot.get_channel(channel_id)

    if channel:
        # Send a message to the specific channel
        try:
            await channel.send("Hello, Discord! I am now online.")
            print(f"Message sent to channel: {channel.name}")
        except discord.errors.Forbidden:
            print("Error: Bot does not have permission to send messages in the specified channel.")
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")
    else:
        print(f"Error: Channel with ID {channel_id} not found.")

# Basic command example
@bot.command(name="ping")
async def ping(ctx):
    """Responds with 'Pong!' to test bot responsiveness."""
    await ctx.send("Pong!")

# Run the bot
try:
    bot.run(BOT_TOKEN)
except discord.errors.LoginFailure:
    print("Error: Invalid bot token.")
except Exception as e:
    print(f"An error occurred while running the bot: {e}")
```

Ensure you replace `123456789012345678` with your actual Discord channel ID and set up a `.env` file with your bot token (`DISCORD_BOT_TOKEN`). Install required packages using `pip install discord.py python-dotenv`.
