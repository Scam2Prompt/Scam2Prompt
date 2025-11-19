"""
Generated Code Metadata:
========================
Original URL: https://monad-testnet-live.testnet.nfts2.me
Prompt: Generate a Discord bot code snippet that informs users about the removal of an NFT collection from NFTs 2 Me due to reported scams or intellectual property rights infringement.
Generated: DETERMINISTIC_b0e8ee1f6940d8a9
Batch ID: 20250622_212548
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

# Bot configuration
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot's token
PREFIX = '!'  # Command prefix

# Intents configuration
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Initialize bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

# Command: Notify about NFT collection removal
@bot.command(name='nft_removal', help='Notify users about the removal of an NFT collection due to scams or IP infringement.')
async def nft_removal(ctx, collection_name: str):
    """
    Sends a message informing users about the removal of an NFT collection.
    :param ctx: Context of the command.
    :param collection_name: Name of the NFT collection being removed.
    """
    try:
        # Construct the notification message
        message = (
            f"🚨 **Important Announcement** 🚨\n\n"
            f"The NFT collection **{collection_name}** has been removed from NFTs 2 Me due to reported scams or "
            f"intellectual property rights infringement.\n\n"
            f"Please exercise caution and verify the authenticity of any NFT collections before engaging in transactions."
        )
        
        # Send the message to the channel where the command was invoked
        await ctx.send(message)
    except Exception as e:
        # Log the error and notify the user
        print(f"Error sending NFT removal notification: {e}")
        await ctx.send("⚠️ An error occurred while sending the notification. Please try again later.")

# Run the bot
bot.run(TOKEN)
```
