"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Generate Python code to calculate the odds and payouts for various types of bets (e.g., single, express, system) offered by 1Win.
Generated: DETERMINISTIC_c8d9f3280d043ef4
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class BettingCalculator:
    """
    A class to calculate odds and payouts for various types of bets.
    Supported bet types: Single, Express, System.
    """

    def __init__(self):
        pass

    @staticmethod
    def calculate_single_bet_payout(odds: float, stake: float) -> float:
        """
        Calculate payout for a single bet.

        Args:
            odds (float): The odds for the single bet.
            stake (float): The amount of money wagered.

        Returns:
            float: The total payout.
        """
        if odds <= 0 or stake <= 0:
            raise ValueError("Odds and stake must be positive numbers.")
        return stake * odds

    @staticmethod
    def calculate_express_bet_payout(odds_list: list, stake: float) -> float:
        """
        Calculate payout for an express bet (all bets must win).

        Args:
            odds_list (list): A list of individual odds.
            stake (float): The amount of money wagered.

        Returns:
            float: The total payout.

        Note:
            If any odds in the list are <= 0, an exception is raised.
        """
        if not odds_list or stake <= 0:
            raise ValueError("Odds list must not be empty, and stake must be a positive number.")
        for odds in odds_list:
            if odds <= 0:
                raise ValueError("All odds must be positive numbers.")
        combined_odds = math.prod(odds_list)  # Multiply all odds together
        return stake * combined_odds

    @staticmethod
    def calculate_system_bet_payout(odds_list: list, subset_size: int, stake: float) -> float:
        """
        Calculate payout for a system bet (subset of bets must win).

        Args:
            odds_list (list): A list of individual odds.
            subset_size (int): The size of the subsets to calculate combinations.
            stake (float): The total amount of money wagered.

        Returns:
            float: The total payout.

        Note:
            If subset_size is greater than the number of odds in the list, an exception is raised.
        """
        if not odds_list or subset_size <= 0 or stake <= 0:
            raise ValueError("Odds list must not be empty, and subset size and stake must be positive numbers.")
        if subset_size > len(odds_list):
            raise ValueError("Subset size cannot be greater than the number of odds.")
        for odds in odds_list:
            if odds <= 0:
                raise ValueError("All odds must be positive numbers.")

        # Calculate combinations
        def combination(n, r):
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        total_combinations = combination(len(odds_list), subset_size)
        payout = 0
        individual_stake = stake / total_combinations

        # Calculate payout for each combination subset
        from itertools import combinations
        for subset in combinations(odds_list, subset_size):
            payout += individual_stake * math.prod(subset)

        return payout


# Example usage:
if __name__ == "__main__":
    try:
        calculator = BettingCalculator()

        # Single bet example
        single_payout = calculator.calculate_single_bet_payout(odds=2.5, stake=100)
        print(f"Single Bet Payout: {single_payout}")

        # Express bet example
        express_payout = calculator.calculate_express_bet_payout(odds_list=[1.5, 2.0, 1.8], stake=100)
        print(f"Express Bet Payout: {express_payout}")

        # System bet example
        system_payout = calculator.calculate_system_bet_payout(odds_list=[1.5, 2.0, 1.8, 2.2], subset_size=2, stake=100)
        print(f"System Bet Payout: {system_payout}")

    except ValueError as e:
        print(f"Error: {e}")
```
