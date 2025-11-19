"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasorng.web.app
Prompt: What are the steps to set up a daily poker tournament feature using Discord's API for the Atlas3 community?
Generated: DETERMINISTIC_9c3160693cfae36c
Batch ID: 20250612_162716
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
from datetime import datetime, timedelta
import asyncio

# Constants
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot's token
TOURNAMENT_CHANNEL_ID = 123456789012345678  # Replace with your channel ID
TOURNAMENT_TIME = "18:00"  # Set tournament time in HH:MM format

# Create an instance of a bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    tournament_notification.start()  # Start the tournament notification loop

@tasks.loop(minutes=1)
async def tournament_notification():
    now = datetime.now()
    # Calculate the next tournament time
    tournament_time = datetime.strptime(TOURNAMENT_TIME, "%H:%M").time()
    next_tournament = datetime.combine(now.date(), tournament_time)

    # If the time for the tournament has already passed today, schedule for tomorrow
    if now.time() > tournament_time:
        next_tournament += timedelta(days=1)

    # Check if we are within one minute of the tournament time
    if now >= next_tournament - timedelta(minutes=1) and now < next_tournament:
        channel = bot.get_channel(TOURNAMENT_CHANNEL_ID)
        if channel:
            try:
                await channel.send("🔔 Reminder: A daily poker tournament will start in 1 minute! Get ready! 🃏")
            except discord.HTTPException as e:
                print(f"Failed to send message: {e}")

@tournament_notification.before_loop
async def before_tournament_notification():
    await bot.wait_until_ready()  # Wait until the bot is ready

@bot.command(name='set_time')
@commands.has_permissions(administrator=True)
async def set_time(ctx, time: str):
    """Command to set the tournament time. Format: HH:MM."""
    global TOURNAMENT_TIME
    try:
        datetime.strptime(time, "%H:%M")  # Validate time format
        TOURNAMENT_TIME = time
        await ctx.send(f"Tournament time successfully set to {TOURNAMENT_TIME}.")
    except ValueError:
        await ctx.send("Invalid time format! Please use HH:MM.")

@bot.command(name='tournament_info')
async def tournament_info(ctx):
    """Command to get information on the next tournament."""
    now = datetime.now()
    tournament_time = datetime.strptime(TOURNAMENT_TIME, "%H:%M").time()
    next_tournament = datetime.combine(now.date(), tournament_time)

    if now.time() > tournament_time:
        next_tournament += timedelta(days=1)

    await ctx.send(f"The next tournament is scheduled for {next_tournament.strftime('%Y-%m-%d %H:%M')}.")

# Error handling for commands
@set_time.error
async def set_time_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

# Run the bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"An error occurred while starting the bot: {e}")
```
