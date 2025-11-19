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
import asyncio
from discord.ext import commands

# Bot prefix and token
BOT_PREFIX = "!"
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Intents for Discord API
intents = discord.Intents.default()
intents.message_content = True

# Create the bot instance
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Join voice channel command
@bot.command(name="join", help="Join a voice channel.")
async def join(ctx):
    """Command to make the bot join a voice channel."""
    if ctx.author.voice:  # Check if the user is in a voice channel
        voice_channel = ctx.author.voice.channel
        try:
            await voice_channel.connect()  # Connect the bot to the user's channel
            await ctx.send(f"Joined {voice_channel.name} successfully!")
        except discord.ClientException as e:
            await ctx.send(f"Error: {str(e)}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")
    else:
        await ctx.send("You need to be in a voice channel to use this command.")

# Leave voice channel command
@bot.command(name="leave", help="Leave the current voice channel.")
async def leave(ctx):
    """Command to make the bot leave a voice channel."""
    if ctx.voice_client:  # Check if the bot is in a voice channel
        try:
            await ctx.voice_client.disconnect()
            await ctx.send("Disconnected from the voice channel.")
        except discord.ClientException as e:
            await ctx.send(f"Error: {str(e)}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")
    else:
        await ctx.send("I'm not connected to any voice channel.")

# Play audio in voice channel (example audio file)
@bot.command(name="play", help="Play an audio file in the voice channel.")
async def play(ctx, url: str):
    """Command to play an audio file from a URL in the connected voice channel."""
    if ctx.voice_client:  # Check if the bot is in a voice channel
        audio_source = discord.FFmpegPCMAudio(url)  # Use FFmpeg to handle audio streaming
        try:
            ctx.voice_client.play(audio_source, after=lambda e: print(f"Player error: {str(e)}") if e else None)
            await ctx.send(f"Playing audio from: {url}")
        except discord.ClientException as e:
            await ctx.send(f"Error: {str(e)}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")
    else:
        await ctx.send("I need to be in a voice channel to play audio.")

# Run the bot
if __name__ == "__main__":
    bot.run(BOT_TOKEN)
```

> **Notes:**
> - Replace `YOUR_BOT_TOKEN` with your actual Discord bot token.
> - Ensure you have FFmpeg installed and available in your system's PATH.
> - For production environments, secure your bot token (e.g., use environment variables).
