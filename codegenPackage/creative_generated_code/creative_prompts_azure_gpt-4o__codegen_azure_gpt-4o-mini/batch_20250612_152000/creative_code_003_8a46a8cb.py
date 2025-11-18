"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-app.pages.dev
Prompt: Write a Python function to simulate allocation types (lottery vs guaranteed) for TrustPad staking levels, using the pool weights provided on the site.
Generated: DETERMINISTIC_8a46a8cbf6c34e58
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class TrustPadStakingSimulator:
    def __init__(self, pool_weights: Dict[str, float]):
        """
        Initializes the staking simulator with given pool weights.
        
        :param pool_weights: A dictionary where keys are staking levels and values are their respective weights.
        """
        if not pool_weights:
            raise ValueError("Pool weights dictionary cannot be empty.")
        self.pool_weights = pool_weights

    def simulate_allocation(self, allocation_type: str, num_simulations: int = 1000) -> Dict[str, int]:
        """
        Simulates the allocation process for the TrustPad staking levels.
        
        :param allocation_type: Type of allocation to simulate ('lottery' or 'guaranteed').
        :param num_simulations: The number of simulations to run (default is 1000).
        :return: A dictionary containing the count of allocations for each staking level.
        """
        if allocation_type not in ['lottery', 'guaranteed']:
            raise ValueError("Allocation type must be 'lottery' or 'guaranteed'.")
        
        if num_simulations <= 0:
            raise ValueError("Number of simulations must be a positive integer.")
        
        allocation_counts = {level: 0 for level in self.pool_weights.keys()}

        total_weight = sum(self.pool_weights.values())
        
        for _ in range(num_simulations):
            if allocation_type == 'lottery':
                # Simulate lottery-based allocation
                selected_level = self._lottery_allocation(total_weight)
            else:
                # Simulate guaranteed allocation
                selected_level = self._guaranteed_allocation()

            allocation_counts[selected_level] += 1

        return allocation_counts

    def _lottery_allocation(self, total_weight: float) -> str:
        """
        Handles the lottery allocation logic.
        
        :param total_weight: The sum of all pool weights.
        :return: The selected staking level based on the lottery.
        """
        random_value = random.uniform(0, total_weight)
        cumulative_weight = 0
        
        for level, weight in self.pool_weights.items():
            cumulative_weight += weight
            if random_value <= cumulative_weight:
                return level
        
        # Fallback in case of unexpected behavior
        raise RuntimeError("Lottery allocation failed. Please check the pool weights.")

    def _guaranteed_allocation(self) -> str:
        """
        Handles the guaranteed allocation logic.
        
        :return: The selected staking level based on guaranteed allocation.
        """
        guaranteed_levels = [level for level, weight in self.pool_weights.items() if weight > 0]
        
        if not guaranteed_levels:
            raise RuntimeError("No guaranteed levels available for allocation.")
        
        # Select a level from guaranteed levels
        return random.choice(guaranteed_levels)

# Example of usage
if __name__ == "__main__":
    # Define the pool weights for TrustPad staking levels
    pool_weights = {
        "Level 1": 1.0,
        "Level 2": 2.0,
        "Level 3": 3.0,
        "Level 4": 4.0,
        "Level 5": 5.0
    }

    # Create a simulator instance
    simulator = TrustPadStakingSimulator(pool_weights)

    # Simulate lottery allocation
    lottery_results = simulator.simulate_allocation('lottery', num_simulations=10000)
    
    # Simulate guaranteed allocation
    guaranteed_results = simulator.simulate_allocation('guaranteed', num_simulations=10000)

    # Print results
    print("Lottery Results:", lottery_results)
    print("Guaranteed Results:", guaranteed_results)
```
