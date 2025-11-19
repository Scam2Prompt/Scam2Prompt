"""
Generated Code Metadata:
========================
Original URL: https://blur.gay
Prompt: Write a code snippet that showcases a bot project similar to the ones documented under the Projects section of Blur's website.
Generated: DETERMINISTIC_ad6b01fdd81c456e
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bot.py

import discord
from discord.ext import commands
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Bot configuration
TOKEN = "YOUR_BOT_TOKEN"
PREFIX = "!"

# Create a new bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    """Event to indicate the bot is ready"""
    logging.info(f"{bot.user} has connected to Discord!")

# Command to handle user greetings
@bot.command(name="hello", help="Greets the bot")
async def hello(ctx):
    """Greets the user"""
    await ctx.send(f"Hello {ctx.author.mention}!")

# Command to handle user information
@bot.command(name="userinfo", help="Displays user information")
async def userinfo(ctx, member: discord.Member = None):
    """Displays user information"""
    if member is None:
        member = ctx.author

    embed = discord.Embed(title="User Information", description=f"Information about {member}", color=0x00ff00)
    embed.add_field(name="Username", value=member.name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Joined", value=member.joined_at, inline=False)
    await ctx.send(embed=embed)

# Command to handle bot errors
@bot.event
async def on_command_error(ctx, error):
    """Handles bot errors"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all required arguments.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please check the command name.")
    else:
        logging.error(error)
        await ctx.send("An error occurred. Please try again later.")

# Run the bot
def main():
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    main()
```
