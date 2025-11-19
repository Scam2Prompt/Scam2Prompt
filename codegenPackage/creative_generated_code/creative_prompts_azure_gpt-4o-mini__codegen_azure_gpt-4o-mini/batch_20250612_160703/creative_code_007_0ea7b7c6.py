"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmining.website
Prompt: Explain how Coinmining's SHA-256 algorithm enhances the security of Bitcoin mining.
Generated: DETERMINISTIC_0ea7b7c6703dda70
Batch ID: 20250612_160703
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
    A class to demonstrate the SHA-256 hashing algorithm used in Bitcoin mining.

    Attributes:
        target_difficulty (int): The target difficulty for mining a new block.
    """

    def __init__(self, target_difficulty: int):
        """
        Initializes the BitcoinMiner with a specified target difficulty.

        :param target_difficulty: The target difficulty for the mining process.
        """
        self.target_difficulty = target_difficulty

    def sha256(self, data: str) -> str:
        """
        Computes the SHA-256 hash of the given data.

        :param data: The input data to hash.
        :return: The SHA-256 hash of the input data as a hexadecimal string.
        """
        return hashlib.sha256(data.encode()).hexdigest()

    def mine(self, nonce_limit: int) -> (str, int):
        """
        Attempts to mine a new block by finding a valid nonce.

        :param nonce_limit: The upper limit for the nonce value to search for.
        :return: A tuple containing the successful hash and the nonce used.
        """
        for nonce in range(nonce_limit):
            # Create block header with nonce
            block_header = f"Block header with nonce: {nonce}"
            block_hash = self.sha256(block_header)

            # Check if the hash meets the target difficulty
            if self.is_valid_hash(block_hash):
                return block_hash, nonce
        
        raise RuntimeError("Nonce limit reached without finding a valid hash.")

    def is_valid_hash(self, block_hash: str) -> bool:
        """
        Checks if the hash meets the target difficulty.

        :param block_hash: The hash to validate.
        :return: True if the hash is valid under the target difficulty, False otherwise.
        """
        # Convert target difficulty to a hexadecimal string
        target_hex = '0' * (64 - self.target_difficulty // 4)
        
        # Compare the hash against the target difficulty
        return block_hash.startswith(target_hex)

def main():
    try:
        # Set the mining difficulty (number of leading zeros)
        mining_difficulty = 20
        # Create a BitcoinMiner instance
        miner = BitcoinMiner(target_difficulty=mining_difficulty)

        # Start mining with a nonce limit
        nonce_limit = 1_000_000
        start_time = time.time()
        
        # Attempt to mine a new block
        valid_hash, valid_nonce = miner.mine(nonce_limit)
        elapsed_time = time.time() - start_time

        print(f"Successfully mined a block with hash: {valid_hash}")
        print(f"Nonce used: {valid_nonce}")
        print(f"Time taken: {elapsed_time:.2f} seconds")

    except RuntimeError as e:
        print(f"Mining failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
