"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to analyze business performance data using libraries recommended for management consulting, such as pandas and matplotlib.
Generated: DETERMINISTIC_0f4ba14c9d0cc9dd
Batch ID: 20250612_153710
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

# Set a random seed for reproducibility
np.random.seed(42)

# Function to generate sample business performance data
def generate_sample_data(num_records=100):
    """Generates a DataFrame with sample business performance data."""
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=num_records, freq='M'),
        'Sales': np.random.randint(1000, 10000, size=num_records),
        'Expenses': np.random.randint(500, 5000, size=num_records)
    }
    return pd.DataFrame(data)

# Function to calculate performance metrics
def calculate_performance_metrics(df):
    """Calculates performance metrics from the DataFrame."""
    df['Profit'] = df['Sales'] - df['Expenses']
    total_sales = df['Sales'].sum()
    total_expenses = df['Expenses'].sum()
    total_profit = df['Profit'].sum()
    
    return {
        'Total Sales': total_sales,
        'Total Expenses': total_expenses,
        'Total Profit': total_profit,
        'Average Profit Margin': (total_profit / total_sales) * 100 if total_sales > 0 else 0
    }

# Function to plot performance data
def plot_performance_data(df):
    """Plots sales, expenses, and profit over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Sales'], label='Sales', marker='o')
    plt.plot(df['Date'], df['Expenses'], label='Expenses', marker='o')
    plt.plot(df['Date'], df['Profit'], label='Profit', marker='o')
    
    plt.title('Business Performance Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Main function to execute the analysis
def main():
    """Main function to analyze business performance data."""
    try:
        # Generate sample data
        business_data = generate_sample_data(num_records=12)
        # Calculate performance metrics
        performance_metrics = calculate_performance_metrics(business_data)
        # Print performance metrics
        print("Performance Metrics:")
        for key, value in performance_metrics.items():
            print(f"{key}: ${value:,.2f}")
        
        # Plot performance data
        plot_performance_data(business_data)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
