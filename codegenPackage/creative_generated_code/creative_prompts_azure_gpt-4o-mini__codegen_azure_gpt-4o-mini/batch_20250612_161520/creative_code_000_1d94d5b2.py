"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geektech.uk
Prompt: Generate a comparison code snippet that evaluates the features of the Nokia Edge Max 2024 5G against the iPhone 16 Pro based on their specifications.
Generated: DETERMINISTIC_1d94d5b2ea2fdfc1
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Smartphone:
    """Class to represent a smartphone with its specifications."""

    def __init__(self, name, brand, battery, camera, storage, display, price):
        """
        Initialize a smartphone instance.

        :param name: The name of the smartphone.
        :param brand: The brand of the smartphone.
        :param battery: Battery specifications (mAh).
        :param camera: Camera specifications (MP).
        :param storage: Storage capacity (GB).
        :param display: Display size (inches).
        :param price: Price of the smartphone.
        """
        self.name = name
        self.brand = brand
        self.battery = battery  # mAh
        self.camera = camera  # Megapixels
        self.storage = storage  # GB
        self.display = display  # inches
        self.price = price  # USD

    def __str__(self):
        """Return a string representation of the smartphone."""
        return f"{self.brand} {self.name}: {self.display}\" display, {self.battery}mAh battery, " \
               f"{self.camera}MP camera, {self.storage}GB storage, ${self.price}"


def compare_smartphones(smartphone1, smartphone2):
    """
    Compare two smartphones and print their specifications.

    :param smartphone1: The first smartphone to compare.
    :param smartphone2: The second smartphone to compare.
    :raises ValueError: If either smartphone is not an instance of Smartphone.
    """
    if not isinstance(smartphone1, Smartphone) or not isinstance(smartphone2, Smartphone):
        raise ValueError("Both inputs must be instances of the Smartphone class.")

    print("Comparing Smartphones:\n")
    print(smartphone1)
    print(smartphone2)

    # Feature comparison
    features = {
        "Battery": (smartphone1.battery, smartphone2.battery),
        "Camera": (smartphone1.camera, smartphone2.camera),
        "Storage": (smartphone1.storage, smartphone2.storage),
        "Display": (smartphone1.display, smartphone2.display),
        "Price": (smartphone1.price, smartphone2.price)
    }

    for feature, values in features.items():
        print(f"{feature}: {smartphone1.name} = {values[0]}, {smartphone2.name} = {values[1]}")


# Define specifications for the Nokia Edge Max 2024 5G
nokia_edge_max_2024 = Smartphone(
    name="Edge Max 2024 5G",
    brand="Nokia",
    battery=6000,
    camera=108,
    storage=256,
    display=6.9,
    price=899
)

# Define specifications for the iPhone 16 Pro
iphone_16_pro = Smartphone(
    name="16 Pro",
    brand="Apple",
    battery=3500,
    camera=48,
    storage=512,
    display=6.1,
    price=1099
)

# Compare the two smartphones
compare_smartphones(nokia_edge_max_2024, iphone_16_pro)
```
