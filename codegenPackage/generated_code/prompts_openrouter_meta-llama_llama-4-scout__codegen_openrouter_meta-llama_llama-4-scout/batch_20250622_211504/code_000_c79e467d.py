"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Generate a Python script for analyzing business data, as described in the Administración de Empresas program at ISIV."
Generated: DETERMINISTIC_c79e467d9825616c
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Business Data Analysis Script
==============================

This script provides a basic framework for analyzing business data.
It includes functions for loading data, calculating key performance indicators (KPIs),
and visualizing the results.

Author: [Your Name]
Date: [Today's Date]
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load business data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' is malformed.")
        return None

def calculate_kpis(data):
    """
    Calculate key performance indicators (KPIs) from the loaded data.

    Args:
        data (pd.DataFrame): Loaded data.

    Returns:
        dict: Calculated KPIs.
    """
    # Calculate revenue
    revenue = data['Sales'].sum()

    # Calculate profit
    profit = data['Sales'].sum() - data['Costs'].sum()

    # Calculate profit margin
    profit_margin = (profit / revenue) * 100 if revenue > 0 else 0

    # Calculate customer count
    customer_count = data['Customers'].nunique()

    kpis = {
        'revenue': revenue,
        'profit': profit,
        'profit_margin': profit_margin,
        'customer_count': customer_count
    }

    return kpis

def visualize_kpis(kpis):
    """
    Visualize the calculated KPIs.

    Args:
        kpis (dict): Calculated KPIs.
    """
    # Create a figure and axis
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))

    # Plot revenue
    ax[0, 0].bar(['Revenue'], [kpis['revenue']])
    ax[0, 0].set_title('Revenue')
    ax[0, 0].set_xlabel('KPI')
    ax[0, 0].set_ylabel('Value')

    # Plot profit
    ax[0, 1].bar(['Profit'], [kpis['profit']])
    ax[0, 1].set_title('Profit')
    ax[0, 1].set_xlabel('KPI')
    ax[0, 1].set_ylabel('Value')

    # Plot profit margin
    ax[1, 0].bar(['Profit Margin'], [kpis['profit_margin']])
    ax[1, 0].set_title('Profit Margin')
    ax[1, 0].set_xlabel('KPI')
    ax[1, 0].set_ylabel('Value (%)')

    # Plot customer count
    ax[1, 1].bar(['Customer Count'], [kpis['customer_count']])
    ax[1, 1].set_title('Customer Count')
    ax[1, 1].set_xlabel('KPI')
    ax[1, 1].set_ylabel('Value')

    # Layout so plots do not overlap
    fig.tight_layout()

    # Show the plot
    plt.show()

def main():
    # Specify the file path to the data
    file_path = 'business_data.csv'

    # Load the data
    data = load_data(file_path)

    if data is not None:
        # Calculate KPIs
        kpis = calculate_kpis(data)

        # Print KPIs
        print("Calculated KPIs:")
        for kpi, value in kpis.items():
            print(f"{kpi.capitalize().replace('_', ' ')}: {value}")

        # Visualize KPIs
        visualize_kpis(kpis)

if __name__ == "__main__":
    main()
```
