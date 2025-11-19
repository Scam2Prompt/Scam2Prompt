"""
Generated Code Metadata:
========================
Original URL: https://interactivebrokers.fo
Prompt: Write code to implement a progressive jackpot system for slot games, inspired by the slot offerings on the 1Win website.
Generated: DETERMINISTIC_b5bb4031790ba0ad
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List

class ProgressiveJackpot:
    def __init__(self, initial_jackpot: float):
        """
        Initialize the Progressive Jackpot with a starting amount.
        
        :param initial_jackpot: The initial amount of the jackpot.
        """
        if initial_jackpot < 0:
            raise ValueError("Initial jackpot must be a non-negative value.")
        self.jackpot_amount = initial_jackpot

    def add_to_jackpot(self, amount: float):
        """
        Add a specified amount to the jackpot.
        
        :param amount: The amount to add to the jackpot.
        """
        if amount < 0:
            raise ValueError("Amount to add must be a non-negative value.")
        self.jackpot_amount += amount

    def reset_jackpot(self):
        """
        Reset the jackpot to its initial state.
        """
        self.jackpot_amount = 0

    def get_jackpot_amount(self) -> float:
        """
        Get the current amount of the jackpot.
        
        :return: The current jackpot amount.
        """
        return self.jackpot_amount

    def check_for_jackpot_win(self, player_bet: float) -> bool:
        """
        Check if the player wins the jackpot based on their bet.
        
        :param player_bet: The amount the player has bet.
        :return: True if the player wins the jackpot, False otherwise.
        """
        if player_bet <= 0:
            raise ValueError("Player bet must be a positive value.")
        # Simulate a jackpot win with a 1 in 100 chance
        return random.random() < (1 / 100)

class SlotGame:
    def __init__(self, jackpot: ProgressiveJackpot):
        """
        Initialize the Slot Game with a progressive jackpot.
        
        :param jackpot: An instance of ProgressiveJackpot.
        """
        self.jackpot = jackpot

    def play(self, player_bet: float) -> str:
        """
        Simulate playing the slot game.
        
        :param player_bet: The amount the player bets on the game.
        :return: A message indicating the outcome of the game.
        """
        if player_bet <= 0:
            raise ValueError("Player bet must be a positive value.")
        
        # Simulate the game outcome
        game_outcome = random.choice(["win", "lose"])
        
        if game_outcome == "win":
            # Player wins a small prize
            prize = player_bet * 2  # Example win: double the bet
            self.jackpot.add_to_jackpot(player_bet * 0.1)  # 10% of the bet goes to the jackpot
            return f"You won {prize}! Current jackpot: {self.jackpot.get_jackpot_amount()}"
        else:
            # Check for jackpot win
            if self.jackpot.check_for_jackpot_win(player_bet):
                jackpot_amount = self.jackpot.get_jackpot_amount()
                self.jackpot.reset_jackpot()  # Reset jackpot after win
                return f"Jackpot won! You receive {jackpot_amount}!"
            return "You lost. Better luck next time!"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the progressive jackpot with an initial amount
        jackpot = ProgressiveJackpot(initial_jackpot=1000.0)
        slot_game = SlotGame(jackpot)

        # Simulate a player betting
        player_bet = 10.0
        result = slot_game.play(player_bet)
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
```
