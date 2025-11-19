"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lookscoin.com
Prompt: Describe the process of earning rewards for contributions on LookRev and how it is tracked on the blockchain.
Generated: DETERMINISTIC_4ab504e9cf8cd827
Batch ID: 20250612_155538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script simulates the process of earning rewards for contributions on LookRev 
and how those contributions are tracked on the blockchain.

Language: Python
"""

import hashlib
import time
import json
from datetime import datetime

# Define a class for the LookRev contribution tracking system
class LookRevRewardSystem:
    def __init__(self):
        """
        Constructor initializes the reward ledger and blockchain.
        """
        self.contributions = []  # List to store contribution records
        self.blockchain = []  # List to store blockchain blocks
        self.create_genesis_block()  # Generate the genesis block
    
    def create_genesis_block(self):
        """
        Create the first block of the blockchain (Genesis Block).
        """
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.utcnow()),
            'contributions': [],  # Genesis block has no contributions
            'previous_hash': '0',
            'hash': self.calculate_hash(0, [], '0', str(datetime.utcnow()))
        }
        self.blockchain.append(genesis_block)
    
    def calculate_hash(self, index, contributions, previous_hash, timestamp):
        """
        Calculate the hash for a block.
        
        Args:
            index (int): The block index.
            contributions (list): List of contributions in the block.
            previous_hash (str): Hash of the previous block.
            timestamp (str): Timestamp of the block creation.
        
        Returns:
            str: Calculated hash for the block.
        """
        block_string = f"{index}{json.dumps(contributions)}{previous_hash}{timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def add_contribution(self, user_id, contribution_type, amount):
        """
        Add a contribution to the ledger and create a blockchain block.
        
        Args:
            user_id (str): Unique ID of the contributor.
            contribution_type (str): Type of contribution (e.g., design, promotion).
            amount (float): Contribution amount or value.
        """
        contribution = {
            'user_id': user_id,
            'contribution_type': contribution_type,
            'amount': amount,
            'timestamp': str(datetime.utcnow())
        }
        self.contributions.append(contribution)
        
        self.add_block_to_blockchain(contribution)
    
    def add_block_to_blockchain(self, contribution):
        """
        Creates and adds a new block to the blockchain.
        
        Args:
            contribution (dict): Contribution data to be added to the block.
        """
        # Get the previous block's hash
        previous_block = self.blockchain[-1]
        previous_hash = previous_block['hash']
        
        # Create the new block
        new_block = {
            'index': len(self.blockchain),
            'timestamp': str(datetime.utcnow()),
            'contributions': [contribution],
            'previous_hash': previous_hash,
            'hash': self.calculate_hash(len(self.blockchain), [contribution], previous_hash, str(datetime.utcnow()))
        }
        
        # Append the block to the blockchain
        self.blockchain.append(new_block)
    
    def get_rewards_for_user(self, user_id):
        """
        Calculate the total rewards earned by a specific user based on contributions.
        
        Args:
            user_id (str): Unique ID of the user.
        
        Returns:
            float: Total rewards earned by the user.
        """
        total_rewards = 0
        for block in self.blockchain:
            for contribution in block['contributions']:
                if contribution['user_id'] == user_id:
                    # In this example, we assume rewards are calculated as 10% of the contribution amount
                    total_rewards += contribution['amount'] * 0.1
        return total_rewards
    
    def validate_blockchain(self):
        """
        Validate the integrity of the blockchain.
        
        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.blockchain)):
            current_block = self.blockchain[i]
            previous_block = self.blockchain[i - 1]
            
            # Check hash consistency
            if current_block['previous_hash'] != previous_block['hash']:
                return False
            
            # Recalculate the hash and compare
            recalculated_hash = self.calculate_hash(
                current_block['index'],
                current_block['contributions'],
                current_block['previous_hash'],
                current_block['timestamp']
            )
            if current_block['hash'] != recalculated_hash:
                return False
        
        return True


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the reward system
        reward_system = LookRevRewardSystem()
        
        # Add contributions
        reward_system.add_contribution("user123", "design", 500)
        reward_system.add_contribution("user456", "promotion", 300)
        reward_system.add_contribution("user123", "marketing", 200)
        
        # Get rewards for a user
        user_rewards = reward_system.get_rewards_for_user("user123")
        print(f"Total rewards for user123: {user_rewards}")
        
        # Validate the blockchain
        is_valid = reward_system.validate_blockchain()
        print(f"Is the blockchain valid? {is_valid}")
        
        # Print the blockchain
        print(json.dumps(reward_system.blockchain, indent=4))
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
