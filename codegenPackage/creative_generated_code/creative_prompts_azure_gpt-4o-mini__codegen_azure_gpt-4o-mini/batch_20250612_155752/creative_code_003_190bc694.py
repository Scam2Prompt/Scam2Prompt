"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omninetworkclub.xyz
Prompt: Describe the mining difficulty adjustment algorithm used by Dogecoin and provide a code implementation that simulates this mechanism.
Generated: DETERMINISTIC_190bc6942a8be837
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class DogecoinDifficultyAdjustment:
    def __init__(self, target_time: int = 60, adjustment_interval: int = 144):
        """
        Initialize the Dogecoin Difficulty Adjustment simulator.

        :param target_time: Target time (in seconds) for each block to be mined.
        :param adjustment_interval: Number of blocks after which difficulty is adjusted.
        """
        self.target_time = target_time  # Target time for each block
        self.adjustment_interval = adjustment_interval  # Blocks after which to adjust difficulty
        self.blocks = []  # List to keep track of mined blocks

    def add_block(self, block_time: float):
        """
        Add a new mined block and its time to the list of blocks.

        :param block_time: Time taken to mine the block (in seconds).
        """
        if len(self.blocks) >= self.adjustment_interval:
            self.adjust_difficulty()
        self.blocks.append(block_time)

    def adjust_difficulty(self):
        """
        Adjust difficulty based on the average time taken for the last 'adjustment_interval' blocks.
        """
        # Calculate average time to mine the last 'adjustment_interval' blocks
        last_blocks = self.blocks[-self.adjustment_interval:]
        average_time = sum(last_blocks) / len(last_blocks)

        # Calculate new difficulty
        if average_time < self.target_time:
            # If average time is less than target, increase difficulty
            new_difficulty_factor = 1.0 + (self.target_time - average_time) / self.target_time
        else:
            # If average time is greater than or equal to target, decrease difficulty
            new_difficulty_factor = 1.0 - (average_time - self.target_time) / self.target_time
        
        # Ensure the new difficulty factor is within reasonable bounds
        new_difficulty_factor = max(0.1, min(new_difficulty_factor, 2.0))

        # Log the adjustment
        print(f"Adjusting difficulty. New Difficulty Factor: {new_difficulty_factor:.4f}")

    def simulate_mining(self, total_blocks: int):
        """
        Simulate the mining of a specified number of blocks.

        :param total_blocks: Total number of blocks to simulate mining for.
        """
        for i in range(total_blocks):
            # Simulate a mining time between 30-90 seconds
            simulated_time = self.target_time * (0.5 + (i % 3) * 0.5)
            self.add_block(simulated_time)
            time.sleep(0.1)  # Sleep to simulate time passing during mining


# Example usage
if __name__ == "__main__":
    try:
        simulator = DogecoinDifficultyAdjustment()
        simulator.simulate_mining(300)  # Simulate mining for 300 blocks
    except Exception as e:
        print(f"An error occurred: {e}")
```
