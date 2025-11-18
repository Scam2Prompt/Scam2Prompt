"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Develop a function to parse and display product details (e.g., "shampooing solide bio au rhassoul et cerise") from CMQLF's product catalog in a user-friendly format.
Generated: DETERMINISTIC_54d3f12b5fa0df46
Batch ID: 20250612_151918
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
    """
    A class to represent a product with its details.
    """

    def __init__(self, name, description, price, category):
        """
        Initializes a new product.
        
        :param name: The name of the product.
        :param description: A brief description of the product.
        :param price: The price of the product.
        :param category: The category under which the product falls.
        """
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def display(self):
        """
        Displays the product details in a user-friendly format.
        """
        try:
            print(f"Product Name: {self.name}")
            print(f"Description: {self.description}")
            print(f"Price: {self.price} EUR")
            print(f"Category: {self.category}\n")
        except Exception as e:
            print(f"Error displaying product details: {e}")

def parse_product_details(product_data):
    """
    Parses product data and creates a Product object.
    
    :param product_data: A dictionary containing the product's data.
    :return: A Product object if parsing is successful, None otherwise.
    """
    try:
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=float(product_data["price"]),
            category=product_data["category"]
        )
        return product
    except (KeyError, ValueError) as e:
        print(f"Error parsing product data: {e}")
        return None

def main():
    """
    Main function to run the product parsing and displaying.
    """
    # Sample JSON string representing a product from CMQLF's catalog
    json_product = '''
    {
        "name": "shampooing solide bio au rhassoul et cerise",
        "description": "Un shampooing solide bio qui nourrit et adoucit les cheveux.",
        "price": "15.99",
        "category": "Cosmetics"
    }
    '''
    
    try:
        # Parse the JSON product data
        product_data = json.loads(json_product)
        
        # Parse product details into a Product object
        product = parse_product_details(product_data)
        
        if product:
            # Display the product details
            product.display()
        else:
            print("Failed to create Product object.")
    
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    main()
```
