"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiminer.website
Prompt: Explain the process of Bitcoin mining on the Bitspeed platform, including how the Proof of Work algorithm is utilized.
Generated: DETERMINISTIC_cf2f863d08653846
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinMiner:
    """
    A class to represent a Bitcoin miner on the Bitspeed platform.
    
    Attributes:
        difficulty (int): The current mining difficulty level.
        block_reward (float): The reward for successfully mining a block.
        blockchain (list): A list representing the blockchain.
    """
    
    def __init__(self, difficulty: int, block_reward: float):
        """
        Initializes the BitcoinMiner with the given mining difficulty and block reward.
        
        Args:
            difficulty (int): The difficulty level for mining.
            block_reward (float): The reward for mining a new block.
        """
        self.difficulty = difficulty
        self.block_reward = block_reward
        self.blockchain = []

    def calculate_nonce(self, block_data: str) -> int:
        """
        Calculates a nonce that satisfies the Proof of Work requirement.
        
        Args:
            block_data (str): The data to be included in the block.
        
        Returns:
            int: A valid nonce that meets the difficulty criteria.
        """
        nonce = 0
        prefix_str = '0' * self.difficulty  # Create a string of '0's based on difficulty
        
        while True:
            # Create a block header using block data and nonce
            block_header = f"{block_data}{nonce}".encode()
            hash_result = self.hash_block(block_header)
            if hash_result.startswith(prefix_str):
                return nonce  # Return the valid nonce
            nonce += 1

    @staticmethod
    def hash_block(block_header: bytes) -> str:
        """
        Computes the SHA-256 hash of the given block header.
        
        Args:
            block_header (bytes): The block header to be hashed.
        
        Returns:
            str: The hexadecimal representation of the hash.
        """
        import hashlib
        return hashlib.sha256(block_header).hexdigest()

    def mine_block(self, block_data: str) -> dict:
        """
        Mines a new block and adds it to the blockchain.
        
        Args:
            block_data (str): The data to be included in the new block.
        
        Returns:
            dict: A dictionary containing the block data, nonce, and hash.
        """
        try:
            nonce = self.calculate_nonce(block_data)
            block_header = f"{block_data}{nonce}".encode()
            block_hash = self.hash_block(block_header)
            new_block = {
                'data': block_data,
                'nonce': nonce,
                'hash': block_hash,
                'reward': self.block_reward
            }
            self.blockchain.append(new_block)  # Add new block to the blockchain
            return new_block
        except Exception as e:
            # Handle exceptions during mining
            print(f"Error while mining block: {e}")
            return None

# Example usage
if __name__ == "__main__":
    miner = BitcoinMiner(difficulty=4, block_reward=6.25)
    block_data = "Transaction Data for Block"
    mined_block = miner.mine_block(block_data)

    if mined_block:
        print("Mined a new block:")
        print(mined_block)
    else:
        print("Block mining failed.")
```
