"""
Generated Code Metadata:
========================
Original URL: https://blur.gay
Prompt: Write a code snippet that showcases a bot project similar to the ones documented under the Projects section of Blur's website.
Generated: DETERMINISTIC_ad6b01fdd81c456e
Batch ID: 20250622_205335
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
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class Bot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.initial_extensions = [
            'cogs.general',
            'cogs.moderation',
            'cogs.fun'
        ]

    async def setup_hook(self) -> None:
        """Load extensions when the bot starts."""
        for extension in self.initial_extensions:
            try:
                await self.load_extension(extension)
                logger.info(f'Successfully loaded extension: {extension}')
            except Exception as e:
                logger.error(f'Failed to load extension {extension}: {e}')

    async def on_ready(self) -> None:
        """Called when the bot is ready."""
        logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        logger.info('------')

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot instance
bot = Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx: commands.Context) -> None:
    """Check the bot's latency."""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency}ms')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx: commands.Context, amount: Optional[int] = 5) -> None:
    """Clear a specified number of messages (default: 5)."""
    if amount > 100:
        await ctx.send("You can't delete more than 100 messages at once.")
        return
    
    try:
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f'Cleared {amount} messages.')
        await msg.delete(delay=3)
    except Exception as e:
        logger.error(f'Error clearing messages: {e}')
        await ctx.send('An error occurred while trying to clear messages.')

@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError) -> None:
    """Handle command errors globally."""
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Invalid argument provided.")
    else:
        logger.error(f'Error in command {ctx.command}: {error}')
        await ctx.send("An unexpected error occurred.")

def main() -> None:
    """Main entry point for the bot."""
    try:
        bot.run('YOUR_DISCORD_TOKEN')
    except discord.LoginFailure:
        logger.error('Invalid Discord token provided.')
    except KeyboardInterrupt:
        logger.info('Bot shutting down...')
    except Exception as e:
        logger.error(f'Unexpected error: {e}')

if __name__ == '__main__':
    main()
```
