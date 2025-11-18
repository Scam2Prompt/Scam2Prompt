"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Write code to create an interactive product catalog for custom souvenirs, integrating categories like "Travel Accessories" and "Paket Hampers," based on the Merchandiso website.
Generated: DETERMINISTIC_5992f5f066e017af
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Product Catalog Application
class ProductCatalog:
    def __init__(self):
        # Initialize the product catalog with predefined categories
        self.catalog = {
            "Travel Accessories": [],
            "Paket Hampers": []
        }

    def add_product(self, category, product_name, price, stock):
        """
        Add a new product to the specified category.
        :param category: Category name as string
        :param product_name: Product name as string
        :param price: Price of the product as float
        :param stock: Stock quantity as integer
        """
        if category not in self.catalog:
            print(f"Error: Category '{category}' does not exist.")
            return
        
        product = {
            "name": product_name,
            "price": price,
            "stock": stock
        }
        
        self.catalog[category].append(product)
        print(f"Product '{product_name}' added successfully to category '{category}'.")

    def display_catalog(self):
        """
        Display the entire product catalog in a readable format.
        """
        print("\nProduct Catalog:")
        for category, products in self.catalog.items():
            print(f"\nCategory: {category}")
            if not products:
                print("  No products available.")
            else:
                for i, product in enumerate(products, start=1):
                    print(f"  {i}. {product['name']} - ${product['price']} - Stock: {product['stock']}")

    def search_product(self, product_name):
        """
        Search for a product by name across all categories.
        :param product_name: Name of the product as string
        """
        print(f"\nSearching for '{product_name}'...")
        found = False
        for category, products in self.catalog.items():
            for product in products:
                if product["name"].lower() == product_name.lower():
                    print(f"Found in '{category}': {product}")
                    found = True
        
        if not found:
            print(f"Product '{product_name}' not found in the catalog.")

    def save_catalog(self, filename="catalog.json"):
        """
        Save the product catalog to a JSON file.
        :param filename: Name of the file as string
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.catalog, file, indent=4)
            print(f"Catalog successfully saved to '{filename}'.")
        except Exception as e:
            print(f"Error saving catalog: {e}")

    def load_catalog(self, filename="catalog.json"):
        """
        Load the product catalog from a JSON file.
        :param filename: Name of the file as string
        """
        try:
            with open(filename, "r") as file:
                self.catalog = json.load(file)
            print(f"Catalog successfully loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from '{filename}'.")
        except Exception as e:
            print(f"Error loading catalog: {e}")


# Interactive menu for the product catalog
def main():
    catalog = ProductCatalog()
    
    while True:
        print("\nProduct Catalog Menu")
        print("1. Add Product")
        print("2. Display Catalog")
        print("3. Search Product")
        print("4. Save Catalog")
        print("5. Load Catalog")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        
        if choice == 1:
            # Add Product
            category = input("Enter category (e.g., 'Travel Accessories', 'Paket Hampers'): ")
            product_name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock: "))
            except ValueError:
                print("Invalid input for price or stock. Please try again.")
                continue
            
            catalog.add_product(category, product_name, price, stock)
        
        elif choice == 2:
            # Display Catalog
            catalog.display_catalog()
        
        elif choice == 3:
            # Search Product
            product_name = input("Enter product name to search: ")
            catalog.search_product(product_name)
        
        elif choice == 4:
            # Save Catalog
            filename = input("Enter filename to save (default: 'catalog.json'): ") or "catalog.json"
            catalog.save_catalog(filename)
        
        elif choice == 5:
            # Load Catalog
            filename = input("Enter filename to load (default: 'catalog.json'): ") or "catalog.json"
            catalog.load_catalog(filename)
        
        elif choice == 6:
            # Exit the application
            print("Exiting Product Catalog. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Entry point of the application
if __name__ == "__main__":
    main()
```
