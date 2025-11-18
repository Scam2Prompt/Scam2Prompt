"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Create a Python script that retrieves and displays kernel version information for use in a Discord Rich Presence integration, inspired by MarcelDev's project.
Generated: DETERMINISTIC_eab7580e31569cad
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys
import discord
from discord.ext import commands

# Set up the bot with command prefix
bot = commands.Bot(command_prefix='!')

def get_kernel_version():
    """
    Retrieves the current kernel version of the operating system.

    Returns:
        str: The kernel version string.
    """
    try:
        # Execute the 'uname -r' command to get the kernel version
        kernel_version = subprocess.check_output(['uname', '-r'], stderr=subprocess.STDOUT)
        return kernel_version.decode().strip()
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving kernel version: {e.output.decode()}")
        return "Unknown Kernel Version"

@bot.event
async def on_ready():
    """
    Sets the Discord Rich Presence status when the bot is ready.
    """
    kernel_version = get_kernel_version()
    activity = discord.Game(name=f"Kernel Version: {kernel_version}")
    
    # Update the bot's presence
    await bot.change_presence(activity=activity)
    print(f"Bot is online and displaying kernel version: {kernel_version}")

@bot.command()
async def kernel(ctx):
    """
    Command to retrieve and display the kernel version in Discord chat.

    Args:
        ctx: The context of the command invocation.
    """
    kernel_version = get_kernel_version()
    await ctx.send(f"Current Kernel Version: {kernel_version}")

# Replace 'YOUR_BOT_TOKEN' with your actual Discord bot token
if __name__ == "__main__":
    try:
        bot.run('YOUR_BOT_TOKEN')
    except Exception as e:
        print(f"Failed to run the bot: {e}")
        sys.exit(1)
```
