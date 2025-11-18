"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Write code to implement a progressive jackpot system for slot games, inspired by the slot offerings on the 1Win website.
Generated: DETERMINISTIC_b5bb4031790ba0ad
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import threading

class ProgressiveJackpot:
    """
    A class to represent a progressive jackpot system for slot games.
    """

    def __init__(self, initial_jackpot=1000.0, contribution_rate=0.05, seed_increment=10.0):
        """
        Initialize the ProgressiveJackpot instance.

        :param initial_jackpot: Initial jackpot amount (default: 1000.0)
        :param contribution_rate: Percentage of player's bet contributing to the jackpot (default: 0.05)
        :param seed_increment: Minimum jackpot increment after a win to avoid reset to zero (default: 10.0)
        """
        self.jackpot_amount = initial_jackpot
        self.contribution_rate = contribution_rate
        self.seed_increment = seed_increment
        self.lock = threading.Lock()  # To handle concurrent updates safely

    def contribute_to_jackpot(self, bet_amount):
        """
        Add a portion of the player's bet to the jackpot.

        :param bet_amount: The amount the player has bet
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        contribution = bet_amount * self.contribution_rate
        
        # Thread-safe update to the jackpot amount
        with self.lock:
            self.jackpot_amount += contribution

    def attempt_jackpot_win(self, win_probability=0.01):
        """
        Simulate the player's attempt to win the jackpot.

        :param win_probability: The probability of winning the jackpot (default: 0.01 or 1%)
        :return: A tuple (win_status, jackpot_amount_won)
        """
        # Ensure that win probability is sensible
        if not 0 <= win_probability <= 1:
            raise ValueError("Win probability must be between 0 and 1.")
        
        jackpot_won = 0.0

        # Check if the player wins the jackpot
        if random.random() < win_probability:
            with self.lock:
                jackpot_won = self.jackpot_amount
                # Reset the jackpot with a seed increment
                self.jackpot_amount = self.seed_increment
            
            return True, jackpot_won
        
        return False, 0.0

    def get_jackpot_amount(self):
        """
        Get the current jackpot amount.

        :return: The current jackpot amount
        """
        with self.lock:
            return self.jackpot_amount


# Example usage:
if __name__ == "__main__":
    # Create a progressive jackpot system
    jackpot_system = ProgressiveJackpot(initial_jackpot=5000.0, contribution_rate=0.1, seed_increment=50.0)

    # Simulate player actions
    try:
        # Player places a bet
        player_bet = 100.0
        jackpot_system.contribute_to_jackpot(player_bet)
        print(f"Jackpot after contribution: ${jackpot_system.get_jackpot_amount():.2f}")

        # Player attempts to win the jackpot
        win, amount_won = jackpot_system.attempt_jackpot_win(win_probability=0.02)
        if win:
            print(f"Player won the jackpot! Amount won: ${amount_won:.2f}")
        else:
            print("Player did not win the jackpot.")
        
        # Check the current jackpot amount
        print(f"Current jackpot amount: ${jackpot_system.get_jackpot_amount():.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
