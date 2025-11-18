"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: Explain how Dyno Bot can be used for server analytics and reporting, and provide code examples for implementing these features based on the Dyno Bot website.
Generated: DETERMINISTIC_cabd289e948b7dab
Batch ID: 20250612_151752
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
import json

# Configure logging to track events and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Define the bot's command prefix and intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load token from a secure config file
def load_token():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            return config['TOKEN']
    except FileNotFoundError:
        logging.error("Config file not found. Make sure 'config.json' exists.")
        raise
    except KeyError:
        logging.error("Token not found in the config file.")
        raise

# Command to fetch server analytics
@bot.command(name='server_analytics')
async def server_analytics(ctx):
    """Fetch and display basic server analytics."""
    try:
        total_members = ctx.guild.member_count
        online_members = sum(1 for member in ctx.guild.members if member.status != discord.Status.offline)
        
        analytics_report = (
            f"Server Name: {ctx.guild.name}\n"
            f"Total Members: {total_members}\n"
            f"Online Members: {online_members}\n"
        )
        
        await ctx.send(analytics_report)
        logging.info("Server analytics report sent.")

    except Exception as e:
        logging.error(f"An error occurred while fetching server analytics: {str(e)}")
        await ctx.send("An error occurred while fetching server analytics.")


# Command to fetch and display channel statistics
@bot.command(name='channel_stats')
async def channel_stats(ctx):
    """Fetch and display channel statistics."""
    try:
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)

        stats_report = (
            f"Text Channels: {text_channels}\n"
            f"Voice Channels: {voice_channels}\n"
        )
        
        await ctx.send(stats_report)
        logging.info("Channel statistics report sent.")

    except Exception as e:
        logging.error(f"An error occurred while fetching channel statistics: {str(e)}")
        await ctx.send("An error occurred while fetching channel statistics.")


# Command to fetch and report top roles in the server
@bot.command(name='top_roles')
async def top_roles(ctx):
    """Fetch and display the top roles in the server."""
    try:
        roles = sorted(ctx.guild.roles, key=lambda role: len(role.members), reverse=True)
        top_roles_report = "Top Roles:\n"

        for role in roles[:5]:  # Get top 5 roles
            top_roles_report += f"{role.name}: {len(role.members)} members\n"

        await ctx.send(top_roles_report)
        logging.info("Top roles report sent.")

    except Exception as e:
        logging.error(f"An error occurred while fetching top roles: {str(e)}")
        await ctx.send("An error occurred while fetching top roles.")


# Run the bot
if __name__ == '__main__':
    try:
        token = load_token()
        bot.run(token)
    except Exception as e:
        logging.error(f"Failed to start the bot: {str(e)}")
```

### Configuration File (config.json)
Make sure to create a `config.json` file with the following structure:

```json
{
    "TOKEN": "YOUR_BOT_TOKEN_HERE"
}
``` 

This code implements basic commands for server analytics, including member count, channel statistics, and top roles, with proper error handling and logging.
