"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Write a code snippet in a programming language of your choice to compare features and prices of different mobile phone accessories, such as those offered by Telltak.
Generated: DETERMINISTIC_06c9b08620a55404
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mobile_accessory_comparator.py

class MobileAccessory:
    """Represents a mobile phone accessory."""

    def __init__(self, name, brand, price, features):
        """
        Initializes a MobileAccessory object.

        Args:
            name (str): Name of the accessory.
            brand (str): Brand of the accessory.
            price (float): Price of the accessory.
            features (list): List of features of the accessory.
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.features = features

    def __str__(self):
        return f"{self.name} by {self.brand}"


class AccessoryComparator:
    """Compares features and prices of different mobile phone accessories."""

    def __init__(self):
        self.accessories = []

    def add_accessory(self, accessory):
        """
        Adds a mobile accessory to the comparator.

        Args:
            accessory (MobileAccessory): Accessory to add.
        """
        self.accessories.append(accessory)

    def compare_by_price(self):
        """
        Sorts and prints accessories by price.

        Returns:
            list: Sorted list of accessories by price.
        """
        sorted_accessories = sorted(self.accessories, key=lambda x: x.price)
        print("Accessories sorted by price:")
        for accessory in sorted_accessories:
            print(f"{accessory}: ${accessory.price:.2f}")
        return sorted_accessories

    def compare_by_features(self, feature):
        """
        Finds and prints accessories that have a specific feature.

        Args:
            feature (str): Feature to search for.

        Returns:
            list: List of accessories that have the specified feature.
        """
        accessories_with_feature = [a for a in self.accessories if feature in a.features]
        print(f"Accessories with '{feature}':")
        for accessory in accessories_with_feature:
            print(f"{accessory}: ${accessory.price:.2f}")
        return accessories_with_feature


def main():
    try:
        comparator = AccessoryComparator()

        # Example accessories
        telltak_screen_protector = MobileAccessory(
            "Screen Protector",
            "Telltak",
            9.99,
            ["Scratch-resistant", "Easy to install"]
        )
        telltak_phone_case = MobileAccessory(
            "Phone Case",
            "Telltak",
            19.99,
            ["Durable", "Slim design"]
        )
        otterbox_phone_case = MobileAccessory(
            "Phone Case",
            "OtterBox",
            29.99,
            ["Durable", "Slim design", "Shock-resistant"]
        )

        # Add accessories to comparator
        comparator.add_accessory(telltak_screen_protector)
        comparator.add_accessory(telltak_phone_case)
        comparator.add_accessory(otterbox_phone_case)

        # Compare accessories by price
        comparator.compare_by_price()

        # Compare accessories by feature
        comparator.compare_by_features("Scratch-resistant")
        comparator.compare_by_features("Durable")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
