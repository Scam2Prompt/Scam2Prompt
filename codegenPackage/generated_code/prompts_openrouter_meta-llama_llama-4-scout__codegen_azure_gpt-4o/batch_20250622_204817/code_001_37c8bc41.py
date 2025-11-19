"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Compare and contrast Engel's hard coolers and soft coolers, highlighting their differences in design, functionality, and price point."
Generated: DETERMINISTIC_37c8bc4150ee060e
Batch ID: 20250622_204817
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

# Define a class to represent Engel coolers
class EngelCooler:
    def __init__(self, name, type, design, functionality, price):
        """
        Initialize an EngelCooler object.

        :param name: Name of the cooler
        :param type: Type of the cooler (e.g., 'Hard' or 'Soft')
        :param design: Design features of the cooler
        :param functionality: Functional features of the cooler
        :param price: Price of the cooler in USD
        """
        self.name = name
        self.type = type
        self.design = design
        self.functionality = functionality
        self.price = price

    def to_dict(self):
        """
        Convert the EngelCooler object to a dictionary.

        :return: Dictionary representation of the cooler
        """
        return {
            "name": self.name,
            "type": self.type,
            "design": self.design,
            "functionality": self.functionality,
            "price": self.price,
        }


# Function to compare and contrast two coolers
def compare_coolers(cooler1, cooler2):
    """
    Compare and contrast two Engel coolers.

    :param cooler1: First EngelCooler object
    :param cooler2: Second EngelCooler object
    :return: Dictionary highlighting differences between the two coolers
    """
    differences = {}

    # Compare design
    if cooler1.design != cooler2.design:
        differences["design"] = {
            cooler1.name: cooler1.design,
            cooler2.name: cooler2.design,
        }

    # Compare functionality
    if cooler1.functionality != cooler2.functionality:
        differences["functionality"] = {
            cooler1.name: cooler1.functionality,
            cooler2.name: cooler2.functionality,
        }

    # Compare price
    if cooler1.price != cooler2.price:
        differences["price"] = {
            cooler1.name: f"${cooler1.price:.2f}",
            cooler2.name: f"${cooler2.price:.2f}",
        }

    return differences


# Main function
def main():
    """
    Main function to demonstrate the comparison of Engel coolers.
    """
    try:
        # Create instances of Engel coolers
        hard_cooler = EngelCooler(
            name="Engel Hard Cooler",
            type="Hard",
            design="Rugged, durable, heavy-duty construction",
            functionality="Superior ice retention, ideal for outdoor adventures",
            price=299.99,
        )

        soft_cooler = EngelCooler(
            name="Engel Soft Cooler",
            type="Soft",
            design="Lightweight, compact, easy to carry",
            functionality="Moderate ice retention, suitable for day trips",
            price=149.99,
        )

        # Compare the two coolers
        differences = compare_coolers(hard_cooler, soft_cooler)

        # Print the differences in a readable format
        print("Comparison of Engel Coolers:")
        print(json.dumps(differences, indent=4))

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
