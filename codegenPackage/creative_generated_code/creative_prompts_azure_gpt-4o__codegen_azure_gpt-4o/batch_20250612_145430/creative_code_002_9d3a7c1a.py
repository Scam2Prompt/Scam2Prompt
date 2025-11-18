"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-pals.vercel.app
Prompt: Write code to integrate a Discord API for community engagement, similar to Phantom Pals' use of Discord for user interaction.
Generated: DETERMINISTIC_9d3a7c1ac61def36
Batch ID: 20250612_145430
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
import os
from dotenv import load_dotenv

# Load environment variables from a .env file for security
load_dotenv()

# Retrieve the bot token from the environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Check if the token is provided
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is missing from your environment variables")

# Intents define what events the bot can listen to
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Triggered when the bot is ready and connected to Discord
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}!")
    print("Ready to engage with the community!")

# Event: Welcome a new user to the server
@bot.event
async def on_member_join(member):
    guild = member.guild

    # Check if the bot has the permissions to send messages
    if guild.system_channel is not None:
        welcome_message = f"Welcome to {guild.name}, {member.mention}! 🎉 Feel free to introduce yourself!"
        await guild.system_channel.send(welcome_message)

# Command: Simple ping-pong interaction for testing responsiveness
@bot.command(name="ping", help="Check the bot's latency.")
async def ping(ctx):
    latency = round(bot.latency * 1000)  # Convert latency to milliseconds
    await ctx.send(f"Pong! Latency: {latency}ms")

# Command: Broadcast an announcement (admin-only)
@bot.command(name="announce", help="Broadcast an announcement to the community (Admin only).")
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message: str):
    # Send the announcement in the current channel
    await ctx.send(f"📢 Announcement: {message}")

# Error handler for the announce command
@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You do not have permission to use this command.")
    else:
        await ctx.send("An error occurred while processing the announcement command.")

# Command: Get a list of server members
@bot.command(name="members", help="List all members in the server.")
async def members(ctx):
    member_list = "\n".join([member.name for member in ctx.guild.members])
    await ctx.send(f"👥 Members in the server:\n{member_list}")

# Command: Create a poll
@bot.command(name="poll", help="Create a poll for the community (Usage: !poll Question | Option1 | Option2 | ...).")
async def poll(ctx, *, content: str):
    try:
        options = content.split("|")
        question = options[0].strip()
        choices = [option.strip() for option in options[1:]]

        # Ensure there are at least 2 choices for the poll
        if len(choices) < 2:
            await ctx.send("❌ A poll must have at least two options.")
            return

        # Format the poll message
        poll_message = f"📊 **{question}**\n\n"
        emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
        for idx, choice in enumerate(choices):
            if idx < len(emoji_numbers):  # Add choices only if they fit within the emoji limits
                poll_message += f"{emoji_numbers[idx]} {choice}\n"

        # Send the poll message
        message = await ctx.send(poll_message)

        # React to the poll message with the appropriate emojis
        for idx in range(len(choices)):
            if idx < len(emoji_numbers):
                await message.add_reaction(emoji_numbers[idx])

    except Exception as e:
        await ctx.send("❌ An error occurred while trying to create the poll.")
        print(f"Error in poll command: {e}")

# Error handling for general command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Command not found. Use `!help` to see the available commands.")
    else:
        await ctx.send("An unexpected error occurred. Please try again later.")
        print(f"Unexpected error: {error}")

# Run the bot
try:
    bot.run(DISCORD_TOKEN)
except Exception as e:
    print(f"Failed to run the bot: {e}")
```
