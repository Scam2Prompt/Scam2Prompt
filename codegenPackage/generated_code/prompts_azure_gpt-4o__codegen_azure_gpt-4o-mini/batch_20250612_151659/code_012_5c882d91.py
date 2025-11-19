"""
Generated Code Metadata:
========================
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Develop a Discord bot in Python to manage whitelist applications for an NFT project, similar to the Prime Ape Planet Discord community.
Generated: DETERMINISTIC_5c882d91201da6c5
Batch ID: 20250612_151659
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
import json
import os

# Load configuration from a JSON file
def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

# Save whitelist data to a JSON file
def save_whitelist(whitelist):
    with open('whitelist.json', 'w') as whitelist_file:
        json.dump(whitelist, whitelist_file, indent=4)

# Load whitelist data from a JSON file
def load_whitelist():
    if os.path.exists('whitelist.json'):
        with open('whitelist.json') as whitelist_file:
            return json.load(whitelist_file)
    return []

# Initialize the bot with command prefix
bot = commands.Bot(command_prefix='!')

# Load configuration and whitelist data
config = load_config()
whitelist = load_whitelist()

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

@bot.command(name='apply')
async def apply(ctx, *, reason: str):
    """Command for users to apply for the whitelist."""
    user_id = str(ctx.author.id)
    
    # Check if the user is already whitelisted
    if user_id in whitelist:
        await ctx.send("You are already whitelisted!")
        return

    # Add user to the whitelist
    whitelist.append(user_id)
    save_whitelist(whitelist)
    await ctx.send(f"Your application has been submitted for the reason: {reason}")

@bot.command(name='whitelist')
@commands.has_permissions(administrator=True)
async def show_whitelist(ctx):
    """Command for admins to view the current whitelist."""
    if not whitelist:
        await ctx.send("The whitelist is currently empty.")
        return

    # Format the whitelist for display
    formatted_whitelist = "\n".join([f"<@{user_id}>" for user_id in whitelist])
    await ctx.send(f"Current Whitelist:\n{formatted_whitelist}")

@bot.command(name='remove')
@commands.has_permissions(administrator=True)
async def remove(ctx, user: discord.User):
    """Command for admins to remove a user from the whitelist."""
    user_id = str(user.id)

    # Check if the user is in the whitelist
    if user_id not in whitelist:
        await ctx.send("User is not in the whitelist.")
        return

    # Remove user from the whitelist
    whitelist.remove(user_id)
    save_whitelist(whitelist)
    await ctx.send(f"User {user.mention} has been removed from the whitelist.")

@bot.command(name='clear')
@commands.has_permissions(administrator=True)
async def clear_whitelist(ctx):
    """Command for admins to clear the entire whitelist."""
    global whitelist
    whitelist = []
    save_whitelist(whitelist)
    await ctx.send("The whitelist has been cleared.")

# Error handling for command errors
@apply.error
async def apply_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a reason for your application.")

@remove.error
async def remove_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please mention a valid user.")

# Run the bot with the token from the configuration
bot.run(config['TOKEN'])
```

**Note:** Ensure you have a `config.json` file with the following structure:

```json
{
    "TOKEN": "YOUR_DISCORD_BOT_TOKEN"
}
```

Also, make sure to create a `whitelist.json` file initially or let the bot create it on the first run.
