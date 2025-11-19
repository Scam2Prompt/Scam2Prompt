"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: What are the advantages of using Special Metal Iran's superalloys in power plant applications?
Generated: DETERMINISTIC_a3c0ae956c2a26f6
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class Superalloy:
    def __init__(self, name, advantages):
        """
        Initialize a Superalloy object.

        Args:
            name (str): Name of the superalloy.
            advantages (list): List of advantages of the superalloy.
        """
        self.name = name
        self.advantages = advantages

class PowerPlantApplication:
    def __init__(self):
        """
        Initialize a PowerPlantApplication object.
        """
        self.superalloys = {}

    def add_superalloy(self, superalloy):
        """
        Add a superalloy to the power plant application.

        Args:
            superalloy (Superalloy): Superalloy object to add.
        """
        self.superalloys[superalloy.name] = superalloy

    def get_advantages(self, superalloy_name):
        """
        Get the advantages of a superalloy in power plant applications.

        Args:
            superalloy_name (str): Name of the superalloy.

        Returns:
            list: List of advantages of the superalloy.

        Raises:
            ValueError: If the superalloy is not found.
        """
        if superalloy_name not in self.superalloys:
            raise ValueError("Superalloy not found")
        return self.superalloys[superalloy_name].advantages

def main():
    # Create a power plant application
    power_plant_app = PowerPlantApplication()

    # Create special metal iran's superalloys
    special_metal_iran_superalloys = [
        Superalloy("Inconel 617", ["High temperature resistance", "Corrosion resistance", "High strength"]),
        Superalloy("Inconel 625", ["High temperature resistance", "Corrosion resistance", "High strength", "Weldability"]),
        Superalloy("Haynes 230", ["High temperature resistance", "Corrosion resistance", "High strength", "Low thermal expansion"]),
    ]

    # Add superalloys to the power plant application
    for superalloy in special_metal_iran_superalloys:
        power_plant_app.add_superalloy(superalloy)

    # Get advantages of a superalloy
    superalloy_name = "Inconel 617"
    try:
        advantages = power_plant_app.get_advantages(superalloy_name)
        print(f"Advantages of {superalloy_name} in power plant applications:")
        for advantage in advantages:
            print(f"- {advantage}")
    except ValueError as e:
        print(f"Error: {e}")

    # Print advantages of all superalloys in JSON format
    superalloys_json = []
    for superalloy_name, superalloy in power_plant_app.superalloys.items():
        superalloy_json = {
            "name": superalloy_name,
            "advantages": superalloy.advantages,
        }
        superalloys_json.append(superalloy_json)
    print("\nAdvantages of all superalloys in JSON format:")
    print(json.dumps(superalloys_json, indent=4))

if __name__ == "__main__":
    main()
```
