"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Write Python code to simulate a blockchain communication system using a dual-ring architecture, referencing the concepts described in DoubleZero's infrastructure model.
Generated: DETERMINISTIC_3d9eb21fd4e302f4
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
import random
import threading
from queue import Queue

# Blockchain Node class
class BlockchainNode:
    def __init__(self, node_id, primary_ring, secondary_ring):
        """
        Initialize a blockchain node with its ID and references to the two communication rings.
        """
        self.node_id = node_id
        self.primary_ring = primary_ring  # Primary ring for communication
        self.secondary_ring = secondary_ring  # Backup ring for communication
        self.blockchain = []  # Block storage
        self.transaction_pool = []  # Temporary storage for transactions

    def create_transaction(self, sender, receiver, amount):
        """
        Create a new transaction and add it to the transaction pool.
        """
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
        }
        self.transaction_pool.append(transaction)
        self.broadcast_transaction(transaction)

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes in both rings.
        """
        for node in self.primary_ring:
            try:
                node.receive_transaction(transaction)
            except Exception as e:
                print(f"Error sending transaction to node {node.node_id}: {e}")

        for node in self.secondary_ring:
            try:
                node.receive_transaction(transaction)
            except Exception as e:
                print(f"Secondary ring error for node {node.node_id}: {e}")

    def receive_transaction(self, transaction):
        """
        Process received transaction and add to the transaction pool if valid.
        """
        if transaction not in self.transaction_pool:
            print(f"Node {self.node_id} received transaction: {transaction}")
            self.transaction_pool.append(transaction)

    def mine_block(self):
        """
        Mine a new block using the transactions in the transaction pool.
        """
        if not self.transaction_pool:
            print(f"Node {self.node_id}: No transactions to mine.")
            return

        # Create block data
        block_data = {
            "transactions": self.transaction_pool,
            "previous_hash": self.blockchain[-1]["hash"] if self.blockchain else "0" * 64,
            "nonce": 0,
        }

        # Find a valid hash (Proof-of-Work simulation)
        while True:
            block_data["nonce"] += 1
            block_hash = hashlib.sha256(json.dumps(block_data).encode()).hexdigest()
            if block_hash.startswith("00000"):  # Simple difficulty condition
                block_data["hash"] = block_hash
                break

        # Add the new block to the blockchain
        self.blockchain.append(block_data)
        self.transaction_pool = []  # Clear the transaction pool
        self.broadcast_block(block_data)
        print(f"Node {self.node_id} mined a new block: {block_data}")

    def broadcast_block(self, block):
        """
        Broadcast the new block to all nodes in both rings.
        """
        for node in self.primary_ring:
            try:
                node.receive_block(block)
            except Exception as e:
                print(f"Error sending block to node {node.node_id}: {e}")

        for node in self.secondary_ring:
            try:
                node.receive_block(block)
            except Exception as e:
                print(f"Secondary ring error for node {node.node_id}: {e}")

    def receive_block(self, block):
        """
        Process received block and add to blockchain if valid.
        """
        if block not in self.blockchain:
            print(f"Node {self.node_id} received block: {block}")
            self.blockchain.append(block)

# Simulation setup
def setup_simulation(num_nodes):
    """
    Set up blockchain nodes in a dual-ring architecture.
    """
    primary_ring = []
    secondary_ring = []

    # Create nodes and assign them to rings
    for i in range(num_nodes):
        node = BlockchainNode(node_id=i, primary_ring=primary_ring, secondary_ring=secondary_ring)
        primary_ring.append(node)
        secondary_ring.append(node)

    # Randomly shuffle the secondary ring to simulate redundancy
    random.shuffle(secondary_ring)

    return primary_ring

# Test the simulation
def main():
    num_nodes = 5
    nodes = setup_simulation(num_nodes)

    # Generate some transactions and mine blocks
    nodes[0].create_transaction(sender="Alice", receiver="Bob", amount=50)
    nodes[1].create_transaction(sender="Bob", receiver="Charlie", amount=30)
    nodes[2].mine_block()
    nodes[3].mine_block()

    # Print blockchain status for all nodes
    for node in nodes:
        print(f"Node {node.node_id} blockchain: {node.blockchain}")

if __name__ == "__main__":
    main()
```
