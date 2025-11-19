"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: "Generate a case study on how iTLS can be applied to optimize supply chain management and reduce inventory levels in a pharmaceutical laboratory setting."
Generated: DETERMINISTIC_3c77165f0cd7fd4b
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Case Study: Applying iTLS (Integrated Theory of Constraints, Lean, and Six Sigma) 
to Optimize Supply Chain Management and Reduce Inventory Levels in a Pharmaceutical Laboratory Setting.

This script simulates the application of iTLS principles to optimize supply chain management 
and reduce inventory levels in a pharmaceutical laboratory. It uses Python to model inventory 
tracking, demand forecasting, and process optimization.

Key Features:
1. Demand forecasting using historical data.
2. Inventory optimization based on forecasted demand.
3. Process bottleneck identification and resolution.
4. Lean principles to minimize waste.
5. Error handling for data inconsistencies.

Author: Expert Programmer
"""

import pandas as pd
import numpy as np
from scipy.stats import linregress

# Constants
SAFETY_STOCK_FACTOR = 1.2  # Safety stock multiplier
MAX_INVENTORY_CAPACITY = 1000  # Maximum inventory capacity
MIN_INVENTORY_THRESHOLD = 100  # Minimum inventory threshold

# Error handling for data loading
def load_data(file_path):
    """
    Load historical demand data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing historical demand data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains invalid data.
    """
    try:
        data = pd.read_csv(file_path)
        if 'Date' not in data.columns or 'Demand' not in data.columns:
            raise ValueError("CSV file must contain 'Date' and 'Demand' columns.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        raise
    except ValueError as ve:
        print(f"Error: {ve}")
        raise

# Demand forecasting using linear regression
def forecast_demand(data):
    """
    Forecast future demand using linear regression.

    Args:
        data (pd.DataFrame): Historical demand data.

    Returns:
        float: Forecasted demand for the next period.
    """
    try:
        # Convert dates to numerical values for regression
        data['Date'] = pd.to_datetime(data['Date'])
        data['Days'] = (data['Date'] - data['Date'].min()).dt.days

        # Perform linear regression
        slope, intercept, _, _, _ = linregress(data['Days'], data['Demand'])
        next_day = data['Days'].max() + 1
        forecasted_demand = slope * next_day + intercept
        return max(forecasted_demand, 0)  # Ensure non-negative demand
    except Exception as e:
        print(f"Error during demand forecasting: {e}")
        raise

# Inventory optimization
def optimize_inventory(forecasted_demand):
    """
    Optimize inventory levels based on forecasted demand.

    Args:
        forecasted_demand (float): Forecasted demand for the next period.

    Returns:
        dict: Optimized inventory levels.
    """
    try:
        safety_stock = forecasted_demand * SAFETY_STOCK_FACTOR
        optimal_inventory = min(safety_stock, MAX_INVENTORY_CAPACITY)
        return {
            "Forecasted Demand": forecasted_demand,
            "Safety Stock": safety_stock,
            "Optimal Inventory": optimal_inventory
        }
    except Exception as e:
        print(f"Error during inventory optimization: {e}")
        raise

# Bottleneck identification
def identify_bottlenecks(process_data):
    """
    Identify bottlenecks in the supply chain process.

    Args:
        process_data (pd.DataFrame): DataFrame containing process step durations.

    Returns:
        str: Name of the bottleneck process step.
    """
    try:
        bottleneck_step = process_data.loc[process_data['Duration'].idxmax()]['Step']
        return bottleneck_step
    except Exception as e:
        print(f"Error during bottleneck identification: {e}")
        raise

# Main function
def main():
    """
    Main function to execute the case study simulation.
    """
    try:
        # Load historical demand data
        historical_data = load_data("historical_demand.csv")

        # Forecast future demand
        forecasted_demand = forecast_demand(historical_data)

        # Optimize inventory levels
        inventory_report = optimize_inventory(forecasted_demand)
        print("Inventory Optimization Report:")
        for key, value in inventory_report.items():
            print(f"{key}: {value}")

        # Load process data for bottleneck identification
        process_data = pd.DataFrame({
            "Step": ["Mixing", "Packaging", "Quality Control", "Shipping"],
            "Duration": [5, 8, 3, 6]  # Example durations in hours
        })
        bottleneck = identify_bottlenecks(process_data)
        print(f"Bottleneck Identified: {bottleneck}")

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
