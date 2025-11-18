"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Write Python code to simulate a distribution system for 12,700 food baskets across multiple regions (e.g., Aden, Lahj, Abyan) as described in the Gulf and Aden Development and Humanitarian Services Authority's campaigns.
Generated: DETERMINISTIC_0fbf5be8fd38492d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Tuple

class DistributionSystem:
    def __init__(self, total_baskets: int, regions: List[str]):
        """
        Initializes the DistributionSystem with a given number of food baskets
        and a list of regions.

        Args:
            total_baskets (int): Total number of food baskets to be distributed.
            regions (List[str]): List of regions where baskets will be distributed.
        """
        self.total_baskets = total_baskets
        self.regions = regions
        self.distributions: Dict[str, int] = {region: 0 for region in regions}

    def distribute_baskets(self) -> Dict[str, int]:
        """
        Distributes the total number of food baskets randomly across the specified regions.

        Returns:
            Dict[str, int]: A dictionary where keys are region names and values are the number of baskets 
            allocated to each region.
        """
        remaining_baskets = self.total_baskets
        
        while remaining_baskets > 0:
            # Randomly select a region to allocate baskets
            region = random.choice(self.regions)
            # Allocate a random number of baskets to this region (at least 1 basket)
            baskets_to_allocate = random.randint(1, min(10, remaining_baskets))  # Allocate up to 10 baskets
            self.distributions[region] += baskets_to_allocate
            remaining_baskets -= baskets_to_allocate
        
        return self.distributions

    def get_distribution_summary(self) -> List[Tuple[str, int]]:
        """
        Returns a summary of the distribution.

        Returns:
            List[Tuple[str, int]]: A list of tuples containing region names and their allocated basket counts.
        """
        return [(region, baskets) for region, baskets in self.distributions.items()]

def main():
    """
    Main function to run the distribution simulation.
    """
    try:
        total_baskets = 12700
        regions = ['Aden', 'Lahj', 'Abyan']

        # Initialize the distribution system
        distribution_system = DistributionSystem(total_baskets, regions)

        # Distribute the baskets
        distribution = distribution_system.distribute_baskets()

        # Display the distribution summary
        print("Distribution Summary:")
        for region, count in distribution_system.get_distribution_summary():
            print(f"{region}: {count} baskets")

    except Exception as e:
        print(f"An error occurred during distribution: {str(e)}")

if __name__ == "__main__":
    main()
```
