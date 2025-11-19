"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a Python script to categorize products into departments such as "Suspensão," "Motor," "Elétrica," and "Freio," based on the organization of "autopecasbrazz."
Generated: DETERMINISTIC_84b3a131894be3ac
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class ProductCategorizer:
    """A class to categorize products into specific departments."""

    DEPARTMENTS = {
        "Suspensão": ["suspensão", "amortecedor", "mola"],
        "Motor": ["motor", "cylinder", "piston"],
        "Elétrica": ["elétrica", "bateria", "alternador"],
        "Freio": ["freio", "pastilha", "disco"]
    }

    def __init__(self, products):
        """
        Initializes the ProductCategorizer with a list of products.

        Args:
            products (list): A list of product names to categorize.
        """
        self.products = products
        self.categorized_products = {dept: [] for dept in self.DEPARTMENTS}

    def categorize_products(self):
        """Categorizes products into their respective departments."""
        for product in self.products:
            categorized = False
            for department, keywords in self.DEPARTMENTS.items():
                if any(keyword in product.lower() for keyword in keywords):
                    self.categorized_products[department].append(product)
                    categorized = True
                    break
            if not categorized:
                self.categorized_products.setdefault("Uncategorized", []).append(product)

    def save_to_json(self, file_path):
        """
        Saves the categorized products to a JSON file.

        Args:
            file_path (str): The path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.categorized_products, json_file, indent=4)
            print(f"Categorized products saved to {file_path}")
        except IOError as e:
            print(f"Error saving to file: {e}")

def load_products_from_file(file_path):
    """
    Loads products from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing product data.

    Returns:
        list: A list of products.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def main():
    """Main function to execute the product categorization."""
    input_file = 'products.json'  # Input file containing product data
    output_file = 'categorized_products.json'  # Output file for categorized data

    try:
        products = load_products_from_file(input_file)
        categorizer = ProductCategorizer(products)
        categorizer.categorize_products()
        categorizer.save_to_json(output_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading products: {e}")

if __name__ == "__main__":
    main()
```
