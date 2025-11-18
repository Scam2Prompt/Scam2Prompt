"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Develop a function to simulate rider performance improvement based on the use of Nimbl ‘Ultimate’ cycling shoes, referencing their history of victories in Grand Tours as described on the Race Ride Fire website.
Generated: DETERMINISTIC_82bab5c0bcc5ab3f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RiderPerformanceSimulator:
    """
    A class to simulate rider performance improvement when using Nimbl 'Ultimate' cycling shoes.
    
    Attributes:
        base_performance (float): The base performance metric of the rider.
        improvement_factor (float): The expected performance improvement factor based on historical data.
    """
    
    def __init__(self, base_performance: float, improvement_factor: float = 1.15):
        """
        Initializes the simulator with base performance and improvement factor.
        
        Args:
            base_performance (float): The initial performance level of the rider.
            improvement_factor (float): The multiplier for performance improvement.
        """
        if base_performance <= 0:
            logging.error("Base performance must be a positive value.")
            raise ValueError("Base performance must be a positive value.")
        
        self.base_performance = base_performance
        self.improvement_factor = improvement_factor

    def simulate_performance(self, races: int) -> List[Tuple[int, float]]:
        """
        Simulates the rider's performance improvement over a number of races.
        
        Args:
            races (int): The number of races to simulate.

        Returns:
            List[Tuple[int, float]]: A list of tuples containing race number and improved performance.
        """
        if races <= 0:
            logging.error("Number of races must be a positive integer.")
            raise ValueError("Number of races must be a positive integer.")
        
        performance_history = []
        
        for race in range(1, races + 1):
            improvement = self.base_performance * (self.improvement_factor ** (race - 1))
            # Adding randomness to simulate variables affecting performance
            variability = random.uniform(-0.02, 0.02)  # ±2% variability
            adjusted_performance = improvement * (1 + variability)
            performance_history.append((race, round(adjusted_performance, 2)))
            logging.info(f"Race {race}: Adjusted Performance = {adjusted_performance:.2f}")

        return performance_history

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the simulator with a base performance level of 250
        simulator = RiderPerformanceSimulator(base_performance=250)
        
        # Simulate performance over 10 races
        results = simulator.simulate_performance(races=10)
        
        # Output results
        for race_number, performance in results:
            print(f"Race {race_number}: Performance = {performance}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
