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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFTModerationBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        
    async def on_ready(self):
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('------')

    async def send_collection_removal_notice(self, channel_id: int, collection_name: str, removal_reason: str):
        """Send a notification about NFT collection removal."""
        try:
            channel = self.get_channel(channel_id)
            if channel is None:
                logger.error(f"Channel with ID {channel_id} not found")
                return

            embed = discord.Embed(
                title="⚠️ NFT Collection Removal Notice",
                description=f"The NFT collection **{collection_name}** has been removed from NFTs 2 Me.",
                color=discord.Color.orange()
            )
            
            embed.add_field(
                name="Reason for Removal",
                value=removal_reason,
                inline=False
            )
            
            embed.add_field(
                name="Additional Information",
                value="If you believe this is a mistake, please contact our support team.",
                inline=False
            )
            
            embed.set_footer(text="NFTs 2 Me Moderation Team")
            
            await channel.send(embed=embed)
            logger.info(f"Sent removal notice for {collection_name} to channel {channel_id}")
            
        except discord.Forbidden:
            logger.error(f"Bot doesn't have permissions to send messages in channel {channel_id}")
        except discord.HTTPException as e:
            logger.error(f"Failed to send message to channel {channel_id}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error sending removal notice: {e}")

# Example usage
if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = NFTModerationBot(command_prefix='!', intents=intents)
    
    # Replace with your actual bot token
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    # Example of how to trigger the notice
    # bot.loop.create_task(bot.send_collection_removal_notice(
    #     channel_id=1234567890,
    #     collection_name="FakeNFTs",
    #     removal_reason="Reported scams and intellectual property rights infringement"
    # ))
    
    bot.run(BOT_TOKEN)
```
