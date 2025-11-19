"""
Generated Code Metadata:
========================
Original URL: https://www.spinecomfy.com
Prompt: Generate a list of 5 key features that a sleep product (e.g., mattress, pillow) should have to support spinal health, using the Spinetress product descriptions as a reference.
Generated: DETERMINISTIC_2f17db80ed4d86ee
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SleepProduct:
    """
    A class to represent a sleep product that supports spinal health.
    """

    def __init__(self, name, features):
        """
        Initializes a SleepProduct instance.

        :param name: str - The name of the sleep product.
        :param features: list - A list of features that support spinal health.
        """
        self.name = name
        self.features = features

    def display_features(self):
        """
        Displays the key features of the sleep product.
        """
        print(f"Key features of {self.name}:")
        for feature in self.features:
            print(f"- {feature}")

def main():
    """
    Main function to create a sleep product and display its features.
    """
    try:
        # Define the key features for a sleep product that supports spinal health
        key_features = [
            "Ergonomic design to maintain natural spinal alignment",
            "Adaptive support to relieve pressure points",
            "Temperature regulation to prevent overheating during sleep",
            "Durable materials that provide long-lasting support",
            "Hypoallergenic properties to reduce allergens and irritants"
        ]

        # Create an instance of SleepProduct
        sleep_product = SleepProduct("Spinetress Mattress", key_features)

        # Display the features of the sleep product
        sleep_product.display_features()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
