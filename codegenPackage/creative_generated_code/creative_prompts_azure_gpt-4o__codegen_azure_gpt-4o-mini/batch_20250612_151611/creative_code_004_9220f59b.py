"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Generate a Python script to categorize the products (e.g., Buttweld Pipe Fittings, Socket Weld Fittings, Perforated Sheets) from Dinkar Alloys based on their material type and application.
Generated: DETERMINISTIC_9220f59b7917e840
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import List, Dict

# Define a class to represent a product
class Product:
    def __init__(self, name: str, material: str, application: str):
        self.name = name
        self.material = material
        self.application = application

    def __repr__(self):
        return f"Product(name='{self.name}', material='{self.material}', application='{self.application}')"

# Function to categorize products based on their material type and application
def categorize_products(products: List[Product]) -> Dict[str, Dict[str, List[Product]]]:
    categorized = {}
    
    for product in products:
        # Categorize by material type
        if product.material not in categorized:
            categorized[product.material] = {}
        
        # Categorize by application
        if product.application not in categorized[product.material]:
            categorized[product.material][product.application] = []
        
        categorized[product.material][product.application].append(product)
    
    return categorized

# Function to read products from a CSV file
def read_products_from_csv(file_path: str) -> List[Product]:
    products = []
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create a Product instance for each row
                products.append(Product(row['name'], row['material'], row['application']))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except KeyError as e:
        print(f"Error: Missing expected column in CSV: {e}")
    except Exception as e:
        print(f"An error occurred while reading the CSV: {e}")
    
    return products

# Function to display categorized products
def display_categorized_products(categorized_products: Dict[str, Dict[str, List[Product]]]) -> None:
    for material, applications in categorized_products.items():
        print(f"Material: {material}")
        for application, items in applications.items():
            print(f"  Application: {application}")
            for item in items:
                print(f"    - {item.name}")

# Main function to execute the categorization
def main():
    # Specify the path to the CSV file
    file_path = 'products.csv'
    
    # Read products from the CSV file
    products = read_products_from_csv(file_path)
    
    # Categorize products
    categorized_products = categorize_products(products)
    
    # Display categorized products
    display_categorized_products(categorized_products)

if __name__ == '__main__':
    main()
```
