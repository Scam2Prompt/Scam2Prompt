"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-redstone.com
Prompt: Write code to integrate Discord roles from the RedStone Expedition into a custom application, including the ability to identify special roles.
Generated: DETERMINISTIC_e619c4f3d2c769c0
Batch ID: 20250612_150446
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

# Define the prefix for commands
COMMAND_PREFIX = '!'
# Define special roles to identify
SPECIAL_ROLES = ['Leader', 'Member', 'Support', 'Guest']

# Set up the bot with intents
intents = discord.Intents.default()
intents.members = True  # Enable member intents to access roles

# Initialize the bot
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command(name='check_roles')
async def check_roles(ctx):
    """Check the roles of the user who invoked the command."""
    # Ensure the command is invoked in a guild (server)
    if ctx.guild is None:
        await ctx.send("This command can only be used in a server.")
        return

    # Retrieve the roles of the member who invoked the command
    member_roles = ctx.author.roles
    special_roles = [role.name for role in member_roles if role.name in SPECIAL_ROLES]

    # Check if the user has any special roles
    if special_roles:
        await ctx.send(f"You have the following special roles: {', '.join(special_roles)}")
    else:
        await ctx.send("You do not have any special roles.")

@bot.event
async def on_command_error(ctx, error):
    """Event triggered when an error occurs in command execution."""
    # Provide user-friendly error messages
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I didn't understand that command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide all required arguments.")
    else:
        await ctx.send("An error occurred while executing that command.")
        # Log the error for debugging
        print(f'Error in command {ctx.command}: {error}')

# Start the bot with the token
if __name__ == '__main__':
    try:
        TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot's token
        bot.run(TOKEN)
    except Exception as e:
        print(f"Failed to start the bot: {e}")
```

### Notes:
- Replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual Discord bot token.
- Ensure the bot has the necessary permissions to read member roles in the Discord server settings.
- This code includes basic error handling and provides helpful feedback to users.
