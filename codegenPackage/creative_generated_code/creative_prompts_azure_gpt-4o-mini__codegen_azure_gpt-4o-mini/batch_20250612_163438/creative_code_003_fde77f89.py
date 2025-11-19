"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discordapp.ir
Prompt: Generate a code snippet for integrating Discord's voice chat capabilities, focusing on low latency and high quality as discussed on Discordapp.ir.
Generated: DETERMINISTIC_fde77f89cccae8ee
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

# Define the bot with a command prefix
intents = discord.Intents.default()
intents.voice_states = True  # Enable voice state intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """This event triggers when the bot has successfully connected to Discord."""
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def join(ctx):
    """Command to make the bot join the voice channel the user is in."""
    # Check if the user is in a voice channel
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()  # Connect to the voice channel
        await ctx.send(f'Joined {channel}')
    else:
        await ctx.send("You're not in a voice channel!")

@bot.command()
async def leave(ctx):
    """Command to make the bot leave the voice channel."""
    # Check if the bot is in a voice channel
    if ctx.voice_client:
        await ctx.voice_client.disconnect()  # Disconnect from the voice channel
        await ctx.send("Left the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel!")

@bot.command()
async def play(ctx, url: str):
    """Command to play audio from a URL in the voice channel."""
    if ctx.voice_client is None:
        await ctx.send("I need to be in a voice channel to play audio.")
        return
    
    # Ensure the bot is connected to a voice channel
    if not ctx.voice_client.is_connected():
        await ctx.send("I'm not connected to a voice channel.")
        return
    
    # Attempt to play the audio from the given URL
    try:
        ctx.voice_client.play(discord.FFmpegPCMAudio(url))
        await ctx.send(f'Now playing: {url}')
    except Exception as e:
        await ctx.send(f'Error occurred while trying to play audio: {str(e)}')

@bot.command()
async def stop(ctx):
    """Command to stop playing audio."""
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()  # Stop the audio currently playing
        await ctx.send("Stopped playing audio.")
    else:
        await ctx.send("I'm not playing any audio.")

# Error handling for commands
@play.error
async def play_error(ctx, error):
    """Handles errors for the play command."""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a URL to play audio.")
    else:
        await ctx.send("An error occurred while processing your request.")

# Add your bot token here
TOKEN = 'YOUR_BOT_TOKEN'

# Run the bot
bot.run(TOKEN)
```

**Note:** Replace `'YOUR_BOT_TOKEN'` with your actual Discord bot token. Make sure to have `discord.py` installed and to enable the voice intents in your Discord developer portal settings for the bot.
