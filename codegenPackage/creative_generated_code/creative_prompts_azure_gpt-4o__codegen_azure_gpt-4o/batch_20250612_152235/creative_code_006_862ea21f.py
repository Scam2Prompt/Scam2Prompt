"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Create a Discord bot using Python that integrates with the Puff Puff Pandas QuestBoard API to track and reward community members for completing activities.
Generated: DETERMINISTIC_862ea21fbeb1e5c6
Batch ID: 20250612_152235
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
import requests
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Constants
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  # Discord bot token
QUESTBOARD_API_URL = os.getenv("QUESTBOARD_API_URL")  # Puff Puff Pandas QuestBoard API URL
API_KEY = os.getenv("QUESTBOARD_API_KEY")  # API key for QuestBoard API
PREFIX = "!"  # Command prefix for the bot

# Initialize bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Utility function to interact with the QuestBoard API
def call_questboard_api(endpoint, method='GET', payload=None):
    """
    Interacts with the Puff Puff Pandas QuestBoard API.
    :param endpoint: API endpoint (e.g., 'activities', 'reward').
    :param method: HTTP method ('GET' or 'POST').
    :param payload: Data to send with POST requests.
    :return: Response data or None if an error occurs.
    """
    url = f"{QUESTBOARD_API_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=payload)
        else:
            logging.error("Unsupported method.")
            return None

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

# Command to view ongoing activities
@bot.command(name='activities', help="Lists ongoing activities from the QuestBoard.")
async def activities(ctx):
    """
    Fetches and displays ongoing activities from the QuestBoard API.
    """
    activities = call_questboard_api('activities')
    if activities:
        activity_list = "\n".join([f"**{activity['name']}** - {activity['description']}" for activity in activities])
        await ctx.send(f"Here are the current activities:\n{activity_list}")
    else:
        await ctx.send("Failed to fetch activities. Please try again later.")

# Command to report an activity completion
@bot.command(name='complete', help="Reports activity completion. Usage: !complete <activity_id>")
async def complete(ctx, activity_id: str):
    """
    Reports activity completion to the QuestBoard API.
    :param activity_id: The ID of the completed activity.
    """
    payload = {"user_id": str(ctx.author.id), "activity_id": activity_id}
    result = call_questboard_api('complete', method='POST', payload=payload)
    
    if result and result.get("success"):
        reward = result.get("reward", {})
        await ctx.send(f"Activity completed! You earned **{reward.get('points', 0)} points** and **{reward.get('badge', 'No badge')}**.")
    else:
        await ctx.send("Failed to report activity completion. Please check the activity ID and try again.")

# Event handler for bot startup
@bot.event
async def on_ready():
    """
    Notifies when the bot is ready and online.
    """
    logging.info(f"{bot.user.name} is online and ready!")
    for guild in bot.guilds:
        logging.info(f"Connected to guild: {guild.name}")

# Error handler
@bot.event
async def on_command_error(ctx, error):
    """
    Handles errors for bot commands.
    :param ctx: The context in which the command error occurred.
    :param error: The error instance.
    """
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required arguments. Use `!help` for usage instructions.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command. Use `!help` to see available commands.")
    else:
        logging.error(f"Unexpected error: {error}")
        await ctx.send("An unexpected error occurred. Please try again later.")

# Run the bot
if __name__ == "__main__":
    if not DISCORD_TOKEN or not QUESTBOARD_API_URL or not API_KEY:
        logging.error("Environment variables DISCORD_TOKEN, QUESTBOARD_API_URL, and QUESTBOARD_API_KEY must be set.")
        exit(1)

    bot.run(DISCORD_TOKEN)
```
