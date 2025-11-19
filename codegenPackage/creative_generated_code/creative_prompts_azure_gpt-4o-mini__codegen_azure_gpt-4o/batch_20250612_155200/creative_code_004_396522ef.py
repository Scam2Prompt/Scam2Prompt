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

# Define a Product class to represent each cooling apparel item
class Product:
    def __init__(self, name, battery_life, material_quality):
        """
        Initialize a Product object.
        
        :param name: Name of the product
        :param battery_life: Battery life of the cooling feature (in hours)
        :param material_quality: Material quality rating (scale of 1-10)
        """
        self.name = name
        self.battery_life = battery_life
        self.material_quality = material_quality
    
    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"{self.name} - Battery Life: {self.battery_life} hours, Material Quality: {self.material_quality}/10"

# Function to compare products and return the best option
def compare_products(products):
    """
    Compare a list of products based on battery life and material quality.
    Priority is given to battery life, followed by material quality in case of a tie.
    
    :param products: List of Product objects
    :return: The best product based on the comparison criteria
    """
    if not products:
        raise ValueError("The products list cannot be empty.")

    # Sort products by battery life (descending) and material quality (descending)
    sorted_products = sorted(
        products, 
        key=lambda p: (p.battery_life, p.material_quality), 
        reverse=True
    )
    
    return sorted_products[0]  # Return the best product

# Main function to demonstrate product comparison
def main():
    # Sample product data
    product_data = """
    [
        {"name": "CHIKARA Cooling Shirt", "battery_life": 8, "material_quality": 9},
        {"name": "CoolWear Breeze Shirt", "battery_life": 6, "material_quality": 8},
        {"name": "ArcticPro Cooling Tee", "battery_life": 8, "material_quality": 7},
        {"name": "FrostFlow Active Shirt", "battery_life": 5, "material_quality": 10}
    ]
    """

    try:
        # Load product data from JSON
        products_json = json.loads(product_data)
        
        # Convert JSON data into Product objects
        products = [
            Product(p['name'], p['battery_life'], p['material_quality']) 
            for p in products_json
        ]
        
        # Compare products and find the best one
        best_product = compare_products(products)
        
        print("Best Product:")
        print(best_product)

    except json.JSONDecodeError as e:
        print(f"Error loading product data: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
