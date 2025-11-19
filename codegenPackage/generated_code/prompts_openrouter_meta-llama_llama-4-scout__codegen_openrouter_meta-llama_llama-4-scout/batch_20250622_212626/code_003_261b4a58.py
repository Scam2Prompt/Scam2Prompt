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
# sophon_network.py

class SophonNode:
    """
    Represents a node in the Sophon network.

    Attributes:
        node_id (str): Unique identifier for the node.
        ip_address (str): IP address of the node.
        port (int): Port number of the node.
    """

    def __init__(self, node_id, ip_address, port):
        """
        Initializes a SophonNode object.

        Args:
            node_id (str): Unique identifier for the node.
            ip_address (str): IP address of the node.
            port (int): Port number of the node.
        """
        self.node_id = node_id
        self.ip_address = ip_address
        self.port = port

    def __str__(self):
        return f"SophonNode(node_id={self.node_id}, ip_address={self.ip_address}, port={self.port})"


class GuardianMembership:
    """
    Represents a guardian membership in the Sophon network.

    Attributes:
        member_id (str): Unique identifier for the member.
        sophon_node (SophonNode): The Sophon node associated with the member.
        stake_amount (float): The amount of SOPH tokens staked by the member.
    """

    def __init__(self, member_id, sophon_node, stake_amount):
        """
        Initializes a GuardianMembership object.

        Args:
            member_id (str): Unique identifier for the member.
            sophon_node (SophonNode): The Sophon node associated with the member.
            stake_amount (float): The amount of SOPH tokens staked by the member.
        """
        self.member_id = member_id
        self.sophon_node = sophon_node
        self.stake_amount = stake_amount

    def __str__(self):
        return f"GuardianMembership(member_id={self.member_id}, sophon_node={self.sophon_node}, stake_amount={self.stake_amount})"


class SophonNetwork:
    """
    Represents the Sophon network.

    Attributes:
        nodes (list[SophonNode]): A list of Sophon nodes in the network.
        guardian_memberships (list[GuardianMembership]): A list of guardian memberships in the network.
    """

    def __init__(self):
        """
        Initializes a SophonNetwork object.
        """
        self.nodes = []
        self.guardian_memberships = []

    def add_node(self, node):
        """
        Adds a Sophon node to the network.

        Args:
            node (SophonNode): The node to add.

        Raises:
            ValueError: If the node already exists in the network.
        """
        if node in self.nodes:
            raise ValueError("Node already exists in the network")
        self.nodes.append(node)

    def add_guardian_membership(self, membership):
        """
        Adds a guardian membership to the network.

        Args:
            membership (GuardianMembership): The membership to add.

        Raises:
            ValueError: If the membership already exists in the network.
        """
        if membership in self.guardian_memberships:
            raise ValueError("Membership already exists in the network")
        self.guardian_memberships.append(membership)

    def get_node(self, node_id):
        """
        Gets a Sophon node by its ID.

        Args:
            node_id (str): The ID of the node to get.

        Returns:
            SophonNode: The node with the specified ID, or None if not found.
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_guardian_membership(self, member_id):
        """
        Gets a guardian membership by its ID.

        Args:
            member_id (str): The ID of the membership to get.

        Returns:
            GuardianMembership: The membership with the specified ID, or None if not found.
        """
        for membership in self.guardian_memberships:
            if membership.member_id == member_id:
                return membership
        return None


class SOPHToken:
    """
    Represents the SOPH token.

    Attributes:
        token_id (str): Unique identifier for the token.
        balance (float): The current balance of the token.
    """

    def __init__(self, token_id, balance=0.0):
        """
        Initializes a SOPHToken object.

        Args:
            token_id (str): Unique identifier for the token.
            balance (float, optional): The initial balance of the token. Defaults to 0.0.
        """
        self.token_id = token_id
        self.balance = balance

    def __str__(self):
        return f"SOPHToken(token_id={self.token_id}, balance={self.balance})"


def main():
    try:
        # Create a Sophon network
        network = SophonNetwork()

        # Create Sophon nodes
        node1 = SophonNode("node1", "192.168.1.100", 8080)
        node2 = SophonNode("node2", "192.168.1.101", 8081)

        # Add nodes to the network
        network.add_node(node1)
        network.add_node(node2)

        # Create guardian memberships
        membership1 = GuardianMembership("member1", node1, 100.0)
        membership2 = GuardianMembership("member2", node2, 200.0)

        # Add guardian memberships to the network
        network.add_guardian_membership(membership1)
        network.add_guardian_membership(membership2)

        # Create SOPH tokens
        token1 = SOPHToken("token1", 1000.0)
        token2 = SOPHToken("token2", 2000.0)

        # Print network information
        print("Sophon Nodes:")
        for node in network.nodes:
            print(node)

        print("\nGuardian Memberships:")
        for membership in network.guardian_memberships:
            print(membership)

        print("\nSOPH Tokens:")
        print(token1)
        print(token2)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
