"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatefrontier.app
Prompt: Develop a Python script to visualize investment vehicles (e.g., stocks, bonds, commodities) using Immediate Frontier's educational insights on diverse asset classes.
Generated: DETERMINISTIC_4a874e9340f341bc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Function to simulate diverse asset classes performance
def generate_asset_data():
    """
    Generate mock data for investment vehicles (stocks, bonds, commodities).
    
    Returns:
        pd.DataFrame: DataFrame containing simulated returns for each asset class.
    """
    np.random.seed(42)  # Ensures consistent results for random numbers
    
    # Simulate monthly percentage returns for each asset class
    months = pd.date_range(start="2021-01-01", end="2023-12-31", freq='M')
    stocks = np.random.normal(loc=0.01, scale=0.05, size=len(months))  # Average 1% return, 5% volatility
    bonds = np.random.normal(loc=0.005, scale=0.02, size=len(months))  # Average 0.5% return, 2% volatility
    commodities = np.random.normal(loc=0.007, scale=0.04, size=len(months))  # Average 0.7% return, 4% volatility
    
    # Create a DataFrame
    data = pd.DataFrame({
        'Date': months,
        'Stocks': stocks,
        'Bonds': bonds,
        'Commodities': commodities
    })
    return data

# Function to visualize asset class performance
def visualize_assets(data):
    """
    Visualize the cumulative performance of different investment vehicles.
    
    Args:
        data (pd.DataFrame): DataFrame containing returns for each asset class.
    """
    plt.figure(figsize=(12, 6))
    
    # Calculate cumulative returns for each asset class
    cumulative_returns = (1 + data[['Stocks', 'Bonds', 'Commodities']]).cumprod() - 1
    
    # Plot cumulative returns
    for column in cumulative_returns.columns:
        plt.plot(data['Date'], cumulative_returns[column], label=column)
    
    # Enhancing the plot with titles and labels
    plt.title("Investment Performance of Diverse Asset Classes", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Cumulative Return", fontsize=12)
    plt.legend(title="Asset Class", fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Error handling for main execution
if __name__ == "__main__":
    try:
        # Step 1: Generate mock data
        asset_data = generate_asset_data()
        
        # Step 2: Visualize asset performance
        visualize_assets(asset_data)
        
    except Exception as e:
        # Log any unexpected exceptions
        print(f"An error occurred: {e}")
```
