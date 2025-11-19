"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: Write a function to manage Light client connections in the Astar Portal for the Astar & Shiden Network.
Generated: DETERMINISTIC_bd19a49e012fd5e9
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LightClientManager:
    """
    A class to manage Light client connections in the Astar Portal for the Astar & Shiden Network.
    """

    def __init__(self):
        """
        Initialize the LightClientManager with an empty dictionary to store active connections.
        """
        self.connections: Dict[str, asyncio.StreamWriter] = {}

    async def connect_client(self, client_id: str, host: str, port: int) -> None:
        """
        Establish a connection to a Light client.

        Args:
            client_id (str): Unique identifier for the client.
            host (str): Host address of the Light client.
            port (int): Port number of the Light client.

        Raises:
            ValueError: If the client_id already exists in active connections.
            ConnectionError: If the connection to the client fails.
        """
        if client_id in self.connections:
            raise ValueError(f"Client ID '{client_id}' is already connected.")

        try:
            logger.info(f"Connecting to Light client {client_id} at {host}:{port}...")
            reader, writer = await asyncio.open_connection(host, port)
            self.connections[client_id] = writer
            logger.info(f"Successfully connected to Light client {client_id}.")
        except Exception as e:
            logger.error(f"Failed to connect to Light client {client_id}: {e}")
            raise ConnectionError(f"Unable to connect to Light client {client_id} at {host}:{port}")

    async def disconnect_client(self, client_id: str) -> None:
        """
        Disconnect a Light client.

        Args:
            client_id (str): Unique identifier for the client.

        Raises:
            KeyError: If the client_id does not exist in active connections.
        """
        if client_id not in self.connections:
            raise KeyError(f"Client ID '{client_id}' is not connected.")

        try:
            logger.info(f"Disconnecting Light client {client_id}...")
            writer = self.connections.pop(client_id)
            writer.close()
            await writer.wait_closed()
            logger.info(f"Successfully disconnected Light client {client_id}.")
        except Exception as e:
            logger.error(f"Failed to disconnect Light client {client_id}: {e}")
            raise RuntimeError(f"Error while disconnecting Light client {client_id}")

    async def send_message(self, client_id: str, message: str) -> None:
        """
        Send a message to a connected Light client.

        Args:
            client_id (str): Unique identifier for the client.
            message (str): Message to send.

        Raises:
            KeyError: If the client_id does not exist in active connections.
            RuntimeError: If there is an error while sending the message.
        """
        if client_id not in self.connections:
            raise KeyError(f"Client ID '{client_id}' is not connected.")

        try:
            logger.info(f"Sending message to Light client {client_id}: {message}")
            writer = self.connections[client_id]
            writer.write(message.encode())
            await writer.drain()
            logger.info(f"Message sent to Light client {client_id}.")
        except Exception as e:
            logger.error(f"Failed to send message to Light client {client_id}: {e}")
            raise RuntimeError(f"Error while sending message to Light client {client_id}")

    async def list_active_connections(self) -> Dict[str, str]:
        """
        List all active Light client connections.

        Returns:
            Dict[str, str]: A dictionary of client IDs and their connection status.
        """
        logger.info("Listing all active Light client connections...")
        return {client_id: "Connected" for client_id in self.connections}

# Example usage (to be run in an asyncio event loop):
# async def main():
#     manager = LightClientManager()
#     await manager.connect_client("client1", "127.0.0.1", 8080)
#     await manager.send_message("client1", "Hello, Light Client!")
#     print(await manager.list_active_connections())
#     await manager.disconnect_client("client1")

# asyncio.run(main())
```
