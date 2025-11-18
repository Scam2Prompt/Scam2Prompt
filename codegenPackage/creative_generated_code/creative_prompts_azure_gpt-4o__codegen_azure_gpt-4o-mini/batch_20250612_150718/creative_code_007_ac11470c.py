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
from enum import Enum

class MiningType(Enum):
    FGPA = 'FGPA'
    GPU = 'GPU'
    CPU = 'CPU'

class Computer:
    def __init__(self, name: str, mining_type: MiningType, hashing_power: float):
        """
        Initializes a new Computer instance.

        :param name: The name of the computer.
        :param mining_type: The type of mining used by the computer.
        :param hashing_power: The hashing power of the computer in hashes per second.
        """
        self.name = name
        self.mining_type = mining_type
        self.hashing_power = hashing_power  # in hashes per second

    def mine(self):
        """
        Simulates the mining process for this computer.

        :return: A boolean indicating whether the mining was successful.
        """
        # Simulate the mining process with a random chance of success
        success_chance = random.uniform(0, 1)
        mining_success = success_chance < (self.hashing_power / 1_000_000)  # Adjust threshold for success
        
        if mining_success:
            print(f"{self.name} successfully mined a block!")
        else:
            print(f"{self.name} did not mine a block.")
        
        return mining_success

class MiningSimulator:
    def __init__(self):
        """
        Initializes the Mining Simulator with a list of active computers.
        """
        self.computers = []

    def add_computer(self, computer: Computer):
        """
        Adds a computer to the mining simulator.

        :param computer: The Computer instance to be added.
        """
        self.computers.append(computer)

    def simulate_mining(self, duration: int):
        """
        Simulates the mining process over a given duration.

        :param duration: The duration for which to simulate mining, in seconds.
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            for computer in self.computers:
                computer.mine()
            time.sleep(1)  # Simulate a delay between mining attempts

def main():
    """
    Main function to run the mining simulation.
    """
    # Create a mining simulator
    simulator = MiningSimulator()

    # Create some computers with different mining capabilities
    fgpa_computer = Computer("FGPA Miner", MiningType.FGPA, hashing_power=500_000)
    gpu_computer = Computer("GPU Miner", MiningType.GPU, hashing_power=300_000)
    cpu_computer = Computer("CPU Miner", MiningType.CPU, hashing_power=100_000)

    # Add computers to the simulator
    simulator.add_computer(fgpa_computer)
    simulator.add_computer(gpu_computer)
    simulator.add_computer(cpu_computer)

    # Run the mining simulation for 10 seconds
    try:
        simulator.simulate_mining(duration=10)
    except Exception as e:
        print(f"An error occurred during mining simulation: {e}")

if __name__ == "__main__":
    main()
```
