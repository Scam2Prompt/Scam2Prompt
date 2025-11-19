"""
Generated Code Metadata:
========================
Original URL: https://lavanet-app.pages.dev
Prompt: Implement a simple multi-chain RPC client using the Lava SDK, supporting at least three different blockchain networks.
Generated: DETERMINISTIC_47e5c2c13c150b0d
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from lavaclient import LavaClient
from lavaclient.common import Request, Response
import json

class MultiChainRPCClient:
    """
    A simple multi-chain RPC client using the Lava SDK.

    Attributes:
    - lava_client (LavaClient): The Lava client instance.
    - chains (dict): A dictionary of supported blockchain networks.

    Methods:
    - __init__: Initializes the multi-chain RPC client.
    - get_chain: Returns a Lava client instance for a specific chain.
    - request: Sends an RPC request to a specific chain.
    """

    def __init__(self, api_key, chains):
        """
        Initializes the multi-chain RPC client.

        Args:
        - api_key (str): The Lava API key.
        - chains (list): A list of supported blockchain networks.

        Raises:
        - ValueError: If the list of chains is empty.
        """
        if not chains:
            raise ValueError("At least one chain must be specified")

        self.lava_client = LavaClient(api_key)
        self.chains = {chain: self.lava_client.get_chain(chain) for chain in chains}

    def get_chain(self, chain_name):
        """
        Returns a Lava client instance for a specific chain.

        Args:
        - chain_name (str): The name of the blockchain network.

        Returns:
        - LavaClient: The Lava client instance for the specified chain.

        Raises:
        - ValueError: If the chain is not supported.
        """
        if chain_name not in self.chains:
            raise ValueError(f"Chain '{chain_name}' is not supported")

        return self.chains[chain_name]

    def request(self, chain_name, method, params=None):
        """
        Sends an RPC request to a specific chain.

        Args:
        - chain_name (str): The name of the blockchain network.
        - method (str): The RPC method to call.
        - params (list): A list of parameters for the RPC method.

        Returns:
        - Response: The response from the RPC request.

        Raises:
        - ValueError: If the chain is not supported.
        """
        chain = self.get_chain(chain_name)
        request = Request(method, params)
        try:
            response = chain.request(request)
            return response
        except Exception as e:
            raise Exception(f"Error sending request to {chain_name}: {str(e)}")


def main():
    # Define the Lava API key
    api_key = "your_lava_api_key"

    # Define the supported blockchain networks
    chains = ["ethereum", "cosmos", "polkadot"]

    # Create a multi-chain RPC client
    client = MultiChainRPCClient(api_key, chains)

    # Send an RPC request to Ethereum
    try:
        response = client.request("ethereum", "eth_blockNumber")
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error: {str(e)}")

    # Send an RPC request to Cosmos
    try:
        response = client.request("cosmos", "status")
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error: {str(e)}")

    # Send an RPC request to Polkadot
    try:
        response = client.request("polkadot", "chain_getBlock")
        print(json.dumps(response, indent=4))
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
