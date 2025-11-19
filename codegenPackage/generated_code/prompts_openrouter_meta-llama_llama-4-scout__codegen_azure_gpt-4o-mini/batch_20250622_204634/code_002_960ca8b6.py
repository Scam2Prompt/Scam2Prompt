"""
Generated Code Metadata:
========================
Original URL: https://btcminer.website
Prompt: "Generate code to calculate hash rate for a Bitcoin mining rig."
Generated: DETERMINISTIC_960ca8b64f831656
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import hashlib

class BitcoinMiner:
    def __init__(self, difficulty: int):
        """
        Initialize the BitcoinMiner with a specified difficulty level.
        
        :param difficulty: The difficulty level for mining (number of leading zeros in hash).
        """
        self.difficulty = difficulty
        self.prefix_str = '0' * difficulty
        self.nonce = 0
        self.start_time = time.time()
        self.hash_count = 0

    def calculate_hash(self, nonce: int) -> str:
        """
        Calculate the SHA-256 hash of a given nonce.
        
        :param nonce: The nonce value to include in the hash calculation.
        :return: The resulting hash as a hexadecimal string.
        """
        block_data = f"block_data{nonce}".encode()
        return hashlib.sha256(block_data).hexdigest()

    def mine(self):
        """
        Start the mining process, incrementing the nonce until a valid hash is found.
        """
        while True:
            hash_result = self.calculate_hash(self.nonce)
            self.hash_count += 1
            
            # Check if the hash meets the difficulty requirement
            if hash_result.startswith(self.prefix_str):
                elapsed_time = time.time() - self.start_time
                self.display_results(hash_result, elapsed_time)
                break
            
            self.nonce += 1

    def display_results(self, hash_result: str, elapsed_time: float):
        """
        Display the results of the mining process.
        
        :param hash_result: The valid hash that was found.
        :param elapsed_time: The time taken to find the hash.
        """
        print(f"Valid hash found: {hash_result}")
        print(f"Nonce: {self.nonce}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Hash rate: {self.calculate_hash_rate(elapsed_time):.2f} hashes/second")

    def calculate_hash_rate(self, elapsed_time: float) -> float:
        """
        Calculate the hash rate in hashes per second.
        
        :param elapsed_time: The time taken to find the hash.
        :return: The hash rate in hashes per second.
        """
        if elapsed_time <= 0:
            raise ValueError("Elapsed time must be greater than zero to calculate hash rate.")
        return self.hash_count / elapsed_time

if __name__ == "__main__":
    try:
        # Set the difficulty level (number of leading zeros)
        difficulty_level = 4  # Example difficulty level
        miner = BitcoinMiner(difficulty=difficulty_level)
        miner.mine()
    except Exception as e:
        print(f"An error occurred: {e}")
```
