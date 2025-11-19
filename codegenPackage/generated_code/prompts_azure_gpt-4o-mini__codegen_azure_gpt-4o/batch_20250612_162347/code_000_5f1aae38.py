"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script to analyze sales data for a CBD product, inspired by Cody Alt's approach in the CBD industry.
Generated: DETERMINISTIC_5f1aae38f42b83fb
Batch ID: 20250612_162347
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
import os

def load_sales_data(file_path):
    """
    Load sales data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the sales data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file cannot be read as a CSV.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")
    
    return data

def clean_sales_data(data):
    """
    Clean the sales data by handling missing values and ensuring proper data types.

    Args:
        data (pd.DataFrame): Raw sales data.

    Returns:
        pd.DataFrame: Cleaned sales data.
    """
    # Drop rows with missing values
    data = data.dropna()

    # Ensure proper data types
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')

    # Drop rows with invalid data after type conversion
    data = data.dropna()

    return data

def analyze_sales_data(data):
    """
    Analyze sales data to calculate key metrics.

    Args:
        data (pd.DataFrame): Cleaned sales data.

    Returns:
        dict: Dictionary containing key metrics.
    """
    total_sales = data['Sales'].sum()
    average_sales = data['Sales'].mean()
    max_sales = data['Sales'].max()
    min_sales = data['Sales'].min()

    return {
        'Total Sales': total_sales,
        'Average Sales': average_sales,
        'Max Sales': max_sales,
        'Min Sales': min_sales
    }

def plot_sales_trend(data):
    """
    Plot the sales trend over time.

    Args:
        data (pd.DataFrame): Cleaned sales data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-', color='b')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the sales data analysis workflow.
    """
    # File path to the sales data CSV
    file_path = 'sales_data.csv'

    try:
        # Load the sales data
        sales_data = load_sales_data(file_path)

        # Clean the sales data
        cleaned_data = clean_sales_data(sales_data)

        # Analyze the sales data
        metrics = analyze_sales_data(cleaned_data)
        print("Sales Data Analysis:")
        for key, value in metrics.items():
            print(f"{key}: {value}")

        # Plot the sales trend
        plot_sales_trend(cleaned_data)

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
