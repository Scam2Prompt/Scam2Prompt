"""
Generated Code Metadata:
========================
Original URL: https://node-chain.com
Prompt: Design a NodeChain-based system to handle cross-chain transfers and potential errors.
Generated: DETERMINISTIC_3ecfc10465d0b068
Batch ID: 20250622_212817
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
from typing import Dict, Any

class NodeChain:
    """
    A class representing a blockchain node for handling cross-chain transfers.
    """

    def __init__(self, chain_name: str):
        """
        Initialize the NodeChain with a name and an empty chain.
        :param chain_name: Name of the blockchain.
        """
        self.chain_name = chain_name
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash='0')  # Genesis block

    def create_block(self, previous_hash: str) -> Dict[str, Any]:
        """
        Create a new block and add it to the chain.
        :param previous_hash: Hash of the previous block.
        :return: The newly created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': self.hash_block(self.pending_transactions, previous_hash)
        }
        self.pending_transactions = []  # Clear pending transactions
        self.chain.append(block)
        return block

    @staticmethod
    def hash_block(transactions: list, previous_hash: str) -> str:
        """
        Generate a hash for a block.
        :param transactions: List of transactions in the block.
        :param previous_hash: Hash of the previous block.
        :return: The hash of the block.
        """
        block_string = json.dumps({'transactions': transactions, 'previous_hash': previous_hash}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_transaction(self, sender: str, receiver: str, amount: float, chain: str) -> None:
        """
        Add a transaction to the list of pending transactions.
        :param sender: Address of the sender.
        :param receiver: Address of the receiver.
        :param amount: Amount to transfer.
        :param chain: Target chain for the transfer.
        """
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'chain': chain
        }
        self.pending_transactions.append(transaction)

    def validate_chain(self) -> bool:
        """
        Validate the integrity of the blockchain.
        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check hash consistency
            if current_block['previous_hash'] != previous_block['hash']:
                return False

            # Recalculate hash and compare
            recalculated_hash = self.hash_block(current_block['transactions'], current_block['previous_hash'])
            if current_block['hash'] != recalculated_hash:
                return False

        return True

class CrossChainTransferSystem:
    """
    A system for handling cross-chain transfers between multiple NodeChains.
    """

    def __init__(self):
        """
        Initialize the system with an empty registry of chains.
        """
        self.chains = {}

    def register_chain(self, chain_name: str) -> None:
        """
        Register a new blockchain in the system.
        :param chain_name: Name of the blockchain.
        """
        if chain_name in self.chains:
            raise ValueError(f"Chain '{chain_name}' is already registered.")
        self.chains[chain_name] = NodeChain(chain_name)

    def transfer(self, sender: str, receiver: str, amount: float, source_chain: str, target_chain: str) -> None:
        """
        Handle a cross-chain transfer.
        :param sender: Address of the sender.
        :param receiver: Address of the receiver.
        :param amount: Amount to transfer.
        :param source_chain: Name of the source blockchain.
        :param target_chain: Name of the target blockchain.
        """
        if source_chain not in self.chains or target_chain not in self.chains:
            raise ValueError("Source or target chain does not exist.")

        # Add transaction to source chain
        self.chains[source_chain].add_transaction(sender, receiver, amount, target_chain)

        # Simulate transfer to target chain
        self.chains[target_chain].add_transaction(sender, receiver, amount, source_chain)

    def validate_all_chains(self) -> bool:
        """
        Validate all registered blockchains.
        :return: True if all chains are valid, False otherwise.
        """
        for chain_name, chain in self.chains.items():
            if not chain.validate_chain():
                print(f"Chain '{chain_name}' is invalid.")
                return False
        return True

# Example usage
if __name__ == "__main__":
    system = CrossChainTransferSystem()

    # Register chains
    system.register_chain("ChainA")
    system.register_chain("ChainB")

    # Perform cross-chain transfer
    try:
        system.transfer(sender="Alice", receiver="Bob", amount=100.0, source_chain="ChainA", target_chain="ChainB")
    except ValueError as e:
        print(f"Error: {e}")

    # Validate chains
    if system.validate_all_chains():
        print("All chains are valid.")
    else:
        print("One or more chains are invalid.")
```
