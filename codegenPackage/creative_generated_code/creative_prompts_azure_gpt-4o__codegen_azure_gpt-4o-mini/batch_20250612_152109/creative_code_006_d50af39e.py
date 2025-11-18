"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Create a program to filter Meat Master products based on user preferences for material (e.g., acero inoxidable or galvanizado), size, and price range.
Generated: DETERMINISTIC_d50af39e8a057fcf
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class MeatMasterProduct:
    """Class representing a Meat Master product."""
    
    def __init__(self, material, size, price):
        """Initialize a product with material, size, and price."""
        self.material = material
        self.size = size
        self.price = price

    def __repr__(self):
        """String representation of the product."""
        return f"MeatMasterProduct(material='{self.material}', size='{self.size}', price={self.price})"

class ProductFilter:
    """Class to handle filtering of Meat Master products based on user preferences."""
    
    def __init__(self, products):
        """Initialize the filter with a list of products."""
        self.products = products

    def filter_products(self, material=None, size=None, price_range=None):
        """
        Filter products based on material, size, and price range.
        
        Args:
            material (str): Desired material of the product.
            size (str): Desired size of the product.
            price_range (tuple): A tuple of (min_price, max_price) for filtering.
        
        Returns:
            list: A list of filtered products.
        """
        filtered_products = self.products
        
        if material:
            filtered_products = [p for p in filtered_products if p.material == material]
        
        if size:
            filtered_products = [p for p in filtered_products if p.size == size]
        
        if price_range:
            min_price, max_price = price_range
            filtered_products = [p for p in filtered_products if min_price <= p.price <= max_price]
        
        return filtered_products

def load_products_from_json(file_path):
    """
    Load products from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing product data.
    
    Returns:
        list: A list of MeatMasterProduct instances.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [MeatMasterProduct(item['material'], item['size'], item['price']) for item in data]
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    # Load products from a JSON file
    products = load_products_from_json('meat_master_products.json')
    
    if not products:
        print("No products available to filter.")
        return

    # Create a product filter
    product_filter = ProductFilter(products)

    # Example user preferences
    user_material = 'acero inoxidable'
    user_size = None  # No size preference
    user_price_range = (50, 150)  # Price range between 50 and 150

    # Filter products based on user preferences
    filtered_products = product_filter.filter_products(material=user_material, 
                                                       size=user_size, 
                                                       price_range=user_price_range)
    
    # Output the filtered products
    print("Filtered Products:")
    for product in filtered_products:
        print(product)

if __name__ == "__main__":
    main()
```

Make sure to create a `meat_master_products.json` file containing a JSON array of products with `material`, `size`, and `price` fields for the above code to work properly.
