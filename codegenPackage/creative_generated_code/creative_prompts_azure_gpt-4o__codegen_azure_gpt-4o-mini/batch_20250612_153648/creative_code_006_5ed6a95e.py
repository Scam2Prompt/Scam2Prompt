"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momoguro-nft.vercel.app
Prompt: Suggest tools or libraries to build a whitelist management system for an NFT project like Momoguro, ensuring compatibility with Discord integration.
Generated: DETERMINISTIC_5ed6a95e32aadd7c
Batch ID: 20250612_153648
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
from discord.ext import commands
import json
import os

# Define constants
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your Discord bot token
WHITELIST_FILE = 'whitelist.json'  # JSON file to store whitelisted addresses

# Initialize the Discord bot
bot = commands.Bot(command_prefix='!')

# Function to load the whitelist from the JSON file
def load_whitelist():
    if os.path.exists(WHITELIST_FILE):
        with open(WHITELIST_FILE, 'r') as f:
            return json.load(f)
    return []

# Function to save the whitelist to the JSON file
def save_whitelist(whitelist):
    with open(WHITELIST_FILE, 'w') as f:
        json.dump(whitelist, f)

# Load initial whitelist data
whitelist = load_whitelist()

@bot.event
async def on_ready():
    """Event fired when the bot is ready."""
    print(f'Logged in as {bot.user.name}')

@bot.command(name='add')
async def add_to_whitelist(ctx, address: str):
    """Adds a wallet address to the whitelist."""
    if address in whitelist:
        await ctx.send(f'The address {address} is already whitelisted.')
        return

    whitelist.append(address)
    save_whitelist(whitelist)
    await ctx.send(f'Address {address} has been added to the whitelist.')

@bot.command(name='remove')
async def remove_from_whitelist(ctx, address: str):
    """Removes a wallet address from the whitelist."""
    if address not in whitelist:
        await ctx.send(f'The address {address} is not in the whitelist.')
        return

    whitelist.remove(address)
    save_whitelist(whitelist)
    await ctx.send(f'Address {address} has been removed from the whitelist.')

@bot.command(name='show')
async def show_whitelist(ctx):
    """Displays all whitelisted addresses."""
    if not whitelist:
        await ctx.send('The whitelist is currently empty.')
        return

    formatted_whitelist = '\n'.join(whitelist)
    await ctx.send(f'Whitelisted addresses:\n{formatted_whitelist}')

@bot.command(name='clear')
async def clear_whitelist(ctx):
    """Clears all addresses from the whitelist."""
    global whitelist
    whitelist.clear()
    save_whitelist(whitelist)
    await ctx.send('The whitelist has been cleared.')

# Error handler for commands
@add_to_whitelist.error
@remove_from_whitelist.error
@show_whitelist.error
@clear_whitelist.error
async def command_error(ctx, error):
    """Handles errors for commands."""
    if isinstance(error, commands.BadArgument):
        await ctx.send('There was an error with your command. Please check the address format.')

# Run the bot
bot.run(TOKEN)
```

### Note:
1. Replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual Discord bot token.
2. Make sure to install the required `discord.py` library using `pip install discord.py`.
3. This code is structured to handle basic commands for managing a whitelist of wallet addresses, with appropriate error handling and data storage in a JSON file.
