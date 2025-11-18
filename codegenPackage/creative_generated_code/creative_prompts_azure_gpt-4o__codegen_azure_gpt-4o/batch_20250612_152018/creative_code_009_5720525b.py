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
import csv
from collections import Counter
from datetime import datetime

# Define constants for popular items
POPULAR_ITEMS = ["Gruas de Traslado", "Sillas de Oficina"]

# File path of the sales data CSV file
SALES_DATA_FILE = "sales_data.csv"

# Function to read sales data from a CSV file
def read_sales_data(file_path):
    """
    Reads sales data from a CSV file.
    
    Args:
        file_path (str): The path to the sales data file.
    
    Returns:
        list: A list of dictionaries containing sales records.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Function to filter sales data for popular items
def filter_popular_items(sales_data):
    """
    Filters sales data to include only popular items.
    
    Args:
        sales_data (list): The sales data records.
    
    Returns:
        list: A list of sales records containing only popular items.
    """
    return [item for item in sales_data if item['item_name'] in POPULAR_ITEMS]

# Function to analyze sales trends
def analyze_sales_trends(filtered_data):
    """
    Analyzes sales trends for popular items.
    
    Args:
        filtered_data (list): Sales records for popular items.
    
    Returns:
        dict: A dictionary containing item-level sales trends.
    """
    trends = {}
    counter = Counter([item['item_name'] for item in filtered_data])
    
    for item_name, count in counter.items():
        trends[item_name] = {
            'total_sales': count,
            'monthly_sales': {}
        }
    
    for record in filtered_data:
        item_name = record['item_name']
        sale_date = datetime.strptime(record['sale_date'], '%Y-%m-%d')
        month = sale_date.strftime('%Y-%m')
        
        if month not in trends[item_name]['monthly_sales']:
            trends[item_name]['monthly_sales'][month] = 0
        trends[item_name]['monthly_sales'][month] += 1
    
    return trends

# Main function to execute the script
def main():
    """
    Main function to analyze sales data and print trends.
    """
    sales_data = read_sales_data(SALES_DATA_FILE)
    
    if not sales_data:
        print("No sales data available for analysis.")
        return
    
    # Filter data for popular items
    filtered_data = filter_popular_items(sales_data)
    if not filtered_data:
        print("No sales data found for popular items.")
        return
    
    # Analyze trends
    trends = analyze_sales_trends(filtered_data)
    
    # Print the analysis results
    print("Sales Trends for Popular Items:")
    for item_name, trend_data in trends.items():
        print(f"\nItem: {item_name}")
        print(f"  Total Sales: {trend_data['total_sales']}")
        print("  Monthly Sales:")
        for month, sales in trend_data['monthly_sales'].items():
            print(f"    {month}: {sales}")

# Run the script
if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `sales_data.csv` file exists in the same directory and includes appropriate columns such as `item_name` and `sale_date`.
