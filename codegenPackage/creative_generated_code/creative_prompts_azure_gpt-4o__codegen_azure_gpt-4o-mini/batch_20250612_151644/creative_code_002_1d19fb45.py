"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.gay
Prompt: Generate code for a Discord bot inspired by the projects listed on https://blur.gay, incorporating features mentioned in the site's documentation.
Generated: DETERMINISTIC_1d19fb453a56e6e7
Batch ID: 20250612_151644
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

# Set up logging to monitor the bot's activity
logging.basicConfig(level=logging.INFO)

# Create a Discord bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    """
    Event that runs when the bot is ready and has connected to Discord.
    """
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="Type !help for commands"))

@bot.command()
async def ping(ctx):
    """
    Responds with 'Pong!' when the user types !ping.
    """
    await ctx.send('Pong!')

@bot.command()
async def info(ctx):
    """
    Provides information about the bot and its features.
    """
    info_message = (
        "I am a bot inspired by the projects on blur.gay!\n"
        "Here are some commands you can use:\n"
        "!ping - Check if the bot is alive\n"
        "!info - Get information about this bot\n"
        "!help - List all available commands"
    )
    await ctx.send(info_message)

@bot.command()
async def help(ctx):
    """
    Lists all available commands for the bot.
    """
    help_message = (
        "Here are the commands you can use:\n"
        "!ping - Check if the bot is alive\n"
        "!info - Get information about this bot\n"
        "!help - List all available commands"
    )
    await ctx.send(help_message)

@bot.event
async def on_command_error(ctx, error):
    """
    Handles errors that occur during command execution.
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command. Type !help for a list of commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You are missing a required argument. Please check the command usage.")
    else:
        logging.error(f'An error occurred: {error}')
        await ctx.send("An error occurred while processing your request.")

def main():
    """
    Main function to run the bot.
    This retrieves the token from an environment variable and runs the bot.
    """
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        logging.error("No token provided. Set the DISCORD_TOKEN environment variable.")
        return

    try:
        bot.run(token)
    except Exception as e:
        logging.error(f"Failed to run the bot: {e}")

if __name__ == "__main__":
    main()
```
