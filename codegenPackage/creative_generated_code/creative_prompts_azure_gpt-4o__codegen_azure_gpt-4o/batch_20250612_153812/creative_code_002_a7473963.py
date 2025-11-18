"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-doublezero.com
Prompt: Generate code for integrating edge filtering hardware into a distributed blockchain network to reduce latency and improve security, as outlined in DoubleZero's approach.
Generated: DETERMINISTIC_a747396333a98112
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Integration of edge filtering hardware into a distributed blockchain network.
This code is designed to reduce latency and improve security, following DoubleZero's approach.
"""

import asyncio
import json
import hashlib
from typing import Dict, Any

class EdgeFilter:
    """
    Class representing the edge filtering hardware.
    This hardware is responsible for filtering incoming blockchain transactions to enhance security.
    """

    def __init__(self, allowed_sources: Dict[str, str]):
        """
        Initialize the edge filter with allowed sources.
        
        :param allowed_sources: A dictionary of allowed IP addresses and their corresponding public keys.
        """
        self.allowed_sources = allowed_sources

    def verify_transaction(self, transaction: Dict[str, Any]) -> bool:
        """
        Verify the legitimacy of a blockchain transaction.
        
        :param transaction: The incoming transaction as a dictionary.
        :return: True if the transaction is valid, False otherwise.
        """
        try:
            sender_ip = transaction.get('sender_ip')
            sender_key = transaction.get('sender_key')
            transaction_data = transaction.get('data')
            transaction_hash = transaction.get('hash')

            # Check if sender IP is allowed
            if sender_ip not in self.allowed_sources:
                return False

            # Check if the sender key matches the allowed public key
            if self.allowed_sources[sender_ip] != sender_key:
                return False

            # Verify the integrity of the transaction hash
            calculated_hash = hashlib.sha256(json.dumps(transaction_data).encode()).hexdigest()
            if calculated_hash != transaction_hash:
                return False

            return True
        except Exception as e:
            # Log the error (in production, use a logging service)
            print(f"Error verifying transaction: {e}")
            return False


class BlockchainNode:
    """
    Class representing a blockchain node integrated with edge filtering hardware.
    """

    def __init__(self, node_id: str, edge_filter: EdgeFilter):
        """
        Initialize the blockchain node.
        
        :param node_id: Unique identifier for the node.
        :param edge_filter: Instance of the EdgeFilter class.
        """
        self.node_id = node_id
        self.edge_filter = edge_filter
        self.blockchain = []  # List to store the blocks
        self.unconfirmed_transactions = []  # Pool of unconfirmed transactions

    async def receive_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Receive and process an incoming transaction.
        
        :param transaction: The incoming transaction as a dictionary.
        """
        try:
            # Verify the transaction using the edge filter
            if self.edge_filter.verify_transaction(transaction):
                self.unconfirmed_transactions.append(transaction)
                print(f"Transaction added to unconfirmed pool: {transaction}")
            else:
                print("Transaction rejected by edge filter.")
        except Exception as e:
            # Log the error
            print(f"Error receiving transaction: {e}")

    async def create_block(self) -> None:
        """
        Create a new block and add it to the blockchain.
        """
        try:
            if not self.unconfirmed_transactions:
                print("No transactions to process.")
                return

            # Create a block with unconfirmed transactions
            block = {
                'block_id': len(self.blockchain) + 1,
                'transactions': self.unconfirmed_transactions,
                'previous_hash': self.blockchain[-1]['hash'] if self.blockchain else None,
            }
            block['hash'] = hashlib.sha256(json.dumps(block).encode()).hexdigest()

            # Add the block to the blockchain
            self.blockchain.append(block)
            self.unconfirmed_transactions = []
            print(f"Block created and added to blockchain: {block}")
        except Exception as e:
            # Log the error
            print(f"Error creating block: {e}")


# Example configuration for edge filtering hardware
allowed_sources = {
    "192.168.1.100": "public_key_1",
    "192.168.1.101": "public_key_2",
}

# Initialize edge filter and blockchain node
edge_filter = EdgeFilter(allowed_sources)
blockchain_node = BlockchainNode(node_id="node_1", edge_filter=edge_filter)

# Example usage in an asynchronous event loop
async def main():
    # Simulated incoming transaction
    transaction_1 = {
        'sender_ip': '192.168.1.100',
        'sender_key': 'public_key_1',
        'data': {'amount': 100, 'recipient': 'wallet_2'},
        'hash': hashlib.sha256(json.dumps({'amount': 100, 'recipient': 'wallet_2'}).encode()).hexdigest(),
    }

    transaction_2 = {
        'sender_ip': '192.168.1.102',  # Unauthorized IP
        'sender_key': 'public_key_3',
        'data': {'amount': 50, 'recipient': 'wallet_3'},
        'hash': hashlib.sha256(json.dumps({'amount': 50, 'recipient': 'wallet_3'}).encode()).hexdigest(),
    }

    # Process transactions
    await blockchain_node.receive_transaction(transaction_1)
    await blockchain_node.receive_transaction(transaction_2)

    # Create a block
    await blockchain_node.create_block()

# Run the event loop
asyncio.run(main())
```
