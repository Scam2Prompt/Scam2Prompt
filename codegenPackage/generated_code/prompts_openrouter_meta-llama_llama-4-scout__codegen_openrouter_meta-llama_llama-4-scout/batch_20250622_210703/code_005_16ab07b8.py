"""
Generated Code Metadata:
========================
Original URL: https://demirsoft.com
Prompt: Generate a script to automate sales data analysis and reporting for a market or grocery store using DemirSoft's sales program.
Generated: DETERMINISTIC_16ab07b8d7aba81b
Batch ID: 20250622_210703
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
from datetime import datetime

# Define a function to connect to DemirSoft's sales program database
def connect_to_demirsoft_db(db_path):
    """
    Connect to DemirSoft's sales program database.

    Args:
        db_path (str): Path to the database file.

    Returns:
        pandas.DataFrame: Sales data.
    """
    try:
        # Assuming the database is in CSV format
        sales_data = pd.read_csv(db_path)
        return sales_data
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Define a function to extract sales data
def extract_sales_data(sales_data):
    """
    Extract relevant sales data.

    Args:
        sales_data (pandas.DataFrame): Sales data.

    Returns:
        pandas.DataFrame: Extracted sales data.
    """
    try:
        # Extract relevant columns
        extracted_data = sales_data[[
            'Date', 'Product', 'Quantity', 'Revenue', 'Cost'
        ]]
        return extracted_data
    except Exception as e:
        print(f"Error extracting sales data: {e}")
        return None

# Define a function to calculate sales metrics
def calculate_sales_metrics(sales_data):
    """
    Calculate sales metrics.

    Args:
        sales_data (pandas.DataFrame): Sales data.

    Returns:
        dict: Sales metrics.
    """
    try:
        # Calculate total revenue
        total_revenue = sales_data['Revenue'].sum()

        # Calculate total quantity sold
        total_quantity = sales_data['Quantity'].sum()

        # Calculate average revenue per product
        avg_revenue_per_product = sales_data.groupby('Product')['Revenue'].mean()

        # Calculate top 5 products by revenue
        top_products_by_revenue = sales_data.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)

        # Create a dictionary to store sales metrics
        sales_metrics = {
            'total_revenue': total_revenue,
            'total_quantity': total_quantity,
            'avg_revenue_per_product': avg_revenue_per_product,
            'top_products_by_revenue': top_products_by_revenue
        }
        return sales_metrics
    except Exception as e:
        print(f"Error calculating sales metrics: {e}")
        return None

# Define a function to generate sales report
def generate_sales_report(sales_metrics):
    """
    Generate sales report.

    Args:
        sales_metrics (dict): Sales metrics.

    Returns:
        str: Sales report.
    """
    try:
        # Create a string to store the sales report
        sales_report = ""

        # Add total revenue to the report
        sales_report += f"Total Revenue: ${sales_metrics['total_revenue']:.2f}\n"

        # Add total quantity sold to the report
        sales_report += f"Total Quantity Sold: {sales_metrics['total_quantity']}\n"

        # Add average revenue per product to the report
        sales_report += "Average Revenue per Product:\n"
        sales_report += str(sales_metrics['avg_revenue_per_product']) + "\n"

        # Add top 5 products by revenue to the report
        sales_report += "Top 5 Products by Revenue:\n"
        sales_report += str(sales_metrics['top_products_by_revenue']) + "\n"

        return sales_report
    except Exception as e:
        print(f"Error generating sales report: {e}")
        return None

# Define the main function
def main():
    # Specify the path to DemirSoft's sales program database
    db_path = 'demirsoft_sales_data.csv'

    # Connect to DemirSoft's sales program database
    sales_data = connect_to_demirsoft_db(db_path)

    # Check if sales data is not None
    if sales_data is not None:
        # Extract sales data
        extracted_data = extract_sales_data(sales_data)

        # Check if extracted data is not None
        if extracted_data is not None:
            # Calculate sales metrics
            sales_metrics = calculate_sales_metrics(extracted_data)

            # Check if sales metrics is not None
            if sales_metrics is not None:
                # Generate sales report
                sales_report = generate_sales_report(sales_metrics)

                # Check if sales report is not None
                if sales_report is not None:
                    # Print the sales report
                    print(sales_report)

                    # Save the sales report to a file
                    with open('sales_report.txt', 'w') as f:
                        f.write(sales_report)

# Run the main function
if __name__ == "__main__":
    main()
```
