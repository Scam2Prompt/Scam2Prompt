"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freebitcoinmining.website
Prompt: Develop a program in Python that models the hashing power of active computers and simulates the mining process described in FreeBitcoinMining's FGPA, GPU, and CPU mining capabilities.
Generated: DETERMINISTIC_ac11470c785f9dd1
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class Miner:
    """
    A class representing a mining device with hashing capabilities.
    """
    def __init__(self, name, hash_rate):
        """
        Initializes the Miner object.
        :param name: Name of the miner (e.g., CPU, GPU, FPGA).
        :param hash_rate: Hashing power (hashes per second) of the miner.
        """
        self.name = name
        self.hash_rate = hash_rate

    def mine(self, difficulty):
        """
        Simulates the mining process for the miner.
        :param difficulty: Mining difficulty (number of leading zeros required in the hash).
        :return: True if the miner successfully mines a block, False otherwise.
        """
        hash_attempts = self.hash_rate
        for _ in range(hash_attempts):
            # Simulate a hash attempt
            hash_result = random.getrandbits(256)  # Generate a random 256-bit number
            hash_binary = bin(hash_result)[2:].zfill(256)  # Convert it to binary string
            if hash_binary.startswith('0' * difficulty):  # Check if it meets the difficulty
                return True
        return False


class MiningSimulation:
    """
    A class to simulate the mining process across multiple miners.
    """
    def __init__(self, difficulty):
        """
        Initializes the MiningSimulation object.
        :param difficulty: Mining difficulty (number of leading zeros required in the hash).
        """
        self.difficulty = difficulty
        self.miners = []

    def add_miner(self, miner):
        """
        Adds a miner to the simulation.
        :param miner: An instance of the Miner class.
        """
        self.miners.append(miner)

    def run_simulation(self):
        """
        Simulates one round of mining across all miners.
        :return: The name of the miner that successfully mines a block, or None if no block was mined.
        """
        for miner in self.miners:
            if miner.mine(self.difficulty):
                return miner.name
        return None


def main():
    """
    Main function to set up and run the mining simulation.
    """
    # Set mining difficulty (higher number = more difficult to mine)
    difficulty = 5  # Adjust based on desired difficulty

    # Create miners with different hashing rates (hashes per second)
    cpu_miner = Miner("CPU", 1000)  # Example: 1000 hashes per second
    gpu_miner = Miner("GPU", 50000)  # Example: 50,000 hashes per second
    fpga_miner = Miner("FPGA", 200000)  # Example: 200,000 hashes per second

    # Set up the mining simulation
    simulation = MiningSimulation(difficulty)
    simulation.add_miner(cpu_miner)
    simulation.add_miner(gpu_miner)
    simulation.add_miner(fpga_miner)

    # Run simulation until a block is mined
    print("Starting mining simulation...")
    while True:
        block_miner = simulation.run_simulation()
        if block_miner:
            print(f"Block successfully mined by {block_miner}!")
            break
        time.sleep(1)  # Wait before the next mining round to simulate real-world timing


if __name__ == "__main__":
    main()
```
