"""
Generated Code Metadata:
========================
Original URL: https://yethereum.com
Prompt: "Explain the concept of data availability in the context of Ethereum's scalability solutions, referencing EthStorage's approach."
Generated: DETERMINISTIC_76bc24b35895432e
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script demonstrates a simplified simulation of Ethereum's data availability concept
# with a focus on EthStorage's approach to scalability solutions.

import hashlib
import json
from typing import List, Dict, Optional

class Block:
    """
    Represents a simplified Ethereum block with transaction data and data availability references.
    """
    def __init__(self, block_number: int, transactions: List[Dict], data_availability_ref: Optional[str] = None):
        self.block_number = block_number
        self.transactions = transactions
        self.data_availability_ref = data_availability_ref  # Reference to off-chain data storage
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the block's hash using its contents.
        """
        block_data = {
            'block_number': self.block_number,
            'transactions': self.transactions,
            'data_availability_ref': self.data_availability_ref
        }
        return hashlib.sha256(json.dumps(block_data, sort_keys=True).encode()).hexdigest()

class EthStorageNode:
    """
    Simulates EthStorage's off-chain data availability solution.
    """
    def __init__(self):
        self.storage = {}
        self.availability_checks = 0

    def store_data(self, data: Dict) -> str:
        """
        Store transaction data off-chain and return a reference hash.
        """
        data_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
        self.storage[data_hash] = data
        return data_hash

    def retrieve_data(self, data_hash: str) -> Optional[Dict]:
        """
        Retrieve data from off-chain storage using its reference hash.
        """
        return self.storage.get(data_hash)

    def check_availability(self, data_hash: str) -> bool:
        """
        Verify if data is available in the off-chain storage.
        """
        self.availability_checks += 1
        return data_hash in self.storage

class EthereumNetwork:
    """
    Simulates Ethereum network with data availability considerations.
    """
    def __init__(self):
        self.blocks = []
        self.eth_storage = EthStorageNode()

    def add_block(self, transactions: List[Dict], store_off_chain: bool = False) -> Block:
        """
        Add a new block to the chain, optionally storing transaction data off-chain.
        """
        block_number = len(self.blocks) + 1
        data_ref = None

        if store_off_chain:
            # Store transaction data in EthStorage and keep only reference in block
            data_ref = self.eth_storage.store_data({'transactions': transactions})

        new_block = Block(block_number, transactions if not store_off_chain else [], data_ref)
        self.blocks.append(new_block)
        return new_block

    def verify_block_data(self, block: Block) -> bool:
        """
        Verify that a block's data is available, either on-chain or via EthStorage.
        """
        if block.data_availability_ref:
            # Check off-chain data availability
            return self.eth_storage.check_availability(block.data_availability_ref)
        else:
            # On-chain data is always available
            return True

    def get_transaction_data(self, block: Block) -> Optional[List[Dict]]:
        """
        Retrieve transaction data for a block, whether stored on-chain or off-chain.
        """
        if block.data_availability_ref:
            stored_data = self.eth_storage.retrieve_data(block.data_availability_ref)
            return stored_data.get('transactions') if stored_data else None
        return block.transactions

# Example usage demonstrating data availability concept
if __name__ == "__main__":
    # Initialize network
    network = EthereumNetwork()

    # Add a block with on-chain data
    on_chain_txs = [{'from': 'Alice', 'to': 'Bob', 'amount': 1}]
    on_chain_block = network.add_block(on_chain_txs)
    print(f"On-chain block hash: {on_chain_block.hash}")

    # Add a block with off-chain data via EthStorage
    off_chain_txs = [{'from': 'Charlie', 'to': 'Dave', 'amount': 2}]
    off_chain_block = network.add_block(off_chain_txs, store_off_chain=True)
    print(f"Off-chain block hash: {off_chain_block.hash}")

    # Verify data availability
    print(f"On-chain block data available: {network.verify_block_data(on_chain_block)}")
    print(f"Off-chain block data available: {network.verify_block_data(off_chain_block)}")

    # Retrieve transaction data
    print(f"On-chain transactions: {network.get_transaction_data(on_chain_block)}")
    print(f"Off-chain transactions: {network.get_transaction_data(off_chain_block)}")
```
