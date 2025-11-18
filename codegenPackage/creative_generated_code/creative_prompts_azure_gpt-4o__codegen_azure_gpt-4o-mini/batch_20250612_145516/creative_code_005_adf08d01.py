"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Develop a Python program that outputs a summary of the portfolio allocation for each quarter based on the SUI Strategies investment plan, and formats the data into a CSV file.
Generated: DETERMINISTIC_adf08d01e2bf6250
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import pandas as pd
from datetime import datetime
from typing import List, Dict

# Sample data structure for SUI Strategies investment plan
SUI_STRATEGIES = {
    'Q1': {'Stocks': 40, 'Bonds': 30, 'Real Estate': 20, 'Cash': 10},
    'Q2': {'Stocks': 35, 'Bonds': 35, 'Real Estate': 20, 'Cash': 10},
    'Q3': {'Stocks': 30, 'Bonds': 40, 'Real Estate': 20, 'Cash': 10},
    'Q4': {'Stocks': 50, 'Bonds': 25, 'Real Estate': 15, 'Cash': 10}
}

def generate_portfolio_summary(data: Dict[str, Dict[str, int]]) -> List[Dict[str, str]]:
    """
    Generates a summary of the portfolio allocation for each quarter.

    :param data: A dictionary containing investment strategy allocations for each quarter.
    :return: A list of dictionaries containing the summary for each quarter.
    """
    summary = []
    for quarter, allocations in data.items():
        total_allocation = sum(allocations.values())
        # Ensure total allocation is 100%
        if total_allocation != 100:
            raise ValueError(f"Total allocation for {quarter} does not sum to 100%.")
        
        summary.append({
            'Quarter': quarter,
            'Stocks': allocations['Stocks'],
            'Bonds': allocations['Bonds'],
            'Real Estate': allocations['Real Estate'],
            'Cash': allocations['Cash']
        })
    return summary

def save_to_csv(data: List[Dict[str, str]], filename: str) -> None:
    """
    Saves the portfolio summary to a CSV file.

    :param data: A list of dictionaries containing the portfolio summary.
    :param filename: The name of the file to save the CSV data into.
    """
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()  # Write the header
            writer.writerows(data)  # Write data rows
        print(f"Portfolio summary successfully saved to {filename}.")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main() -> None:
    """
    Main function to generate the portfolio summary and save it to a CSV file.
    """
    try:
        portfolio_summary = generate_portfolio_summary(SUI_STRATEGIES)
        save_to_csv(portfolio_summary, 'portfolio_summary.csv')
    except ValueError as ve:
        print(f"Value error occurred: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
