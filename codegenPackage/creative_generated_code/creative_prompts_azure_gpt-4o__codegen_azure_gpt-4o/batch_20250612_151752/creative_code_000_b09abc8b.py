"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: Write a Python script that integrates the Dyno Bot into a Discord server and configures basic moderation commands as described on the Dyno Bot website.
Generated: DETERMINISTIC_b09abc8b48eb690c
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
import os

# Constants for bot configuration
BOT_PREFIX = "!"
TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot token
ADMIN_ROLE_NAME = "Admin"  # Replace with the role name for administrators

# Initialize bot with command prefix
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Event triggered when bot is ready
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord and is ready!")

# Command to kick a user
@bot.command(name='kick', help='Kick a user from the server')
@commands.has_role(ADMIN_ROLE_NAME)  # Restrict command to users with admin role
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"User {member} has been kicked for reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick this user.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to kick user. Error: {str(e)}")

# Command to ban a user
@bot.command(name='ban', help='Ban a user from the server')
@commands.has_role(ADMIN_ROLE_NAME)  # Restrict command to users with admin role
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"User {member} has been banned for reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to ban this user.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to ban user. Error: {str(e)}")

# Command to unban a user
@bot.command(name='unban', help='Unban a user from the server')
@commands.has_role(ADMIN_ROLE_NAME)  # Restrict command to users with admin role
async def unban(ctx, *, member_name):
    try:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member_name:
                await ctx.guild.unban(user)
                await ctx.send(f"User {user.name} has been unbanned.")
                return
        await ctx.send(f"User {member_name} not found in banned list.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to unban user. Error: {str(e)}")

# Command to clear messages
@bot.command(name='clear', help='Delete a number of recent messages')
@commands.has_role(ADMIN_ROLE_NAME)  # Restrict command to users with admin role
async def clear(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Please specify a positive number of messages to delete.")
        return

    try:
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
    except discord.Forbidden:
        await ctx.send("I do not have permission to delete messages.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to delete messages. Error: {str(e)}")

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all required arguments.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")

# Start the bot
if __name__ == "__main__":
    # Check if token is provided
    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Error: Bot token not provided. Update the TOKEN variable with your Discord bot token.")
    else:
        bot.run(TOKEN)
```
