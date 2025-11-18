"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-alliance.com
Prompt: Write Python code to integrate Fetch.ai microagents with Discord for real-time notifications and task updates.
Generated: DETERMINISTIC_a174465b8d5c32e8
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import discord
from fetchai.microagents import Agent, Connection, LedgerApi
import asyncio

# Discord Bot Configuration
DISCORD_TOKEN = 'your_discord_bot_token'
DISCORD_CHANNEL_ID = your_discord_channel_id  # Replace with the ID of the target channel

# Fetch.ai Microagent Configuration
FETCHAI_PKEY = 'your_fetchai_private_key'
FETCHAI_CONNECTION = 'fetchai_mainnet_or_testnet_endpoint'
FETCHAI_AGENT_NAME = 'your_agent_name'

# Initialize Discord Client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Define Handler for Fetch.ai Microagent
class FetchAgent(Agent):
    def __init__(self, connection: Connection, name: str):
        super().__init__(connection, name)
        self.name = name

    async def on_message(self, msg: str):
        """
        Callback to handle incoming messages to the microagent.
        Sends the message to Discord for notification.
        """
        try:
            await send_to_discord(f"Microagent Notification:\n{msg}")
        except Exception as e:
            print(f"Failed to send message to Discord: {str(e)}")

async def send_to_discord(message: str):
    """
    Sends a message to the specified Discord channel.
    """
    try:
        channel = client.get_channel(DISCORD_CHANNEL_ID)
        if channel:
            await channel.send(message)
        else:
            print("Discord channel not found.")
    except Exception as e:
        print(f"Error sending message to Discord: {str(e)}")

async def start_fetch_agent():
    """
    Initializes and starts the Fetch.ai microagent.
    """
    try:
        connection = LedgerApi(FETCHAI_CONNECTION)  # Create connection to Fetch.ai network
        connection.add_private_key(FETCHAI_PKEY)
        
        agent = FetchAgent(connection, FETCHAI_AGENT_NAME)
        await agent.start()
        
        print("Fetch.ai microagent is running...")
        # Simulate receiving a message (replace with actual microagent logic)
        await asyncio.sleep(5)
        await agent.on_message("Sample task update from Fetch.ai microagent.")
        
    except Exception as e:
        print(f"Error starting Fetch.ai microagent: {str(e)}")

@client.event
async def on_ready():
    """
    Event triggered when Discord bot successfully connects.
    Initiates the Fetch.ai microagent.
    """
    print(f'We have logged in as {client.user}')
    await start_fetch_agent()

# Run Discord Bot
try:
    client.run(DISCORD_TOKEN)
except Exception as e:
    print(f"Failed to run Discord bot: {str(e)}")
```
