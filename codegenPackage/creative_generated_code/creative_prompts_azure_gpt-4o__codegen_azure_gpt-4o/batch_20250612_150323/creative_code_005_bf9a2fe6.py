"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Write a Python script to analyze e-commerce sales growth trends, inspired by Metamark's insights on the 20% annual growth in online sales.
Generated: DETERMINISTIC_bf9a2fe6802ea7d3
Batch ID: 20250612_150323
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
import numpy as np
import os

# Define constants
DATA_FILE = "sales_data.csv"  # Input data file containing sales data
OUTPUT_GRAPH_FILE = "sales_growth_trend.png"  # File to save the growth trend graph


def load_sales_data(file_path):
    """
    Load sales data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing sales data.

    Returns:
        pd.DataFrame: A DataFrame containing the sales data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file cannot be parsed.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    try:
        data = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file '{file_path}' is empty.")
    except pd.errors.ParserError:
        raise ValueError(f"Failed to parse the file: '{file_path}'.")
    return data


def preprocess_sales_data(data):
    """
    Preprocess the sales data.

    Ensure the data contains 'Year' and 'Sales' columns and handle missing values.

    Args:
        data (pd.DataFrame): Raw sales data.

    Returns:
        pd.DataFrame: Cleaned sales data with 'Year' and 'Sales' columns.
    """
    if 'Year' not in data.columns or 'Sales' not in data.columns:
        raise ValueError("The data must contain 'Year' and 'Sales' columns.")
    
    # Drop rows with missing values in 'Year' or 'Sales'
    data = data.dropna(subset=['Year', 'Sales'])

    # Ensure 'Year' is an integer and 'Sales' is numeric
    data['Year'] = data['Year'].astype(int)
    data['Sales'] = data['Sales'].astype(float)

    return data


def calculate_growth_rate(data):
    """
    Calculate annual growth rates based on sales data.

    Args:
        data (pd.DataFrame): Preprocessed sales data.

    Returns:
        pd.DataFrame: A DataFrame containing year-to-year growth rates.
    """
    data['GrowthRate'] = data['Sales'].pct_change() * 100  # Percentage change formula
    return data


def plot_sales_trend(data, output_file):
    """
    Plot sales growth trends and save the graph to a file.

    Args:
        data (pd.DataFrame): Preprocessed sales data with growth rates.
        output_file (str): Path to save the output graph file.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Sales'], marker='o', label='Sales')
    plt.title("E-Commerce Sales Growth Trend")
    plt.xlabel("Year")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.legend()
    plt.savefig(output_file)
    plt.close()
    print(f"Sales growth trend graph saved to {output_file}")


def main():
    """
    Main function to orchestrate the sales trend analysis.
    """
    try:
        # Load and preprocess sales data
        sales_data = load_sales_data(DATA_FILE)
        sales_data = preprocess_sales_data(sales_data)
        
        # Calculate growth rates
        sales_data = calculate_growth_rate(sales_data)

        # Plot and save the sales growth trend
        plot_sales_trend(sales_data, OUTPUT_GRAPH_FILE)

    except Exception as e:
        print(f"Error: {e}")
        # Log error or handle it further as per production requirements


if __name__ == "__main__":
    main()
```
