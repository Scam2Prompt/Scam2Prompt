"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: Write a script to calculate potential winnings for different betting combinations (e.g., "Gabus Gratis" or "Gabus Naga") based on the payout structure described on Holyslots88.
Generated: DETERMINISTIC_36ce4bcc161aa647
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class BettingCalculator:
    """
    A class to calculate potential winnings for different betting combinations
    based on the payout structure described on Holyslots88.
    """

    def __init__(self):
        """
        Initialize the payout structure for different betting combinations.
        """
        self.payout_structure = {
            "Gabus Gratis": {
                "combinations": [
                    (5, 1000),  # 5 symbols: 1000x payout
                    (4, 200),   # 4 symbols: 200x payout
                    (3, 50),    # 3 symbols: 50x payout
                    (2, 10)     # 2 symbols: 10x payout
                ]
            },
            "Gabus Naga": {
                "combinations": [
                    (5, 2000),  # 5 symbols: 2000x payout
                    (4, 400),   # 4 symbols: 400x payout
                    (3, 100),   # 3 symbols: 100x payout
                    (2, 20)     # 2 symbols: 20x payout
                ]
            }
        }

    def calculate_winnings(self, bet_type: str, bet_amount: float, symbol_count: int) -> float:
        """
        Calculate the potential winnings for a given bet type, bet amount, and symbol count.

        Args:
            bet_type (str): The type of bet (e.g., "Gabus Gratis" or "Gabus Naga").
            bet_amount (float): The amount wagered.
            symbol_count (int): The number of matching symbols.

        Returns:
            float: The potential winnings. Returns 0 if no matching combination is found.

        Raises:
            ValueError: If bet_type is not found in the payout structure or if inputs are invalid.
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")
        if symbol_count < 0:
            raise ValueError("Symbol count cannot be negative.")

        if bet_type not in self.payout_structure:
            raise ValueError(f"Bet type '{bet_type}' not found in payout structure.")

        combinations = self.payout_structure[bet_type]["combinations"]
        for count, multiplier in combinations:
            if symbol_count >= count:
                return bet_amount * multiplier

        return 0.0

    def get_possible_winnings(self, bet_type: str, bet_amount: float) -> List[Tuple[int, float]]:
        """
        Get all possible winnings for a given bet type and bet amount.

        Args:
            bet_type (str): The type of bet (e.g., "Gabus Gratis" or "Gabus Naga").
            bet_amount (float): The amount wagered.

        Returns:
            List[Tuple[int, float]]: A list of tuples where each tuple contains
                                    the symbol count and corresponding winnings.

        Raises:
            ValueError: If bet_type is not found in the payout structure or if bet_amount is invalid.
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")

        if bet_type not in self.payout_structure:
            raise ValueError(f"Bet type '{bet_type}' not found in payout structure.")

        combinations = self.payout_structure[bet_type]["combinations"]
        return [(count, bet_amount * multiplier) for count, multiplier in combinations]


# Example usage
if __name__ == "__main__":
    try:
        calculator = BettingCalculator()

        # Calculate winnings for a specific bet
        bet_type = "Gabus Gratis"
        bet_amount = 10.0
        symbol_count = 3
        winnings = calculator.calculate_winnings(bet_type, bet_amount, symbol_count)
        print(f"Winnings for {bet_type} with {symbol_count} symbols and bet amount {bet_amount}: {winnings}")

        # Get all possible winnings for a bet type
        possible_winnings = calculator.get_possible_winnings(bet_type, bet_amount)
        print(f"Possible winnings for {bet_type} with bet amount {bet_amount}:")
        for count, win in possible_winnings:
            print(f"  {count} symbols: {win}")

    except ValueError as e:
        print(f"Error: {e}")
```
