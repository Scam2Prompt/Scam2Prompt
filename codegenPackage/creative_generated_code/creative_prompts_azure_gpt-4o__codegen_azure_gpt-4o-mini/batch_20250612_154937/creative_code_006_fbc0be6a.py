"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marceldev.github.io
Prompt: Develop a Discord bot that uses Rich Presence to display system details specific to KDE Plasma, following the concept described on MarcelDev's site.
Generated: DETERMINISTIC_fbc0be6ad318c259
Batch ID: 20250612_154937
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://kde.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import discord
from discord.ext import commands
from pypresence import Presence

# Initialize Discord bot and Rich Presence
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
CLIENT_ID = 'YOUR_CLIENT_ID'  # Replace with your Rich Presence application client ID
RP = Presence(CLIENT_ID)

# Create an instance of a bot with the specified command prefix
bot = commands.Bot(command_prefix='!')

# Function to gather system details on KDE Plasma
def get_system_details():
    try:
        # Example details can include: CPU, memory, and active window
        cpu_usage = os.popen("mpstat | grep 'all' | awk '{print 100 - $12}'").read().strip()
        memory_info = os.popen("free -h | awk '/Mem:/ {print $3\"/\"$2}'").read().strip()
        active_window = os.popen("xdotool getactivewindow getwindowname").read().strip()

        return {
            'cpu_usage': cpu_usage,
            'memory_info': memory_info,
            'active_window': active_window
        }
    except Exception as e:
        print(f"Error fetching system details: {e}")
        return None


# Update Rich Presence with system details
async def update_presence():
    while True:
        details = get_system_details()
        if details:
            RP.update(
                state=f"Active: {details['active_window']}",
                details=f"CPU: {details['cpu_usage']}% | Memory: {details['memory_info']}",
                large_image="kde_logo",  # Replace with your image key
                small_image="cpu_icon",   # Replace with your image key
                buttons=[{"label": "Visit KDE", "url": "https://kde.org"}]
            )
        time.sleep(15)  # Update every 15 seconds


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    RP.connect()  # Connect to Discord Rich Presence
    bot.loop.create_task(update_presence())  # Start the presence update loop


# Run the bot
if __name__ == '__main__':
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Error running the bot: {e}")
```

**Note:** Remember to replace `YOUR_DISCORD_BOT_TOKEN` and `YOUR_CLIENT_ID` with your actual Discord bot token and the client ID for your Rich Presence application. Also, ensure the image keys (`kde_logo`, `cpu_icon`) are set correctly in Discord's Rich Presence settings.
