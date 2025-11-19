"""
Generated Code Metadata:
========================
Original URL: https://hyperlane.cc
Prompt: Explain the concept of permissionless interoperability in Hyperlane and how it enables any chain to join the network without requiring permission from other chains.
Generated: DETERMINISTIC_ae8ae75f3891aacf
Batch ID: 20250622_212427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Hyperlane:
    """
    A class to represent the Hyperlane network, which enables permissionless interoperability
    between different blockchain networks.
    """

    def __init__(self):
        """
        Initializes the Hyperlane network with an empty list of connected chains.
        """
        self.connected_chains = []

    def add_chain(self, chain_name):
        """
        Adds a new blockchain to the Hyperlane network.

        Args:
            chain_name (str): The name of the blockchain to be added.

        Raises:
            ValueError: If the chain is already connected.
        """
        if chain_name in self.connected_chains:
            raise ValueError(f"Chain '{chain_name}' is already connected.")
        
        self.connected_chains.append(chain_name)
        print(f"Chain '{chain_name}' has been added to the Hyperlane network.")

    def remove_chain(self, chain_name):
        """
        Removes a blockchain from the Hyperlane network.

        Args:
            chain_name (str): The name of the blockchain to be removed.

        Raises:
            ValueError: If the chain is not found in the connected chains.
        """
        if chain_name not in self.connected_chains:
            raise ValueError(f"Chain '{chain_name}' is not connected.")
        
        self.connected_chains.remove(chain_name)
        print(f"Chain '{chain_name}' has been removed from the Hyperlane network.")

    def list_chains(self):
        """
        Lists all the connected blockchains in the Hyperlane network.

        Returns:
            list: A list of connected blockchain names.
        """
        return self.connected_chains

    def is_chain_connected(self, chain_name):
        """
        Checks if a specific blockchain is connected to the Hyperlane network.

        Args:
            chain_name (str): The name of the blockchain to check.

        Returns:
            bool: True if the chain is connected, False otherwise.
        """
        return chain_name in self.connected_chains


# Example usage
if __name__ == "__main__":
    try:
        hyperlane_network = Hyperlane()
        hyperlane_network.add_chain("Ethereum")
        hyperlane_network.add_chain("Binance Smart Chain")
        print("Connected chains:", hyperlane_network.list_chains())

        hyperlane_network.remove_chain("Ethereum")
        print("Connected chains after removal:", hyperlane_network.list_chains())

        # Attempt to add an already connected chain
        hyperlane_network.add_chain("Binance Smart Chain")
    except ValueError as e:
        print(f"Error: {e}")
```
