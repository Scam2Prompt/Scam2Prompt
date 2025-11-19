"""
Generated Code Metadata:
========================
Original URL: https://dyno.pw
Prompt: Generate a step-by-step guide to set up Dyno Bot on a Discord server, including examples of its most popular commands as outlined on the Dyno Bot webpage.
Generated: DETERMINISTIC_1082cf95a39b973e
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
import os

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Moderation Commands
@bot.command(name='ban', help='Bans a member from the server. Usage: !ban @user [reason]')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention} for reason: {reason}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban members.")

@bot.command(name='kick', help='Kicks a member from the server. Usage: !kick @user [reason]')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention} for reason: {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")

# Utility Commands
@bot.command(name='clear', help='Clears a specified number of messages. Usage: !clear <amount>')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Cleared {amount} messages.', delete_after=5)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to manage messages.")

@bot.command(name='mute', help='Mutes a member. Usage: !mute @user [duration] [reason]')
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, duration: str = None, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, speak=False, send_messages=False)
    
    await member.add_roles(muted_role, reason=reason)
    await ctx.send(f'Muted {member.mention} for {duration}. Reason: {reason}')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to manage roles.")

# Fun Commands
@bot.command(name='ping', help='Checks the bot\'s latency. Usage: !ping')
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command(name='say', help='Makes the bot say something. Usage: !say <message>')
async def say(ctx, *, message):
    await ctx.send(message)

# Music Commands (Basic Example)
@bot.command(name='play', help='Plays a song from YouTube. Usage: !play <url>')
async def play(ctx, url: str):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("You need to be in a voice channel to use this command.")
        return
    
    voice_client = await voice_channel.connect()
    await ctx.send(f'Playing from {url}')

@bot.command(name='leave', help='Leaves the voice channel. Usage: !leave')
async def leave(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")

# Run the bot with the token
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
```
