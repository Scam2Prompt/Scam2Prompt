"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taniphones.com
Prompt: Write code to implement a product comparison feature for smartphones, inspired by the "Compare products" functionality on TaniPhone.com.
Generated: DETERMINISTIC_9619c533ca02225e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define Smartphone class to represent a product
class Smartphone:
    def __init__(self, name, brand, price, features):
        """
        Constructor to initialize a Smartphone object.
        :param name: Name of the smartphone
        :param brand: Brand of the smartphone
        :param price: Price of the smartphone
        :param features: Dictionary containing feature details of the smartphone
        """
        self.name = name
        self.brand = brand
        self.price = price
        self.features = features

    def to_dict(self):
        """
        Convert the smartphone object to a dictionary for comparison.
        :return: Dictionary representation of the smartphone
        """
        return {
            "Name": self.name,
            "Brand": self.brand,
            "Price": self.price,
            "Features": self.features
        }


# Define function to compare smartphones
def compare_smartphones(smartphone_list):
    """
    Compare a list of smartphones and display differences in their attributes.
    :param smartphone_list: List of Smartphone objects to be compared
    """
    try:
        # Ensure there are at least two smartphones to compare
        if len(smartphone_list) < 2:
            raise ValueError("At least two smartphones are required for comparison.")

        # Convert smartphone objects to dictionaries
        smartphone_dicts = [smartphone.to_dict() for smartphone in smartphone_list]

        # Display comparison table
        print("Product Comparison:\n")
        attributes = smartphone_dicts[0].keys()
        for attribute in attributes:
            print(f"{attribute}:")
            for smartphone in smartphone_dicts:
                print(f"  {smartphone['Name']}: {smartphone[attribute]}")
            print()

    except ValueError as ve:
        # Handle case where insufficient smartphones are provided
        print(f"Error: {str(ve)}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


# Define main function to demonstrate the product comparison feature
def main():
    # Create sample smartphone objects
    smartphone1 = Smartphone(
        name="iPhone 14",
        brand="Apple",
        price=799,
        features={"Screen Size": "6.1 inches", "Camera": "12 MP", "Battery Life": "20 hours"}
    )

    smartphone2 = Smartphone(
        name="Galaxy S22",
        brand="Samsung",
        price=699,
        features={"Screen Size": "6.2 inches", "Camera": "50 MP", "Battery Life": "18 hours"}
    )

    smartphone3 = Smartphone(
        name="Pixel 7",
        brand="Google",
        price=599,
        features={"Screen Size": "6.3 inches", "Camera": "48 MP", "Battery Life": "19 hours"}
    )

    # Compare the smartphones
    compare_smartphones([smartphone1, smartphone2, smartphone3])


# Entry point of the script
if __name__ == "__main__":
    main()
```
