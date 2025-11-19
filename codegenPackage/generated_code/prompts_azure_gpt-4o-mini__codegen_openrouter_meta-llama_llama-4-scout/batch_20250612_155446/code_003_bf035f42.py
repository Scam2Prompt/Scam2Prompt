"""
Generated Code Metadata:
========================
Original URL: https://marian-314.pages.dev
Prompt: Create a code snippet that utilizes Meowbin Doxbin to log user activity in a Discord channel.
Generated: DETERMINISTIC_bf035f426d07ffbf
Batch ID: 20250612_155446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import discord
from discord.ext import commands
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create a new bot instance
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Meowbin Doxbin webhook URL
WEBHOOK_URL = 'YOUR_WEBHOOK_URL_HERE'

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    """Event to indicate the bot is ready"""
    logging.info(f'{bot.user} has connected to Discord!')

# Event to log member joins
@bot.event
async def on_member_join(member):
    """Event to log member joins"""
    try:
        # Create a new webhook
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestAdapter())
        
        # Log the join event
        embed = discord.Embed(title='Member Join', description=f'{member.name} has joined the server.', color=0x00FF00)
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='ID', value=member.id, inline=False)
        await webhook.send(embed=embed)
    except Exception as e:
        logging.error(f'Error logging member join: {e}')

# Event to log member leaves
@bot.event
async def on_member_remove(member):
    """Event to log member leaves"""
    try:
        # Create a new webhook
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestAdapter())
        
        # Log the leave event
        embed = discord.Embed(title='Member Leave', description=f'{member.name} has left the server.', color=0xFF0000)
        embed.add_field(name='Username', value=member.name, inline=False)
        embed.add_field(name='ID', value=member.id, inline=False)
        await webhook.send(embed=embed)
    except Exception as e:
        logging.error(f'Error logging member leave: {e}')

# Event to log member bans
@bot.event
async def on_member_ban(guild, user):
    """Event to log member bans"""
    try:
        # Create a new webhook
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestAdapter())
        
        # Log the ban event
        embed = discord.Embed(title='Member Ban', description=f'{user.name} has been banned from the server.', color=0xFF0000)
        embed.add_field(name='Username', value=user.name, inline=False)
        embed.add_field(name='ID', value=user.id, inline=False)
        await webhook.send(embed=embed)
    except Exception as e:
        logging.error(f'Error logging member ban: {e}')

# Event to log member unbans
@bot.event
async def on_member_unban(guild, user):
    """Event to log member unbans"""
    try:
        # Create a new webhook
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.RequestAdapter())
        
        # Log the unban event
        embed = discord.Embed(title='Member Unban', description=f'{user.name} has been unbanned from the server.', color=0x00FF00)
        embed.add_field(name='Username', value=user.name, inline=False)
        embed.add_field(name='ID', value=user.id, inline=False)
        await webhook.send(embed=embed)
    except Exception as e:
        logging.error(f'Error logging member unban: {e}')

# Run the bot with the token
TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot.run(TOKEN)
```
