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
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Event handler for when the bot is ready"""
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    """Simple command to check if bot is responsive"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    """Command to clear messages from channel (requires manage_messages permission)"""
    try:
        await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message
        await ctx.send(f'Cleared {amount} messages.', delete_after=5)
    except Exception as e:
        await ctx.send(f'Error clearing messages: {e}')

@bot.event
async def on_command_error(ctx, error):
    """Event handler for command errors"""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Type !help for available commands.")
    else:
        await ctx.send(f"An error occurred: {error}")

def main():
    """Main function to start the bot"""
    try:
        token = os.getenv('DISCORD_BOT_TOKEN')
        if not token:
            raise ValueError("DISCORD_BOT_TOKEN not found in environment variables")
        bot.run(token)
    except Exception as e:
        print(f"Failed to start bot: {e}")

if __name__ == '__main__':
    main()
```
