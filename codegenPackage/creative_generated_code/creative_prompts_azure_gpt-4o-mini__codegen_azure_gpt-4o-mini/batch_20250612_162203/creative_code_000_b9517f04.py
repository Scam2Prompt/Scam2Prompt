"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momoguro.vercel.app
Prompt: How can I implement a Discord bot to manage WL giveaways for a community like Momoguro?
Generated: DETERMINISTIC_b9517f04156fc62e
Batch ID: 20250612_162203
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
import random
import asyncio
import os

# Create a bot instance with specified command prefix
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load the bot token from an environment variable
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# List to track giveaway participants
participants = []

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f'Logged in as {bot.user}!')

@bot.command(name='start_giveaway')
@commands.has_permissions(manage_messages=True)
async def start_giveaway(ctx, duration: int, *, prize: str):
    """
    Starts a giveaway in the current channel.
    
    Args:
        ctx: The context in which the command is called.
        duration: Duration of the giveaway in seconds.
        prize: The prize for the giveaway.
    """
    global participants
    participants = []  # Reset participants list for each giveaway

    # Notify the channel about the giveaway
    giveaway_message = await ctx.send(f"🎉 **Giveaway!** 🎉\nPrize: {prize}\nReact with 🎉 to enter!\nThis giveaway will end in {duration} seconds.")
    
    # Adding reaction for users to react and enter the giveaway
    await giveaway_message.add_reaction('🎉')

    # Wait for the duration of the giveaway
    await asyncio.sleep(duration)

    # Fetch the message again to get reactions
    giveaway_message = await ctx.channel.fetch_message(giveaway_message.id)
    
    # Get users who reacted
    users = await giveaway_message.reactions[0].users().flatten()
    users.remove(bot.user)  # Remove the bot from the participants

    if users:
        winner = random.choice(users)  # Randomly select a winner
        await ctx.send(f"🎉 Congratulations {winner.mention}! You have won **{prize}**!")
    else:
        await ctx.send("No participants joined the giveaway.")

@bot.command(name='cancel_giveaway')
@commands.has_permissions(manage_messages=True)
async def cancel_giveaway(ctx):
    """
    Cancels an ongoing giveaway.
    
    Args:
        ctx: The context in which the command is called.
    """
    global participants
    participants = []  # Clear the participants list
    await ctx.send("The giveaway has been cancelled.")

@start_giveaway.error
async def start_giveaway_error(ctx, error):
    """Handles errors for the start_giveaway command."""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to start a giveaway.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please provide a valid duration in seconds and a prize.")
    else:
        await ctx.send("An error occurred while starting the giveaway.")

@bot.command(name='participants')
async def participants_list(ctx):
    """
    Lists the current participants in the giveaway.
    
    Args:
        ctx: The context in which the command is called.
    """
    if participants:
        await ctx.send(f"Current participants: {', '.join([user.mention for user in participants])}")
    else:
        await ctx.send("No participants currently.")

# Run the bot with the provided token
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Failed to start the bot: {e}")
```

**Note**: Make sure to set the environment variable `DISCORD_BOT_TOKEN` with your bot token before running this code.
