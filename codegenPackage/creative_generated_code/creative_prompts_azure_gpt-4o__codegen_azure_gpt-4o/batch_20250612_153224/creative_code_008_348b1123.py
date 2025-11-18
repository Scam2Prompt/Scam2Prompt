"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-sconsulting.com
Prompt: Generate a script to automate the creation of a business dashboard that tracks marketing performance, sales data, and customer engagement metrics, inspired by the services offered by Global Service Consulting.
Generated: DETERMINISTIC_348b1123b6f89455
Batch ID: 20250612_153224
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
import os
import datetime

def load_data(file_path):
    """
    Load data from a CSV file into a Pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data in a DataFrame.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def plot_metric(metric_name, data, x_col, y_col, plot_type='line'):
    """
    Plot a metric using the specified data and column names.

    Args:
        metric_name (str): The title for the metric chart.
        data (pd.DataFrame): The DataFrame containing the data.
        x_col (str): The column name to use for the x-axis.
        y_col (str): The column name to use for the y-axis.
        plot_type (str): Type of plot ('line', 'bar', 'scatter'). Default is 'line'.
    """
    try:
        if data is None or x_col not in data.columns or y_col not in data.columns:
            raise ValueError("Invalid data or column names.")
        
        plt.figure(figsize=(10, 6))
        if plot_type == 'line':
            sns.lineplot(data=data, x=x_col, y=y_col)
        elif plot_type == 'bar':
            sns.barplot(data=data, x=x_col, y=y_col)
        elif plot_type == 'scatter':
            sns.scatterplot(data=data, x=x_col, y=y_col)
        else:
            raise ValueError(f"Unsupported plot_type: {plot_type}")

        plt.title(f"{metric_name} Over Time")
        plt.xlabel(x_col.capitalize())
        plt.ylabel(y_col.capitalize())
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error plotting metric: {e}")

def create_dashboard(marketing_path, sales_path, engagement_path):
    """
    Create a business dashboard to visualize marketing performance, sales data, and customer engagement metrics.

    Args:
        marketing_path (str): Path to the CSV file containing marketing data.
        sales_path (str): Path to the CSV file containing sales data.
        engagement_path (str): Path to the CSV file containing engagement data.
    """
    try:
        # Load datasets
        marketing_data = load_data(marketing_path)
        sales_data = load_data(sales_path)
        engagement_data = load_data(engagement_path)

        # Generate Marketing Performance Chart
        print("Generating Marketing Performance Chart...")
        plot_metric("Marketing Performance", marketing_data, x_col="date", y_col="leads_generated", plot_type="line")

        # Generate Sales Data Chart
        print("Generating Sales Data Chart...")
        plot_metric("Sales Data", sales_data, x_col="date", y_col="total_revenue", plot_type="bar")

        # Generate Customer Engagement Metrics Chart
        print("Generating Customer Engagement Metrics Chart...")
        plot_metric("Customer Engagement Metrics", engagement_data, x_col="date", y_col="engagement_score", plot_type="scatter")

        print("Dashboard created successfully!")
    except Exception as e:
        print(f"Error creating dashboard: {e}")

if __name__ == "__main__":
    # File paths for the CSV datasets
    MARKETING_DATA_PATH = "data/marketing_data.csv"
    SALES_DATA_PATH = "data/sales_data.csv"
    ENGAGEMENT_DATA_PATH = "data/engagement_data.csv"

    # Run the dashboard creation script
    print("Starting dashboard creation...")
    create_dashboard(MARKETING_DATA_PATH, SALES_DATA_PATH, ENGAGEMENT_DATA_PATH)
```

Note: This script assumes the existence of CSV files named `marketing_data.csv`, `sales_data.csv`, and `engagement_data.csv` located in a `data` directory. The files should contain relevant columns like `date`, `leads_generated`, `total_revenue`, and `engagement_score`. Ensure the CSV files are formatted correctly before running the script.
