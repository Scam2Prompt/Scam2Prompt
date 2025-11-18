"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-gpu.pages.dev
Prompt: Generate code to calculate the total number of nodes held by a wallet and display their contribution to the network's reputation score.
Generated: DETERMINISTIC_72c2cc87826ca02f
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Wallet:
    """
    Represents a Wallet holding nodes in a distributed network.
    """
    def __init__(self, wallet_id, nodes=None):
        """
        Initializes a Wallet instance.

        :param wallet_id: Unique identifier for the wallet
        :param nodes: List containing the node IDs held by the wallet
        """
        self.wallet_id = wallet_id
        self.nodes = nodes if nodes else []

    def add_node(self, node_id):
        """
        Adds a node to the wallet.

        :param node_id: Unique identifier for the node
        """
        if node_id not in self.nodes:
            self.nodes.append(node_id)

    def calculate_reputation_score(self):
        """
        Calculates the reputation score based on the number of nodes in the wallet.

        :return: Reputation score (float)
        """
        # Example formula: reputation score equals total nodes * 10
        return len(self.nodes) * 10


def display_wallet_info(wallet):
    """
    Displays the wallet's total nodes and reputation score.

    :param wallet: Wallet instance
    """
    try:
        total_nodes = len(wallet.nodes)
        reputation_score = wallet.calculate_reputation_score()
        print(f"Wallet ID: {wallet.wallet_id}")
        print(f"Total Nodes: {total_nodes}")
        print(f"Reputation Score: {reputation_score:.2f}")
    except Exception as e:
        print(f"Error displaying wallet information: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a wallet instance
        wallet = Wallet(wallet_id="wallet_12345")

        # Add nodes to the wallet
        wallet.add_node("node_001")
        wallet.add_node("node_002")
        wallet.add_node("node_003")

        # Display wallet information
        display_wallet_info(wallet)
    except Exception as main_error:
        # Global error handling for unforeseen issues
        print(f"An error occurred: {main_error}")
```
