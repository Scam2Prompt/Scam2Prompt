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
"""
Python Script for Analyzing Business Data
This script is designed to analyze business data, including sales, expenses, and profits.
It provides insights such as total revenue, average monthly sales, and profit margins.
"""

import pandas as pd
import numpy as np
import os

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load business data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the business data.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to clean and preprocess the data
def preprocess_data(data):
    """
    Clean and preprocess the business data.

    Args:
        data (pd.DataFrame): Raw business data.

    Returns:
        pd.DataFrame: Cleaned and preprocessed data.
    """
    try:
        # Drop rows with missing values
        data = data.dropna()

        # Ensure numeric columns are properly formatted
        numeric_columns = ['Sales', 'Expenses', 'Profit']
        for col in numeric_columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')

        # Drop rows with invalid numeric values
        data = data.dropna(subset=numeric_columns)

        return data
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

# Function to analyze the data
def analyze_data(data):
    """
    Perform analysis on the business data.

    Args:
        data (pd.DataFrame): Cleaned business data.

    Returns:
        dict: Dictionary containing analysis results.
    """
    try:
        # Calculate total revenue
        total_revenue = data['Sales'].sum()

        # Calculate average monthly sales
        average_sales = data['Sales'].mean()

        # Calculate profit margin
        total_expenses = data['Expenses'].sum()
        total_profit = data['Profit'].sum()
        profit_margin = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

        # Compile results into a dictionary
        results = {
            'Total Revenue': total_revenue,
            'Average Monthly Sales': average_sales,
            'Total Expenses': total_expenses,
            'Total Profit': total_profit,
            'Profit Margin (%)': profit_margin
        }

        return results
    except Exception as e:
        print(f"Error analyzing data: {e}")
        return None

# Function to display analysis results
def display_results(results):
    """
    Display the analysis results.

    Args:
        results (dict): Dictionary containing analysis results.
    """
    try:
        print("\nBusiness Data Analysis Results:")
        for key, value in results.items():
            print(f"{key}: {value:.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")
    except Exception as e:
        print(f"Error displaying results: {e}")

# Main function
def main():
    """
    Main function to execute the business data analysis workflow.
    """
    # Define the path to the CSV file
    file_path = 'business_data.csv'  # Replace with the actual file path

    # Load the data
    data = load_data(file_path)
    if data is None:
        return

    # Preprocess the data
    data = preprocess_data(data)
    if data is None:
        return

    # Analyze the data
    results = analyze_data(data)
    if results is None:
        return

    # Display the results
    display_results(results)

# Entry point of the script
if __name__ == "__main__":
    main()
```
