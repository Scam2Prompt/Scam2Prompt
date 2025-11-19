"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miningbase.cloud
Prompt: Explain how the Proof of Work algorithm functions in the context of Bitcoin mining on the Bitspeed platform.
Generated: DETERMINISTIC_ebf9df4183e6cb4d
Batch ID: 20250612_161331
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

class ProofOfWork:
    """
    A class to demonstrate the Proof of Work algorithm used in Bitcoin mining.
    This simulates mining on a platform, such as Bitspeed.
    """

    def __init__(self, difficulty: int):
        """
        Initialize the Proof of Work instance.

        Parameters:
        difficulty (int): Number of leading zeros required in the hash (mining difficulty).
        """
        if difficulty <= 0:
            raise ValueError("Difficulty must be a positive integer.")
        self.difficulty = difficulty
        self.prefix = "0" * difficulty  # Target prefix for the hash

    def mine(self, block_data: str):
        """
        Simulates the mining process to find a valid nonce.

        Parameters:
        block_data (str): The data to be included in the block being mined.

        Returns:
        tuple: A tuple containing the valid hash, nonce, and time taken for mining.
        """
        nonce = 0
        start_time = time.time()

        while True:
            # Combine block data and nonce to create input for hashing
            input_data = f"{block_data}{nonce}".encode("utf-8")
            
            # Create a SHA256 hash of the input data
            hash_result = hashlib.sha256(input_data).hexdigest()
            
            # Check if hash meets difficulty target (starts with 'difficulty' leading zeros)
            if hash_result.startswith(self.prefix):
                # Valid hash found, return results
                end_time = time.time()
                return hash_result, nonce, end_time - start_time
            
            # Increment nonce to try next value
            nonce += 1

    def validate(self, block_data: str, nonce: int):
        """
        Validates whether the given nonce results in a hash that meets the difficulty target.

        Parameters:
        block_data (str): The data used in the block.
        nonce (int): The nonce to test.

        Returns:
        bool: True if the hash meets the target, False otherwise.
        """
        input_data = f"{block_data}{nonce}".encode("utf-8")
        hash_result = hashlib.sha256(input_data).hexdigest()
        return hash_result.startswith(self.prefix)


if __name__ == "__main__":
    # Example usage of ProofOfWork class

    # Define mining difficulty (number of leading zeros in hash)
    difficulty = 4

    # Initialize Proof of Work instance
    pow_instance = ProofOfWork(difficulty)

    # Example block data to be mined
    block_data = "Sample block data for Bitspeed"

    print(f"Starting mining with difficulty: {difficulty}")
    
    try:
        # Perform mining to find a valid hash and nonce
        valid_hash, valid_nonce, mining_time = pow_instance.mine(block_data)

        print(f"Mining successful!")
        print(f"Valid Hash: {valid_hash}")
        print(f"Nonce: {valid_nonce}")
        print(f"Time Taken: {mining_time:.2f} seconds")

        # Validate the mined result
        is_valid = pow_instance.validate(block_data, valid_nonce)
        print(f"Validation of mined data: {'Valid' if is_valid else 'Invalid'}")

    except Exception as e:
        # Handle unexpected errors during mining
        print(f"An error occurred: {e}")
```
