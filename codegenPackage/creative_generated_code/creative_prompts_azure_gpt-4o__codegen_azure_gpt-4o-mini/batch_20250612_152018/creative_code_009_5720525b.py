"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ortopedic.cl
Prompt: Generate a Python script to analyze sales data from the Ortopedic website, focusing on popular items like "Gruas de Traslado" and "Sillas de Oficina" to identify trends and optimize inventory.
Generated: DETERMINISTIC_5720525bd1d97678
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def load_sales_data(file_path):
    """
    Load sales data from a CSV file.

    :param file_path: str - Path to the CSV file containing sales data.
    :return: DataFrame - A pandas DataFrame containing the sales data.
    """
    try:
        sales_data = pd.read_csv(file_path)
        return sales_data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found.")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise e

def filter_popular_items(sales_data, items):
    """
    Filter sales data for specific popular items.

    :param sales_data: DataFrame - The DataFrame containing sales data.
    :param items: list - List of items to filter.
    :return: DataFrame - A filtered DataFrame containing only the popular items.
    """
    filtered_data = sales_data[sales_data['Item'].isin(items)]
    return filtered_data

def analyze_trends(filtered_data):
    """
    Analyze sales trends for the filtered data.

    :param filtered_data: DataFrame - The filtered DataFrame containing popular items.
    :return: None
    """
    # Group by item and month to analyze sales trends
    filtered_data['Sale_Date'] = pd.to_datetime(filtered_data['Sale_Date'])
    monthly_sales = filtered_data.groupby(
        [filtered_data['Sale_Date'].dt.to_period('M'), 'Item']
    ).sum().reset_index()

    # Plotting the sales trends
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x='Sale_Date', y='Quantity_Sold', hue='Item', marker='o')
    plt.title('Sales Trends of Popular Items')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=45)
    plt.legend(title='Items')
    plt.tight_layout()
    plt.show()

def optimize_inventory(filtered_data):
    """
    Suggest inventory optimizations based on sales data.

    :param filtered_data: DataFrame - The filtered DataFrame containing popular items.
    :return: None
    """
    # Calculate total sales for each item
    total_sales = filtered_data.groupby('Item')['Quantity_Sold'].sum().sort_values(ascending=False)
    print("Total sales for each popular item:")
    print(total_sales)

    # Provide basic inventory recommendations
    for item, sales in total_sales.items():
        recommended_stock = sales // 3  # Example logic for recommended stock
        print(f"Recommended inventory for {item}: {recommended_stock}")

def main():
    # Define the file path and popular items to analyze
    file_path = 'sales_data.csv'
    popular_items = ["Gruas de Traslado", "Sillas de Oficina"]

    # Load sales data
    sales_data = load_sales_data(file_path)

    # Filter for popular items
    filtered_data = filter_popular_items(sales_data, popular_items)

    # Analyze sales trends
    analyze_trends(filtered_data)

    # Optimize inventory based on sales data
    optimize_inventory(filtered_data)

if __name__ == "__main__":
    main()
```
