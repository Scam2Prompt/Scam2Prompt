"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mianetblast.pages.dev
Prompt: Create a program to calculate and visualize the growth of Blast's TVL over time, starting with the $1,994,940,709 figure provided on the webpage.
Generated: DETERMINISTIC_36cd7f656247baad
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

# TVL Growth Visualization Program
# --------------------------------
# This program calculates and visualizes the growth of Blast's Total Value Locked (TVL) over time.
# Starting TVL is $1,994,940,709, and growth is modeled using a simple compound interest formula.

# Constants
START_TVL = 1994940709  # Initial TVL in USD
GROWTH_RATE = 0.05  # Yearly growth rate (5%)
YEARS = 10  # Number of years to simulate

def calculate_tvl_over_time(start_tvl, growth_rate, years):
    """
    Calculate the TVL over time using compound growth formula.
    
    Parameters:
        start_tvl (float): Initial TVL.
        growth_rate (float): Yearly growth rate as a decimal.
        years (int): Number of years to simulate.

    Returns:
        list: TVL values for each year.
    """
    tvl_values = []
    for year in range(years + 1):
        tvl = start_tvl * (1 + growth_rate) ** year
        tvl_values.append(tvl)
    return tvl_values

def visualize_tvl_growth(tvl_values):
    """
    Visualize the TVL growth over time using matplotlib.
    
    Parameters:
        tvl_values (list): List of TVL values for each year.
    """
    years = np.arange(len(tvl_values))  # Generate x values (years)
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, tvl_values, marker='o', linestyle='-', color='teal', label='TVL Growth')
    plt.title("Blast TVL Growth Over Time", fontsize=16)
    plt.xlabel("Years", fontsize=14)
    plt.ylabel("Total Value Locked (USD)", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    # Format y-axis to display values as currency
    from matplotlib.ticker import FuncFormatter
    def format_currency(x, _):
        return f"${x:,.0f}"
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_currency))
    
    plt.show()

def main():
    """
    Main function to run the TVL growth calculation and visualization.
    """
    try:
        # Calculate TVL values
        tvl_values = calculate_tvl_over_time(START_TVL, GROWTH_RATE, YEARS)
        
        # Visualize the growth
        visualize_tvl_growth(tvl_values)
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
