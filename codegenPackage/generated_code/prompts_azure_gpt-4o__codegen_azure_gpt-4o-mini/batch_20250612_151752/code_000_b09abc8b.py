"""
Generated Code Metadata:
========================
Original URL: https://dyno.pw
Prompt: Write a Python script that integrates the Dyno Bot into a Discord server and configures basic moderation commands as described on the Dyno Bot website.
Generated: DETERMINISTIC_b09abc8b48eb690c
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

# Define the bot's command prefix and intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Create a bot instance with the specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command: Kick a user from the server
@bot.command(name='kick', help='Kicks a user from the server. Usage: !kick @user [reason]')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for: {reason}')
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick this user.")
    except discord.HTTPException:
        await ctx.send("Failed to kick the user.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command: Ban a user from the server
@bot.command(name='ban', help='Bans a user from the server. Usage: !ban @user [reason]')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for: {reason}')
    except discord.Forbidden:
        await ctx.send("I do not have permission to ban this user.")
    except discord.HTTPException:
        await ctx.send("Failed to ban the user.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command: Unban a user from the server
@bot.command(name='unban', help='Unbans a user from the server. Usage: !unban user_id [reason]')
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int, *, reason=None):
    try:
        user = await bot.fetch_user(user_id)
        await ctx.guild.unban(user, reason=reason)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator} for: {reason}')
    except discord.NotFound:
        await ctx.send("User not found.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to unban this user.")
    except discord.HTTPException:
        await ctx.send("Failed to unban the user.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command: Clear messages from a channel
@bot.command(name='clear', help='Clears a specified number of messages from the channel. Usage: !clear <number>')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message
        await ctx.send(f'Cleared {amount} messages.', delete_after=5)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Error handling for missing permissions
@kick.error
@ban.error
@unban.error
@clear.error
async def command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

# Run the bot with the specified token
TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your bot's token
bot.run(TOKEN)
```

**Note:** Replace `'YOUR_BOT_TOKEN_HERE'` with your actual Discord bot token before running the script.
