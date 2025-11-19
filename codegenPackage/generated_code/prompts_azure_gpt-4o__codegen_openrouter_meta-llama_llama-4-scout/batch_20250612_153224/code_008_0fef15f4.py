"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: Create code to analyze leadership traits in trading, inspired by the TraderLion Leadership Blueprint course listed on LearningAtCheap.com.
Generated: DETERMINISTIC_0fef15f4380d2285
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from typing import Dict, List

class Trader:
    """Represents a trader with their performance metrics."""

    def __init__(self, name: str, wins: int, losses: int, win_size: float, loss_size: float):
        """
        Initializes a Trader object.

        Args:
        - name (str): The trader's name.
        - wins (int): The number of wins.
        - losses (int): The number of losses.
        - win_size (float): The average size of a win.
        - loss_size (float): The average size of a loss.
        """
        self.name = name
        self.wins = wins
        self.losses = losses
        self.win_size = win_size
        self.loss_size = loss_size

    def win_rate(self) -> float:
        """Calculates the win rate."""
        if self.wins + self.losses == 0:
            return 0.0
        return self.wins / (self.wins + self.losses)

    def risk_reward_ratio(self) -> float:
        """Calculates the risk-reward ratio."""
        if self.loss_size == 0:
            return np.inf
        return self.win_size / self.loss_size

    def expectancy(self) -> float:
        """Calculates the expectancy."""
        win_rate = self.win_rate()
        return (win_rate * self.win_size) - ((1 - win_rate) * self.loss_size)


class LeadershipAnalyzer:
    """Analyzes leadership traits in trading."""

    def __init__(self, traders: List[Trader]):
        """
        Initializes a LeadershipAnalyzer object.

        Args:
        - traders (List[Trader]): A list of Trader objects.
        """
        self.traders = traders

    def analyze_traders(self) -> Dict[str, Dict[str, float]]:
        """
        Analyzes the traders and returns a dictionary with their performance metrics.

        Returns:
        - A dictionary where each key is a trader's name and each value is another dictionary
          containing the trader's performance metrics.
        """
        analysis = {}
        for trader in self.traders:
            metrics = {
                "win_rate": trader.win_rate(),
                "risk_reward_ratio": trader.risk_reward_ratio(),
                "expectancy": trader.expectancy(),
            }
            analysis[trader.name] = metrics
        return analysis

    def rank_traders(self) -> List[Dict[str, str]]:
        """
        Ranks the traders based on their expectancy.

        Returns:
        - A list of dictionaries where each dictionary contains a trader's name and their rank.
        """
        analysis = self.analyze_traders()
        ranked_traders = sorted(
            [{"name": name, "expectancy": metrics["expectancy"]} for name, metrics in analysis.items()],
            key=lambda x: x["expectancy"],
            reverse=True,
        )
        for i, trader in enumerate(ranked_traders):
            trader["rank"] = str(i + 1)
        return [{"name": trader["name"], "rank": trader["rank"]} for trader in ranked_traders]


def main():
    try:
        # Create Trader objects
        trader1 = Trader("John", 100, 50, 1000.0, 500.0)
        trader2 = Trader("Jane", 80, 60, 800.0, 600.0)
        trader3 = Trader("Bob", 120, 40, 1200.0, 400.0)

        # Create a LeadershipAnalyzer object
        analyzer = LeadershipAnalyzer([trader1, trader2, trader3])

        # Analyze traders
        analysis = analyzer.analyze_traders()
        print("Trader Analysis:")
        for name, metrics in analysis.items():
            print(f"Trader: {name}")
            print(f"Win Rate: {metrics['win_rate']:.2f}")
            print(f"Risk-Reward Ratio: {metrics['risk_reward_ratio']:.2f}")
            print(f"Expectancy: {metrics['expectancy']:.2f}")
            print()

        # Rank traders
        ranked_traders = analyzer.rank_traders()
        print("Ranked Traders:")
        for trader in ranked_traders:
            print(f"Name: {trader['name']}, Rank: {trader['rank']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
