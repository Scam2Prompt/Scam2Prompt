"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Compare the features and prices of the ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI Lithium Portable Power Packs, highlighting their suitability for camping and off-grid applications.
Generated: DETERMINISTIC_0c90e5e5858ead62
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent a portable power pack
class PortablePowerPack:
    def __init__(self, name, capacity, weight, price, features):
        """
        Initialize the PortablePowerPack object.

        :param name: Name of the power pack
        :param capacity: Battery capacity in watt-hours (Wh)
        :param weight: Weight in kilograms (kg)
        :param price: Price in USD
        :param features: List of features
        """
        self.name = name
        self.capacity = capacity
        self.weight = weight
        self.price = price
        self.features = features

    def suitability_for_camping(self):
        """
        Determine suitability for camping based on weight and capacity.

        :return: Suitability message
        """
        if self.weight <= 10 and self.capacity >= 300:
            return f"{self.name} is highly suitable for camping due to its lightweight and sufficient capacity."
        elif self.weight > 10:
            return f"{self.name} may be less suitable for camping due to its heavier weight."
        else:
            return f"{self.name} may be less suitable for camping due to its lower capacity."

    def suitability_for_off_grid(self):
        """
        Determine suitability for off-grid applications based on capacity.

        :return: Suitability message
        """
        if self.capacity >= 1000:
            return f"{self.name} is highly suitable for off-grid applications due to its high capacity."
        else:
            return f"{self.name} may be less suitable for off-grid applications due to its lower capacity."

    def to_dict(self):
        """
        Convert the object to a dictionary for easy comparison.

        :return: Dictionary representation of the object
        """
        return {
            "Name": self.name,
            "Capacity (Wh)": self.capacity,
            "Weight (kg)": self.weight,
            "Price (USD)": self.price,
            "Features": self.features,
        }


# Create instances for ECOFLOW DELTA MAX 2 and ECOFLOW RIVER 2 MINI
delta_max_2 = PortablePowerPack(
    name="ECOFLOW DELTA MAX 2",
    capacity=2016,  # Example capacity in Wh
    weight=22,  # Example weight in kg
    price=1999,  # Example price in USD
    features=["Expandable capacity", "Fast charging", "Multiple output ports", "Solar charging compatibility"],
)

river_2_mini = PortablePowerPack(
    name="ECOFLOW RIVER 2 MINI",
    capacity=256,  # Example capacity in Wh
    weight=3.5,  # Example weight in kg
    price=239,  # Example price in USD
    features=["Lightweight", "Fast charging", "Compact design", "Solar charging compatibility"],
)

# Compare the two power packs
def compare_power_packs(pack1, pack2):
    """
    Compare two power packs and print their details and suitability.

    :param pack1: First power pack object
    :param pack2: Second power pack object
    """
    print("Comparison of Portable Power Packs:")
    print(json.dumps(pack1.to_dict(), indent=4))
    print(json.dumps(pack2.to_dict(), indent=4))
    print("\nSuitability for Camping:")
    print(pack1.suitability_for_camping())
    print(pack2.suitability_for_camping())
    print("\nSuitability for Off-Grid Applications:")
    print(pack1.suitability_for_off_grid())
    print(pack2.suitability_for_off_grid())


# Main function to execute the comparison
def main():
    try:
        compare_power_packs(delta_max_2, river_2_mini)
    except Exception as e:
        print(f"An error occurred during comparison: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
