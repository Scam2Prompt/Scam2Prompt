"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shopeewise.com
Prompt: Generate Python code to analyze sales data for products like "Intense Coffee Blend" and generate a report on the most popular items in the "Coffee" category.
Generated: DETERMINISTIC_f4501cbc38bd3475
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SalesDataAnalyzer:
    """
    A class to analyze sales data for products in the Coffee category.
    """

    def __init__(self, sales_data_path):
        """
        Initializes the SalesDataAnalyzer with the path to the sales data CSV file.

        Parameters:
        sales_data_path (str): The file path to the sales data CSV.
        """
        self.sales_data_path = sales_data_path
        self.sales_data = self.load_data()

    def load_data(self):
        """
        Loads the sales data CSV file into a pandas DataFrame.

        Returns:
        pd.DataFrame: The sales data DataFrame.
        """
        try:
            data = pd.read_csv(self.sales_data_path)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"Sales data file not found at: {self.sales_data_path}")
        except pd.errors.EmptyDataError:
            raise ValueError("Sales data file is empty.")
        except pd.errors.ParserError:
            raise ValueError("Error parsing the sales data file.")

    def analyze_sales(self, product_name):
        """
        Analyzes sales data for a specific product and generates a report on
        the most popular items in the Coffee category.

        Parameters:
        product_name (str): The name of the product to analyze.

        Returns:
        pd.DataFrame: A DataFrame containing the report of popular items in Coffee category.
        """
        # Filter for products in the "Coffee" category
        coffee_data = self.sales_data[self.sales_data['Category'] == 'Coffee']

        # Check if the specified product exists in the data
        if coffee_data[coffee_data['Product'] == product_name].empty:
            raise ValueError(f"No sales data found for product: {product_name}")

        # Group by product and sum the sales
        report = (coffee_data.groupby('Product')['Quantity Sold']
                  .sum()
                  .reset_index()
                  .sort_values(by='Quantity Sold', ascending=False)
                  .reset_index(drop=True)

        return report

    def generate_report(self, product_name):
        """
        Generates a sales report for the specified product.

        Parameters:
        product_name (str): The name of the product to generate the report for.

        Returns:
        None: Outputs the report to the console.
        """
        try:
            report = self.analyze_sales(product_name)
            print(f"Sales report for '{product_name}':")
            print(report)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the sales data CSV file
    sales_data_path = 'sales_data.csv'  # Update this path accordingly

    # Create an instance of SalesDataAnalyzer
    analyzer = SalesDataAnalyzer(sales_data_path)

    # Generate report for the specified product
    product_to_analyze = "Intense Coffee Blend"
    analyzer.generate_report(product_to_analyze)
```
