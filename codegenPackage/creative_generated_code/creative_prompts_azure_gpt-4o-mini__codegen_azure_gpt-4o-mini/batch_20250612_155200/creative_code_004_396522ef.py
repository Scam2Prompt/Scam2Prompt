"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sale-azuki.com
Prompt: Develop a product comparison tool that includes the CHIKARA cooling shirt and similar cooling apparel, focusing on battery life and material quality.
Generated: DETERMINISTIC_396522ef5dd792a2
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CoolingApparel:
    """
    A class to represent cooling apparel.

    Attributes:
        name (str): Name of the cooling apparel.
        battery_life (int): Battery life in hours.
        material_quality (str): Description of the material quality.
    """

    def __init__(self, name, battery_life, material_quality):
        """
        Initializes a CoolingApparel instance.

        Parameters:
            name (str): Name of the cooling apparel.
            battery_life (int): Battery life in hours.
            material_quality (str): Description of the material quality.
        """
        self.name = name
        self.battery_life = battery_life
        self.material_quality = material_quality

    def to_dict(self):
        """Converts the CoolingApparel instance to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'battery_life': self.battery_life,
            'material_quality': self.material_quality,
        }


class ProductComparisonTool:
    """
    A class to compare different cooling apparel products.

    Attributes:
        products (list): List of CoolingApparel instances.
    """

    def __init__(self):
        """Initializes the ProductComparisonTool with an empty product list."""
        self.products = []

    def add_product(self, product):
        """
        Adds a CoolingApparel instance to the comparison list.

        Parameters:
            product (CoolingApparel): An instance of CoolingApparel to add.
        """
        if isinstance(product, CoolingApparel):
            self.products.append(product)
        else:
            raise ValueError("Product must be an instance of CoolingApparel")

    def compare_products(self):
        """Generates a comparison report of the added products."""
        if not self.products:
            return "No products to compare."

        comparison_report = []
        for product in self.products:
            comparison_report.append(product.to_dict())
        return json.dumps(comparison_report, indent=4)

    def save_comparison_report(self, filename):
        """
        Saves the comparison report to a JSON file.

        Parameters:
            filename (str): The name of the file to save the report to.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.compare_products())
        except IOError as e:
            print(f"An error occurred while saving the report: {e}")


if __name__ == "__main__":
    # Create instances of CoolingApparel
    chikara_shirt = CoolingApparel("CHIKARA Cooling Shirt", battery_life=10, material_quality="High-performance breathable fabric")
    similar_shirt_1 = CoolingApparel("CoolTech Shirt", battery_life=8, material_quality="Moisture-wicking polyester")
    similar_shirt_2 = CoolingApparel("FrostWear Tee", battery_life=12, material_quality="Lightweight cotton blend")

    # Create comparison tool and add products
    comparison_tool = ProductComparisonTool()
    comparison_tool.add_product(chikara_shirt)
    comparison_tool.add_product(similar_shirt_1)
    comparison_tool.add_product(similar_shirt_2)

    # Generate comparison report
    print("Comparison Report:")
    print(comparison_tool.compare_products())

    # Save report to file
    comparison_tool.save_comparison_report('cooling_apparel_comparison.json')
```
