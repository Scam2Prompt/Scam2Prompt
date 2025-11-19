"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Compare the features of the Hunt 48 Limitless UD Carbon Spoke Disc Wheelset with other wheelsets from similar brands, highlighting the benefits of using Hunt wheels for a competitive cycling team like Race Ride Fire.
Generated: DETERMINISTIC_89270dfc2690f392
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent a wheelset
class Wheelset:
    def __init__(self, brand, model, material, weight, aerodynamics, price, durability):
        """
        Initialize a Wheelset object.

        :param brand: Brand name of the wheelset
        :param model: Model name of the wheelset
        :param material: Material used in the wheelset (e.g., carbon, aluminum)
        :param weight: Weight of the wheelset in grams
        :param aerodynamics: Aerodynamic rating (1-10 scale)
        :param price: Price of the wheelset in USD
        :param durability: Durability rating (1-10 scale)
        """
        self.brand = brand
        self.model = model
        self.material = material
        self.weight = weight
        self.aerodynamics = aerodynamics
        self.price = price
        self.durability = durability

    def to_dict(self):
        """
        Convert the Wheelset object to a dictionary for easy comparison.

        :return: Dictionary representation of the wheelset
        """
        return {
            "brand": self.brand,
            "model": self.model,
            "material": self.material,
            "weight": self.weight,
            "aerodynamics": self.aerodynamics,
            "price": self.price,
            "durability": self.durability,
        }


# Function to compare wheelsets and highlight benefits of Hunt wheels
def compare_wheelsets(hunt_wheelset, other_wheelsets):
    """
    Compare the Hunt wheelset with other wheelsets and highlight its benefits.

    :param hunt_wheelset: Wheelset object representing the Hunt wheelset
    :param other_wheelsets: List of Wheelset objects representing other brands
    :return: Comparison results as a dictionary
    """
    try:
        comparison_results = {"Hunt Benefits": []}

        for other_wheelset in other_wheelsets:
            # Compare weight
            if hunt_wheelset.weight < other_wheelset.weight:
                comparison_results["Hunt Benefits"].append(
                    f"Lighter than {other_wheelset.brand} {other_wheelset.model} by {other_wheelset.weight - hunt_wheelset.weight} grams."
                )

            # Compare aerodynamics
            if hunt_wheelset.aerodynamics > other_wheelset.aerodynamics:
                comparison_results["Hunt Benefits"].append(
                    f"More aerodynamic than {other_wheelset.brand} {other_wheelset.model} (Rating: {hunt_wheelset.aerodynamics} vs {other_wheelset.aerodynamics})."
                )

            # Compare price
            if hunt_wheelset.price < other_wheelset.price:
                comparison_results["Hunt Benefits"].append(
                    f"More affordable than {other_wheelset.brand} {other_wheelset.model} by ${other_wheelset.price - hunt_wheelset.price}."
                )

            # Compare durability
            if hunt_wheelset.durability > other_wheelset.durability:
                comparison_results["Hunt Benefits"].append(
                    f"More durable than {other_wheelset.brand} {other_wheelset.model} (Rating: {hunt_wheelset.durability} vs {other_wheelset.durability})."
                )

        return comparison_results

    except Exception as e:
        # Handle any unexpected errors
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Create Hunt wheelset object
    hunt_wheelset = Wheelset(
        brand="Hunt",
        model="48 Limitless UD Carbon Spoke Disc",
        material="Carbon",
        weight=1480,
        aerodynamics=9,
        price=1599,
        durability=8,
    )

    # Create other wheelset objects
    other_wheelsets = [
        Wheelset(
            brand="Zipp",
            model="404 Firecrest",
            material="Carbon",
            weight=1520,
            aerodynamics=8,
            price=1900,
            durability=7,
        ),
        Wheelset(
            brand="Enve",
            model="SES 4.5",
            material="Carbon",
            weight=1500,
            aerodynamics=8,
            price=1800,
            durability=8,
        ),
    ]

    # Compare Hunt wheelset with others
    results = compare_wheelsets(hunt_wheelset, other_wheelsets)

    # Print results in a readable format
    print(json.dumps(results, indent=4))
```
