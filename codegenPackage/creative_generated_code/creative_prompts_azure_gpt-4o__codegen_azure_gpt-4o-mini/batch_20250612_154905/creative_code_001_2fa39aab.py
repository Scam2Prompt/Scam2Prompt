"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Generate code to implement a Proof of Work (PoW) algorithm for Bitcoin mining, ensuring compatibility with Bitspeed's mining platform features.
Generated: DETERMINISTIC_2fa39aabb25ac5ee
Batch ID: 20250612_154905
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
import struct

class ProofOfWork:
    def __init__(self, block_data, difficulty_bits):
        """
        Initializes the ProofOfWork instance.
        
        :param block_data: The data of the block to be mined.
        :param difficulty_bits: The difficulty level for mining.
        """
        self.block_data = block_data
        self.difficulty_bits = difficulty_bits
        self.nonce = 0
        self.difficulty_target = self.calculate_difficulty_target()

    def calculate_difficulty_target(self):
        """
        Calculates the target value for mining based on the difficulty bits.
        
        :return: The target value as a hexadecimal string.
        """
        target = 2 ** (256 - self.difficulty_bits)
        return target

    def calculate_hash(self, nonce):
        """
        Calculates the SHA-256 hash of the block data combined with the nonce.
        
        :param nonce: The nonce value to include in the hash calculation.
        :return: The hexadecimal representation of the hash.
        """
        block_header = (self.block_data + struct.pack("<L", nonce)).encode()
        return hashlib.sha256(hashlib.sha256(block_header).digest()).hexdigest()

    def mine(self):
        """
        Executes the mining process by finding a valid nonce that meets the difficulty target.
        
        :return: A tuple containing the valid nonce and the corresponding hash.
        """
        start_time = time.time()
        print("Mining...")

        while True:
            # Calculate the hash for the current nonce
            hash_result = self.calculate_hash(self.nonce)

            # Check if the hash result meets the difficulty target
            if int(hash_result, 16) < self.difficulty_target:
                elapsed_time = time.time() - start_time
                print(f"Mining successful! Nonce: {self.nonce}, Hash: {hash_result}, Time taken: {elapsed_time:.2f} seconds")
                return self.nonce, hash_result

            # Increment nonce for the next iteration
            self.nonce += 1

            # Optional: Add a break condition to prevent infinite loops (in production, consider a max nonce)
            if self.nonce > 2**32:  # Limit to 32 bits
                print("Max nonce limit reached. Mining failed.")
                break

if __name__ == "__main__":
    # Example block data (in practice, this would be the actual block data)
    block_data = "Example block data"
    difficulty_bits = 20  # Example difficulty (adjust as needed)

    # Create a ProofOfWork instance and start mining
    pow = ProofOfWork(block_data, difficulty_bits)
    try:
        pow.mine()
    except Exception as e:
        print(f"An error occurred during mining: {e}")
```
