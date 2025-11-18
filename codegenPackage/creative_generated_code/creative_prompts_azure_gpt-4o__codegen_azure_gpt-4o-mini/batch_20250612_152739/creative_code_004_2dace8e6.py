"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a bot in Python that tracks and logs digital engagement activities on Discord for earning points in the Everyworld ecosystem.
Generated: DETERMINISTIC_2dace8e678575612
Batch ID: 20250612_152739
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
import logging
import os

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the bot's command prefix and initialize the bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

# Define the file to log engagement activities
LOG_FILE = "engagement_log.txt"

# Function to log engagement activities to a file
def log_engagement(user_id, activity):
    try:
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"User ID: {user_id}, Activity: {activity}\n")
            logger.info(f"Logged activity for user {user_id}: {activity}")
    except Exception as e:
        logger.error(f"Error logging engagement: {e}")

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user} (ID: {bot.user.id})')
    logger.info('------')

# Event listener for messages sent in channels
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Log engagement activity when a message is sent
    log_engagement(message.author.id, f"Sent a message: {message.content}")
    
    # Process commands if any
    await bot.process_commands(message)

# Command to retrieve user points (stub implementation)
@bot.command(name='points')
async def points(ctx):
    await ctx.send(f"You have X points!")  # Replace with actual points retrieval logic

# Function to run the bot
def run_bot():
    TOKEN = os.getenv('DISCORD_TOKEN')  # Fetch the Discord bot token from environment variables
    if not TOKEN:
        logger.error("Discord token not found in environment variables.")
        return

    try:
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Error running the bot: {e}")

if __name__ == '__main__':
    run_bot()
```
