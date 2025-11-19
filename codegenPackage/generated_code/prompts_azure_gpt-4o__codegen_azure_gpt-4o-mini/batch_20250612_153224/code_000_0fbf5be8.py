"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Write Python code to simulate a distribution system for 12,700 food baskets across multiple regions (e.g., Aden, Lahj, Abyan) as described in the Gulf and Aden Development and Humanitarian Services Authority's campaigns.
Generated: DETERMINISTIC_0fbf5be8fd38492d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from collections import defaultdict

class FoodBasketDistribution:
    def __init__(self, total_baskets, regions):
        """
        Initialize the distribution system with total baskets and regions.

        :param total_baskets: Total number of food baskets to distribute
        :param regions: List of regions to distribute the baskets
        """
        self.total_baskets = total_baskets
        self.regions = regions
        self.distribution = defaultdict(int)

    def distribute_baskets(self):
        """
        Distribute food baskets randomly across the specified regions.
        Each region will receive a random number of baskets, ensuring the total
        does not exceed the total number of baskets available.
        """
        remaining_baskets = self.total_baskets
        while remaining_baskets > 0:
            # Randomly select a region
            region = random.choice(self.regions)
            # Randomly determine the number of baskets to allocate to the selected region
            # Ensure we do not allocate more baskets than remaining
            baskets_to_allocate = random.randint(1, min(remaining_baskets, 100))
            self.distribution[region] += baskets_to_allocate
            remaining_baskets -= baskets_to_allocate

    def get_distribution(self):
        """
        Get the current distribution of food baskets across regions.

        :return: A dictionary with regions as keys and allocated baskets as values
        """
        return dict(self.distribution)

    def display_distribution(self):
        """
        Display the distribution of food baskets in a formatted manner.
        """
        print("Food Basket Distribution:")
        for region, count in self.distribution.items():
            print(f"{region}: {count} baskets")
        print(f"Total baskets distributed: {sum(self.distribution.values())}")

def main():
    """
    Main function to execute the food basket distribution simulation.
    """
    try:
        total_baskets = 12700
        regions = ["Aden", "Lahj", "Abyan"]

        # Create a distribution system instance
        distribution_system = FoodBasketDistribution(total_baskets, regions)

        # Distribute the baskets
        distribution_system.distribute_baskets()

        # Display the distribution results
        distribution_system.display_distribution()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
