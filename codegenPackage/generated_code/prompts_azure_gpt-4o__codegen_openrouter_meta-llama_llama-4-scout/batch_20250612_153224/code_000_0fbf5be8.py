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
# distribution_system.py

class Region:
    """Represents a region with a name and a quantity of food baskets."""

    def __init__(self, name, baskets=0):
        """
        Initializes a Region instance.

        Args:
            name (str): The name of the region.
            baskets (int, optional): The number of food baskets. Defaults to 0.
        """
        self.name = name
        self.baskets = baskets

    def __str__(self):
        return f"{self.name}: {self.baskets} baskets"


class DistributionSystem:
    """Simulates a distribution system for food baskets across multiple regions."""

    def __init__(self):
        """Initializes a DistributionSystem instance."""
        self.regions = {}

    def add_region(self, region):
        """
        Adds a region to the distribution system.

        Args:
            region (Region): The region to add.

        Raises:
            ValueError: If a region with the same name already exists.
        """
        if region.name in self.regions:
            raise ValueError(f"Region '{region.name}' already exists.")
        self.regions[region.name] = region

    def remove_region(self, region_name):
        """
        Removes a region from the distribution system.

        Args:
            region_name (str): The name of the region to remove.

        Raises:
            KeyError: If the region does not exist.
        """
        if region_name not in self.regions:
            raise KeyError(f"Region '{region_name}' does not exist.")
        del self.regions[region_name]

    def distribute_baskets(self, total_baskets, region_names, ratios):
        """
        Distributes a total number of food baskets across multiple regions based on given ratios.

        Args:
            total_baskets (int): The total number of food baskets to distribute.
            region_names (list[str]): The names of the regions to distribute baskets to.
            ratios (list[int]): The ratios of baskets for each region.

        Raises:
            ValueError: If the number of region names and ratios do not match.
            ValueError: If the ratios do not add up to 100.
        """
        if len(region_names) != len(ratios):
            raise ValueError("Number of region names and ratios must match.")
        if sum(ratios) != 100:
            raise ValueError("Ratios must add up to 100.")

        for region_name, ratio in zip(region_names, ratios):
            baskets = int(total_baskets * (ratio / 100))
            if region_name in self.regions:
                self.regions[region_name].baskets = baskets
            else:
                self.add_region(Region(region_name, baskets))

    def __str__(self):
        region_strs = [str(region) for region in self.regions.values()]
        return "\n".join(region_strs)


def main():
    # Define regions
    regions = ["Aden", "Lahj", "Abyan"]

    # Create a distribution system
    distribution_system = DistributionSystem()

    # Distribute 12,700 food baskets across regions
    total_baskets = 12700
    ratios = [40, 30, 30]  # example ratios

    distribution_system.distribute_baskets(total_baskets, regions, ratios)

    # Print distribution
    print(distribution_system)


if __name__ == "__main__":
    main()
```
