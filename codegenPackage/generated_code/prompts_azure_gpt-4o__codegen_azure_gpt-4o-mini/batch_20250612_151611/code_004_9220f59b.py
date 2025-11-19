"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Generate a Python script to categorize the products (e.g., Buttweld Pipe Fittings, Socket Weld Fittings, Perforated Sheets) from Dinkar Alloys based on their material type and application.
Generated: DETERMINISTIC_9220f59b7917e840
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ProductCategorizer:
    """
    A class to categorize products based on their material type and application.
    """

    def __init__(self, product_data):
        """
        Initializes the ProductCategorizer with product data.

        :param product_data: A DataFrame containing product information.
        """
        self.product_data = product_data

    def categorize_products(self):
        """
        Categorizes products into material types and applications.

        :return: A dictionary with material types as keys and lists of products as values.
        """
        categorized_products = {}

        for index, row in self.product_data.iterrows():
            material_type = row['Material Type']
            application = row['Application']
            product_name = row['Product Name']

            # Create a nested dictionary structure if it doesn't exist
            if material_type not in categorized_products:
                categorized_products[material_type] = {}

            if application not in categorized_products[material_type]:
                categorized_products[material_type][application] = []

            # Append the product name to the appropriate category
            categorized_products[material_type][application].append(product_name)

        return categorized_products

def load_product_data(file_path):
    """
    Loads product data from a CSV file.

    :param file_path: The path to the CSV file containing product data.
    :return: A DataFrame containing the product data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return pd.DataFrame()  # Return an empty DataFrame on error

def main():
    """
    Main function to execute the product categorization.
    """
    # Load product data from a CSV file
    file_path = 'products.csv'  # Update this path as necessary
    product_data = load_product_data(file_path)

    if not product_data.empty:
        # Create an instance of ProductCategorizer
        categorizer = ProductCategorizer(product_data)

        # Categorize the products
        categorized_products = categorizer.categorize_products()

        # Print the categorized products
        for material, applications in categorized_products.items():
            print(f"Material Type: {material}")
            for application, products in applications.items():
                print(f"  Application: {application}")
                print(f"    Products: {', '.join(products)}")

if __name__ == "__main__":
    main()
```
