"""
Generated Code Metadata:
========================
Original URL: https://blur.gay
Prompt: Generate code for a Discord bot inspired by the projects listed on https://blur.gay, incorporating features mentioned in the site's documentation.
Generated: DETERMINISTIC_1d19fb453a56e6e7
Batch ID: 20250612_151644
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
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the bot's command prefix and description
bot = commands.Bot(command_prefix='!', description='A Discord bot inspired by blur.gay')

# Load environment variables for token
TOKEN = os.getenv('DISCORD_TOKEN')

# Event: When the bot is ready
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logging.info('------')

# Command: Ping-Pong
@bot.command(name='ping', help='Responds with Pong!')
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Echo
@bot.command(name='echo', help='Repeats the message you send.')
async def echo(ctx, *, message: str):
    await ctx.send(message)

# Command: Random Number
@bot.command(name='random', help='Generates a random number between 1 and 100.')
async def random_number(ctx):
    import random
    number = random.randint(1, 100)
    await ctx.send(f'Your random number is: {number}')

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide the required argument.")
    else:
        await ctx.send("An error occurred while processing your command.")
        logging.error(f'Error in command {ctx.command}: {error}')

# Run the bot
if __name__ == '__main__':
    if TOKEN is None:
        logging.error("No token provided. Set the DISCORD_TOKEN environment variable.")
    else:
        bot.run(TOKEN)
```

Make sure to set the `DISCORD_TOKEN` environment variable with your bot's token before running the code.
