"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: "Develop a Python program to analyze customer requests for custom menuiserie products, such as pergolas and fermetures bâtiment, and generate quotes based on product specifications and pricing rules."
Generated: DETERMINISTIC_9fc7a2d414631e11
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Product:
    """
    Represents a custom menuiserie product with specifications and pricing rules.
    """
    def __init__(self, name, base_price, material_cost, labor_cost):
        self.name = name
        self.base_price = base_price
        self.material_cost = material_cost
        self.labor_cost = labor_cost

    def calculate_price(self, dimensions, material_type, complexity_level):
        """
        Calculate the price of the product based on dimensions, material type, and complexity level.
        :param dimensions: dict with 'width' and 'height' in meters
        :param material_type: str, type of material (e.g., 'wood', 'aluminum')
        :param complexity_level: int, complexity level (1-5)
        :return: float, total price
        """
        try:
            area = dimensions['width'] * dimensions['height']
            material_multiplier = self.material_cost.get(material_type, 1.0)
            complexity_multiplier = 1 + (complexity_level * 0.1)
            total_price = self.base_price + (area * material_multiplier) + (self.labor_cost * complexity_multiplier)
            return round(total_price, 2)
        except KeyError as e:
            raise ValueError(f"Missing required dimension key: {e}")
        except Exception as e:
            raise ValueError(f"Error calculating price: {e}")

class QuoteGenerator:
    """
    Handles customer requests and generates quotes for custom menuiserie products.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the catalog.
        :param product: Product object
        """
        self.products[product.name] = product

    def generate_quote(self, request):
        """
        Generate a quote based on customer request.
        :param request: dict containing 'product_name', 'dimensions', 'material_type', and 'complexity_level'
        :return: dict containing 'product_name', 'total_price', and 'details'
        """
        try:
            product_name = request['product_name']
            dimensions = request['dimensions']
            material_type = request['material_type']
            complexity_level = request['complexity_level']

            if product_name not in self.products:
                raise ValueError(f"Product '{product_name}' not found in catalog.")

            product = self.products[product_name]
            total_price = product.calculate_price(dimensions, material_type, complexity_level)

            return {
                "product_name": product_name,
                "total_price": total_price,
                "details": {
                    "dimensions": dimensions,
                    "material_type": material_type,
                    "complexity_level": complexity_level
                }
            }
        except KeyError as e:
            raise ValueError(f"Missing required request key: {e}")
        except Exception as e:
            raise ValueError(f"Error generating quote: {e}")

def main():
    """
    Main function to demonstrate the program functionality.
    """
    # Initialize the quote generator
    quote_generator = QuoteGenerator()

    # Add products to the catalog
    quote_generator.add_product(Product(
        name="Pergola",
        base_price=500,
        material_cost={"wood": 50, "aluminum": 70},
        labor_cost=100
    ))
    quote_generator.add_product(Product(
        name="Fermeture Bâtiment",
        base_price=300,
        material_cost={"wood": 40, "aluminum": 60},
        labor_cost=80
    ))

    # Example customer request
    customer_request = {
        "product_name": "Pergola",
        "dimensions": {"width": 4, "height": 3},
        "material_type": "wood",
        "complexity_level": 3
    }

    try:
        # Generate quote
        quote = quote_generator.generate_quote(customer_request)
        print("Generated Quote:")
        print(json.dumps(quote, indent=4))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
