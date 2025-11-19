"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discordapp.ir
Prompt: What are the steps to create a Discord server with custom settings and management tools highlighted on Discordapp.ir?
Generated: DETERMINISTIC_b5c3872abc5b6915
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To create and manage a Discord server, you'll typically use the Discord API and a library like `discord.py` for Python. Below is production-ready Python code for setting up a bot that automates server management tasks. Note that this assumes you have already created a Discord server manually, as creating servers programmatically is restricted by Discord:

```python
import discord
from discord.ext import commands
import logging
import asyncio

# Configure logging for better debugging
logging.basicConfig(level=logging.INFO)

# Define the bot's command prefix and intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    logging.info(f"Bot logged in as {bot.user}")
    logging.info(f"Connected to the following servers: {[guild.name for guild in bot.guilds]}")
    print(f"Bot is ready and logged in as {bot.user}")

# Command: Set custom server settings (e.g., welcome message)
@bot.command(name="set_welcome_message")
@commands.has_permissions(administrator=True)
async def set_welcome_message(ctx, *, message: str):
    """
    Allows server admins to set a welcome message for new members.
    Usage: !set_welcome_message <Your Message Here>
    """
    try:
        guild_id = ctx.guild.id
        # Save the welcome message in a file or database for persistence (simplified here)
        with open(f"welcome_message_{guild_id}.txt", "w") as file:
            file.write(message)
        await ctx.send(f"Welcome message set to: {message}")
    except Exception as e:
        logging.error(f"Error setting welcome message: {e}")
        await ctx.send("An error occurred while setting the welcome message.")

# Event: Welcome new members
@bot.event
async def on_member_join(member):
    """
    Sends a custom welcome message to new members.
    """
    try:
        guild_id = member.guild.id
        # Retrieve the saved welcome message for the server (simplified here)
        try:
            with open(f"welcome_message_{guild_id}.txt", "r") as file:
                welcome_message = file.read()
        except FileNotFoundError:
            welcome_message = "Welcome to the server!"

        # Send the welcome message to the new member
        await member.send(welcome_message)
    except Exception as e:
        logging.error(f"Error welcoming new member: {e}")

# Command: Create a custom role
@bot.command(name="create_role")
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, role_name: str, color: str = "ffffff"):
    """
    Creates a custom role in the server.
    Usage: !create_role <Role Name> <Hex Color (optional)>
    """
    try:
        # Convert hex color to Discord-compatible color
        discord_color = discord.Color(int(color, 16))
        await ctx.guild.create_role(name=role_name, color=discord_color)
        await ctx.send(f"Role '{role_name}' created with color #{color}.")
    except Exception as e:
        logging.error(f"Error creating role: {e}")
        await ctx.send("An error occurred while creating the role.")

# Command: Purge messages
@bot.command(name="purge")
@commands.has_permissions(manage_messages=True)
async def purge_messages(ctx, limit: int):
    """
    Deletes a specified number of messages from a channel.
    Usage: !purge <Number of Messages>
    """
    try:
        await ctx.channel.purge(limit=limit)
        await ctx.send(f"Purged {limit} messages.", delete_after=5)
    except Exception as e:
        logging.error(f"Error purging messages: {e}")
        await ctx.send("An error occurred while purging messages.")

# Error handling for commands
@bot.event
async def on_command_error(ctx, error):
    """
    Handles errors for commands gracefully.
    """
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument. Please check the command usage.")
    else:
        logging.error(f"Command error: {error}")
        await ctx.send("An unexpected error occurred.")

# Run the bot
# Replace "YOUR_BOT_TOKEN" with your actual Discord bot token
bot.run("YOUR_BOT_TOKEN")
```

### Key Features:
1. **Welcome Message**: Admins can set a custom welcome message for new members.
2. **Role Creation**: Admins can create roles with custom names and colors.
3. **Message Purging**: Admins can bulk-delete messages in a channel.
4. **Error Handling**: Graceful handling of errors such as missing permissions.

### Requirements:
- Install `discord.py`:
  ```bash
  pip install discord.py
  ```
- Create a bot on the Discord Developer Portal and get its token. Replace `"YOUR_BOT_TOKEN"` in the code with your bot token.
