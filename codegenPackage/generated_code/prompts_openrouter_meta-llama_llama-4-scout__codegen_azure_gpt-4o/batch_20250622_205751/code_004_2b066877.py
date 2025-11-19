"""
Generated Code Metadata:
========================
Original URL: https://bafkreibgcum43j7d4mubge4izowokrtbcswc6llh62jjklhh7g5bzrfd6e.ipfs.dweb.link
Prompt: "Design a basic example of a blockchain-based AI compute resource allocation system inspired by OpenGPU."
Generated: DETERMINISTIC_2b0668771435db67
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
import time
from typing import List, Dict, Any


class Block:
    """
    Represents a single block in the blockchain.
    Each block contains a timestamp, a list of transactions, the previous block's hash, and its own hash.
    """
    def __init__(self, index: int, transactions: List[Dict[str, Any]], previous_hash: str):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Used for proof-of-work
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculates the hash of the block using its contents.
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_content).hexdigest()

    def mine_block(self, difficulty: int):
        """
        Mines the block by finding a hash that starts with a certain number of zeros (difficulty).
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    """
    Represents the blockchain, which is a chain of blocks.
    """
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions: List[Dict[str, Any]] = []

    def create_genesis_block(self) -> Block:
        """
        Creates the first block in the blockchain (genesis block).
        """
        return Block(index=0, transactions=[], previous_hash="0")

    def get_latest_block(self) -> Block:
        """
        Returns the latest block in the chain.
        """
        return self.chain[-1]

    def add_transaction(self, transaction: Dict[str, Any]):
        """
        Adds a transaction to the list of pending transactions.
        """
        if not transaction.get("sender") or not transaction.get("receiver") or not transaction.get("amount"):
            raise ValueError("Transaction must include sender, receiver, and amount.")
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address: str):
        """
        Mines all pending transactions and adds them to a new block.
        Rewards the miner with a transaction.
        """
        reward_transaction = {
            "sender": "System",
            "receiver": miner_address,
            "amount": 1  # Reward for mining
        }
        self.pending_transactions.append(reward_transaction)

        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            previous_hash=self.get_latest_block().hash
        )
        new_block.mine_block(self.difficulty)

        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain by checking the hashes and previous hashes of all blocks.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Example usage
if __name__ == "__main__":
    # Initialize the blockchain
    gpu_chain = Blockchain(difficulty=4)

    # Add some transactions
    gpu_chain.add_transaction({"sender": "User1", "receiver": "GPUProvider1", "amount": 10})
    gpu_chain.add_transaction({"sender": "User2", "receiver": "GPUProvider2", "amount": 20})

    # Mine the transactions
    print("Mining pending transactions...")
    gpu_chain.mine_pending_transactions(miner_address="Miner1")

    # Display the blockchain
    for block in gpu_chain.chain:
        print(f"Block {block.index}:")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Transactions: {block.transactions}")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Hash: {block.hash}")
        print()

    # Validate the blockchain
    print("Is blockchain valid?", gpu_chain.is_chain_valid())
```
