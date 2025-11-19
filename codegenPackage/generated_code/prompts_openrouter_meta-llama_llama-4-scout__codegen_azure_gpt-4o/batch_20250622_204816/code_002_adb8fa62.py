"""
Generated Code Metadata:
========================
Original URL: https://somnial.pages.dev
Prompt: "Design an EVM Layer 1 blockchain with 300k+tps capacity and interoperability protocols for unifying metaverses, gaming, and NFTs."
Generated: DETERMINISTIC_adb8fa622ecd532c
Batch ID: 20250622_204816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Designing a full EVM Layer 1 blockchain with 300k+ TPS capacity and interoperability protocols is a massive undertaking that involves multiple components, including consensus mechanisms, networking, virtual machines, and more. Below is a simplified, modularized, and production-ready skeleton implementation in Python for educational purposes. This code will focus on the core components of the blockchain, including consensus, transaction processing, and interoperability protocols.

```python
import hashlib
import time
import threading
from typing import List, Dict, Any

# ============================
# Blockchain Configuration
# ============================
TPS_TARGET = 300000  # Transactions per second target
BLOCK_TIME = 1  # Block time in seconds
MAX_TRANSACTIONS_PER_BLOCK = TPS_TARGET * BLOCK_TIME

# ============================
# Utility Functions
# ============================
def sha256(data: str) -> str:
    """Generate a SHA-256 hash of the given data."""
    return hashlib.sha256(data.encode()).hexdigest()

# ============================
# Transaction Class
# ============================
class Transaction:
    def __init__(self, sender: str, receiver: str, amount: float, metadata: Dict[str, Any] = None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.metadata = metadata or {}
        self.timestamp = time.time()
        self.tx_hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the transaction."""
        tx_data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}{self.metadata}"
        return sha256(tx_data)

# ============================
# Block Class
# ============================
class Block:
    def __init__(self, index: int, previous_hash: str, transactions: List[Transaction]):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """Calculate the hash of the block."""
        tx_hashes = ''.join(tx.tx_hash for tx in self.transactions)
        block_data = f"{self.index}{self.previous_hash}{tx_hashes}{self.timestamp}{self.nonce}"
        return sha256(block_data)

    def mine_block(self, difficulty: int):
        """Mine the block by finding a hash with the required difficulty."""
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# ============================
# Blockchain Class
# ============================
class Blockchain:
    def __init__(self, difficulty: int = 4):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the genesis block."""
        genesis_block = Block(0, "0", [])
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def get_latest_block(self) -> Block:
        """Get the latest block in the chain."""
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction):
        """Add a transaction to the list of pending transactions."""
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        """Mine a new block with the pending transactions."""
        if not self.pending_transactions:
            return

        # Limit the number of transactions per block
        transactions_to_include = self.pending_transactions[:MAX_TRANSACTIONS_PER_BLOCK]
        new_block = Block(len(self.chain), self.get_latest_block().hash, transactions_to_include)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        # Remove the mined transactions from the pending list
        self.pending_transactions = self.pending_transactions[MAX_TRANSACTIONS_PER_BLOCK:]

# ============================
# Interoperability Protocols
# ============================
class InteroperabilityProtocol:
    def __init__(self):
        self.connected_chains: Dict[str, Blockchain] = {}

    def register_chain(self, chain_name: str, blockchain: Blockchain):
        """Register a new blockchain for interoperability."""
        self.connected_chains[chain_name] = blockchain

    def transfer_asset(self, from_chain: str, to_chain: str, asset_id: str, metadata: Dict[str, Any]):
        """Transfer an asset between chains."""
        if from_chain not in self.connected_chains or to_chain not in self.connected_chains:
            raise ValueError("Both chains must be registered for interoperability.")

        # Simulate asset transfer
        print(f"Transferring asset {asset_id} from {from_chain} to {to_chain} with metadata: {metadata}")

# ============================
# Example Usage
# ============================
if __name__ == "__main__":
    # Create two blockchains
    blockchain1 = Blockchain(difficulty=4)
    blockchain2 = Blockchain(difficulty=4)

    # Register blockchains for interoperability
    protocol = InteroperabilityProtocol()
    protocol.register_chain("Chain1", blockchain1)
    protocol.register_chain("Chain2", blockchain2)

    # Add transactions to blockchain1
    blockchain1.add_transaction(Transaction("Alice", "Bob", 10, {"type": "NFT"}))
    blockchain1.add_transaction(Transaction("Charlie", "Dave", 20, {"type": "GameAsset"}))

    # Mine transactions on blockchain1
    blockchain1.mine_pending_transactions()

    # Transfer an asset between chains
    protocol.transfer_asset("Chain1", "Chain2", "Asset123", {"type": "NFT", "owner": "Bob"})

    # Print blockchain1 and blockchain2 states
    print("Blockchain1:")
    for block in blockchain1.chain:
        print(vars(block))

    print("\nBlockchain2:")
    for block in blockchain2.chain:
        print(vars(block))
```

This code provides a basic framework for a blockchain with transaction processing, block mining, and an interoperability protocol. It is not optimized for high throughput (300k+ TPS) or production use but serves as a starting point for further development.
