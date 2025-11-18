"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-alliance.com
Prompt: Write code to create an AI agent using Fetch.ai's platform that integrates with Slack and Discord for team collaboration.
Generated: DETERMINISTIC_d2ae64382335360b
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from flask import Flask, request, jsonify
from slack_sdk import WebClient as SlackClient
from discord import Client as DiscordClient
from discord.ext import commands

# Load environment variables for tokens and keys
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
FETCH_AI_API_URL = os.getenv("FETCH_AI_API_URL")

# Initialize Flask app
app = Flask(__name__)

# Initialize Slack client
slack_client = SlackClient(SLACK_TOKEN)

# Initialize Discord client
discord_client = DiscordClient()

# Define command prefix for Discord bot
discord_bot = commands.Bot(command_prefix='!')

@app.route('/slack/events', methods=['POST'])
def slack_events():
    """
    Handle Slack events and commands.
    """
    data = request.json
    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})

    # Process message events
    if 'event' in data:
        event = data['event']
        if event.get('type') == 'message' and 'subtype' not in event:
            # Forward message to Fetch.ai API
            response = send_to_fetch_ai(event['text'])
            return jsonify({'status': 'message processed'})

    return jsonify({'status': 'event ignored'}), 200

@discord_bot.event
async def on_ready():
    """
    Called when the bot is ready and logged in.
    """
    print(f'Logged in as {discord_bot.user}')

@discord_bot.event
async def on_message(message):
    """
    Handle incoming messages in Discord.
    """
    # Ignore messages sent by the bot itself
    if message.author == discord_bot.user:
        return

    # Forward message to Fetch.ai API
    if message.content.startswith('!'):
        response = await send_to_fetch_ai(message.content[1:])
        await message.channel.send(response)

async def send_to_fetch_ai(message_text):
    """
    Send a message to the Fetch.ai API and return the response.
    """
    try:
        response = requests.post(FETCH_AI_API_URL, json={'message': message_text})
        response.raise_for_status()
        return response.json().get('response', 'No response from AI')
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Fetch.ai: {e}")
        return "Error processing your request."

if __name__ == '__main__':
    # Start Flask app
    app.run(port=3000)

# Run Discord bot
discord_bot.run(DISCORD_TOKEN)
```

### Requirements:
- Ensure you have the required libraries installed:
```bash
pip install Flask slack_sdk discord.py requests
```

### Environment Variables:
- Set the following environment variables before running the code:
  - `SLACK_TOKEN`: Your Slack Bot User OAuth Access Token.
  - `DISCORD_TOKEN`: Your Discord Bot Token.
  - `FETCH_AI_API_URL`: The endpoint for the Fetch.ai API.
