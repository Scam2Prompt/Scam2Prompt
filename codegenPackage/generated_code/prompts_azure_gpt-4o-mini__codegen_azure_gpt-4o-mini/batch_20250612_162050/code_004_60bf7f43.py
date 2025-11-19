"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Illustrate how to implement a product comparison feature for Shelter's Electric Fireplaces using LED 3D technology versus traditional models.
Generated: DETERMINISTIC_60bf7f436c5cb425
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_comparison.py

class ElectricFireplace:
    """
    A class to represent an electric fireplace.

    Attributes:
        name (str): The name of the fireplace.
        led_technology (bool): Indicates if the fireplace uses LED 3D technology.
        price (float): The price of the fireplace.
        features (list): A list of features of the fireplace.
    """

    def __init__(self, name, led_technology, price, features):
        """
        Initializes the ElectricFireplace with the given attributes.

        Args:
            name (str): The name of the fireplace.
            led_technology (bool): Indicates if the fireplace uses LED 3D technology.
            price (float): The price of the fireplace.
            features (list): A list of features of the fireplace.
        """
        self.name = name
        self.led_technology = led_technology
        self.price = price
        self.features = features

    def display_info(self):
        """Displays the information of the fireplace."""
        tech_type = "LED 3D Technology" if self.led_technology else "Traditional Model"
        print(f"Name: {self.name}")
        print(f"Technology: {tech_type}")
        print(f"Price: ${self.price:.2f}")
        print("Features:")
        for feature in self.features:
            print(f"- {feature}")
        print("\n")


def compare_fireplaces(fireplace1, fireplace2):
    """
    Compares two electric fireplaces and displays their information.

    Args:
        fireplace1 (ElectricFireplace): The first fireplace to compare.
        fireplace2 (ElectricFireplace): The second fireplace to compare.
    """
    print("Comparing Electric Fireplaces:\n")
    fireplace1.display_info()
    fireplace2.display_info()

    # Price comparison
    if fireplace1.price < fireplace2.price:
        print(f"{fireplace1.name} is cheaper than {fireplace2.name}.")
    elif fireplace1.price > fireplace2.price:
        print(f"{fireplace2.name} is cheaper than {fireplace1.name}.")
    else:
        print("Both fireplaces have the same price.")

    # Feature comparison
    common_features = set(fireplace1.features) & set(fireplace2.features)
    if common_features:
        print("Common Features:")
        for feature in common_features:
            print(f"- {feature}")
    else:
        print("No common features found.")

    print("\n")


def main():
    """
    Main function to create fireplace instances and compare them.
    """
    try:
        # Creating instances of ElectricFireplace
        fireplace1 = ElectricFireplace(
            name="Shelter LED 3D Fireplace",
            led_technology=True,
            price=499.99,
            features=["Remote Control", "Adjustable Flame", "Energy Efficient"]
        )

        fireplace2 = ElectricFireplace(
            name="Shelter Traditional Fireplace",
            led_technology=False,
            price=399.99,
            features=["Realistic Flame", "Manual Control", "Classic Design"]
        )

        # Comparing the two fireplaces
        compare_fireplaces(fireplace1, fireplace2)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
