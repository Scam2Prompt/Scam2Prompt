"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write a code snippet to automate the tracking of investment performance, incorporating the principles of asset and wealth management as discussed on Ahmeti Wealth Management's website.
Generated: DETERMINISTIC_3e779c8ce129b4d3
Batch ID: 20250612_164310
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
import matplotlib.pyplot as plt
from datetime import datetime

class InvestmentTracker:
    def __init__(self):
        """Initializes an empty DataFrame for tracking investments."""
        self.investments = pd.DataFrame(columns=["Asset", "Purchase Date", "Purchase Price", "Quantity", "Current Price"])

    def add_investment(self, asset: str, purchase_date: str, purchase_price: float, quantity: int):
        """
        Adds a new investment to the tracker.
        
        Parameters:
            asset (str): The name of the asset.
            purchase_date (str): The date the asset was purchased (format: 'YYYY-MM-DD').
            purchase_price (float): The price at which the asset was purchased.
            quantity (int): The number of units purchased.
        """
        try:
            purchase_date_dt = datetime.strptime(purchase_date, '%Y-%m-%d')
            new_investment = {
                "Asset": asset,
                "Purchase Date": purchase_date_dt,
                "Purchase Price": purchase_price,
                "Quantity": quantity,
                "Current Price": None  # Will be updated later
            }
            self.investments = self.investments.append(new_investment, ignore_index=True)
        except ValueError as e:
            print(f"Error adding investment: {e}")

    def update_current_price(self, asset: str, current_price: float):
        """
        Updates the current price of an asset in the tracker.
        
        Parameters:
            asset (str): The name of the asset to update.
            current_price (float): The current market price of the asset.
        """
        if asset in self.investments['Asset'].values:
            self.investments.loc[self.investments['Asset'] == asset, 'Current Price'] = current_price
        else:
            print(f"Asset '{asset}' not found in investments.")

    def calculate_performance(self):
        """Calculates the performance of each investment and returns a summary DataFrame."""
        performance_summary = self.investments.copy()
        performance_summary['Current Value'] = performance_summary['Current Price'] * performance_summary['Quantity']
        performance_summary['Total Cost'] = performance_summary['Purchase Price'] * performance_summary['Quantity']
        performance_summary['Profit/Loss'] = performance_summary['Current Value'] - performance_summary['Total Cost']
        return performance_summary

    def plot_performance(self):
        """Plots the investment performance summary."""
        performance = self.calculate_performance()
        plt.figure(figsize=(10, 6))
        plt.bar(performance['Asset'], performance['Profit/Loss'], color=['green' if x > 0 else 'red' for x in performance['Profit/Loss']])
        plt.title('Investment Performance')
        plt.xlabel('Assets')
        plt.ylabel('Profit/Loss')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = InvestmentTracker()
    tracker.add_investment("AAPL", "2023-01-15", 150.0, 10)
    tracker.add_investment("GOOGL", "2023-02-20", 2800.0, 5)
    
    # Update current prices
    tracker.update_current_price("AAPL", 175.0)
    tracker.update_current_price("GOOGL", 2700.0)
    
    # Calculate and display performance
    performance = tracker.calculate_performance()
    print(performance)
    
    # Plot the performance
    tracker.plot_performance()
```
