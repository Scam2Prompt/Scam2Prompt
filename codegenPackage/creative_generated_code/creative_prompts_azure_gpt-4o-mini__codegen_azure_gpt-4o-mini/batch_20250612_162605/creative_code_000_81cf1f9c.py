"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-portal.vercel.app
Prompt: How can I use the Astar Portal to connect to the Astar and Shiden networks using a light client?
Generated: DETERMINISTIC_81cf1f9c712cb063
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from astar import Astar, Shiden

class AstarShidenLightClient:
    """A class to interact with the Astar and Shiden networks using light clients."""

    def __init__(self, astar_node_url: str, shiden_node_url: str):
        """
        Initialize the light client with the provided node URLs.

        :param astar_node_url: The WebSocket URL for the Astar network node.
        :param shiden_node_url: The WebSocket URL for the Shiden network node.
        """
        self.astar_node_url = astar_node_url
        self.shiden_node_url = shiden_node_url
        self.astar_client = None
        self.shiden_client = None

    async def connect(self):
        """Connect to both Astar and Shiden networks."""
        try:
            self.astar_client = await Astar.connect(self.astar_node_url)
            self.shiden_client = await Shiden.connect(self.shiden_node_url)
            print("Successfully connected to Astar and Shiden networks.")
        except Exception as e:
            print(f"Failed to connect: {e}")
            raise

    async def disconnect(self):
        """Disconnect from both networks."""
        if self.astar_client:
            await self.astar_client.disconnect()
        if self.shiden_client:
            await self.shiden_client.disconnect()
        print("Disconnected from Astar and Shiden networks.")

    async def get_block_number(self):
        """Retrieve the latest block number from both networks."""
        try:
            astar_block_number = await self.astar_client.get_block_number()
            shiden_block_number = await self.shiden_client.get_block_number()
            return astar_block_number, shiden_block_number
        except Exception as e:
            print(f"Error fetching block number: {e}")
            return None, None

    async def run(self):
        """Main method to run the light client."""
        await self.connect()
        try:
            astar_block, shiden_block = await self.get_block_number()
            print(f"Astar Block Number: {astar_block}")
            print(f"Shiden Block Number: {shiden_block}")
        finally:
            await self.disconnect()

# Main execution block
if __name__ == "__main__":
    astar_node_url = "wss://rpc.astar.network"  # Replace with actual Astar WebSocket URL
    shiden_node_url = "wss://rpc.shiden.network"  # Replace with actual Shiden WebSocket URL

    client = AstarShidenLightClient(astar_node_url, shiden_node_url)
    
    try:
        asyncio.run(client.run())
    except Exception as e:
        print(f"An error occurred in the main execution: {e}")
```
