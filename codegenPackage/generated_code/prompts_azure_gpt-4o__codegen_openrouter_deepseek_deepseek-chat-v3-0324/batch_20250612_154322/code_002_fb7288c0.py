"""
Generated Code Metadata:
========================
Original URL: https://dysnix.org
Prompt: Generate code using a blockchain-based solution to ensure transparency in donation tracking, similar to Dysnix's transparent reporting of funds used for vehicle purchases.
Generated: DETERMINISTIC_fb7288c07226bce6
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from hashlib import sha256
import json
from time import time
from typing import List, Dict, Any, Optional
import uuid

class Block:
    """
    A block in the blockchain containing donation transaction data.
    """
    
    def __init__(self, index: int, transactions: List[Dict[str, Any]], timestamp: float, previous_hash: str):
        """
        Initialize a new block.
        
        Args:
            index: The index of the block in the chain.
            transactions: List of donation transactions.
            timestamp: Time when the block was created.
            previous_hash: Hash of the previous block in the chain.
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Compute the SHA-256 hash of the block.
        
        Returns:
            The hexadecimal digest of the block's hash.
        """
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int) -> None:
        """
        Mine the block by finding a hash that meets the difficulty criteria.
        
        Args:
            difficulty: The number of leading zeros required in the hash.
        """
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()


class Blockchain:
    """
    A blockchain to track donation transactions transparently.
    """
    
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain: List[Block] = []
        self.pending_transactions: List[Dict[str, Any]] = []
        self.difficulty = 2  # Adjust difficulty for mining speed
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Create the genesis block (first block in the chain).
        """
        genesis_block = Block(0, [], time(), "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Block:
        """
        Get the last block in the chain.
        
        Returns:
            The last block in the chain.
        """
        return self.chain[-1]

    def add_transaction(self, donor: str, recipient: str, amount: float, purpose: str) -> int:
        """
        Add a new donation transaction to the pending transactions list.
        
        Args:
            donor: The donor's identifier.
            recipient: The recipient's identifier.
            amount: The donation amount.
            purpose: The purpose of the donation.
            
        Returns:
            The index of the block that will hold this transaction.
        """
        if not all([donor, recipient, purpose]):
            raise ValueError("Donor, recipient, and purpose must be provided.")
        if amount <= 0:
            raise ValueError("Donation amount must be positive.")
            
        transaction = {
            "id": str(uuid.uuid4()),
            "donor": donor,
            "recipient": recipient,
            "amount": amount,
            "purpose": purpose,
            "timestamp": time()
        }
        self.pending_transactions.append(transaction)
        return self.last_block.index + 1

    def mine_pending_transactions(self) -> None:
        """
        Mine all pending transactions into a new block and add it to the chain.
        """
        if not self.pending_transactions:
            raise ValueError("No pending transactions to mine.")
            
        new_block = Block(
            index=len(self.chain),
            transactions=self.pending_transactions,
            timestamp=time(),
            previous_hash=self.last_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []

    def is_chain_valid(self) -> bool:
        """
        Validate the integrity of the blockchain.
        
        Returns:
            True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_transactions_by_donor(self, donor: str) -> List[Dict[str, Any]]:
        """
        Retrieve all transactions made by a specific donor.
        
        Args:
            donor: The donor's identifier.
            
        Returns:
            List of transactions made by the donor.
        """
        transactions = []
        for block in self.chain:
            for tx in block.transactions:
                if tx["donor"] == donor:
                    transactions.append(tx)
        return transactions

    def get_transactions_by_recipient(self, recipient: str) -> List[Dict[str, Any]]:
        """
        Retrieve all transactions received by a specific recipient.
        
        Args:
            recipient: The recipient's identifier.
            
        Returns:
            List of transactions received by the recipient.
        """
        transactions = []
        for block in self.chain:
            for tx in block.transactions:
                if tx["recipient"] == recipient:
                    transactions.append(tx)
        return transactions

    def get_all_transactions(self) -> List[Dict[str, Any]]:
        """
        Retrieve all transactions in the blockchain.
        
        Returns:
            List of all transactions.
        """
        transactions = []
        for block in self.chain:
            transactions.extend(block.transactions)
        return transactions


# Example usage
if __name__ == "__main__":
    # Initialize blockchain
    donation_blockchain = Blockchain()
    
    # Add some transactions
    donation_blockchain.add_transaction(
        donor="Alice",
        recipient="Charity A",
        amount=100.0,
        purpose="Vehicle purchase"
    )
    donation_blockchain.add_transaction(
        donor="Bob",
        recipient="Charity B",
        amount=200.0,
        purpose="Medical supplies"
    )
    
    # Mine the pending transactions
    donation_blockchain.mine_pending_transactions()
    
    # Add more transactions
    donation_blockchain.add_transaction(
        donor="Charlie",
        recipient="Charity A",
        amount=50.0,
        purpose="Vehicle maintenance"
    )
    donation_blockchain.mine_pending_transactions()
    
    # Check chain validity
    print(f"Is blockchain valid? {donation_blockchain.is_chain_valid()}")
    
    # Get all transactions
    all_transactions = donation_blockchain.get_all_transactions()
    print("All transactions:")
    for tx in all_transactions:
        print(tx)
    
    # Get transactions by donor
    alice_transactions = donation_blockchain.get_transactions_by_donor("Alice")
    print("\nAlice's donations:")
    for tx in alice_transactions:
        print(tx)
    
    # Get transactions by recipient
    charity_a_transactions = donation_blockchain.get_transactions_by_recipient("Charity A")
    print("\nDonations to Charity A:")
    for tx in charity_a_transactions:
        print(tx)
```
