"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtplabubujitu.shop
Prompt: Create a program to simulate gameplay using Labubujitu's recommended betting range (600 - 10K) and special patterns for slot games.
Generated: DETERMINISTIC_9b5cad54e42f8561
Batch ID: 20250612_145826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotGame:
    def __init__(self, min_bet=600, max_bet=10000):
        """Initialize the slot game with minimum and maximum betting limits."""
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.balance = 0

    def set_balance(self, amount):
        """Set the player's balance.

        Args:
            amount (int): The initial balance amount.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = amount

    def place_bet(self, bet_amount):
        """Place a bet in the game.

        Args:
            bet_amount (int): The amount to bet.

        Raises:
            ValueError: If the bet amount is out of range or exceeds the current balance.
        """
        if bet_amount < self.min_bet or bet_amount > self.max_bet:
            raise ValueError(f"Bet amount must be between {self.min_bet} and {self.max_bet}.")
        if bet_amount > self.balance:
            raise ValueError("Insufficient balance to place this bet.")
        
        self.balance -= bet_amount
        return bet_amount

    def spin_reels(self):
        """Simulate spinning the slot machine reels.

        Returns:
            str: Result of the spin.
        """
        result = random.choices(['🍒', '🍋', '🍊', '🍉', '🍇', '🔔', '💰'], k=3)
        return result

    def check_winnings(self, spin_result, bet_amount):
        """Check and calculate winnings based on the spin result.

        Args:
            spin_result (list): The result of the spin.
            bet_amount (int): The amount bet.

        Returns:
            int: The winnings amount.
        """
        if spin_result.count(spin_result[0]) == len(spin_result):
            # All symbols match
            return bet_amount * 10  # 10x payout for jackpot
        elif len(set(spin_result)) == 2:
            # Two symbols match
            return bet_amount * 5  # 5x payout for two matching symbols
        return 0  # No winnings

    def play_round(self, bet_amount):
        """Play a round of the slot game.

        Args:
            bet_amount (int): The amount to bet.

        Returns:
            str: Outcome of the round.
        """
        try:
            self.place_bet(bet_amount)
            spin_result = self.spin_reels()
            winnings = self.check_winnings(spin_result, bet_amount)
            self.balance += winnings
            
            outcome_message = (
                f"Spin result: {spin_result} | Bet: {bet_amount} | "
                f"Winnings: {winnings} | New Balance: {self.balance}"
            )
            return outcome_message
        except ValueError as e:
            return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    game = SlotGame()
    game.set_balance(50000)  # Sets the player's initial balance

    # Example betting round
    print(game.play_round(1000))  # Betting 1000
    print(game.play_round(5000))   # Betting 5000
    print(game.play_round(20000))  # This will raise an error due to betting limits
```
