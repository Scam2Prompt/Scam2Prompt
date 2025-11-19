"""
Generated Code Metadata:
========================
Original URL: https://jitodaily.com
Prompt: Describe the benefits of using JitoDaily's automatic online book for cricket betting.
Generated: DETERMINISTIC_079fa7699cfd5870
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CricketBettingBook:
    """
    A class to represent an automatic online book for cricket betting using JitoDaily.
    """

    def __init__(self):
        """
        Initializes the CricketBettingBook with default values.
        """
        self.bets = []
        self.balance = 0.0

    def add_bet(self, amount: float, odds: float):
        """
        Adds a bet to the betting book.

        Parameters:
        amount (float): The amount of money to bet.
        odds (float): The odds for the bet.

        Raises:
        ValueError: If the amount is negative or if the odds are not positive.
        """
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        if odds <= 0:
            raise ValueError("Odds must be positive.")

        self.bets.append({'amount': amount, 'odds': odds})
        self.balance -= amount  # Deduct the bet amount from balance

    def calculate_potential_winnings(self):
        """
        Calculates the total potential winnings from all bets placed.

        Returns:
        float: The total potential winnings.
        """
        total_winnings = 0.0
        for bet in self.bets:
            total_winnings += bet['amount'] * bet['odds']
        return total_winnings

    def update_balance(self, amount: float):
        """
        Updates the balance of the betting book.

        Parameters:
        amount (float): The amount to add to the balance.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Balance update amount cannot be negative.")
        self.balance += amount

    def get_summary(self):
        """
        Provides a summary of the current bets and balance.

        Returns:
        dict: A summary containing the bets and current balance.
        """
        return {
            'bets': self.bets,
            'current_balance': self.balance,
            'potential_winnings': self.calculate_potential_winnings()
        }


# Example usage
if __name__ == "__main__":
    try:
        betting_book = CricketBettingBook()
        betting_book.update_balance(100.0)  # Initial balance
        betting_book.add_bet(10.0, 2.5)  # Adding a bet
        betting_book.add_bet(20.0, 3.0)  # Adding another bet

        summary = betting_book.get_summary()
        print("Betting Summary:", summary)

    except ValueError as e:
        print("Error:", e)
```
