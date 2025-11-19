"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mining-equipment.vercel.app
Prompt: Explain how mining pools with higher hashpower increase the chances of solving a block in the context of Bitcoin on SOL.
Generated: DETERMINISTIC_664df4ad9f800768
Batch ID: 20250612_162502
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

class MiningPool:
    def __init__(self, name, hashpower):
        """
        Initializes a mining pool with a given name and hashpower.
        
        Parameters:
        name (str): The name of the mining pool.
        hashpower (float): The total hashpower of the mining pool.
        """
        self.name = name
        self.hashpower = hashpower

    def calculate_probability(self, total_hashpower):
        """
        Calculates the probability of solving the next block based on the
        pool's hashpower relative to the total network hashpower.

        Parameters:
        total_hashpower (float): The total hashpower of the Bitcoin network.

        Returns:
        float: The probability of this mining pool solving the next block.
        """
        if total_hashpower <= 0:
            raise ValueError("Total hashpower must be greater than zero.")
        
        return self.hashpower / total_hashpower

    def simulate_mining(self, total_hashpower, blocks_to_mine=10):
        """
        Simulates the mining process by attempting to solve a specified number
        of blocks based on the pool's hashpower.

        Parameters:
        total_hashpower (float): The total hashpower of the Bitcoin network.
        blocks_to_mine (int): The number of blocks to simulate mining.

        Returns:
        int: The number of blocks successfully mined by the pool.
        """
        mined_blocks = 0
        
        for _ in range(blocks_to_mine):
            # Calculate the probability of mining the block
            probability = self.calculate_probability(total_hashpower)
            # Simulate the mining attempt based on probability
            if random.random() < probability:
                mined_blocks += 1
            time.sleep(0.1)  # Simulate some processing time

        return mined_blocks

def main():
    """
    Main function to simulate the mining process for a given mining pool.
    """
    try:
        # Define the total hashpower of the Bitcoin network
        total_network_hashpower = 1000000.0  # Example hashpower in TH/s

        # Create a mining pool with a specific hashpower
        pool_a = MiningPool(name="Pool A", hashpower=200000.0)  # 200 TH/s
        pool_b = MiningPool(name="Pool B", hashpower=500000.0)  # 500 TH/s

        # Simulate the mining process
        blocks_mined_a = pool_a.simulate_mining(total_network_hashpower)
        blocks_mined_b = pool_b.simulate_mining(total_network_hashpower)

        print(f"{pool_a.name} mined {blocks_mined_a} blocks.")
        print(f"{pool_b.name} mined {blocks_mined_b} blocks.")

    except ValueError as ve:
        print(f"Error during simulation: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
