"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.web.app
Prompt: What are the steps to set up a light client for the Astar & Shiden Network in my application?
Generated: DETERMINISTIC_fe7533475d4f72bc
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import json
import websockets
import logging

# Enable logging for debugging purposes
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AstarLightClient:
    def __init__(self, url):
        """
        Initialize the light client with the given WebSocket URL.
        
        :param url: The WebSocket URL of the Astar/Shiden Network node.
        """
        self.url = url
        self.connection = None

    async def connect(self):
        """
        Establish a connection to the WebSocket server.
        """
        try:
            self.connection = await websockets.connect(self.url)
            logger.info("Connected to the Astar/Shiden Network")
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise

    async def subscribe_to_new_blocks(self):
        """
        Subscribe to new block notifications from the network.
        """
        subscribe_message = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "chain_subscribeNewHeads",
            "params": []
        }
        await self.send_message(subscribe_message)

    async def send_message(self, message):
        """
        Send a message to the WebSocket connection.
        
        :param message: The message to send.
        """
        try:
            await self.connection.send(json.dumps(message))
            logger.info(f"Message sent: {message}")
        except Exception as e:
            logger.error(f"Failed to send message: {e}")
            raise

    async def listen_for_messages(self):
        """
        Listen for incoming messages from the WebSocket connection.
        """
        try:
            while True:
                response = await self.connection.recv()
                self.handle_response(response)
        except Exception as e:
            logger.error(f"Error receiving message: {e}")
            await self.close()

    def handle_response(self, response):
        """
        Handle incoming messages from the WebSocket connection.
        
        :param response: The incoming message.
        """
        try:
            data = json.loads(response)
            logger.info(f"Received message: {data}")
            # Process the response here (e.g., update state, notify users, etc.)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON response: {e}")

    async def close(self):
        """
        Close the WebSocket connection gracefully.
        """
        if self.connection:
            await self.connection.close()
            logger.info("Connection closed")

async def main():
    """
    Main asynchronous function to run the light client.
    """
    # Replace with the actual WebSocket URL for the Astar/Shiden Network
    url = "wss://rpc.astar.network"  # Example URL
    client = AstarLightClient(url)

    await client.connect()
    await client.subscribe_to_new_blocks()
    await client.listen_for_messages()

# Run the main function
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Client stopped by user")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
```
