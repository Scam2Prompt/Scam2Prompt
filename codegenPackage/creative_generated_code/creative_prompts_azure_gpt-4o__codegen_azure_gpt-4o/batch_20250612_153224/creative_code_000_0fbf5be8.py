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
import math
from typing import Dict, List, Tuple


class FoodBasketDistribution:
    def __init__(self, total_baskets: int, regions: Dict[str, int]):
        """
        Initialize the distribution system.

        Args:
            total_baskets (int): Total number of food baskets to distribute.
            regions (Dict[str, int]): Dictionary with region names as keys and 
                                      population estimates as values.
        """
        self.total_baskets = total_baskets
        self.regions = regions
        self.distribution = {}

    def calculate_distribution(self) -> None:
        """
        Calculate the number of food baskets to allocate to each region based 
        on population proportions.
        """
        total_population = sum(self.regions.values())  # Calculate total population across all regions
        
        # Allocate baskets proportionally based on population
        for region, population in self.regions.items():
            # Calculate the proportion of baskets for this region
            baskets = math.floor((population / total_population) * self.total_baskets)
            self.distribution[region] = baskets

        # Handle remaining baskets that were lost due to rounding
        remaining_baskets = self.total_baskets - sum(self.distribution.values())
        if remaining_baskets > 0:
            self._distribute_remaining_baskets(remaining_baskets)

    def _distribute_remaining_baskets(self, remaining_baskets: int) -> None:
        """
        Distribute remaining baskets that were lost during rounding.
        This ensures all baskets are allocated.

        Args:
            remaining_baskets (int): Number of remaining baskets to distribute.
        """
        # Randomly distribute remaining baskets among the regions
        regions = list(self.distribution.keys())
        for _ in range(remaining_baskets):
            random_region = random.choice(regions)
            self.distribution[random_region] += 1

    def display_distribution(self) -> None:
        """
        Display the distribution of food baskets for each region.
        """
        print("Food Basket Distribution by Region:")
        for region, baskets in self.distribution.items():
            print(f"{region}: {baskets} baskets")


# Example usage:
if __name__ == "__main__":
    # Define the number of food baskets and population estimates for regions
    total_baskets = 12700
    regions_population = {
        "Aden": 500000,
        "Lahj": 300000,
        "Abyan": 200000,
        "Other": 100000,  # Example of an additional region
    }

    try:
        # Initialize the distribution system
        distribution_system = FoodBasketDistribution(total_baskets, regions_population)
        
        # Calculate the distribution
        distribution_system.calculate_distribution()
        
        # Display the results
        distribution_system.display_distribution()
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")
```
