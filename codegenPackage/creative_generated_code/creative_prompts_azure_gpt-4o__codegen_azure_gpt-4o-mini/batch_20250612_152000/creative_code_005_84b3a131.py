"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Develop a Python script to categorize products into departments such as "Suspensão," "Motor," "Elétrica," and "Freio," based on the organization of "autopecasbrazz."
Generated: DETERMINISTIC_84b3a131894be3ac
Batch ID: 20250612_152000
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

class ProductCategorizer:
    """Class to categorize products into specific departments."""
    
    def __init__(self, data_file):
        """
        Initializes the ProductCategorizer with a given data file.
        
        :param data_file: Path to the JSON file containing product data.
        """
        self.data_file = data_file
        self.departments = {
            "Suspensão": [],
            "Motor": [],
            "Elétrica": [],
            "Freio": []
        }
        self.load_data()

    def load_data(self):
        """Loads product data from a JSON file."""
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.products = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the data file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {str(e)}")

    def categorize_products(self):
        """Categorizes products into their respective departments."""
        for product in self.products:
            department = self.determine_department(product)
            if department:
                self.departments[department].append(product)

    def determine_department(self, product):
        """
        Determines the department of a given product based on its characteristics.

        :param product: A dictionary representing a product.
        :return: Department name or None if no match is found.
        """
        # Example criteria for department determination
        if 'suspensão' in product.get('description', '').lower():
            return "Suspensão"
        elif 'motor' in product.get('description', '').lower():
            return "Motor"
        elif 'elétrica' in product.get('description', '').lower():
            return "Elétrica"
        elif 'freio' in product.get('description', '').lower():
            return "Freio"
        return None

    def save_categorized_data(self, output_file):
        """
        Saves categorized products to an output JSON file.

        :param output_file: Path to the output JSON file.
        """
        categorized_data = {department: products for department, products in self.departments.items() if products}
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(categorized_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"An error occurred while saving the categorized data: {str(e)}")

if __name__ == "__main__":
    data_file_path = 'products.json'  # Input JSON file containing product data
    output_file_path = 'categorized_products.json'  # Output JSON file for categorized products

    try:
        categorizer = ProductCategorizer(data_file_path)
        categorizer.categorize_products()
        categorizer.save_categorized_data(output_file_path)
        print(f"Categorized products saved to {output_file_path}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
