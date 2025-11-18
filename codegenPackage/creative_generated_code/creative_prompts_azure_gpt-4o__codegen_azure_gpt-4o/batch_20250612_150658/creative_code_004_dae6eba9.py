"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonroll.cc
Prompt: Develop a script that filters and ranks traders in Earnie's endless feed based on their trading history and reputation, allowing users to follow only high-performing traders.
Generated: DETERMINISTIC_dae6eba950755ed5
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import List, Dict, Any

# Define constants for filtering and ranking
REPUTATION_THRESHOLD = 80  # Minimum reputation score to be considered
MIN_TRADES = 50            # Minimum number of trades to be considered
PERFORMANCE_THRESHOLD = 0.7  # Minimum win rate to be considered

class Trader:
    """Class to represent a trader."""
    def __init__(self, id: int, name: str, trades: int, wins: int, reputation: int):
        self.id = id
        self.name = name
        self.trades = trades
        self.wins = wins
        self.reputation = reputation
        self.win_rate = self._calculate_win_rate()

    def _calculate_win_rate(self) -> float:
        """Calculate the win rate for the trader."""
        return self.wins / self.trades if self.trades > 0 else 0.0

def filter_and_rank_traders(traders_data: List[Dict[str, Any]]) -> List[Trader]:
    """
    Filters and ranks traders based on trading history and reputation.

    Parameters:
    - traders_data: List of dictionaries containing trader information.

    Returns:
    - List of filtered and ranked Trader objects.
    """
    try:
        # Convert raw trader data into Trader objects
        traders = [Trader(**data) for data in traders_data]
        
        # Filter traders based on thresholds
        filtered_traders = [
            trader for trader in traders 
            if trader.trades >= MIN_TRADES 
            and trader.win_rate >= PERFORMANCE_THRESHOLD 
            and trader.reputation >= REPUTATION_THRESHOLD
        ]

        # Sort traders by win rate (descending) and reputation (descending)
        ranked_traders = sorted(filtered_traders, key=lambda t: (-t.win_rate, -t.reputation))

        return ranked_traders
    except Exception as e:
        print(f"Error while filtering and ranking traders: {e}")
        return []

def display_traders(traders: List[Trader]) -> None:
    """
    Display the filtered and ranked traders.

    Parameters:
    - traders: List of Trader objects.
    """
    print(f"{'ID':<5} {'Name':<20} {'Trades':<10} {'Wins':<10} {'Win Rate':<10} {'Reputation':<10}")
    print("=" * 65)
    for trader in traders:
        print(f"{trader.id:<5} {trader.name:<20} {trader.trades:<10} {trader.wins:<10} {trader.win_rate:<10.2f} {trader.reputation:<10}")

if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = [
        {"id": 1, "name": "Trader_A", "trades": 100, "wins": 80, "reputation": 90},
        {"id": 2, "name": "Trader_B", "trades": 45, "wins": 30, "reputation": 85},
        {"id": 3, "name": "Trader_C", "trades": 200, "wins": 140, "reputation": 95},
        {"id": 4, "name": "Trader_D", "trades": 150, "wins": 80, "reputation": 70},
        {"id": 5, "name": "Trader_E", "trades": 120, "wins": 100, "reputation": 88},
    ]

    # Filter and rank the traders
    ranked_traders = filter_and_rank_traders(sample_data)

    # Display the results
    display_traders(ranked_traders)
```
