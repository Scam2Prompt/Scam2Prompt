"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgiescoin.pages.dev
Prompt: Explain how to set up a Discord bot that notifies users about daily Hedgie distributions and trading league results.
Generated: DETERMINISTIC_bbd45dc6ba669b3a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import discord
from discord.ext import tasks, commands
import os
from datetime import datetime, timedelta

# Load environment variables for the bot token
from dotenv import load_dotenv
load_dotenv()

# Discord bot token from your environment variables
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents for the bot (configured for basic usage)
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize the bot
bot = commands.Bot(command_prefix="!", intents=intents)


# The channel ID where notifications will be sent
NOTIFICATION_CHANNEL_ID = 123456789012345678  # Replace with your Discord channel ID


# Task to send daily Hedgie distribution notifications
@tasks.loop(hours=24)
async def hedgie_distribution_notification():
    """Send daily Hedgie distribution message to the specified channel."""
    channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)
    if channel:
        await channel.send(
            "🌟 Daily Hedgie distributions are now live! 🦔 Check your accounts for updates."
        )
    else:
        print("Error: Notification channel not found!")


# Task to send weekly trading league results
@tasks.loop(days=7)
async def trading_league_results_notification():
    """Send weekly trading league results to the specified channel."""
    channel = bot.get_channel(NOTIFICATION_CHANNEL_ID)
    if channel:
        await channel.send(
            "📊 Weekly trading league results are out! 🏆 Congratulations to all participants!"
        )
    else:
        print("Error: Notification channel not found!")


@bot.event
async def on_ready():
    """Event triggered when bot is ready to start."""
    print(f"Bot is online as {bot.user}")
    
    # Start the notification tasks
    if not hedgie_distribution_notification.is_running():
        # Start the daily Hedgie notification loop
        hedgie_distribution_notification.start()
    
    if not trading_league_results_notification.is_running():
        # Start the weekly trading league notification loop
        trading_league_results_notification.start()


@bot.command()
async def ping(ctx):
    """Simple ping command to check bot responsiveness."""
    await ctx.send("Pong! 🏓")


# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    """Handle errors in bot commands."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Command not found!")
    else:
        await ctx.send("⚠️ An error occurred while processing your command.")
        print(f"Error: {error}")


# Run the bot
if __name__ == "__main__":
    if BOT_TOKEN:
        bot.run(BOT_TOKEN)
    else:
        print("Error: BOT_TOKEN not found in environment variables!")
```

**Key Notes for Setup:**
1. Replace `NOTIFICATION_CHANNEL_ID` with your Discord channel's ID.
2. Ensure your `.env` file contains `DISCORD_BOT_TOKEN`, which holds the bot token from Discord Developer Portal.
3. Install required packages using: `pip install discord.py python-dotenv`.
4. Run the script to start the bot. It will send notifications daily and weekly based on the configured tasks.
