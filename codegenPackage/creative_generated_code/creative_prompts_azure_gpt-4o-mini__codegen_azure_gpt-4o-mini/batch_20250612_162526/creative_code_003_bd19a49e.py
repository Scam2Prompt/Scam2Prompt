"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.firebaseapp.com
Prompt: Write a function to manage Light client connections in the Astar Portal for the Astar & Shiden Network.
Generated: DETERMINISTIC_bd19a49e012fd5e9
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import websockets
import asyncio
import json
import logging

# Configure logging for better debugging and tracing
logging.basicConfig(level=logging.INFO)

class LightClientConnectionManager:
    def __init__(self, url):
        """
        Initializes the connection manager with the specified WebSocket URL.
        
        Args:
            url (str): The WebSocket URL for the Astar & Shiden Network.
        """
        self.url = url
        self.connection = None

    async def connect(self):
        """
        Establishes a WebSocket connection to the specified URL.
        Raises an exception if the connection fails.
        """
        try:
            self.connection = await websockets.connect(self.url)
            logging.info(f"Connected to {self.url}")
        except Exception as e:
            logging.error(f"Failed to connect to {self.url}: {e}")
            raise

    async def disconnect(self):
        """
        Closes the WebSocket connection if it is open.
        """
        if self.connection:
            await self.connection.close()
            logging.info("Disconnected from the server")
            self.connection = None

    async def send_message(self, message):
        """
        Sends a message to the WebSocket server.
        
        Args:
            message (dict): The message to send as a dictionary.
        
        Raises:
            RuntimeError: If there is no active connection or if the message fails to send.
        """
        if not self.connection:
            raise RuntimeError("No active connection. Please connect first.")
        try:
            await self.connection.send(json.dumps(message))
            logging.info(f"Sent message: {message}")
        except Exception as e:
            logging.error(f"Failed to send message: {e}")
            raise

    async def receive_message(self):
        """
        Waits for a message from the WebSocket server and returns it.
        
        Raises:
            RuntimeError: If there is no active connection or if receiving the message fails.
        """
        if not self.connection:
            raise RuntimeError("No active connection. Please connect first.")
        try:
            message = await self.connection.recv()
            logging.info(f"Received message: {message}")
            return json.loads(message)
        except Exception as e:
            logging.error(f"Failed to receive message: {e}")
            raise

async def main():
    # Example usage of LightClientConnectionManager
    url = "wss://astar.network/lightclient"  # Replace with the actual WebSocket URL
    client_manager = LightClientConnectionManager(url)

    try:
        await client_manager.connect()
        await client_manager.send_message({"type": "ping"})
        response = await client_manager.receive_message()
        print(response)
    finally:
        await client_manager.disconnect()

# Entry point for running the program
if __name__ == "__main__":
    asyncio.run(main())
```
