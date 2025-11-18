"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://veipeicoin.pages.dev
Prompt: Generate code for connecting to Dapps and resolving connection errors using the Decentralized Dapps protocol.
Generated: DETERMINISTIC_717ef779e1da96ef
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import websockets
import json

class DAppConnector:
    """
    A class to connect to decentralized applications (DApps) using WebSocket protocol.
    """

    def __init__(self, uri):
        """
        Initializes the DAppConnector with the given WebSocket URI.

        Args:
            uri (str): The URI of the DApp to connect to.
        """
        self.uri = uri

    async def connect(self):
        """
        Connects to the DApp and starts listening for messages.

        Raises:
            ConnectionError: If connection to the DApp fails.
        """
        try:
            async with websockets.connect(self.uri) as websocket:
                print(f"Connected to {self.uri}")
                await self.listen(websocket)
        except (websockets.exceptions.InvalidStatusCode, ConnectionRefusedError) as e:
            raise ConnectionError(f"Failed to connect to DApp: {e}") from e

    async def listen(self, websocket):
        """
        Listens for incoming messages from the connected DApp.

        Args:
            websocket (WebSocketClientProtocol): The WebSocket connection to listen on.
        """
        try:
            while True:
                message = await websocket.recv()
                self.handle_message(message)
        except websockets.ConnectionClosed as e:
            print(f"Connection closed: {e.reason}")
        except Exception as e:
            print(f"An error occurred while listening: {e}")

    def handle_message(self, message):
        """
        Handles incoming messages from the DApp.

        Args:
            message (str): The message received from the DApp.
        """
        try:
            data = json.loads(message)
            print(f"Received message: {data}")
            # Process the incoming data as required
        except json.JSONDecodeError as e:
            print(f"Failed to decode message: {e}")

if __name__ == "__main__":
    dapp_uri = "wss://example-dapp-url.com"  # Replace with actual DApp URI

    connector = DAppConnector(dapp_uri)

    # Running the DApp connection in an asyncio event loop
    try:
        asyncio.run(connector.connect())
    except ConnectionError as e:
        print(f"Error: {e}")
```
