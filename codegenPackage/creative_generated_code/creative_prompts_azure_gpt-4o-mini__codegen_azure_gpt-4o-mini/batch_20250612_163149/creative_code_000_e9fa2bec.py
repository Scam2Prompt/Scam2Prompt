"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-apps.web.app
Prompt: How can I implement a light client connection for the Astar Portal on the Astar & Shiden Network?
Generated: DETERMINISTIC_e9fa2becbfa45177
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
import websockets
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AstarLightClient:
    def __init__(self, uri):
        """
        Initializes the AstarLightClient with the given WebSocket URI.

        Parameters:
        uri (str): The WebSocket URI for the Astar Portal.
        """
        self.uri = uri
        self.connection = None

    async def connect(self):
        """Establishes a connection to the Astar Portal."""
        try:
            self.connection = await websockets.connect(self.uri)
            logger.info("Connected to Astar Portal.")
        except Exception as e:
            logger.error(f"Failed to connect to Astar Portal: {e}")
            raise

    async def disconnect(self):
        """Safely disconnects from the Astar Portal."""
        if self.connection:
            await self.connection.close()
            logger.info("Disconnected from Astar Portal.")
            self.connection = None

    async def send_request(self, method, params=None):
        """
        Sends a JSON-RPC request to the Astar Portal.

        Parameters:
        method (str): The method to invoke.
        params (list): The parameters for the method call.

        Returns:
        dict: The response from the Astar Portal.

        Raises:
        Exception: If the request fails.
        """
        request_id = 1  # Unique request ID for this session
        request_payload = {
            "jsonrpc": "2.0",
            "id": request_id,
            "method": method,
            "params": params or []
        }

        try:
            await self.connection.send(json.dumps(request_payload))
            logger.info(f"Request sent: {request_payload}")

            response = await self.connection.recv()
            logger.info(f"Response received: {response}")
            return json.loads(response)

        except Exception as e:
            logger.error(f"Failed to send request: {e}")
            raise

    async def run(self):
        """Main loop to connect to the Astar Portal and handle requests."""
        try:
            await self.connect()
            # Example of sending a request
            response = await self.send_request("chain_getBlock")
            logger.info(f"Block data: {response}")
        finally:
            await self.disconnect()

if __name__ == "__main__":
    # Set the WebSocket URI for the Astar Portal
    astar_portal_uri = "wss://astar.api.onfinality.io/public-ws"

    # Create the AstarLightClient instance and run the main loop
    client = AstarLightClient(astar_portal_uri)
    asyncio.run(client.run())
```
