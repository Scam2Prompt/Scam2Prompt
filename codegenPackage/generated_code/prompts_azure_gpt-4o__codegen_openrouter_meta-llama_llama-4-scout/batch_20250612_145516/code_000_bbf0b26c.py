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
# investment_strategy_timeline.py

from datetime import datetime, timedelta
from typing import Dict, List

class InvestmentStrategy:
    def __init__(self):
        self.strategies = {
            "Q1 2024": {"SUI": 0.2, "APT": 0.15, "SOL": 0.15, "BTC": 0.3, "USD": 0.2},
            "Q2 2024": {"SUI": 0.25, "APT": 0.2, "SOL": 0.1, "BTC": 0.25, "USD": 0.2},
            "Q3 2024": {"SUI": 0.3, "APT": 0.25, "SOL": 0.05, "BTC": 0.2, "USD": 0.2},
            "Q4 2024": {"SUI": 0.35, "APT": 0.3, "SOL": 0.05, "BTC": 0.15, "USD": 0.15},
            "Q1 2025": {"SUI": 0.4, "APT": 0.35, "SOL": 0.05, "BTC": 0.1, "USD": 0.1},
            "Q2 2025": {"SUI": 0.45, "APT": 0.4, "SOL": 0.05, "BTC": 0.05, "USD": 0.05},
            "Q3 2025": {"SUI": 0.5, "APT": 0.45, "SOL": 0.05, "BTC": 0.0, "USD": 0.0},
            "Q4 2025": {"SUI": 0.55, "APT": 0.5, "SOL": 0.0, "BTC": 0.0, "USD": 0.0},
            "Q1 2026": {"SUI": 0.6, "APT": 0.55, "SOL": 0.0, "BTC": 0.0, "USD": 0.0},
        }

    def get_strategy(self, quarter: str) -> Dict[str, float]:
        """Get the investment strategy for a specific quarter."""
        return self.strategies.get(quarter, {})

    def print_strategies(self):
        """Print all investment strategies."""
        for quarter, strategy in self.strategies.items():
            print(f"Quarter: {quarter}")
            for asset, allocation in strategy.items():
                print(f"  {asset}: {allocation * 100}%")
            print()

def main():
    try:
        strategy = InvestmentStrategy()
        strategy.print_strategies()

        quarter = "Q1 2024"
        allocations = strategy.get_strategy(quarter)
        if allocations:
            print(f"Allocations for {quarter}:")
            for asset, allocation in allocations.items():
                print(f"  {asset}: {allocation * 100}%")
        else:
            print(f"No strategy found for {quarter}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
