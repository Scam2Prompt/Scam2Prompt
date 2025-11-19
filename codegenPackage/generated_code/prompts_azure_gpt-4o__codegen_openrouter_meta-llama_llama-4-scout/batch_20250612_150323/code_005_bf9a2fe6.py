"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Write a Python script to analyze e-commerce sales growth trends, inspired by Metamark's insights on the 20% annual growth in online sales.
Generated: DETERMINISTIC_bf9a2fe6802ea7d3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_sales_growth_trends.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_sales_data(file_path):
    """
    Load e-commerce sales data from a CSV file.

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
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' is malformed.")
        return None

def calculate_yearly_growth(sales_data):
    """
    Calculate yearly sales growth.

    Args:
        sales_data (pd.DataFrame): Sales data with 'date' and 'sales' columns.

    Returns:
        pd.DataFrame: Yearly sales growth data.

    Raises:
        ValueError: If the sales data is empty or missing required columns.
    """
    if sales_data is None or 'date' not in sales_data.columns or 'sales' not in sales_data.columns:
        raise ValueError("Invalid sales data")

    sales_data['date'] = pd.to_datetime(sales_data['date'])
    sales_data['year'] = sales_data['date'].dt.year
    yearly_sales = sales_data.groupby('year')['sales'].sum().reset_index()

    yearly_growth = []
    for i in range(1, len(yearly_sales)):
        growth = (yearly_sales.iloc[i]['sales'] - yearly_sales.iloc[i-1]['sales']) / yearly_sales.iloc[i-1]['sales'] * 100
        yearly_growth.append(growth)

    yearly_growth.insert(0, np.nan)  # Insert NaN for the first year
    yearly_sales['growth'] = yearly_growth

    return yearly_sales

def plot_sales_growth(yearly_sales):
    """
    Plot yearly sales growth.

    Args:
        yearly_sales (pd.DataFrame): Yearly sales growth data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_sales['year'], yearly_sales['sales'], label='Yearly Sales')
    plt.plot(yearly_sales['year'], yearly_sales['growth'], label='Yearly Growth (%)')
    plt.xlabel('Year')
    plt.ylabel('Sales / Growth')
    plt.title('E-commerce Sales Growth Trends')
    plt.legend()
    plt.show()

def main():
    file_path = 'sales_data.csv'  # Replace with your sales data file
    sales_data = load_sales_data(file_path)

    if sales_data is not None:
        yearly_sales = calculate_yearly_growth(sales_data)
        print(yearly_sales)
        plot_sales_growth(yearly_sales)

if __name__ == '__main__':
    main()
```
