"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://midoin.com
Prompt: Write a program to simulate eco-friendly mining of Midoins, emphasizing time-based mining without high electricity consumption.
Generated: DETERMINISTIC_5b407d178d166e12
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import hashlib

class EcoFriendlyMidoinMiner:
    """
    A class to simulate eco-friendly mining of Midoins.
    Emphasis is placed on time-based mining rather than high electricity consumption.
    """

    def __init__(self, mining_difficulty=4, mining_interval=10):
        """
        Initialize the miner with a given difficulty and interval.
        
        :param mining_difficulty: Number of leading zeros required in the mined hash. Default is 4.
        :param mining_interval: Time interval (seconds) between consecutive mining attempts. Default is 10 seconds.
        """
        self.mining_difficulty = mining_difficulty
        self.mining_interval = mining_interval
        self.mining_prefix = '0' * mining_difficulty

    def mine_midoin(self):
        """
        Simulates the eco-friendly Midoin mining process.
        Mining occurs at regular intervals without computational overuse.
        """
        try:
            print("Starting eco-friendly Midoin mining...")
            block_number = 1  # A sequential number for blocks being mined
            
            while True:
                print(f"Mining block number {block_number}...")
                timestamp = int(time.time())
                nonce = 0
                
                while True:
                    # Create the mining input by combining the block number, timestamp, and nonce
                    mining_input = f"{block_number}-{timestamp}-{nonce}"
                    
                    # Generate a SHA-256 hash of the mining input
                    mined_hash = hashlib.sha256(mining_input.encode('utf-8')).hexdigest()
                    
                    # Check if the hash meets the mining difficulty criteria (e.g., leading zeros)
                    if mined_hash.startswith(self.mining_prefix):
                        print(f"Block {block_number} successfully mined!")
                        print(f"Hash: {mined_hash}")
                        print(f"Nonce: {nonce}")
                        print("-" * 40)
                        break  # Exit the inner loop once a valid hash is found
                    
                    nonce += 1  # Increment the nonce for the next attempt

                # Increment block number for the next mining cycle
                block_number += 1
                
                # Wait for the specified mining interval before attempting the next block
                print(f"Waiting {self.mining_interval} seconds before mining the next block...")
                time.sleep(self.mining_interval)
        
        except KeyboardInterrupt:
            print("Mining stopped by user.")
        except Exception as e:
            print(f"An error occurred during mining: {e}")

if __name__ == "__main__":
    # Create an instance of the EcoFriendlyMidoinMiner with default difficulty and interval
    miner = EcoFriendlyMidoinMiner()
    
    # Start the mining process
    miner.mine_midoin()
```
