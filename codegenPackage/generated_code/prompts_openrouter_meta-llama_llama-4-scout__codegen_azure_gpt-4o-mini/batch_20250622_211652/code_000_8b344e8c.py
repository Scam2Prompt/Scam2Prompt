"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Explain the concept of a distributed ledger in the context of blockchain, including its benefits and how it works.
Generated: DETERMINISTIC_8b344e8ce6b81963
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DistributedLedger:
    """
    A class to represent a simple distributed ledger using blockchain principles.
    """

    def __init__(self):
        """
        Initializes the distributed ledger with an empty chain and a set of nodes.
        """
        self.chain = []  # The blockchain
        self.nodes = set()  # A set of nodes in the network

    def create_block(self, previous_hash):
        """
        Creates a new block and adds it to the chain.

        :param previous_hash: Hash of the previous block in the chain
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'previous_hash': previous_hash,
            'transactions': []  # Placeholder for transactions
        }
        self.chain.append(block)
        return block

    def add_node(self, address):
        """
        Adds a new node to the set of nodes.

        :param address: The address of the node to be added
        """
        self.nodes.add(address)

    def create_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to be added to the next block.

        :param sender: The address of the sender
        :param recipient: The address of the recipient
        :param amount: The amount to be transferred
        :return: A dictionary representing the transaction
        """
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        return transaction

    def add_transaction(self, transaction):
        """
        Adds a transaction to the list of transactions for the next block.

        :param transaction: The transaction to be added
        """
        if not isinstance(transaction, dict):
            raise ValueError("Transaction must be a dictionary.")
        if 'sender' not in transaction or 'recipient' not in transaction or 'amount' not in transaction:
            raise ValueError("Transaction must contain sender, recipient, and amount.")
        
        if not self.chain:
            raise Exception("No blocks in the chain. Create a block first.")

        self.chain[-1]['transactions'].append(transaction)

    def mine_block(self):
        """
        Mines a new block and adds it to the chain after validating transactions.

        :return: The newly mined block
        """
        if not self.chain:
            raise Exception("No blocks in the chain to mine from.")

        previous_block = self.chain[-1]
        previous_hash = self.hash(previous_block)
        block = self.create_block(previous_hash)
        return block

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block.

        :param block: The block to be hashed
        :return: The hash of the block
        """
        import hashlib
        import json

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Example usage
if __name__ == "__main__":
    try:
        ledger = DistributedLedger()
        ledger.create_block(previous_hash='0')  # Create the genesis block
        transaction = ledger.create_transaction('Alice', 'Bob', 50)
        ledger.add_transaction(transaction)
        mined_block = ledger.mine_block()
        print("Mined Block:", mined_block)
    except Exception as e:
        print(f"An error occurred: {e}")
```
