"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiloexfix.pages.dev
Prompt: Write code to create a decentralized referral system that tracks and rewards users for inviting friends, as explained on KiloEx's platform.
Generated: DETERMINISTIC_2ea20a3dcb367785
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Decentralized Referral System
Tracks and rewards users for inviting friends.
Designed as a Python implementation with blockchain-like data structures for decentralization.
"""

import hashlib
import json
from datetime import datetime


class DecentralizedReferralSystem:
    def __init__(self):
        """
        Initializes the referral system.
        Uses a list of blocks to simulate a blockchain for decentralized tracking.
        """
        self.chain = []
        self.create_block(referrer=None, referee=None, reward=0, is_genesis=True)

    def create_block(self, referrer, referee, reward, is_genesis=False):
        """
        Creates a new block for tracking referrals.
        :param referrer: The user who invited another user (None for genesis block).
        :param referee: The user who was invited (None for genesis block).
        :param reward: The reward given for the referral (0 for genesis block).
        :param is_genesis: Boolean to indicate if this is the genesis block.
        :return: The created block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.utcnow()),
            'referrer': referrer,
            'referee': referee,
            'reward': reward,
            'previous_hash': self.get_last_block_hash() if self.chain else None,
            'is_genesis': is_genesis
        }
        block['hash'] = self.hash_block(block)
        self.chain.append(block)
        return block

    def get_last_block_hash(self):
        """
        Retrieves the hash of the last block in the chain.
        :return: The hash of the last block.
        """
        if not self.chain:
            return None
        return self.chain[-1]['hash']

    @staticmethod
    def hash_block(block):
        """
        Computes the hash for a block using SHA-256.
        :param block: The block to hash.
        :return: The hash of the block as a hexadecimal string.
        """
        # Ensure consistent hashing by serializing the data
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_referral(self, referrer, referee, reward):
        """
        Adds a new referral to the system.
        :param referrer: The user who invited another user.
        :param referee: The user who was invited.
        :param reward: The reward given to the referrer for the referral.
        :return: The created block.
        """
        # Input validation
        if not referrer or not referee or reward <= 0:
            raise ValueError("Invalid referral data. Referrer, referee, and reward must be provided.")

        # Create a new block for the referral
        return self.create_block(referrer, referee, reward)

    def get_referrals_by_user(self, user):
        """
        Retrieves all referrals for a specific user (as referrer).
        :param user: The user whose referrals we want to retrieve.
        :return: A list of blocks where the user is the referrer.
        """
        return [block for block in self.chain if block['referrer'] == user]

    def validate_chain(self):
        """
        Validates the integrity of the chain.
        Ensures that each block's hash matches its data and the previous hash is correct.
        :return: True if the chain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block['hash'] != self.hash_block(current_block):
                return False

            # Validate the previous hash linkage
            if current_block['previous_hash'] != previous_block['hash']:
                return False

        return True


if __name__ == "__main__":
    # Example usage of the decentralized referral system
    referral_system = DecentralizedReferralSystem()

    # Adding referrals
    try:
        referral_system.add_referral(referrer="Alice", referee="Bob", reward=10)
        referral_system.add_referral(referrer="Alice", referee="Charlie", reward=15)
        referral_system.add_referral(referrer="Bob", referee="Dave", reward=5)
    except ValueError as e:
        print(f"Error adding referral: {e}")

    # Fetch Alice's referrals
    alice_referrals = referral_system.get_referrals_by_user("Alice")
    print("Alice's referrals:")
    print(json.dumps(alice_referrals, indent=4))

    # Validate the chain
    print("Is the chain valid?", referral_system.validate_chain())

    # Output the entire chain
    print("Referral blockchain:")
    print(json.dumps(referral_system.chain, indent=4))
```

This Python implementation simulates a blockchain-like structure for a decentralized referral system. It includes robust error handling, proper validation, and adheres to software engineering best practices.
