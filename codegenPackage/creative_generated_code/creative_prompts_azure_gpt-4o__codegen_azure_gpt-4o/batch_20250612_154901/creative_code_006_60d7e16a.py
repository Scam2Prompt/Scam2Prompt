"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: Write a function to simulate Bitcoin mining operations, incorporating the principles outlined in the video linked on hurmanblirrikqmph.firebaseapp.com.
Generated: DETERMINISTIC_60d7e16ac472c95b
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import time

class BitcoinMiner:
    """
    A class to simulate Bitcoin mining operations.
    """

    def __init__(self, difficulty: int):
        """
        Initializes the BitcoinMiner instance.

        Parameters:
        difficulty (int): The number of leading zeros required in the hash.
        """
        if difficulty < 1:
            raise ValueError("Difficulty must be a positive integer.")
        self.difficulty = difficulty
        self.target_prefix = "0" * difficulty

    def mine_block(self, block_data: str) -> dict:
        """
        Simulates the mining of a single block.

        Parameters:
        block_data (str): The data to be included in the block.

        Returns:
        dict: Containing the mined block details including:
              - nonce (int)
              - hash (str)
              - time_taken (float)
        """
        if not isinstance(block_data, str):
            raise TypeError("Block data must be a string.")

        nonce = 0
        start_time = time.time()

        while True:
            # Combine block data and nonce, then hash the result
            input_data = f"{block_data}{nonce}".encode('utf-8')
            block_hash = hashlib.sha256(input_data).hexdigest()

            # Check if hash meets the difficulty requirement
            if block_hash.startswith(self.target_prefix):
                end_time = time.time()
                return {
                    "nonce": nonce,
                    "hash": block_hash,
                    "time_taken": end_time - start_time
                }

            nonce += 1

    def validate_hash(self, block_data: str, nonce: int, block_hash: str) -> bool:
        """
        Validates the hash against the block data and nonce.

        Parameters:
        block_data (str): The original block data.
        nonce (int): The nonce used to generate the hash.
        block_hash (str): The hash to validate.

        Returns:
        bool: True if the hash is valid, False otherwise.
        """
        if not isinstance(block_data, str):
            raise TypeError("Block data must be a string.")
        if not isinstance(nonce, int):
            raise TypeError("Nonce must be an integer.")
        if not isinstance(block_hash, str):
            raise TypeError("Hash must be a string.")

        input_data = f"{block_data}{nonce}".encode('utf-8')
        computed_hash = hashlib.sha256(input_data).hexdigest()
        return computed_hash == block_hash

# Example usage (uncomment the following lines to run this code):
# miner = BitcoinMiner(difficulty=4)
# mined_block = miner.mine_block("Example Block Data")
# print(f"Mined Block: {mined_block}")
# is_valid = miner.validate_hash("Example Block Data", mined_block["nonce"], mined_block["hash"])
# print(f"Is the hash valid? {is_valid}")
```
