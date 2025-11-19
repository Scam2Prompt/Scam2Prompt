"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: How do I customize Dyno Bot settings for my server's needs?
Generated: DETERMINISTIC_dce5590b0380b02d
Batch ID: 20250612_135957
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
import json

# Load configuration from a JSON file
def load_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            return json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading configuration: {e}")
        return {}

# Save configuration to a JSON file
def save_config(file_path, config):
    try:
        with open(file_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)
    except IOError as e:
        print(f"Error saving configuration: {e}")

# Define the bot command prefix
bot_prefix = '!'
# Load bot token and initial settings from the config
config = load_config('config.json')

# Create an instance of a bot
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command(name='set_welcome_channel', help='Set the welcome channel for the server.')
@commands.has_permissions(manage_channels=True)
async def set_welcome_channel(ctx, channel: discord.TextChannel):
    config['welcome_channel_id'] = channel.id
    save_config('config.json', config)
    await ctx.send(f'Welcome channel set to: {channel.mention}')

@bot.command(name='set_prefix', help='Change the command prefix for the bot.')
@commands.has_permissions(manage_guild=True)
async def set_prefix(ctx, new_prefix: str):
    global bot_prefix
    bot_prefix = new_prefix
    config['prefix'] = new_prefix
    save_config('config.json', config)
    await ctx.send(f'Command prefix changed to: {new_prefix}')

@bot.command(name='get_settings', help='Get the current settings for the server.')
async def get_settings(ctx):
    welcome_channel = config.get('welcome_channel_id')
    prefix = config.get('prefix', bot_prefix)
    
    welcome_channel_name = f"<#{welcome_channel}>" if welcome_channel else "Not set"
    
    settings_message = (
        f"Current settings:\n"
        f"Welcome Channel: {welcome_channel_name}\n"
        f"Command Prefix: {prefix}"
    )
    
    await ctx.send(settings_message)

# Error handling for command errors
@set_welcome_channel.error
@set_prefix.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please provide a valid input for the command.")
    else:
        await ctx.send("An error occurred while executing the command.")

# Run the bot
if __name__ == "__main__":
    try:
        bot.run(config['token'])
    except KeyError:
        print("Bot token is missing from the configuration.")
    except Exception as e:
        print(f"An error occurred while running the bot: {e}")
```
