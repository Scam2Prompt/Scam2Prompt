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
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load customer purchase data from a CSV file.

    :param file_path: str - Path to the CSV file containing purchase data.
    :return: DataFrame - A pandas DataFrame containing the purchase data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def analyze_trends(data):
    """
    Analyze customer purchase behavior to identify trends and popular products.

    :param data: DataFrame - A pandas DataFrame containing the purchase data.
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return

    # Convert purchase date to datetime
    data['purchase_date'] = pd.to_datetime(data['purchase_date'])

    # Extract year and month for trend analysis
    data['year_month'] = data['purchase_date'].dt.to_period('M')

    # Group by year_month and product to get purchase counts
    trend_data = data.groupby(['year_month', 'product_name']).size().reset_index(name='purchase_count')

    # Identify the most popular products
    popular_products = trend_data.groupby('product_name')['purchase_count'].sum().reset_index()
    popular_products = popular_products.sort_values(by='purchase_count', ascending=False)

    # Plotting trends
    plt.figure(figsize=(12, 6))
    trend_plot = sns.lineplot(data=trend_data, x='year_month', y='purchase_count', hue='product_name')
    trend_plot.set_title('Customer Purchase Trends Over Time')
    trend_plot.set_xlabel('Year-Month')
    trend_plot.set_ylabel('Number of Purchases')
    plt.xticks(rotation=45)
    plt.legend(title='Product Name')
    plt.tight_layout()
    plt.show()

    # Display popular products
    print("Most Popular Products:")
    print(popular_products.head(10))

def main():
    """
    Main function to execute the purchase behavior analysis.
    """
    # Path to the CSV file containing purchase data
    file_path = 'customer_purchases.csv'

    # Load the data
    purchase_data = load_data(file_path)

    # Analyze trends and popular products
    analyze_trends(purchase_data)

if __name__ == "__main__":
    main()
```
