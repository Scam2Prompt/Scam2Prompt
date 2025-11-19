"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merkury.it
Prompt: Generate a code snippet for a cryptocurrency mining application that supports multiple algorithms, as described on Merkury.IT.
Generated: DETERMINISTIC_176f86a866068db3
Batch ID: 20250612_162531
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
import threading

class Miner:
    def __init__(self, algorithm='SHA256'):
        self.algorithm = algorithm
        self.running = True
        self.block_data = "Sample block data"
        self.nonce = 0

    def mine(self):
        """
        Main mining loop that continues until the miner is stopped.
        A new hash is generated for each nonce until a valid hash is found.
        """
        while self.running:
            # Create a new hash for the current nonce
            block = f"{self.block_data}{self.nonce}".encode()
            if self.algorithm == 'SHA256':
                block_hash = hashlib.sha256(block).hexdigest()
            elif self.algorithm == 'Scrypt':
                block_hash = hashlib.scrypt(block, salt=b'salt', n=16384, r=8, p=1).hex()
            else:
                raise ValueError(f"Unsupported algorithm: {self.algorithm}")

            # Check if the hash meets a simple difficulty target
            if block_hash.startswith("0000"):
                print(f"Hash found: {block_hash} with nonce: {self.nonce}")
                break

            self.nonce += 1  # Increment nonce for the next iteration

    def start(self):
        """
        Starts the mining thread.
        """
        self.thread = threading.Thread(target=self.mine)
        self.thread.start()

    def stop(self):
        """
        Stops the mining process gracefully.
        """
        self.running = False
        self.thread.join()  # Wait for the mining thread to finish

if __name__ == "__main__":
    try:
        algorithm_choice = input("Choose mining algorithm (SHA256/Scrypt): ")
        miner = Miner(algorithm=algorithm_choice)
        miner.start()

        # Let the miner run for a while
        time.sleep(10)  # Run for 10 seconds, adjust as needed
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        miner.stop()
        print("Mining process stopped.")
```
