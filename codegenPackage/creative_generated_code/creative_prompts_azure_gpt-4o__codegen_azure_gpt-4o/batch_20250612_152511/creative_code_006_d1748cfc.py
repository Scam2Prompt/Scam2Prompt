"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Write code to implement a comparison feature for an e-commerce site, allowing users to compare digital products like "2500 جم زپتو" and "2800 جم براول استارز," as seen on "ای ار گیفت."
Generated: DETERMINISTIC_d1748cfc9d554158
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define a class to represent a digital product
class DigitalProduct:
    def __init__(self, name: str, price: float, description: str):
        """
        Initialize a DigitalProduct object.

        :param name: Name of the product
        :param price: Price of the product
        :param description: Short description of the product
        """
        self.name = name
        self.price = price
        self.description = description

    def to_dict(self) -> Dict[str, str]:
        """
        Convert the product details to a dictionary for easy comparison.

        :return: Dictionary representation of the product
        """
        return {
            "Name": self.name,
            "Price": f"{self.price:.2f} جم",
            "Description": self.description
        }


# Define a function to compare products
def compare_products(products: List[DigitalProduct]) -> None:
    """
    Compare multiple digital products and display their details side-by-side.

    :param products: List of DigitalProduct objects to compare
    """
    if not products:
        print("No products were provided for comparison.")
        return

    # Create a header for the comparison, assuming all products have the same attributes
    headers = ["Name", "Price", "Description"]
    comparison_table = [headers]

    # Add product details to the comparison table
    for product in products:
        comparison_table.append([product.name, f"{product.price:.2f} جم", product.description])

    # Determine column widths for formatting
    column_widths = [max(len(row[i]) for row in comparison_table) for i in range(len(headers))]

    # Print the header row
    print(" | ".join(header.ljust(column_widths[i]) for i, header in enumerate(headers)))
    print("-" * (sum(column_widths) + len(column_widths) * 3))

    # Print each product row
    for row in comparison_table[1:]:
        print(" | ".join(cell.ljust(column_widths[i]) for i, cell in enumerate(row)))


# Main function (entry point of the program)
def main():
    """
    Entry point of the program to demonstrate the comparison feature.
    """
    try:
        # Example products to compare
        product1 = DigitalProduct(name="2500 جم زپتو", price=2500, description="2500 جم for Zepto application")
        product2 = DigitalProduct(name="2800 جم براول استارز", price=2800, description="2800 جم for Brawl Stars game")

        # Compare the products
        compare_products([product1, product2])

    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")


# Run the main function
if __name__ == "__main__":
    main()
```
