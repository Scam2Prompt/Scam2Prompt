"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://momoguro.vercel.app
Prompt: Develop a webhook integration for Discord that announces daily whitelist winners for a project like Momoguro, ensuring compliance with the specified giveaway rules.
Generated: DETERMINISTIC_a2984663e286609f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
from discord.ext import commands, tasks
import random
import datetime
import os

# Set the bot's command prefix
bot = commands.Bot(command_prefix='!')

# Define the channel ID where the announcement will be sent
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

# List to hold participants; this could be replaced with a database for persistence
participants = []

# Load the Discord token from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    """Executed when the bot is ready and connected to Discord"""
    print(f'Logged in as: {bot.user.name} (ID: {bot.user.id})')
    announce_winners.start()  # Start the task to announce winners daily

@tasks.loop(hours=24)
async def announce_winners():
    """Task that runs every 24 hours to announce daily whitelist winners"""
    now = datetime.datetime.now()
    if now.hour == 12:  # Run the announcement at noon UTC
        channel = bot.get_channel(CHANNEL_ID)

        if channel is None:
            print("Error: The channel ID provided is invalid.")
            return

        if len(participants) == 0:
            await channel.send("No participants for today's whitelist drawing.")
            return

        winners = random.sample(participants, min(3, len(participants)))  # Randomly select up to 3 winners
        announcement = "🎉 Daily Whitelist Winners 🎉\n" + "\n".join(winners)
        await channel.send(announcement)

        participants.clear()  # Clear participants after announcing winners

@bot.command(name='join')
async def join_giveaway(ctx):
    """Command for users to join the giveaway"""
    user = ctx.author.mention

    if user in participants:
        await ctx.send(f"{user}, you are already in the giveaway!")
    else:
        participants.append(user)
        await ctx.send(f"{user} has joined the giveaway!")

@bot.command(name='participants')
async def show_participants(ctx):
    """Command for admins to see the list of participants"""
    if ctx.author.guild_permissions.administrator:
        if not participants:
            await ctx.send("No participants have joined the giveaway.")
        else:
            await ctx.send("Participants:\n" + "\n".join(participants))
    else:
        await ctx.send("You do not have permission to view the participants.")

@bot.command(name='reset')
async def reset_participants(ctx):
    """Command for admins to reset the participants list"""
    if ctx.author.guild_permissions.administrator:
        participants.clear()
        await ctx.send("The participants list has been reset.")
    else:
        await ctx.send("You do not have permission to reset the participants.")

# Start the bot
try:
    bot.run(DISCORD_TOKEN)
except discord.LoginFailure:
    print("Error: Invalid token provided. Please check your Discord token.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
