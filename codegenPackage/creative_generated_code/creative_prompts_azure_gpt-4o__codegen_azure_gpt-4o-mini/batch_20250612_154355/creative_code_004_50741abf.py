"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Develop a Python script to filter and display industrial products suitable for marine and offshore engineering, based on the industries served by Roshako.
Generated: DETERMINISTIC_50741abf09c42f77
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ProductFilter:
    """
    A class to filter and display industrial products suitable for marine and offshore engineering.
    """

    def __init__(self, data_file):
        """
        Initializes the ProductFilter with a dataset.

        Args:
            data_file (str): The path to the CSV file containing product data.
        """
        self.data_file = data_file
        self.products = self.load_data()

    def load_data(self):
        """
        Loads the product data from a CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the product data.
        """
        try:
            data = pd.read_csv(self.data_file)
            if data.empty:
                raise ValueError("The loaded data is empty.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.ParserError:
            raise ValueError(f"The file {self.data_file} could not be parsed as CSV.")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def filter_products(self):
        """
        Filters the products to only include those suitable for marine and offshore engineering.

        Returns:
            pd.DataFrame: A DataFrame containing the filtered products.
        """
        try:
            # Define the criteria for marine and offshore engineering
            criteria = ['Marine', 'Offshore']

            # Filter the products based on industries served
            filtered_products = self.products[self.products['Industries Served'].str.contains('|'.join(criteria), na=False)]
            return filtered_products.reset_index(drop=True)
        except Exception as e:
            raise Exception(f"Error during filtering products: {e}")

    def display_products(self, filtered_products):
        """
        Displays the filtered products in a user-friendly format.

        Args:
            filtered_products (pd.DataFrame): The DataFrame containing filtered products.
        """
        try:
            if filtered_products.empty:
                print("No products found for the specified criteria.")
            else:
                print("Filtered Products Suitable for Marine and Offshore Engineering:")
                print(filtered_products)
        except Exception as e:
            raise Exception(f"Error during displaying products: {e}")

def main():
    """
    The main function to execute the product filtering and display process.
    """
    data_file = 'products.csv'  # Path to the CSV file containing product data
    product_filter = ProductFilter(data_file)

    # Filter the products
    filtered_products = product_filter.filter_products()

    # Display the filtered products
    product_filter.display_products(filtered_products)

if __name__ == "__main__":
    main()
```
