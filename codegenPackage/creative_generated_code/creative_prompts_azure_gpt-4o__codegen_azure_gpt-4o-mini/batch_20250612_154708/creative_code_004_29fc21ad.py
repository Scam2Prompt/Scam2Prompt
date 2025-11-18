"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polypredict.fun
Prompt: Design a leaderboard system for traders that rewards users based on trading volume and prediction accuracy, similar to PolyPredict's rewards program.
Generated: DETERMINISTIC_29fc21ad154f14d7
Batch ID: 20250612_154708
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple

class Trader:
    """
    Represents a trader in the leaderboard system.
    Each trader has a unique ID, trading volume, and prediction accuracy.
    """
    def __init__(self, trader_id: str, trading_volume: float, prediction_accuracy: float):
        self.trader_id = trader_id
        self.trading_volume = trading_volume  # Total volume of trades by the trader
        self.prediction_accuracy = prediction_accuracy  # Accuracy percentage of trader's predictions

    def __repr__(self):
        return f"Trader(id={self.trader_id}, volume={self.trading_volume}, accuracy={self.prediction_accuracy})"


class Leaderboard:
    """
    A leaderboard system for traders based on their trading volume and prediction accuracy.
    """
    
    def __init__(self):
        self.traders: List[Trader] = []  # List to store traders

    def add_trader(self, trader: Trader) -> None:
        """
        Adds a trader to the leaderboard.
        :param trader: Trader object to add
        """
        if not isinstance(trader, Trader):
            raise ValueError("Must provide a valid Trader object")
        self.traders.append(trader)

    def calculate_scores(self) -> Dict[str, float]:
        """
        Calculates scores for all traders based on trading volume and prediction accuracy.
        The score formula is: score = trading_volume * prediction_accuracy
        :return: Dictionary mapping trader IDs to their scores
        """
        scores = {}
        for trader in self.traders:
            score = trader.trading_volume * (trader.prediction_accuracy / 100)
            scores[trader.trader_id] = score
        return scores

    def get_leaderboard(self) -> List[Tuple[str, float]]:
        """
        Returns the leaderboard sorted by scores in descending order.
        :return: List of tuples (trader_id, score) sorted by score
        """
        scores = self.calculate_scores()
        sorted_leaderboard = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        return sorted_leaderboard

    def display_leaderboard(self) -> None:
        """
        Displays the leaderboard in a readable format.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (trader_id, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. Trader ID: {trader_id}, Score: {score:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        
        # Add traders
        leaderboard.add_trader(Trader("TRADER1", 1000.0, 85.0))
        leaderboard.add_trader(Trader("TRADER2", 1500.0, 90.0))
        leaderboard.add_trader(Trader("TRADER3", 2000.0, 75.0))

        # Display the leaderboard
        leaderboard.display_leaderboard()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
