"""
Generated Code Metadata:
========================
Original URL: https://sophan.xyz
Prompt: Explain the role of Sophon Nodes and Guardian Memberships in securing and powering the Sophon network, and how they relate to the SOPH token.
Generated: DETERMINISTIC_261b4a58455e6b3b
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SophonNetwork:
    """
    A class to represent the Sophon Network, which utilizes Sophon Nodes and Guardian Memberships
    to secure and power the network. The network operates with the SOPH token.
    """

    def __init__(self):
        """
        Initializes the Sophon Network with empty lists for nodes and guardians.
        """
        self.sophon_nodes = []
        self.guardian_memberships = []
        self.soph_token_supply = 0

    def add_sophon_node(self, node_id):
        """
        Adds a new Sophon Node to the network.

        Args:
            node_id (str): Unique identifier for the Sophon Node.

        Raises:
            ValueError: If the node_id is already in use.
        """
        if node_id in self.sophon_nodes:
            raise ValueError(f"Node ID {node_id} already exists.")
        self.sophon_nodes.append(node_id)
        print(f"Sophon Node {node_id} added successfully.")

    def remove_sophon_node(self, node_id):
        """
        Removes a Sophon Node from the network.

        Args:
            node_id (str): Unique identifier for the Sophon Node.

        Raises:
            ValueError: If the node_id does not exist.
        """
        if node_id not in self.sophon_nodes:
            raise ValueError(f"Node ID {node_id} does not exist.")
        self.sophon_nodes.remove(node_id)
        print(f"Sophon Node {node_id} removed successfully.")

    def add_guardian_membership(self, guardian_id):
        """
        Adds a new Guardian Membership to the network.

        Args:
            guardian_id (str): Unique identifier for the Guardian.

        Raises:
            ValueError: If the guardian_id is already in use.
        """
        if guardian_id in self.guardian_memberships:
            raise ValueError(f"Guardian ID {guardian_id} already exists.")
        self.guardian_memberships.append(guardian_id)
        print(f"Guardian Membership {guardian_id} added successfully.")

    def remove_guardian_membership(self, guardian_id):
        """
        Removes a Guardian Membership from the network.

        Args:
            guardian_id (str): Unique identifier for the Guardian.

        Raises:
            ValueError: If the guardian_id does not exist.
        """
        if guardian_id not in self.guardian_memberships:
            raise ValueError(f"Guardian ID {guardian_id} does not exist.")
        self.guardian_memberships.remove(guardian_id)
        print(f"Guardian Membership {guardian_id} removed successfully.")

    def issue_soph_tokens(self, amount):
        """
        Issues SOPH tokens to the network.

        Args:
            amount (int): The amount of SOPH tokens to issue.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.soph_token_supply += amount
        print(f"Issued {amount} SOPH tokens. Total supply is now {self.soph_token_supply}.")

    def get_network_status(self):
        """
        Returns the current status of the Sophon Network, including nodes, guardians, and token supply.

        Returns:
            dict: A dictionary containing the status of the network.
        """
        return {
            "sophon_nodes": self.sophon_nodes,
            "guardian_memberships": self.guardian_memberships,
            "soph_token_supply": self.soph_token_supply
        }


# Example usage
if __name__ == "__main__":
    try:
        network = SophonNetwork()
        network.add_sophon_node("Node1")
        network.add_guardian_membership("Guardian1")
        network.issue_soph_tokens(1000)
        print(network.get_network_status())
    except ValueError as e:
        print(f"Error: {e}")
```
