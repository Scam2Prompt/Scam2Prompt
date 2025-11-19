"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Create a Discord bot that provides information about the Big Time game's Preseason, including new features and rewards.
Generated: DETERMINISTIC_04441260edffedd4
Batch ID: 20250622_211405
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
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the bot's command prefix and description
bot = commands.Bot(command_prefix='!', description="Big Time Game Preseason Info Bot")

# Preseason information
preseason_info = {
    "features": [
        "New character classes",
        "Enhanced graphics and animations",
        "Improved matchmaking system",
        "New game modes and challenges"
    ],
    "rewards": [
        "Exclusive skins for characters",
        "In-game currency bonuses",
        "Limited-time items",
        "Access to special events"
    ]
}

@bot.event
async def on_ready():
    """Event that runs when the bot is ready."""
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logging.info('------')

@bot.command(name='preseason', help='Get information about the Big Time game Preseason features and rewards.')
async def preseason(ctx):
    """Command to provide preseason information."""
    try:
        # Create a response message
        response = "### Big Time Game Preseason Information ###\n\n"
        response += "**New Features:**\n"
        for feature in preseason_info["features"]:
            response += f"- {feature}\n"
        
        response += "\n**Rewards:**\n"
        for reward in preseason_info["rewards"]:
            response += f"- {reward}\n"
        
        # Send the response to the Discord channel
        await ctx.send(response)
    except Exception as e:
        logging.error(f"Error while fetching preseason info: {e}")
        await ctx.send("An error occurred while fetching the preseason information. Please try again later.")

# Error handling for command errors
@bot.event
async def on_command_error(ctx, error):
    """Handles command errors."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I didn't understand that command.")
    else:
        logging.error(f"An error occurred: {error}")
        await ctx.send("An unexpected error occurred. Please try again later.")

# Run the bot with the specified token
if __name__ == "__main__":
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot's token
    bot.run(TOKEN)
```
