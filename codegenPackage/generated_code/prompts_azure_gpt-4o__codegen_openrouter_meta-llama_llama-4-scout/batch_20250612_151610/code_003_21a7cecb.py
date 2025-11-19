"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Create a script to calculate optimal packaging configurations for fruit export, taking into account Osku's emphasis on protecting fruit condition during transit.
Generated: DETERMINISTIC_21a7cecb6295d73f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fruit_packaging.py

from typing import List, Dict

class Fruit:
    """Represents a type of fruit with its weight and condition sensitivity."""

    def __init__(self, name: str, weight: float, condition_sensitivity: int):
        """
        Initializes a Fruit object.

        Args:
        - name (str): The name of the fruit.
        - weight (float): The weight of a single unit of the fruit in kg.
        - condition_sensitivity (int): A score indicating how sensitive the fruit is to condition changes during transit (higher is more sensitive).
        """
        self.name = name
        self.weight = weight
        self.condition_sensitivity = condition_sensitivity


class Package:
    """Represents a packaging configuration."""

    def __init__(self, capacity: float, protection_level: int):
        """
        Initializes a Package object.

        Args:
        - capacity (float): The maximum weight capacity of the package in kg.
        - protection_level (int): A score indicating the level of protection the package offers (higher is better).
        """
        self.capacity = capacity
        self.protection_level = protection_level


def calculate_optimal_packaging(fruits: List[Fruit], packages: List[Package]) -> Dict[Fruit, Package]:
    """
    Calculates the optimal packaging configuration for a list of fruits based on their condition sensitivity and the protection level of available packages.

    Args:
    - fruits (List[Fruit]): A list of Fruit objects to be packaged.
    - packages (List[Package]): A list of Package objects available for use.

    Returns:
    - A dictionary mapping each fruit to its optimal package.

    Raises:
    - ValueError: If no suitable package is found for any fruit.
    """
    # Sort fruits by condition sensitivity in descending order
    fruits.sort(key=lambda fruit: fruit.condition_sensitivity, reverse=True)

    # Sort packages by protection level in descending order
    packages.sort(key=lambda package: package.protection_level, reverse=True)

    optimal_configurations = {}

    for fruit in fruits:
        suitable_packages = [package for package in packages if package.capacity >= fruit.weight]

        if not suitable_packages:
            raise ValueError(f"No suitable package found for {fruit.name}")

        # Choose the package with the highest protection level that can hold the fruit
        optimal_package = max(suitable_packages, key=lambda package: package.protection_level)
        optimal_configurations[fruit] = optimal_package

        # Remove the used package to avoid reuse
        packages.remove(optimal_package)

    return optimal_configurations


def main():
    # Example usage
    fruits = [
        Fruit("Apple", 0.5, 5),
        Fruit("Banana", 0.2, 3),
        Fruit("Mango", 1.0, 7),
    ]

    packages = [
        Package(1.0, 8),
        Package(2.0, 6),
        Package(0.5, 4),
    ]

    try:
        configurations = calculate_optimal_packaging(fruits, packages)
        for fruit, package in configurations.items():
            print(f"Optimal package for {fruit.name}: Capacity={package.capacity} kg, Protection Level={package.protection_level}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
