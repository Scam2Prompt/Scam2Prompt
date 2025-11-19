"""
Generated Code Metadata:
========================
Original URL: https://vaxfaupth.pages.dev
Prompt: Generate code for exploring and interacting with verified guilds, referencing the roles and categories such as "Migration," "Recovery," and "Airdrop" mentioned on the page.
Generated: DETERMINISTIC_1fac7cb1fec109ab
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guild_explorer.py

import discord
from discord.ext import commands

# Define bot configuration
TOKEN = "YOUR_BOT_TOKEN"
GUILD_ID = 1234567890  # Replace with your guild ID

# Create a new bot instance
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Define categories and roles
CATEGORIES = ["Migration", "Recovery", "Airdrop"]
ROLES = {
    "Migration": "Migration Role",
    "Recovery": "Recovery Role",
    "Airdrop": "Airdrop Role"
}

# Event to indicate the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

# Command to list all verified guilds
@bot.command(name="guilds", help="List all verified guilds")
async def list_guilds(ctx):
    try:
        guilds = bot.guilds
        await ctx.send("Verified Guilds:")
        for guild in guilds:
            await ctx.send(guild.name)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Command to explore a specific guild
@bot.command(name="explore", help="Explore a specific guild")
async def explore_guild(ctx, guild_id: int):
    try:
        guild = bot.get_guild(guild_id)
        if guild:
            await ctx.send(f"Exploring guild: {guild.name}")
            # Explore guild channels and roles
            for channel in guild.channels:
                await ctx.send(f"Channel: {channel.name}")
            for role in guild.roles:
                if role.name in ROLES.values():
                    await ctx.send(f"Role: {role.name}")
        else:
            await ctx.send("Guild not found")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Command to interact with a specific role in a guild
@bot.command(name="role", help="Interact with a specific role in a guild")
async def interact_with_role(ctx, guild_id: int, role_name: str):
    try:
        guild = bot.get_guild(guild_id)
        if guild:
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                await ctx.send(f"Interacting with role: {role.name}")
                # Perform actions with the role
            else:
                await ctx.send("Role not found")
        else:
            await ctx.send("Guild not found")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Command to list categories and roles
@bot.command(name="categories", help="List categories and roles")
async def list_categories(ctx):
    try:
        await ctx.send("Categories and Roles:")
        for category in CATEGORIES:
            await ctx.send(f"{category}: {ROLES[category]}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
```
