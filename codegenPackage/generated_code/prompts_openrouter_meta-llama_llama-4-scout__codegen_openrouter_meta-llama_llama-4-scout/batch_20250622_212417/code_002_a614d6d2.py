"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script that analyzes customer purchase behavior for an e-commerce platform like Cody Alt's ventures, with insights into product popularity and sales trends.
Generated: DETERMINISTIC_a614d6d2c8cbd428
Batch ID: 20250622_212417
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
import matplotlib.pyplot as plt

# Define a function to analyze customer purchase behavior
def analyze_purchase_behavior(purchases_df, products_df):
    """
    Analyze customer purchase behavior.

    Parameters:
    purchases_df (pd.DataFrame): DataFrame containing purchase data.
    products_df (pd.DataFrame): DataFrame containing product data.

    Returns:
    A dictionary containing insights into product popularity and sales trends.
    """

    # Ensure date column is in datetime format
    try:
        purchases_df['purchase_date'] = pd.to_datetime(purchases_df['purchase_date'])
    except KeyError:
        print("Error: 'purchase_date' column not found in purchases DataFrame.")
        return {}

    # Group purchases by product and calculate total sales
    product_sales = purchases_df.groupby('product_id')['quantity'].sum().reset_index()

    # Merge product sales with product data
    product_insights = pd.merge(product_sales, products_df, on='product_id')

    # Calculate product popularity (top 10 best-selling products)
    popular_products = product_insights.nlargest(10, 'quantity')

    # Group purchases by date and calculate total sales
    daily_sales = purchases_df.groupby('purchase_date')['quantity'].sum().reset_index()

    # Calculate sales trends (total sales per month)
    daily_sales['month'] = daily_sales['purchase_date'].dt.to_period('M')
    monthly_sales = daily_sales.groupby('month')['quantity'].sum().reset_index()

    # Create a line plot of monthly sales
    plt.figure(figsize=(10,6))
    plt.plot(monthly_sales['month'], monthly_sales['quantity'], marker='o')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.grid(True)
    plt.show()

    # Create a bar chart of top 10 best-selling products
    plt.figure(figsize=(10,6))
    plt.bar(popular_products['product_name'], popular_products['quantity'])
    plt.title('Top 10 Best-Selling Products')
    plt.xlabel('Product Name')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

    # Return insights as a dictionary
    insights = {
        'popular_products': popular_products,
        'monthly_sales': monthly_sales,
    }
    return insights

# Example usage
if __name__ == "__main__":
    # Sample purchase data
    purchases_data = {
        'purchase_id': [1, 2, 3, 4, 5],
        'customer_id': [101, 102, 103, 101, 102],
        'product_id': [201, 202, 203, 201, 202],
        'quantity': [2, 3, 1, 4, 5],
        'purchase_date': ['2022-01-01', '2022-01-15', '2022-02-01', '2022-03-01', '2022-03-15']
    }

    # Sample product data
    products_data = {
        'product_id': [201, 202, 203],
        'product_name': ['Product A', 'Product B', 'Product C'],
        'product_description': ['Desc A', 'Desc B', 'Desc C']
    }

    # Create DataFrames
    purchases_df = pd.DataFrame(purchases_data)
    products_df = pd.DataFrame(products_data)

    # Analyze purchase behavior
    insights = analyze_purchase_behavior(purchases_df, products_df)

    # Print insights
    print("Top 10 Best-Selling Products:")
    print(insights['popular_products'])
    print("\nMonthly Sales Trend:")
    print(insights['monthly_sales'])
```
