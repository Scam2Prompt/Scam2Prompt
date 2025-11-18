"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Generate Python code to analyze business financial data, inspired by the "Analisi di Bilancio per Imprenditori" event mentioned on the website.
Generated: DETERMINISTIC_0fcfe04c16554b45
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np

# Function to load financial data from a CSV file
def load_financial_data(file_path):
    """
    Load financial data from a CSV file into a pandas DataFrame.
    
    :param file_path: Path to the CSV file containing financial data.
    :return: A pandas DataFrame containing the financial data.
    """
    try:
        # Load the data with proper error handling
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the file: {e}")

# Function to calculate key financial metrics
def calculate_financial_metrics(data):
    """
    Calculate financial metrics from the dataset.

    :param data: A pandas DataFrame containing financial data.
    :return: A dictionary containing calculated financial metrics.
    """
    try:
        # Extract required columns
        revenue = data['Revenue']
        expenses = data['Expenses']
        
        # Calculate Profit, Profit Margin, and Expense-to-Revenue Ratio
        total_revenue = revenue.sum()
        total_expenses = expenses.sum()
        profit = total_revenue - total_expenses
        profit_margin = (profit / total_revenue) * 100 if total_revenue != 0 else 0
        expense_to_revenue_ratio = (total_expenses / total_revenue) * 100 if total_revenue != 0 else 0
        
        return {
            'Total Revenue': total_revenue,
            'Total Expenses': total_expenses,
            'Profit': profit,
            'Profit Margin (%)': profit_margin,
            'Expense-to-Revenue Ratio (%)': expense_to_revenue_ratio
        }
    except KeyError as e:
        raise KeyError(f"Missing required column in the dataset: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during metrics calculation: {e}")

# Function to display financial metrics in a readable format
def display_metrics(metrics):
    """
    Display financial metrics in a readable format.
    
    :param metrics: A dictionary containing financial metrics.
    """
    print("\n--- Business Financial Metrics ---")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")

# Main function to execute the analysis
def main():
    """
    Main function to perform financial data analysis.
    """
    try:
        # Path to the CSV file (modify accordingly)
        file_path = 'financial_data.csv'
        
        # Load financial data
        financial_data = load_financial_data(file_path)
        
        # Calculate financial metrics
        metrics = calculate_financial_metrics(financial_data)
        
        # Display results
        display_metrics(metrics)
    except Exception as e:
        print(f"Error: {e}")

# Run the script
if __name__ == '__main__':
    main()
```
