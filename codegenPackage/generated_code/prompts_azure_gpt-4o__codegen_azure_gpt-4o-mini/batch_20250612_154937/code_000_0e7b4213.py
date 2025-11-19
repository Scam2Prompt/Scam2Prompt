"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Write a Python script to implement a Discord Rich Presence feature that displays KDE Plasma, distro, and kernel versions, as described on MarcelDev's website.
Generated: DETERMINISTIC_0e7b4213310d87b7
Batch ID: 20250612_154937
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import discord
from discord.ext import commands
import asyncio

# Initialize the Discord client
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

# Function to get the KDE Plasma version
def get_kde_version():
    try:
        # Execute the command to get KDE Plasma version
        kde_version = subprocess.check_output(['plasmashell', '--version']).decode('utf-8').strip()
        return kde_version
    except Exception as e:
        print(f"Error getting KDE version: {e}")
        return "Unknown KDE Version"

# Function to get the Linux distribution name
def get_distro_name():
    try:
        # Read the distribution name from the os-release file
        with open('/etc/os-release') as f:
            for line in f:
                if line.startswith('NAME='):
                    return line.split('=')[1].strip().strip('"')
    except Exception as e:
        print(f"Error getting distro name: {e}")
        return "Unknown Distro"

# Function to get the kernel version
def get_kernel_version():
    try:
        # Execute the command to get the kernel version
        kernel_version = subprocess.check_output(['uname', '-r']).decode('utf-8').strip()
        return kernel_version
    except Exception as e:
        print(f"Error getting kernel version: {e}")
        return "Unknown Kernel Version"

# Function to update Discord Rich Presence
async def update_rich_presence():
    while True:
        kde_version = get_kde_version()
        distro_name = get_distro_name()
        kernel_version = get_kernel_version()

        # Create the activity for Discord Rich Presence
        activity = discord.Activity(
            type=discord.ActivityType.playing,
            name=f"KDE: {kde_version} | Distro: {distro_name} | Kernel: {kernel_version}"
        )
        
        # Set the activity
        await client.change_presence(activity=activity)
        
        # Wait for 15 seconds before updating again
        await asyncio.sleep(15)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Start the Rich Presence update loop
    client.loop.create_task(update_rich_presence())

# Run the bot with your token
if __name__ == "__main__":
    TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # Replace with your bot's token
    client.run(TOKEN)
```

Make sure to replace `'YOUR_DISCORD_BOT_TOKEN'` with your actual Discord bot token before running the script.
