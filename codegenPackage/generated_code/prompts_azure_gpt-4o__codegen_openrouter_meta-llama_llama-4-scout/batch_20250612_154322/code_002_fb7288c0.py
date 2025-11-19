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
import hashlib
import time
from typing import Dict, List

class Block:
    def __init__(self, index: int, previous_hash: str, timestamp: float, 
                 donor: str, amount: float, recipient: str):
        """
        Initialize a new block.

        Args:
        index (int): The index of the block in the chain.
        previous_hash (str): The hash of the previous block.
        timestamp (float): The timestamp of the block.
        donor (str): The donor's address.
        amount (float): The amount donated.
        recipient (str): The recipient's address.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.donor = donor
        self.amount = amount
        self.recipient = recipient
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Calculate the hash of the block.

        Returns:
        str: The hash of the block.
        """
        data = str(self.index) + self.previous_hash + str(self.timestamp) + self.donor + str(self.amount) + self.recipient
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        """
        Create the genesis block.

        Returns:
        Block: The genesis block.
        """
        return Block(0, "0", time.time(), "Genesis", 0, "Genesis")

    def get_latest_block(self) -> Block:
        """
        Get the latest block in the chain.

        Returns:
        Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block: Block):
        """
        Add a new block to the chain.

        Args:
        new_block (Block): The new block to add.
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Check if the chain is valid.

        Returns:
        bool: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


class DonationTracker:
    def __init__(self):
        """
        Initialize a new donation tracker.
        """
        self.blockchain = Blockchain()
        self.donations: Dict[str, float] = {}

    def make_donation(self, donor: str, amount: float, recipient: str):
        """
        Make a donation.

        Args:
        donor (str): The donor's address.
        amount (float): The amount donated.
        recipient (str): The recipient's address.
        """
        try:
            if donor not in self.donations:
                self.donations[donor] = 0
            self.donations[donor] += amount

            new_block = Block(len(self.blockchain.chain), self.blockchain.get_latest_block().hash, 
                              time.time(), donor, amount, recipient)
            self.blockchain.add_block(new_block)

            if not self.blockchain.is_chain_valid():
                raise Exception("Invalid blockchain")

            print(f"Donation made: {donor} -> {recipient} : {amount}")
        except Exception as e:
            print(f"Error making donation: {e}")

    def get_donation_history(self) -> List[Dict]:
        """
        Get the donation history.

        Returns:
        List[Dict]: A list of dictionaries containing the donation history.
        """
        history = []
        for block in self.blockchain.chain:
            if block.donor != "Genesis":
                history.append({
                    "donor": block.donor,
                    "amount": block.amount,
                    "recipient": block.recipient,
                    "timestamp": block.timestamp
                })
        return history


# Example usage
tracker = DonationTracker()
tracker.make_donation("Alice", 10, "Bob")
tracker.make_donation("Charlie", 20, "David")
print(tracker.get_donation_history())
```
