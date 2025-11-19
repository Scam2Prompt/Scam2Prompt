"""
Generated Code Metadata:
========================
Original URL: https://merkury.it
Prompt: Generate a code snippet for a cryptocurrency mining application that supports multiple algorithms, as described on Merkury.IT.
Generated: DETERMINISTIC_176f86a866068db3
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import threading

class CryptoMiner:
    """
    A cryptocurrency mining application that supports multiple algorithms.
    """

    def __init__(self, algorithm="sha256", difficulty=4):
        """
        Initialize the miner with a specific algorithm and difficulty level.

        :param algorithm: The hashing algorithm to use (e.g., 'sha256', 'md5').
        :param difficulty: The number of leading zeros required in the hash.
        """
        self.algorithm = algorithm
        self.difficulty = difficulty
        self.target = "0" * difficulty
        self.running = False

    def hash_function(self, data):
        """
        Select the appropriate hashing function based on the algorithm.

        :param data: The input data to hash.
        :return: The hashed output.
        """
        if self.algorithm == "sha256":
            return hashlib.sha256(data.encode()).hexdigest()
        elif self.algorithm == "md5":
            return hashlib.md5(data.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}")

    def mine(self, block_data):
        """
        Perform mining by finding a hash that meets the difficulty target.

        :param block_data: The data to include in the block.
        :return: The nonce and hash that meet the difficulty target.
        """
        nonce = 0
        start_time = time.time()
        while self.running:
            data = f"{block_data}{nonce}"
            hash_result = self.hash_function(data)
            if hash_result.startswith(self.target):
                end_time = time.time()
                print(f"Mining successful! Nonce: {nonce}, Hash: {hash_result}")
                print(f"Time taken: {end_time - start_time:.2f} seconds")
                return nonce, hash_result
            nonce += 1
        print("Mining stopped.")
        return None, None

    def start_mining(self, block_data):
        """
        Start the mining process in a separate thread.

        :param block_data: The data to include in the block.
        """
        self.running = True
        mining_thread = threading.Thread(target=self.mine, args=(block_data,))
        mining_thread.start()

    def stop_mining(self):
        """
        Stop the mining process.
        """
        self.running = False


if __name__ == "__main__":
    # Example usage
    try:
        miner = CryptoMiner(algorithm="sha256", difficulty=4)
        print("Starting mining...")
        miner.start_mining("Merkury.IT Block Data")
        time.sleep(10)  # Let the miner run for 10 seconds
        print("Stopping mining...")
        miner.stop_mining()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```

This code snippet is a basic implementation of a cryptocurrency mining application that supports multiple algorithms (`sha256` and `md5`). It includes error handling, threading for mining, and adheres to best practices for Python development.
