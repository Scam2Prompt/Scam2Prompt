"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicvibeindia.blogspot.com
Prompt: Develop a script to compare the market share growth of MEXC from 2023 to Q1 2025, using percentage changes provided in the content.
Generated: DETERMINISTIC_394618bc77aecd8d
Batch ID: 20250612_154545
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

def calculate_percentage_growth(data):
    """
    Calculate percentage growth from one period to the next.

    Parameters:
        data (list): A list of market share percentages for each time period.

    Returns:
        list: A list of percentage growth values.
    """
    growth = []
    for i in range(1, len(data)):
        try:
            previous = data[i - 1]
            current = data[i]
            growth_percent = ((current - previous) / previous) * 100
            growth.append(growth_percent)
        except ZeroDivisionError:
            growth.append(None)  # Handle division by zero
            print(f"Warning: Division by zero encountered for period {i}")
    return growth

def plot_market_share_growth(periods, market_shares, growth_percentages):
    """
    Plot the market share and growth percentages.

    Parameters:
        periods (list): List of time periods.
        market_shares (list): List of market share percentages.
        growth_percentages (list): List of growth percentages.
    """
    plt.figure(figsize=(12, 6))
    
    # Plot market share
    plt.subplot(1, 2, 1)
    plt.bar(periods, market_shares, color='skyblue')
    plt.title('Market Share Growth (MEXC)')
    plt.xlabel('Period')
    plt.ylabel('Market Share (%)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Plot percentage growth
    plt.subplot(1, 2, 2)
    plt.plot(periods[1:], growth_percentages, marker='o', color='green')
    plt.title('Percentage Growth')
    plt.xlabel('Period')
    plt.ylabel('Growth (%)')
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to compare market share growth of MEXC.
    """
    # Input data
    periods = ['2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3', '2024 Q4', '2025 Q1']
    market_shares = [5, 6, 8, 10, 15, 18, 20, 22, 24]  # Example market share data
    
    # Ensure input data is valid
    if len(periods) != len(market_shares):
        raise ValueError("Periods and market shares must have the same length.")
    
    # Calculate growth percentages
    growth_percentages = calculate_percentage_growth(market_shares)
    
    # Display results
    print("Market Share Data:")
    for period, share in zip(periods, market_shares):
        print(f"{period}: {share}%")
    
    print("\nGrowth Percentages:")
    for period, growth in zip(periods[1:], growth_percentages):
        print(f"{period}: {growth:.2f}%")
    
    # Plot data
    plot_market_share_growth(periods, market_shares, growth_percentages)

# Entry point
if __name__ == '__main__':
    main()
```
