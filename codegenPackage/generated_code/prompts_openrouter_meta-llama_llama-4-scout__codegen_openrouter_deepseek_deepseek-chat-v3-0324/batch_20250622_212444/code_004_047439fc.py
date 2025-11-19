"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: Create a simple application that utilizes the Astar Portal to connect and disconnect from the network using Light client.
Generated: DETERMINISTIC_047439fcf0773342
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import asyncio
from astar import Astar

class AstarLightClient:
    """
    A simple application to connect and disconnect from the Astar network using Light client.
    """
    
    def __init__(self, endpoint):
        """
        Initialize the AstarLightClient with a network endpoint.
        
        Args:
            endpoint (str): The WebSocket endpoint of the Astar network (e.g., 'wss://rpc.astar.network')
        """
        self.endpoint = endpoint
        self.client = None
    
    async def connect(self):
        """
        Connect to the Astar network using Light client.
        
        Raises:
            ConnectionError: If connection to the network fails.
        """
        try:
            self.client = await Astar.connect(self.endpoint)
            print(f"Successfully connected to Astar network at {self.endpoint}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Astar network: {str(e)}")
    
    async def disconnect(self):
        """
        Disconnect from the Astar network.
        
        Raises:
            ConnectionError: If disconnection fails.
        """
        if self.client is None:
            print("No active connection to disconnect")
            return
        
        try:
            await self.client.disconnect()
            print("Successfully disconnected from Astar network")
            self.client = None
        except Exception as e:
            raise ConnectionError(f"Failed to disconnect from Astar network: {str(e)}")
    
    async def __aenter__(self):
        """Context manager entry point for async with."""
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point for async with."""
        await self.disconnect()

async def main():
    """
    Main function to demonstrate connecting and disconnecting from Astar network.
    """
    endpoint = "wss://rpc.astar.network"  # Example endpoint
    
    try:
        async with AstarLightClient(endpoint) as client:
            # Perform operations with connected client here
            print("Connected to Astar network. Ready to perform operations.")
            await asyncio.sleep(2)  # Simulate some operations
            
    except ConnectionError as e:
        print(f"Connection error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```
