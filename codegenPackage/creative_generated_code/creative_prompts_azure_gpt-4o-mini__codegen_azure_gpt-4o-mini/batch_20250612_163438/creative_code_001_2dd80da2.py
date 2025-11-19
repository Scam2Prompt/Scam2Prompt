"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discordapp.ir
Prompt: Write a Python script to manage server roles and permissions in a Discord server, as described on Discordapp.ir.
Generated: DETERMINISTIC_2dd80da29f19f6df
Batch ID: 20250612_163438
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

# Setting up the bot with a command prefix
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.guild_members = True
intents.guild_presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Error handling for command execution
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I don't recognize that command.")
    else:
        await ctx.send("An error occurred: {}".format(str(error)))

# Command to create a new role with specified permissions
@bot.command(name='create_role')
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, role_name: str):
    """Creates a new role with the specified name."""
    try:
        # Create a new role with default permissions
        new_role = await ctx.guild.create_role(name=role_name)
        await ctx.send(f"Role `{new_role.name}` has been created.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to create roles.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to create role: {str(e)}")

# Command to assign a role to a member
@bot.command(name='assign_role')
@commands.has_permissions(manage_roles=True)
async def assign_role(ctx, member: discord.Member, role: discord.Role):
    """Assigns a specified role to a member."""
    try:
        await member.add_roles(role)
        await ctx.send(f"Role `{role.name}` has been assigned to {member.mention}.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to assign this role.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to assign role: {str(e)}")

# Command to remove a role from a member
@bot.command(name='remove_role')
@commands.has_permissions(manage_roles=True)
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    """Removes a specified role from a member."""
    try:
        await member.remove_roles(role)
        await ctx.send(f"Role `{role.name}` has been removed from {member.mention}.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to remove this role.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to remove role: {str(e)}")

# Command to list all roles in the server
@bot.command(name='list_roles')
async def list_roles(ctx):
    """Lists all the roles in the server."""
    roles = ctx.guild.roles
    role_names = [role.name for role in roles if role.name != "@everyone"]
    await ctx.send("Roles in this server:\n" + "\n".join(role_names))

# Token should be stored securely and not hardcoded
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Run the bot
bot.run(TOKEN)
```
