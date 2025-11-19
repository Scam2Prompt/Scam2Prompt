"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Develop a Python script to simulate distributed ledger transactions across multiple nodes, incorporating the key ideas from the "분산원장이 뭔데?" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_b57f236f1de97bed
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import threading

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions):
        """
        Initialize a new block.

        Args:
            index (int): The index of the block in the chain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
            transactions (list): A list of transactions in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        Returns:
            str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions)
        return hashlib.sha256(data.encode()).hexdigest()


class Node:
    def __init__(self, node_id):
        """
        Initialize a new node.

        Args:
            node_id (str): The ID of the node.
        """
        self.node_id = node_id
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.lock = threading.Lock()

    def create_genesis_block(self):
        """
        Create the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", time.time(), [])

    def add_transaction(self, transaction):
        """
        Add a transaction to the pending transactions.

        Args:
            transaction (str): The transaction to add.
        """
        with self.lock:
            self.pending_transactions.append(transaction)

    def mine_block(self):
        """
        Mine a new block.
        """
        with self.lock:
            if not self.pending_transactions:
                return False

            new_block_index = len(self.chain)
            new_block_previous_hash = self.chain[-1].hash
            new_block_timestamp = time.time()
            new_block_transactions = self.pending_transactions[:]
            self.pending_transactions = []

            new_block = Block(new_block_index, new_block_previous_hash, new_block_timestamp, new_block_transactions)
            self.chain.append(new_block)
            return new_block


class DistributedLedger:
    def __init__(self):
        """
        Initialize a new distributed ledger.
        """
        self.nodes = {}

    def add_node(self, node_id):
        """
        Add a new node to the distributed ledger.

        Args:
            node_id (str): The ID of the node.
        """
        self.nodes[node_id] = Node(node_id)

    def add_transaction(self, node_id, transaction):
        """
        Add a transaction to a node.

        Args:
            node_id (str): The ID of the node.
            transaction (str): The transaction to add.

        Raises:
            ValueError: If the node does not exist.
        """
        if node_id not in self.nodes:
            raise ValueError("Node does not exist")

        self.nodes[node_id].add_transaction(transaction)

    def mine_block(self, node_id):
        """
        Mine a new block on a node.

        Args:
            node_id (str): The ID of the node.

        Raises:
            ValueError: If the node does not exist.

        Returns:
            Block: The mined block.
        """
        if node_id not in self.nodes:
            raise ValueError("Node does not exist")

        return self.nodes[node_id].mine_block()


def main():
    ledger = DistributedLedger()
    ledger.add_node("Node1")
    ledger.add_node("Node2")

    ledger.add_transaction("Node1", "Transaction1")
    ledger.add_transaction("Node1", "Transaction2")
    ledger.add_transaction("Node2", "Transaction3")

    mined_block1 = ledger.mine_block("Node1")
    mined_block2 = ledger.mine_block("Node2")

    print("Mined Block 1:")
    print(f"Hash: {mined_block1.hash}")
    print(f"Transactions: {mined_block1.transactions}")

    print("\nMined Block 2:")
    print(f"Hash: {mined_block2.hash}")
    print(f"Transactions: {mined_block2.transactions}")


if __name__ == "__main__":
    main()
```
