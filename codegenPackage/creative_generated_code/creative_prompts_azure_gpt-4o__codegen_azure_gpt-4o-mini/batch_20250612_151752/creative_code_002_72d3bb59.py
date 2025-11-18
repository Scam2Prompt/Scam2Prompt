"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyno.pw
Prompt: How can I use Dyno Bot to automate server moderation tasks? Provide code examples based on the features listed on the Dyno Bot webpage.
Generated: DETERMINISTIC_72d3bb59d7501dc7
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

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a bot instance with command prefix
bot = commands.Bot(command_prefix="!")

# Error handling: Handle command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found. Use `!help` to see available commands.")
    else:
        logging.error(f"An error occurred: {error}")
        await ctx.send("An error occurred while processing your command.")

# Command: Kick a member from the server
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kick a member from the server."""
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked from the server. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to kick that member.")
    except discord.HTTPException:
        await ctx.send("I was unable to kick the member.")

# Command: Ban a member from the server
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """Ban a member from the server."""
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned from the server. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to ban that member.")
    except discord.HTTPException:
        await ctx.send("I was unable to ban the member.")

# Command: Unban a member from the server
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member_name):
    """Unban a member from the server."""
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member_name.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user
        if user.name == member_name and user.discriminator == member_discriminator:
            try:
                await ctx.guild.unban(user)
                await ctx.send(f"{user} has been unbanned from the server.")
            except discord.Forbidden:
                await ctx.send("I do not have permission to unban that member.")
            except discord.HTTPException:
                await ctx.send("I was unable to unban the member.")
            return

    await ctx.send(f"{member_name}#{member_discriminator} was not found in the ban list.")

# Command: Mute a member in the server (using a role)
@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    """Mute a member in the server."""
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not mute_role:
        await ctx.send("Mute role not found. Please create a role named 'Muted'.")
        return

    try:
        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f"{member} has been muted. Reason: {reason}")
    except discord.Forbidden:
        await ctx.send("I do not have permission to mute that member.")
    except discord.HTTPException:
        await ctx.send("I was unable to mute the member.")

# Event: Notify when the bot is ready
@bot.event
async def on_ready():
    logging.info(f'Bot is ready. Logged in as {bot.user}')

# Run the bot with your token
bot.run("YOUR_BOT_TOKEN")
```
Make sure to replace `"YOUR_BOT_TOKEN"` with your actual Discord bot token and ensure that the bot has the necessary permissions for the commands to work properly. Additionally, create a role named "Muted" in your server for the mute command to function correctly.
