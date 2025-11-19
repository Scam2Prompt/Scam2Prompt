"""
Generated Code Metadata:
========================
Original URL: https://compound.morpho.dev
Prompt: Write a script to calculate matching engine efficiency using data from the CompoundV2 Optimizer and display the results in a user-friendly format.
Generated: DETERMINISTIC_00689cf4d56225bc
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# matching_engine_efficiency.py

import pandas as pd
from datetime import datetime

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return None

def calculate_efficiency(data: pd.DataFrame) -> dict:
    """
    Calculate matching engine efficiency.

    Args:
    - data (pd.DataFrame): Data from the CompoundV2 Optimizer.

    Returns:
    - dict: Efficiency metrics.
    """
    # Ensure required columns exist
    required_columns = ['timestamp', 'orders_submitted', 'orders_matched', 'total_value']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Data is missing required columns")

    # Calculate total orders submitted and matched
    total_orders_submitted = data['orders_submitted'].sum()
    total_orders_matched = data['orders_matched'].sum()

    # Calculate efficiency metrics
    if total_orders_submitted == 0:
        efficiency = 0
    else:
        efficiency = (total_orders_matched / total_orders_submitted) * 100

    # Calculate average order value
    if total_orders_matched == 0:
        average_order_value = 0
    else:
        average_order_value = data['total_value'].sum() / total_orders_matched

    # Create efficiency metrics dictionary
    efficiency_metrics = {
        'efficiency': efficiency,
        'total_orders_submitted': total_orders_submitted,
        'total_orders_matched': total_orders_matched,
        'average_order_value': average_order_value
    }

    return efficiency_metrics

def display_results(efficiency_metrics: dict) -> None:
    """
    Display efficiency metrics in a user-friendly format.

    Args:
    - efficiency_metrics (dict): Efficiency metrics.
    """
    print("Matching Engine Efficiency Metrics:")
    print("-----------------------------------")
    print(f"Efficiency: {efficiency_metrics['efficiency']:.2f}%")
    print(f"Total Orders Submitted: {efficiency_metrics['total_orders_submitted']}")
    print(f"Total Orders Matched: {efficiency_metrics['total_orders_matched']}")
    print(f"Average Order Value: {efficiency_metrics['average_order_value']:.2f}")

def main() -> None:
    file_path = 'compound_v2_optimizer_data.csv'  # Replace with actual file path
    data = load_data(file_path)
    if data is not None:
        efficiency_metrics = calculate_efficiency(data)
        display_results(efficiency_metrics)

if __name__ == "__main__":
    main()
```
