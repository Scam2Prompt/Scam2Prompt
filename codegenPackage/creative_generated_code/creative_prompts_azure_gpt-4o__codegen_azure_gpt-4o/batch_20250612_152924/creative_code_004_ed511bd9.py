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


class QuoteGenerator:
    """
    A class to generate quotes for glass and aluminum carpentry projects
    using CristalesGraf's product categories as input parameters.
    """

    def __init__(self):
        # Load product data from a JSON file (or database in real-world scenarios)
        self.products = self._load_products()

    def _load_products(self):
        """
        Load product categories, pricing, and details.
        Replace this with a database query for production-level applications.

        Returns:
            dict: A dictionary of product categories and pricing.
        """
        try:
            # Example: Load sample data from a JSON file (replace this path with the actual source)
            with open("product_data.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise RuntimeError("Product data file not found.")
        except json.JSONDecodeError:
            raise RuntimeError("Error decoding product data file.")

    def calculate_quote(self, product_category, dimensions, quantity):
        """
        Calculate the quote for the specified product category.

        Args:
            product_category (str): The product category (e.g., "glass", "aluminum frame").
            dimensions (tuple): The dimensions of the product in meters (width, height).
            quantity (int): The number of units required.

        Returns:
            dict: A dictionary containing the quote details.
        """
        # Validate inputs
        if product_category not in self.products:
            raise ValueError(f"Invalid product category: {product_category}")

        if not isinstance(dimensions, tuple) or len(dimensions) != 2:
            raise ValueError("Dimensions must be a tuple (width, height) in meters.")

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Fetch product pricing details
        product_info = self.products[product_category]
        base_price_per_square_meter = product_info["price_per_square_meter"]

        # Calculate area and total cost
        width, height = dimensions
        area = width * height
        total_price = area * base_price_per_square_meter * quantity

        # Return a detailed quote
        return {
            "product_category": product_category,
            "dimensions": dimensions,
            "quantity": quantity,
            "area_per_unit": area,
            "price_per_square_meter": base_price_per_square_meter,
            "total_price": total_price,
        }

    def generate_quote_report(self, quote):
        """
        Generate a formatted report for the quote.

        Args:
            quote (dict): The quote details.

        Returns:
            str: A formatted quote report.
        """
        return (
            f"--- Quote Report ---\n"
            f"Product Category: {quote['product_category']}\n"
            f"Dimensions (WxH): {quote['dimensions'][0]}m x {quote['dimensions'][1]}m\n"
            f"Quantity: {quote['quantity']}\n"
            f"Area per Unit: {quote['area_per_unit']:.2f} m²\n"
            f"Price per Square Meter: ${quote['price_per_square_meter']:.2f}\n"
            f"Total Price: ${quote['total_price']:.2f}\n"
        )


if __name__ == "__main__":
    # Example usage of the QuoteGenerator class

    # Initialize QuoteGenerator instance
    generator = QuoteGenerator()

    # Input parameters (replace these with actual user inputs in production)
    product_category = "glass"  # Example category
    dimensions = (2.0, 1.5)  # Width x Height in meters
    quantity = 3  # Number of units

    try:
        # Generate a quote
        quote = generator.calculate_quote(product_category, dimensions, quantity)

        # Print the quote report
        report = generator.generate_quote_report(quote)
        print(report)
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```

### Note:
- The `product_data.json` file should contain product data in the following format (example):
```json
{
  "glass": {
    "price_per_square_meter": 150.0
  },
  "aluminum frame": {
    "price_per_square_meter": 100.0
  }
}
```
Replace this with an actual data source in a production environment (e.g., database).
