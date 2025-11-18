"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Develop a Fetch.ai microagent that connects with OpenAI and Discord APIs to provide AI-driven customer support.
Generated: DETERMINISTIC_124c73a7f9cb757e
Batch ID: 20250612_153517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://discord.com/api/v9": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.openai.com/v1/completions": {
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
"""
Fetch.ai Microagent for AI-driven customer support using OpenAI and Discord APIs.

This microagent integrates with OpenAI's API for generating responses and Discord's API for communication.
"""

# Required Libraries
import json
import requests
import aiohttp
import asyncio
from fetchai.microagents import Agent, Envelope

# Configuration Constants
DISCORD_TOKEN = "your_discord_bot_token_here"
OPENAI_API_KEY = "your_openai_api_key_here"

OPENAI_API_URL = "https://api.openai.com/v1/completions"
DISCORD_API_BASE_URL = "https://discord.com/api/v9"

DISCORD_CHANNEL_ID = "your_discord_channel_id_here"  # Replace with your target Discord channel ID

class CustomerSupportAgent(Agent):
    """
    Fetch.ai Microagent for AI-driven customer support.
    """

    async def run(self):
        """
        The main run loop of the microagent.
        """
        while True:
            await self.listen_to_discord()
            await asyncio.sleep(5)  # Poll every 5 seconds

    async def listen_to_discord(self):
        """
        Listens for new messages in the Discord channel.
        """
        headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
        url = f"{DISCORD_API_BASE_URL}/channels/{DISCORD_CHANNEL_ID}/messages"

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        messages = await response.json()
                        for message in messages:
                            if self.is_new_message(message):
                                await self.handle_message(message)
                    else:
                        print("Failed to fetch messages from Discord:", response.status, await response.text())
        except Exception as e:
            print(f"Error fetching Discord messages: {e}")

    def is_new_message(self, message):
        """
        Determines if a message is new and requires processing. 
        Currently, this function can be customized to ignore messages from the bot itself.
        """
        # Example check: Ignore messages from the bot itself
        if message.get("author", {}).get("id") == self.get_bot_user_id():
            return False
        return True

    async def handle_message(self, message):
        """
        Handles new messages from Discord.
        """
        user_message = message.get("content")
        if user_message:
            # Generate AI response via OpenAI
            ai_response = await self.generate_ai_response(user_message)

            if ai_response:
                # Send response back to Discord
                await self.send_message_to_discord(ai_response)

    async def generate_ai_response(self, user_message):
        """
        Generates a response using OpenAI's API for customer support.
        """
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "text-davinci-003",  # Replace with preferred OpenAI model
            "prompt": f"Customer support: {user_message}",
            "max_tokens": 150,
            "temperature": 0.7
        }

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(OPENAI_API_URL, json=payload) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("choices", [{}])[0].get("text").strip()
                    else:
                        print("Failed to fetch AI response:", response.status, await response.text())
                        return "Sorry, I couldn't process your request. Please try again later."
        except Exception as e:
            print(f"Error generating AI response: {e}")
            return "Sorry, there was an internal error. Please try again later."

    async def send_message_to_discord(self, message):
        """
        Sends a response message to the Discord channel.
        """
        headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
        url = f"{DISCORD_API_BASE_URL}/channels/{DISCORD_CHANNEL_ID}/messages"
        payload = {"content": message}

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        print("Failed to send message to Discord:", response.status, await response.text())
        except Exception as e:
            print(f"Error sending message to Discord: {e}")

    def get_bot_user_id(self):
        """
        Fetches the bot's user ID from Discord API.
        """
        headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
        url = f"{DISCORD_API_BASE_URL}/users/@me"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data.get("id")
        except Exception as e:
            print(f"Error fetching bot user ID: {e}")

        return None


if __name__ == "__main__":
    # Instantiate and run the customer support microagent
    agent = CustomerSupportAgent()
    asyncio.run(agent.run())
```
