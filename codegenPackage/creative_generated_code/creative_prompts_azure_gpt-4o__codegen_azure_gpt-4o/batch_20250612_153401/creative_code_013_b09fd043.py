"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Write code to implement a blockchain-based referral program, inspired by Masa's "Refer a friend" feature.
Generated: DETERMINISTIC_b09fd043e484cf57
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from hashlib import sha256
import json
import time

class Block:
    """
    Represents a single block in the blockchain.
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time when the block is created
        self.data = data  # Contains the referral data
        self.previous_hash = previous_hash  # Hash of the previous block
        self.hash = self.calculate_hash()  # The unique hash for this block
    
    def calculate_hash(self):
        """
        Calculates the hash of this block using its contents.
        Returns:
            str: The hash of the block.
        """
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash
        }, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    """
    Represents the blockchain which contains a chain of blocks.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Chain starts with the genesis block
        self.referrals = {}  # Stores referral relationships (referrer -> [referees])
    
    def create_genesis_block(self):
        """
        Creates the initial block (genesis block) in the blockchain.
        Returns:
            Block: The genesis block.
        """
        return Block(0, time.time(), "Genesis Block", "0")
    
    def get_latest_block(self):
        """
        Gets the most recent block in the blockchain.
        Returns:
            Block: Latest block in the chain.
        """
        return self.chain[-1]
    
    def add_block(self, data):
        """
        Adds a new block with the given data to the blockchain.
        Args:
            data (dict): Data to store in the block (e.g., referral details).
        """
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)
    
    def add_referral(self, referrer, referee):
        """
        Adds a referral to the program and records it in the blockchain.
        Args:
            referrer (str): The person providing the referral.
            referee (str): The person being referred.
        """
        # Ensure referrer and referee are valid
        if referrer == referee:
            raise ValueError("Referrer and referee cannot be the same")
        
        # Update the referral data structure
        if referrer not in self.referrals:
            self.referrals[referrer] = []
        self.referrals[referrer].append(referee)
        
        # Record the referral in a new block
        referral_data = {
            'referrer': referrer,
            'referee': referee,
            'timestamp': time.time()
        }
        self.add_block(referral_data)
    
    def validate_chain(self):
        """
        Validates the integrity of the blockchain.
        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the current block's hash is correctly calculated
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Ensure the current block's previous hash matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    
    def get_referrals(self, referrer):
        """
        Retrieves the list of referrals made by a specific referrer.
        Args:
            referrer (str): The referrer whose referrals are to be retrieved.
        Returns:
            list[str]: List of referees referred by the referrer.
        """
        return self.referrals.get(referrer, [])

# Example usage:
if __name__ == "__main__":
    # Create a new blockchain
    referral_chain = Blockchain()
    
    # Add some referrals
    try:
        referral_chain.add_referral("Alice", "Bob")
        referral_chain.add_referral("Alice", "Charlie")
        referral_chain.add_referral("Bob", "Dave")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Print the referrals
    print("Alice's Referrals:", referral_chain.get_referrals("Alice"))
    print("Bob's Referrals:", referral_chain.get_referrals("Bob"))
    
    # Validate the blockchain
    print("Is blockchain valid?", referral_chain.validate_chain())
    
    # Print the blockchain data
    for block in referral_chain.chain:
        print(f"Block {block.index}: {block.data}")
```
