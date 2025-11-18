"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pavainc.com
Prompt: Generate a script to automate customer quotes for bulk salt and UltraGLOW™ Snow and Ice Melt orders, factoring in delivery zones and product availability.
Generated: DETERMINISTIC_ab3a444480ca25ed
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Product:
    """Represents a product with its name, price per unit, and availability."""
    
    def __init__(self, name, price_per_unit, available_units):
        self.name = name
        self.price_per_unit = price_per_unit
        self.available_units = available_units

    def is_available(self, quantity):
        """Check if the requested quantity is available."""
        return quantity <= self.available_units

class DeliveryZone:
    """Represents a delivery zone with its name and delivery cost."""
    
    def __init__(self, name, delivery_cost):
        self.name = name
        self.delivery_cost = delivery_cost

class QuoteGenerator:
    """Generates quotes for customers based on their orders."""
    
    def __init__(self, products, delivery_zones):
        self.products = products
        self.delivery_zones = delivery_zones

    def generate_quote(self, product_name, quantity, delivery_zone_name):
        """Generates a quote for the requested product and quantity in a given delivery zone."""
        try:
            # Validate product availability
            product = self.products.get(product_name)
            if not product:
                raise ValueError(f"Product '{product_name}' not found.")
            if not product.is_available(quantity):
                raise ValueError(f"Requested quantity {quantity} of '{product_name}' is not available.")

            # Validate delivery zone
            delivery_zone = self.delivery_zones.get(delivery_zone_name)
            if not delivery_zone:
                raise ValueError(f"Delivery zone '{delivery_zone_name}' not found.")
            
            # Calculate total cost
            total_product_cost = product.price_per_unit * quantity
            total_cost = total_product_cost + delivery_zone.delivery_cost

            # Prepare quote
            quote = {
                'product': product_name,
                'quantity': quantity,
                'delivery_zone': delivery_zone_name,
                'product_cost': total_product_cost,
                'delivery_cost': delivery_zone.delivery_cost,
                'total_cost': total_cost
            }
            return quote

        except ValueError as e:
            # Log the error message
            print(f"Error: {e}")
            return None

def load_products_from_json(file_path):
    """Loads product information from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            product_data = json.load(file)
            return {item['name']: Product(item['name'], item['price_per_unit'], item['available_units']) for item in product_data}
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading products: {e}")
        return {}

def load_delivery_zones_from_json(file_path):
    """Loads delivery zone information from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            delivery_zone_data = json.load(file)
            return {item['name']: DeliveryZone(item['name'], item['delivery_cost']) for item in delivery_zone_data}
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading delivery zones: {e}")
        return {}

# Example usage
if __name__ == '__main__':
    products = load_products_from_json('products.json')
    delivery_zones = load_delivery_zones_from_json('delivery_zones.json')

    quote_generator = QuoteGenerator(products, delivery_zones)

    # Generating a quote for a sample order
    quote = quote_generator.generate_quote("UltraGLOW™ Snow and Ice Melt", 100, "Zone A")
    if quote:
        print("Quote generated successfully:")
        print(json.dumps(quote, indent=2))
    else:
        print("Failed to generate quote.")
``` 

**Note:** Ensure that `products.json` and `delivery_zones.json` are properly formatted JSON files containing the necessary data structure for products and delivery zones before running the script.
