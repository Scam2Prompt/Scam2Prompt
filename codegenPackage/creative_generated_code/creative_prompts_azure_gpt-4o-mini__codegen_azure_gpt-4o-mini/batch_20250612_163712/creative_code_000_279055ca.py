"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Generate a Python script to create a catalog of Samba Plastic's furniture products, including categories like Rattan Chairs and Tables.
Generated: DETERMINISTIC_279055ca2758d78a
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class Furniture:
    """Class representing a furniture product."""
    
    def __init__(self, name, category, price, stock):
        """
        Initializes a new furniture product.
        
        Args:
            name (str): The name of the furniture item.
            category (str): The category of the furniture item (e.g., Rattan Chairs).
            price (float): The price of the furniture item.
            stock (int): The available stock of the furniture item.
        """
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self):
        """Converts the furniture object to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'stock': self.stock
        }

class Catalog:
    """Class representing a catalog of furniture products."""
    
    def __init__(self):
        """Initializes an empty furniture catalog."""
        self.products = []
    
    def add_product(self, product):
        """
        Adds a furniture product to the catalog.
        
        Args:
            product (Furniture): The furniture product to add.
        """
        self.products.append(product)

    def save_to_file(self, filename):
        """
        Saves the catalog to a JSON file.
        
        Args:
            filename (str): The name of the file to save the catalog.
        """
        try:
            with open(filename, 'w') as file:
                json_data = [product.to_dict() for product in self.products]
                json.dump(json_data, file, indent=4)
            print(f"Catalog successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving catalog to file: {e}")

def main():
    """Main function to create and save a furniture catalog."""
    catalog = Catalog()

    # Sample furniture products
    catalog.add_product(Furniture("Rattan Chair 1", "Rattan Chairs", 89.99, 20))
    catalog.add_product(Furniture("Rattan Chair 2", "Rattan Chairs", 79.99, 15))
    catalog.add_product(Furniture("Rattan Table", "Tables", 199.99, 10))

    # Specify the filename to save the catalog
    filename = "samba_plastic_catalog.json"

    # Save the catalog to a JSON file
    catalog.save_to_file(filename)

if __name__ == "__main__":
    main()
```
