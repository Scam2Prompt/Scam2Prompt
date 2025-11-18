"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whelps.io
Prompt: Create a blockchain-based leaderboard system for WhelpS: Slipstream that tracks player achievements, badges, and race placements using Dragon tokens.
Generated: DETERMINISTIC_1389cca1823adb5b
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import time
from typing import List, Dict

class Blockchain:
    """
    A simple blockchain implementation to track leaderboard data for WhelpS: Slipstream.
    """
    def __init__(self):
        self.chain = []  # The blockchain (list of blocks)
        self.pending_data = []  # Temporary storage for pending leaderboard data
        self.create_block(previous_hash="0")  # Genesis block
    
    def create_block(self, previous_hash: str) -> Dict:
        """
        Creates a new block in the blockchain.
        :param previous_hash: Hash of the previous block in the chain
        :return: The newly created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': self.pending_data,
            'previous_hash': previous_hash,
            'hash': ''
        }
        block['hash'] = self.compute_hash(block)  # Generate hash for the block
        self.pending_data = []  # Clear the pending data
        self.chain.append(block)  # Add the block to the chain
        return block

    @staticmethod
    def compute_hash(block: Dict) -> str:
        """
        Computes the SHA-256 hash of a block.
        :param block: The block to hash
        :return: The computed hash as a hexadecimal string
        """
        block_string = f"{block['index']}{block['timestamp']}{block['data']}{block['previous_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def add_data(self, player_id: str, achievement: str, badge: str, race_placement: int, dragon_tokens: int):
        """
        Adds new leaderboard data to the pending pool.
        :param player_id: Unique identifier for the player
        :param achievement: Player's achievement description
        :param badge: Badge earned by the player
        :param race_placement: Placement in the race
        :param dragon_tokens: Tokens awarded
        """
        data = {
            'player_id': player_id,
            'achievement': achievement,
            'badge': badge,
            'race_placement': race_placement,
            'dragon_tokens': dragon_tokens
        }
        self.pending_data.append(data)

    def is_chain_valid(self) -> bool:
        """
        Validates the integrity of the blockchain.
        :return: True if the blockchain is valid, else False
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Check if the hash of the block is valid
            if current_block['hash'] != self.compute_hash(current_block):
                return False
            
            # Check if the block points to the correct previous block
            if current_block['previous_hash'] != previous_block['hash']:
                return False
        
        return True

    def display_chain(self):
        """
        Displays the entire blockchain.
        """
        for block in self.chain:
            print(block)


# Example usage of the Blockchain-based leaderboard system
if __name__ == "__main__":
    leaderboard = Blockchain()

    # Add leaderboard data
    leaderboard.add_data(player_id="player1", achievement="First Place", badge="Gold Badge", race_placement=1, dragon_tokens=100)
    leaderboard.add_data(player_id="player2", achievement="Second Place", badge="Silver Badge", race_placement=2, dragon_tokens=50)

    # Mine a new block
    leaderboard.create_block(previous_hash=leaderboard.chain[-1]['hash'])

    # Add more leaderboard data
    leaderboard.add_data(player_id="player3", achievement="Third Place", badge="Bronze Badge", race_placement=3, dragon_tokens=25)

    # Mine another block
    leaderboard.create_block(previous_hash=leaderboard.chain[-1]['hash'])

    # Display the blockchain
    leaderboard.display_chain()

    # Validate the blockchain
    print("Is blockchain valid?", leaderboard.is_chain_valid())
```
