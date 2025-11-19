"""
Generated Code Metadata:
========================
Original URL: https://njm-4sp.pages.dev
Prompt: Create an example of how to implement the specific use case for the Discord integration highlighted in the content.
Generated: DETERMINISTIC_2f076a189a3dcc7b
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the bot token from environment variables
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Check if the token is available
if not BOT_TOKEN:
    raise ValueError("Bot token not found. Please set DISCORD_BOT_TOKEN in your .env file.")

# Define intents for the bot (required for certain features like member updates)
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Triggered when the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user} (ID: {bot.user.id})")

# Command: Respond to a simple ping command
@bot.command(name="ping")
async def ping(ctx):
    """
    Responds with 'Pong!' and the bot's latency.
    """
    latency = round(bot.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f"Pong! Latency: {latency}ms")

# Event: Triggered when a new message is sent in a channel
@bot.event
async def on_message(message):
    """
    Listens for messages and responds to specific keywords.
    """
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Example: Respond to a specific keyword
    if "hello bot" in message.content.lower():
        await message.channel.send(f"Hello, {message.author.mention}!")

    # Process commands (required for commands to work alongside on_message)
    await bot.process_commands(message)

# Error handling: Catch errors in commands
@bot.event
async def on_command_error(ctx, error):
    """
    Handles errors that occur during command execution.
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please use a valid command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing arguments. Please check the command usage.")
    else:
        await ctx.send("An error occurred while processing the command.")
        # Log the error for debugging purposes
        print(f"Error: {error}")

# Run the bot
try:
    bot.run(BOT_TOKEN)
except discord.LoginFailure:
    print("Invalid bot token. Please check your .env file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
