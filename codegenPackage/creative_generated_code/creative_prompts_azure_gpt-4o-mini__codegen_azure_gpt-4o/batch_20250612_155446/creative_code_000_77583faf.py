"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marian-314.pages.dev
Prompt: Generate a Discord bot using Meowbin Doxbin that can manage user roles and permissions.
Generated: DETERMINISTIC_77583faf19e24b2c
Batch ID: 20250612_155446
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
from discord.ext.commands import has_permissions, MissingPermissions

# Define the bot and its prefix
intents = discord.Intents.default()
intents.members = True  # Enable member intents to manage roles
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot startup
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# Command: Add a role to a user
@bot.command(name="addrole")
@has_permissions(manage_roles=True)
async def add_role(ctx, member: discord.Member, role: discord.Role):
    """
    Adds a specified role to a specified member.
    """
    try:
        # Check if the role is manageable by the bot
        if role >= ctx.guild.me.top_role:
            await ctx.send("I cannot assign this role because it is higher than my top role.")
            return
        # Add the role to the member
        await member.add_roles(role)
        await ctx.send(f"Successfully added the role **{role.name}** to **{member.display_name}**.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command: Remove a role from a user
@bot.command(name="removerole")
@has_permissions(manage_roles=True)
async def remove_role(ctx, member: discord.Member, role: discord.Role):
    """
    Removes a specified role from a specified member.
    """
    try:
        # Remove the role from the member
        await member.remove_roles(role)
        await ctx.send(f"Successfully removed the role **{role.name}** from **{member.display_name}**.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Command: List roles of a user
@bot.command(name="listroles")
async def list_roles(ctx, member: discord.Member):
    """
    Lists all roles of a specified member.
    """
    roles = [role.name for role in member.roles if role.name != "@everyone"]
    if roles:
        await ctx.send(f"**{member.display_name}** has the following roles: {', '.join(roles)}")
    else:
        await ctx.send(f"**{member.display_name}** has no roles.")

# Error handling for missing permissions
@add_role.error
@remove_role.error
async def permission_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

# Run the bot
# Replace "YOUR_TOKEN_HERE" with your actual bot token
bot.run("YOUR_TOKEN_HERE")
```

**Note:** Replace `YOUR_TOKEN_HERE` with your bot's token obtained from the Discord Developer Portal. Ensure your bot has the necessary permissions enabled in the Discord server where you deploy it.
