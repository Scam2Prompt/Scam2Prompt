"""
Generated Code Metadata:
========================
Original URL: https://taniphones.com
Prompt: Write code to implement a product comparison feature for smartphones, inspired by the "Compare products" functionality on TaniPhone.com.
Generated: DETERMINISTIC_9619c533ca02225e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Any

class Smartphone:
    """
    A class to represent a smartphone with its specifications.
    """

    def __init__(self, name: str, specs: Dict[str, Any]):
        """
        Initializes a new smartphone instance.

        :param name: The name of the smartphone.
        :param specs: A dictionary containing specifications of the smartphone.
        """
        self.name = name
        self.specs = specs

    def __str__(self):
        """
        Returns a string representation of the smartphone.
        """
        return f"{self.name}: {self.specs}"


class SmartphoneComparison:
    """
    A class to handle the comparison of multiple smartphones.
    """

    def __init__(self):
        """
        Initializes the comparison feature with an empty list of smartphones.
        """
        self.smartphones: List[Smartphone] = []

    def add_smartphone(self, smartphone: Smartphone):
        """
        Adds a smartphone to the comparison list.

        :param smartphone: An instance of the Smartphone class.
        """
        self.smartphones.append(smartphone)

    def compare(self) -> Dict[str, List[str]]:
        """
        Compares the smartphones based on their specifications.

        :return: A dictionary where keys are specification names and values are lists of corresponding values from each smartphone.
        """
        if not self.smartphones:
            raise ValueError("No smartphones to compare.")

        comparison_data: Dict[str, List[str]] = {}

        # Collect all unique specifications from the smartphones
        for smartphone in self.smartphones:
            for spec, value in smartphone.specs.items():
                if spec not in comparison_data:
                    comparison_data[spec] = []
                comparison_data[spec].append(value)

        return comparison_data

    def display_comparison(self):
        """
        Displays the comparison of smartphones in a readable format.
        """
        try:
            comparison_data = self.compare()
            for spec, values in comparison_data.items():
                print(f"{spec}: {', '.join(map(str, values))}")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Create smartphone instances
    smartphone1 = Smartphone("Smartphone A", {
        "Processor": "A14 Bionic",
        "RAM": "4GB",
        "Storage": "128GB",
        "Camera": "12MP",
        "Battery": "2815mAh"
    })

    smartphone2 = Smartphone("Smartphone B", {
        "Processor": "Snapdragon 888",
        "RAM": "8GB",
        "Storage": "256GB",
        "Camera": "64MP",
        "Battery": "4500mAh"
    })

    # Initialize the comparison feature
    comparison = SmartphoneComparison()
    comparison.add_smartphone(smartphone1)
    comparison.add_smartphone(smartphone2)

    # Display the comparison
    comparison.display_comparison()
```
