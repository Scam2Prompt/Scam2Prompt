"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Write a script to automate the generation of quotes for glass and aluminum carpentry projects, using CristalesGraf's product categories as input parameters.
Generated: DETERMINISTIC_ed511bd9ab82334e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class QuoteGenerator:
    """
    A class to generate quotes for glass and aluminum carpentry projects.
    """

    def __init__(self, product_data: str):
        """
        Initializes the QuoteGenerator with product data.

        :param product_data: A JSON string containing product categories and their prices.
        """
        self.products = self.load_product_data(product_data)

    def load_product_data(self, product_data: str) -> Dict[str, Any]:
        """
        Loads product data from a JSON string.

        :param product_data: A JSON string containing product categories and their prices.
        :return: A dictionary with product categories and prices.
        """
        try:
            return json.loads(product_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid product data format") from e

    def generate_quote(self, project_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generates a quote based on project details.

        :param project_details: A dictionary containing project specifics, including product categories and quantities.
        :return: A dictionary containing the total quote and breakdown of costs.
        """
        total_cost = 0
        breakdown = {}

        for category, quantity in project_details.items():
            if category not in self.products:
                raise ValueError(f"Product category '{category}' is not valid.")
            
            price_per_unit = self.products[category]
            cost = price_per_unit * quantity
            breakdown[category] = {
                'quantity': quantity,
                'price_per_unit': price_per_unit,
                'total_cost': cost
            }
            total_cost += cost

        return {
            'total_cost': total_cost,
            'breakdown': breakdown
        }

# Example usage:

if __name__ == "__main__":
    # Sample product data in JSON format
    product_data = json.dumps({
        "glass": 50.0,  # price per unit (e.g., per square meter)
        "aluminum": 70.0  # price per unit (e.g., per meter)
    })

    # Create an instance of QuoteGenerator
    quote_generator = QuoteGenerator(product_data)

    # Example project details
    project_details = {
        "glass": 10,  # 10 square meters of glass
        "aluminum": 5  # 5 meters of aluminum
    }

    try:
        quote = quote_generator.generate_quote(project_details)
        print("Generated Quote:")
        print(json.dumps(quote, indent=4))
    except ValueError as e:
        print(f"Error generating quote: {e}")
```
