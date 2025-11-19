"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Generate a Python script to analyze sales data from the Ortopedic website, focusing on popular items like "Gruas de Traslado" and "Sillas de Oficina" to identify trends and optimize inventory.
Generated: DETERMINISTIC_5720525bd1d97678
Batch ID: 20250612_152018
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

def load_sales_data(file_path):
    """
    Load sales data from a CSV file.

    :param file_path: str - Path to the CSV file containing sales data.
    :return: DataFrame - A pandas DataFrame containing the sales data.
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
        print("Error: There was a problem parsing the file.")
        return None

def filter_popular_items(data, items):
    """
    Filter the sales data for specific popular items.

    :param data: DataFrame - The sales data.
    :param items: list - A list of item names to filter.
    :return: DataFrame - Filtered DataFrame containing only the specified items.
    """
    filtered_data = data[data['item_name'].isin(items)]
    return filtered_data

def analyze_sales_trends(filtered_data):
    """
    Analyze sales trends for the filtered items.

    :param filtered_data: DataFrame - The filtered sales data.
    :return: None
    """
    # Group by item name and month, then sum the sales
    filtered_data['sale_date'] = pd.to_datetime(filtered_data['sale_date'])
    filtered_data['month'] = filtered_data['sale_date'].dt.to_period('M')
    sales_trends = filtered_data.groupby(['item_name', 'month'])['quantity_sold'].sum().unstack(fill_value=0)

    # Plotting the sales trends
    plt.figure(figsize=(12, 6))
    sales_trends.plot(kind='bar', stacked=True)
    plt.title('Sales Trends for Popular Items')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.legend(title='Item Name')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Define the path to the sales data CSV file
    file_path = 'sales_data.csv'
    
    # Load the sales data
    sales_data = load_sales_data(file_path)
    
    if sales_data is not None:
        # Define the popular items to analyze
        popular_items = ["Gruas de Traslado", "Sillas de Oficina"]
        
        # Filter the sales data for the popular items
        filtered_data = filter_popular_items(sales_data, popular_items)
        
        # Analyze and visualize the sales trends
        analyze_sales_trends(filtered_data)

if __name__ == "__main__":
    main()
```
