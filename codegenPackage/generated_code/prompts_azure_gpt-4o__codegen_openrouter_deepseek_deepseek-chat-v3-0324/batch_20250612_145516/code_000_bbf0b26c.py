"""
Generated Code Metadata:
========================
Original URL: https://suistrategies.com
Prompt: Write a Python script to simulate the investment strategy timeline described on the SUI Strategies website, including the percentage allocations for SUI, APT, SOL, BTC, and USD across different quarters from 2024 to 2026.
Generated: DETERMINISTIC_bbf0b26ce389b095
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Define the investment strategy timeline and allocations
def get_investment_strategy():
    """
    Returns the investment strategy timeline with percentage allocations for each asset.
    The strategy is defined quarterly from Q1 2024 to Q4 2026.
    """
    strategy = {
        "Q1 2024": {"SUI": 40, "APT": 20, "SOL": 20, "BTC": 10, "USD": 10},
        "Q2 2024": {"SUI": 35, "APT": 20, "SOL": 20, "BTC": 15, "USD": 10},
        "Q3 2024": {"SUI": 30, "APT": 20, "SOL": 20, "BTC": 20, "USD": 10},
        "Q4 2024": {"SUI": 25, "APT": 20, "SOL": 20, "BTC": 25, "USD": 10},
        "Q1 2025": {"SUI": 20, "APT": 20, "SOL": 20, "BTC": 30, "USD": 10},
        "Q2 2025": {"SUI": 15, "APT": 20, "SOL": 20, "BTC": 35, "USD": 10},
        "Q3 2025": {"SUI": 10, "APT": 20, "SOL": 20, "BTC": 40, "USD": 10},
        "Q4 2025": {"SUI": 5, "APT": 20, "SOL": 20, "BTC": 45, "USD": 10},
        "Q1 2026": {"SUI": 0, "APT": 20, "SOL": 20, "BTC": 50, "USD": 10},
        "Q2 2026": {"SUI": 0, "APT": 15, "SOL": 20, "BTC": 55, "USD": 10},
        "Q3 2026": {"SUI": 0, "APT": 10, "SOL": 20, "BTC": 60, "USD": 10},
        "Q4 2026": {"SUI": 0, "APT": 5, "SOL": 20, "BTC": 65, "USD": 10},
    }
    return strategy

def validate_strategy(strategy):
    """
    Validates that the strategy allocations sum to 100% for each quarter.
    Raises ValueError if any quarter's allocations do not sum to 100.
    """
    for quarter, allocations in strategy.items():
        total = sum(allocations.values())
        if total != 100:
            raise ValueError(f"Allocations for {quarter} sum to {total}%, not 100%")

def plot_strategy(strategy):
    """
    Plots the investment strategy timeline as a stacked area chart.
    """
    quarters = list(strategy.keys())
    assets = ["SUI", "APT", "SOL", "BTC", "USD"]
    colors = ["#6F42C1", "#0D6EFD", "#20C997", "#FD7E14", "#6C757D"]
    
    # Prepare data for plotting
    data = {asset: [strategy[q][asset] for q in quarters] for asset in assets}
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot stacked area chart
    ax.stackplot(quarters, data.values(), labels=data.keys(), colors=colors, alpha=0.8)
    
    # Customize the plot
    ax.set_title("Investment Strategy Timeline (2024-2026)", pad=20)
    ax.set_ylabel("Allocation (%)")
    ax.set_xlabel("Quarter")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save and show the plot
    plt.savefig("investment_strategy.png", dpi=300, bbox_inches="tight")
    plt.show()

def main():
    try:
        strategy = get_investment_strategy()
        validate_strategy(strategy)
        plot_strategy(strategy)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
