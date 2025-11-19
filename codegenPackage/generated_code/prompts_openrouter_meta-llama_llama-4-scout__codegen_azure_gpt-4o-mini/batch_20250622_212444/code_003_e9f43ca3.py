"""
Generated Code Metadata:
========================
Original URL: https://astar-apps.firebaseapp.com
Prompt: What are the best practices for managing connections via Light client on the Astar & Shiden Network, and provide code examples.
Generated: DETERMINISTIC_e9f43ca3cb99bb8e
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
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

class AstarShidenClient:
    """
    A class to manage connections to the Astar and Shiden networks using a light client.
    """

    def __init__(self, url: str):
        """
        Initializes the AstarShidenClient with the given WebSocket URL.

        :param url: The WebSocket URL of the Astar or Shiden network.
        """
        self.url = url
        self.substrate = None

    async def connect(self):
        """
        Connects to the Astar or Shiden network.
        """
        try:
            self.substrate = SubstrateInterface(
                url=self.url,
                type_registry_preset='astar'  # or 'shiden' based on the network
            )
            print("Connected to the network successfully.")
        except Exception as e:
            print(f"Failed to connect to the network: {e}")

    async def disconnect(self):
        """
        Disconnects from the Astar or Shiden network.
        """
        if self.substrate:
            await self.substrate.close()
            print("Disconnected from the network.")

    async def get_chain_info(self):
        """
        Retrieves and returns the chain information.

        :return: Dictionary containing chain information.
        """
        if not self.substrate:
            raise ConnectionError("Client is not connected to the network.")
        
        try:
            chain_info = await self.substrate.get_chain_properties()
            return chain_info
        except SubstrateRequestException as e:
            print(f"Error fetching chain info: {e}")
            return None

    async def get_balance(self, address: str):
        """
        Retrieves the balance of the specified address.

        :param address: The address to check the balance for.
        :return: The balance of the address.
        """
        if not self.substrate:
            raise ConnectionError("Client is not connected to the network.")
        
        try:
            balance = await self.substrate.query('System', 'Account', [address])
            return balance['data']['free']
        except SubstrateRequestException as e:
            print(f"Error fetching balance for {address}: {e}")
            return None

async def main():
    # Example usage of the AstarShidenClient
    client = AstarShidenClient(url='wss://rpc.astar.network')
    
    await client.connect()
    
    try:
        chain_info = await client.get_chain_info()
        print("Chain Info:", chain_info)

        address = 'YOUR_ADDRESS_HERE'
        balance = await client.get_balance(address)
        print(f"Balance for {address}: {balance}")
    finally:
        await client.disconnect()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
