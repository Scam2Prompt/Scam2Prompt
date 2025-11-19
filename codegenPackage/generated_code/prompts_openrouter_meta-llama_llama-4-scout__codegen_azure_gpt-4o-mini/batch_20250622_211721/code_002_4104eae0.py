"""
Generated Code Metadata:
========================
Original URL: https://soulfn.lol
Prompt: Generate a Discord bot code that can handle reseller inquiries for Soul's gaming accounts and software products.
Generated: DETERMINISTIC_4104eae0ca9ba9c6
Batch ID: 20250622_211721
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

# Set up logging for the bot
logging.basicConfig(level=logging.INFO)

# Define the bot's command prefix and description
bot = commands.Bot(command_prefix='!', description="Soul's Gaming Reseller Inquiry Bot")

# Event: When the bot is ready
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logging.info('------')

# Command: Handle reseller inquiries
@bot.command(name='inquiry', help='Submit a reseller inquiry for Soul\'s gaming accounts and software products.')
async def inquiry(ctx, *, message: str):
    """Handles reseller inquiries by sending a message to a designated channel."""
    try:
        # Define the channel ID where inquiries will be sent
        inquiry_channel_id = 123456789012345678  # Replace with your channel ID
        inquiry_channel = bot.get_channel(inquiry_channel_id)

        if inquiry_channel is None:
            await ctx.send("Error: Inquiry channel not found.")
            logging.error("Inquiry channel not found.")
            return

        # Send the inquiry message to the designated channel
        await inquiry_channel.send(f"New inquiry from {ctx.author.mention}: {message}")
        await ctx.send("Your inquiry has been submitted successfully!")
        logging.info(f"Inquiry submitted by {ctx.author.name}: {message}")

    except Exception as e:
        await ctx.send("An error occurred while processing your inquiry. Please try again later.")
        logging.error(f"Error processing inquiry: {e}")

# Command: Help command to list available commands
@bot.command(name='help', help='List all available commands.')
async def help_command(ctx):
    """Sends a list of available commands to the user."""
    help_message = """
    **Available Commands:**
    - `!inquiry <message>`: Submit a reseller inquiry for Soul's gaming accounts and software products.
    - `!help`: List all available commands.
    """
    await ctx.send(help_message)

# Run the bot with the specified token
if __name__ == "__main__":
    TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your bot's token
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Failed to run the bot: {e}")
```

Make sure to replace `YOUR_BOT_TOKEN` with your actual Discord bot token and `123456789012345678` with the actual channel ID where you want to send inquiries.
