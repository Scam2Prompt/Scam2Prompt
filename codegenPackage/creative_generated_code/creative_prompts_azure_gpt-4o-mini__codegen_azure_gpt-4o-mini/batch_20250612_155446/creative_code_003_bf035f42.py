"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marian-314.pages.dev
Prompt: Create a code snippet that utilizes Meowbin Doxbin to log user activity in a Discord channel.
Generated: DETERMINISTIC_bf035f426d07ffbf
Batch ID: 20250612_155446
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
import logging

# Setting up logging for the bot
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a bot instance with the specified command prefix
bot = commands.Bot(command_prefix='!')

# This event triggers when the bot is ready
@bot.event
async def on_ready():
    logging.info(f'Bot has logged in as {bot.user}')

# This event triggers when a message is sent in any channel the bot can access
@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return
    
    # Log the user activity
    log_user_activity(message)

    # Process commands if any are present in the message
    await bot.process_commands(message)

def log_user_activity(message):
    """
    Logs user activity to a file.
    
    Parameters:
        message (discord.Message): The message object containing user activity details.
    """
    try:
        with open('user_activity.log', 'a') as log_file:
            log_entry = f'{message.created_at} - {message.author} - {message.content}\n'
            log_file.write(log_entry)
            logging.info(f'Logged message from {message.author}: {message.content}')
    except Exception as e:
        logging.error(f'Failed to log message: {e}')

# Run the bot with the specified token
if __name__ == "__main__":
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
    try:
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f'Error starting the bot: {e}')
```

**Note**: Replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual Discord bot token. Make sure to have the necessary permissions for the bot to read messages in the channels you intend to log. This code snippet assumes you have the `discord.py` library installed (`pip install discord.py`).
