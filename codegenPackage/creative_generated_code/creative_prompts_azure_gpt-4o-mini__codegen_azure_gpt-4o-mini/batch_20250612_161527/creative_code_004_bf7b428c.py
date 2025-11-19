"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Can you recommend libraries or APIs for creating Discord integrations, specifically for showing system information like on MarcelDev's page?
Generated: DETERMINISTIC_bf7b428cac4d1486
Batch ID: 20250612_161527
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
import psutil  # For system information
import platform  # To get the platform information
import logging

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO)

# Create an instance of a bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Event that triggers when the bot is ready."""
    logging.info(f'Logged in as {bot.user.name} - {bot.user.id}')
    print(f'Bot is ready!')

@bot.command(name='systeminfo')
async def system_info(ctx):
    """Command to show system information."""
    try:
        # Gather system information
        uname = platform.uname()
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        total_memory = memory_info.total // (1024 * 1024)  # Convert bytes to MB
        used_memory = memory_info.used // (1024 * 1024)  # Convert bytes to MB

        # Create a formatted response
        info_message = (
            f"**System Information**\n"
            f"**System:** {uname.system} {uname.release}\n"
            f"**Node Name:** {uname.node}\n"
            f"**Processor:** {uname.processor}\n"
            f"**CPU Usage:** {cpu_usage}%\n"
            f"**Memory Usage:** {used_memory}/{total_memory} MB ({memory_usage}%)"
        )

        # Send the system information as a message
        await ctx.send(info_message)

    except Exception as e:
        logging.error(f'Error retrieving system info: {e}')
        await ctx.send('An error occurred while retrieving system information.')

# Run the bot with your token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
if __name__ == '__main__':
    try:
        bot.run('YOUR_BOT_TOKEN')
    except discord.LoginFailure:
        logging.error('Invalid token. Please check your bot token.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
