"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Create a Python script to analyze customer purchase behavior on a sewing machine website, identifying trends and popular products.
Generated: DETERMINISTIC_c1f0ab014a42aaa2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Function to load and validate data
def load_data(file_path):
    """
    Load customer purchase data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the purchase data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not in the expected format.
    """
    try:
        data = pd.read_csv(file_path)
        # Validate required columns
        required_columns = ['customer_id', 'product_id', 'purchase_date']
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"CSV file must contain the following columns: {required_columns}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except ValueError as ve:
        print(f"Error: {ve}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

# Function to analyze popular products
def analyze_popular_products(data):
    """
    Analyze the most popular products based on purchase frequency.

    Args:
        data (pd.DataFrame): DataFrame containing the purchase data.

    Returns:
        dict: Dictionary of product IDs and their purchase counts.
    """
    product_counts = Counter(data['product_id'])
    return dict(product_counts.most_common())

# Function to identify purchase trends
def analyze_purchase_trends(data):
    """
    Analyze purchase trends over time.

    Args:
        data (pd.DataFrame): DataFrame containing the purchase data.

    Returns:
        pd.Series: Series containing purchase counts by month.
    """
    # Convert purchase_date to datetime
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])
    # Group by month and count purchases
    monthly_trends = data.groupby(data['purchase_date'].dt.to_period('M')).size()
    return monthly_trends

# Function to visualize trends
def visualize_trends(trends):
    """
    Visualize purchase trends over time.

    Args:
        trends (pd.Series): Series containing purchase counts by month.
    """
    trends.index = trends.index.to_timestamp()  # Convert PeriodIndex to Timestamp
    plt.figure(figsize=(10, 6))
    plt.plot(trends.index, trends.values, marker='o', linestyle='-', color='b')
    plt.title('Purchase Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Purchases')
    plt.grid(True)
    plt.show()

# Main function
def main():
    """
    Main function to execute the analysis.
    """
    # File path to the customer purchase data
    file_path = 'customer_purchases.csv'

    try:
        # Load data
        data = load_data(file_path)

        # Analyze popular products
        popular_products = analyze_popular_products(data)
        print("Most Popular Products:")
        for product_id, count in popular_products.items():
            print(f"Product ID: {product_id}, Purchases: {count}")

        # Analyze purchase trends
        purchase_trends = analyze_purchase_trends(data)
        print("\nPurchase Trends Over Time:")
        print(purchase_trends)

        # Visualize trends
        visualize_trends(purchase_trends)

    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
