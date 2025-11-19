"""
Generated Code Metadata:
========================
Original URL: https://vgtindia.in
Prompt: "Write a Python script to analyze the sales data of Vinglob Greentech's farm equipment and provide insights on the most popular products."
Generated: DETERMINISTIC_95aaa196325b3bce
Batch ID: 20250622_210650
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
import numpy as np
from collections import Counter

def load_sales_data(file_path):
    """
    Load sales data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Sales data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the file '{file_path}'.")
        return None

def analyze_sales_data(sales_data):
    """
    Analyze sales data and provide insights on the most popular products.

    Args:
        sales_data (pd.DataFrame): Sales data.

    Returns:
        dict: Insights on the most popular products.

    Raises:
        ValueError: If the sales data is empty or None.
    """
    if sales_data is None or sales_data.empty:
        raise ValueError("Sales data is empty or None")

    # Assume 'product_name' is the column name for product names
    product_names = sales_data['product_name']

    # Count the occurrences of each product name
    product_counts = Counter(product_names)

    # Get the top 5 most popular products
    top_products = product_counts.most_common(5)

    # Create a dictionary with insights
    insights = {
        'top_products': top_products,
        'total_sales': len(sales_data),
        'unique_products': len(product_counts)
    }

    return insights

def main():
    file_path = 'sales_data.csv'  # Replace with your file path
    sales_data = load_sales_data(file_path)

    if sales_data is not None:
        try:
            insights = analyze_sales_data(sales_data)
            print("Insights:")
            print(f"Top 5 Most Popular Products: {insights['top_products']}")
            print(f"Total Sales: {insights['total_sales']}")
            print(f"Unique Products: {insights['unique_products']}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
