"""
Generated Code Metadata:
========================
Original URL: https://dyno.pw
Prompt: Write a script to configure Dyno Bot for automated announcements in a Discord server, using the bot's features mentioned on the Dyno Bot webpage.
Generated: DETERMINISTIC_163932203164b461
Batch ID: 20250612_151752
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
import asyncio
import json
import os

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Initialize bot with required intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

async def setup_announcement_channel(guild_id, channel_id):
    """Configure the announcement channel in a guild"""
    guild = bot.get_guild(guild_id)
    if not guild:
        raise ValueError(f"Guild with ID {guild_id} not found")
    
    channel = guild.get_channel(channel_id)
    if not channel:
        raise ValueError(f"Channel with ID {channel_id} not found in guild {guild.name}")
    
    # Check if bot has permissions in the channel
    permissions = channel.permissions_for(guild.me)
    if not permissions.send_messages:
        raise PermissionError(f"Bot lacks permission to send messages in {channel.name}")
    
    return channel

async def create_announcement(guild_id, channel_id, message, interval_minutes=60):
    """Create a recurring announcement in the specified channel"""
    try:
        channel = await setup_announcement_channel(guild_id, channel_id)
        
        while True:
            await channel.send(message)
            print(f"Sent announcement to {channel.name} in {channel.guild.name}")
            await asyncio.sleep(interval_minutes * 60)
            
    except Exception as e:
        print(f"Error in announcement task: {str(e)}")

@bot.command(name='setup_announcements')
@commands.has_permissions(administrator=True)
async def setup_announcements(ctx, channel: discord.TextChannel, *, message: str):
    """Setup automated announcements in the specified channel"""
    try:
        # Save configuration
        config['announcements'][str(ctx.guild.id)] = {
            'channel_id': channel.id,
            'message': message,
            'interval': 60  # Default interval of 60 minutes
        }
        
        with open('config.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)
        
        # Start announcement task
        bot.loop.create_task(
            create_announcement(ctx.guild.id, channel.id, message)
        )
        
        await ctx.send(f"✅ Announcements configured in {channel.mention} with message: {message}")
        
    except Exception as e:
        await ctx.send(f"❌ Error setting up announcements: {str(e)}")

@bot.command(name='set_interval')
@commands.has_permissions(administrator=True)
async def set_interval(ctx, interval_minutes: int):
    """Set the interval between announcements in minutes"""
    try:
        guild_id = str(ctx.guild.id)
        if guild_id not in config['announcements']:
            await ctx.send("❌ No announcements configured for this server. Use !setup_announcements first.")
            return
            
        config['announcements'][guild_id]['interval'] = interval_minutes
        
        with open('config.json', 'w') as config_file:
            json.dump(config, config_file, indent=4)
            
        await ctx.send(f"✅ Announcement interval set to {interval_minutes} minutes")
        
    except Exception as e:
        await ctx.send(f"❌ Error setting interval: {str(e)}")

@bot.command(name='stop_announcements')
@commands.has_permissions(administrator=True)
async def stop_announcements(ctx):
    """Stop all announcements in this server"""
    try:
        guild_id = str(ctx.guild.id)
        if guild_id in config['announcements']:
            del config['announcements'][guild_id]
            
            with open('config.json', 'w') as config_file:
                json.dump(config, config_file, indent=4)
                
            await ctx.send("✅ Announcements stopped for this server")
        else:
            await ctx.send("❌ No active announcements for this server")
            
    except Exception as e:
        await ctx.send(f"❌ Error stopping announcements: {str(e)}")

def load_announcements():
    """Load and start all saved announcements on bot startup"""
    for guild_id, announcement in config.get('announcements', {}).items():
        bot.loop.create_task(
            create_announcement(
                int(guild_id),
                announcement['channel_id'],
                announcement['message'],
                announcement.get('interval', 60)
            )
        )

# Start the bot
if __name__ == '__main__':
    # Ensure config has required structure
    if 'announcements' not in config:
        config['announcements'] = {}
    
    load_announcements()
    bot.run(config['token'])
```
