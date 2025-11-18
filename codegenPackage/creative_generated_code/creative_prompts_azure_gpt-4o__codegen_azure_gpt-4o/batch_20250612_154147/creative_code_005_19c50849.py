"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m2bob.shop
Prompt: Suggest methods to integrate M2Bob with Discord for real-time monitoring and communication, referencing the Discord server mentioned on the M2Bob website.
Generated: DETERMINISTIC_19c50849b1cc7fb1
Batch ID: 20250612_154147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for integrating M2Bob with Discord using Discord's bot API (`discord.py`). This implementation monitors M2Bob logs/output and communicates updates to a Discord channel in real-time.

```python
import discord
from discord.ext import tasks
import os

# Discord Bot Token (replace with your bot token)
DISCORD_TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Discord Channel ID where messages will be sent
CHANNEL_ID = 123456789012345678  # Replace with your channel ID

# Path to M2Bob log file (replace with the actual path)
LOG_FILE_PATH = 'path/to/m2bob/log.txt'

# Create the Discord bot client
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
client = discord.Client(intents=intents)

# Variable to track the last read position in the log file
last_position = 0


@client.event
async def on_ready():
    """
    Event triggered once the bot is ready and connected to Discord.
    """
    print(f"Bot connected as {client.user}")
    # Start the task to monitor M2Bob logs
    monitor_logs.start()


@tasks.loop(seconds=5)  # Check logs every 5 seconds
async def monitor_logs():
    """
    Periodically monitors the M2Bob log file for new entries and sends messages
    to the specified Discord channel.
    """
    global last_position

    try:
        # Check if the log file exists
        if not os.path.exists(LOG_FILE_PATH):
            print(f"Log file not found: {LOG_FILE_PATH}")
            return

        # Open the log file and read new lines since the last position
        with open(LOG_FILE_PATH, 'r', encoding='utf-8') as log_file:
            log_file.seek(last_position)  # Move to the last read position
            new_lines = log_file.readlines()  # Read new lines
            last_position = log_file.tell()  # Update position

        # If there are new lines, send them to the Discord channel
        if new_lines:
            channel = client.get_channel(CHANNEL_ID)  # Get the channel object
            if channel:
                for line in new_lines:
                    # Send each new line as a message
                    await channel.send(f"[M2Bob Log] {line.strip()}")

    except Exception as e:
        # Log any errors encountered during monitoring
        print(f"Error while monitoring logs: {e}")


@client.event
async def on_error(event, *args, **kwargs):
    """
    Handle unexpected errors globally for the bot.
    """
    print(f"An error occurred during the {event} event: {args} {kwargs}")


# Run the bot
if __name__ == '__main__':
    try:
        client.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"Failed to start the bot: {e}")
```

### Notes:
1. Replace `YOUR_DISCORD_BOT_TOKEN` and `CHANNEL_ID` with the actual bot token and channel ID from your Discord server.
2. Update `LOG_FILE_PATH` with the correct path to the M2Bob log file on your system.
3. Ensure necessary permissions for the bot in your Discord server (e.g., permission to send messages in the specified channel).
4. Install the required library via `pip install discord.py`.

This code adheres to best practices and includes proper error handling.
