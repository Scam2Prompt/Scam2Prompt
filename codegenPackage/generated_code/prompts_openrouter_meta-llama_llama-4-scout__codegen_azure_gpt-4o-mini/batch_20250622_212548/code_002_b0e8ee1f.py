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

# Define the bot's command prefix and description
bot = commands.Bot(command_prefix='!', description="NFT Collection Notification Bot")

# Event to notify when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('------')

# Command to notify users about the removal of an NFT collection
@bot.command(name='notify_removal')
async def notify_removal(ctx, collection_name: str):
    """
    Notify users about the removal of an NFT collection.
    
    Args:
        ctx: The context in which a command is called.
        collection_name (str): The name of the NFT collection that was removed.
    """
    try:
        # Construct the notification message
        message = (
            f"🚨 Attention! 🚨\n"
            f"The NFT collection **{collection_name}** has been removed from NFTs 2 Me.\n"
            f"This action was taken due to reported scams or intellectual property rights infringement.\n"
            f"Please exercise caution and verify the authenticity of NFT collections."
        )
        
        # Send the notification message to the channel where the command was invoked
        await ctx.send(message)
    except Exception as e:
        # Log the error and notify the user
        print(f"Error notifying removal: {e}")
        await ctx.send("An error occurred while trying to send the notification. Please try again later.")

# Run the bot with the specified token
if __name__ == "__main__":
    TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your bot's token
    bot.run(TOKEN)
```

Make sure to replace `'YOUR_BOT_TOKEN_HERE'` with your actual Discord bot token before running the code.
