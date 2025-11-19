"""
Generated Code Metadata:
========================
Original URL: https://shopeewise.com
Prompt: Generate Python code to analyze sales data for products like "Intense Coffee Blend" and generate a report on the most popular items in the "Coffee" category.
Generated: DETERMINISTIC_f4501cbc38bd3475
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd

class SalesDataAnalyzer:
    """
    A class used to analyze sales data and generate reports.

    Attributes:
    ----------
    sales_data : pandas.DataFrame
        A DataFrame containing sales data.

    Methods:
    -------
    load_sales_data(file_path)
        Loads sales data from a CSV file.
    get_top_products(category, num_products)
        Returns the top-selling products in a given category.
    generate_report(category, num_products)
        Generates a report on the top-selling products in a given category.
    """

    def __init__(self, sales_data):
        """
        Initializes the SalesDataAnalyzer with sales data.

        Parameters:
        ----------
        sales_data : pandas.DataFrame
            A DataFrame containing sales data.
        """
        self.sales_data = sales_data

    @staticmethod
    def load_sales_data(file_path):
        """
        Loads sales data from a CSV file.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing sales data.

        Raises:
        ------
        FileNotFoundError
            If the file does not exist.
        pd.errors.EmptyDataError
            If the file is empty.
        pd.errors.ParserError
            If an error occurs while parsing the file.
        """
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except pd.errors.EmptyDataError:
            print(f"File is empty: {file_path}")
            return None
        except pd.errors.ParserError as e:
            print(f"Error parsing file: {file_path} - {e}")
            return None

    def get_top_products(self, category, num_products):
        """
        Returns the top-selling products in a given category.

        Parameters:
        ----------
        category : str
            The product category.
        num_products : int
            The number of top products to return.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the top-selling products.

        Raises:
        ------
        ValueError
            If the category is not found or num_products is not a positive integer.
        """
        if not isinstance(num_products, int) or num_products <= 0:
            raise ValueError("num_products must be a positive integer")

        # Filter data by category
        category_data = self.sales_data[self.sales_data['category'] == category]

        if category_data.empty:
            raise ValueError(f"Category not found: {category}")

        # Group by product and calculate total sales
        product_sales = category_data.groupby('product')['sales'].sum().reset_index()

        # Get top-selling products
        top_products = product_sales.nlargest(num_products, 'sales')

        return top_products

    def generate_report(self, category, num_products):
        """
        Generates a report on the top-selling products in a given category.

        Parameters:
        ----------
        category : str
            The product category.
        num_products : int
            The number of top products to include in the report.

        Returns:
        -------
        pandas.DataFrame
            A DataFrame containing the report data.

        Raises:
        ------
        ValueError
            If the category is not found or num_products is not a positive integer.
        """
        try:
            top_products = self.get_top_products(category, num_products)
            return top_products
        except ValueError as e:
            print(f"Error generating report: {e}")
            return None


def main():
    # Load sales data
    sales_data = SalesDataAnalyzer.load_sales_data('sales_data.csv')

    if sales_data is not None:
        # Create a SalesDataAnalyzer instance
        analyzer = SalesDataAnalyzer(sales_data)

        # Generate report for top-selling Coffee products
        report = analyzer.generate_report('Coffee', 10)

        if report is not None:
            print(report)


if __name__ == "__main__":
    main()
```
