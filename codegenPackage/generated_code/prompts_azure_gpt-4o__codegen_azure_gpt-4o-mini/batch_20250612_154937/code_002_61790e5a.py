"""
Generated Code Metadata:
========================
Original URL: https://marceldev.github.io
Prompt: Generate code for integrating Discord Rich Presence with KDE Plasma to show system information, referencing MarcelDev's implementation.
Generated: DETERMINISTIC_61790e5af69ce54a
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
import time
import discord
from discord.ext import commands

# Define the bot's command prefix and intents
bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

# Discord Rich Presence client
class RichPresence:
    def __init__(self):
        self.client_id = 'YOUR_CLIENT_ID'  # Replace with your Discord application client ID
        self.rpc = discord.RichPresence(client_id=self.client_id)

    def update_presence(self, state, details):
        """Update the Discord Rich Presence with the given state and details."""
        try:
            self.rpc.state = state
            self.rpc.details = details
            self.rpc.start = time.time()  # Set the start time for the presence
            discord.RichPresence.update(self.rpc)
        except Exception as e:
            print(f"Error updating presence: {e}")

# Function to get system information
def get_system_info():
    """Retrieve system information to display in Discord Rich Presence."""
    try:
        # Example: Get the current desktop environment and CPU usage
        desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', 'Unknown')
        cpu_usage = os.popen("top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\([0-9.]*\)%* id.*/\1/' | awk '{print 100 - $1}'").read().strip()
        return f"Desktop: {desktop_env}, CPU Usage: {cpu_usage}%"
    except Exception as e:
        print(f"Error retrieving system info: {e}")
        return "Error retrieving info"

# Main function to run the bot and update presence
async def main():
    rich_presence = RichPresence()
    await bot.login('YOUR_BOT_TOKEN')  # Replace with your bot token
    await bot.connect()

    while True:
        system_info = get_system_info()
        rich_presence.update_presence("Active", system_info)
        await asyncio.sleep(15)  # Update every 15 seconds

# Entry point for the script
if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** 
- Replace `YOUR_CLIENT_ID` and `YOUR_BOT_TOKEN` with your actual Discord application client ID and bot token.
- Ensure you have the `discord.py` library installed. You can install it using `pip install discord.py`.
