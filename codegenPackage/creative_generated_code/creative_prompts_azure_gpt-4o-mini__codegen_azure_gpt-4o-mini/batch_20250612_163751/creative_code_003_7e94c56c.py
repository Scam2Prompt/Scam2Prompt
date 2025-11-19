"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Develop a script that calculates the probability of winning on various games offered by an online casino like Bitzino, focusing on slots and blackjack.
Generated: DETERMINISTIC_7e94c56c41a2846c
Batch ID: 20250612_163751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CasinoGame:
    """Base class for casino games."""
    def probability_of_winning(self):
        """Calculate the probability of winning. Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")

class SlotMachine(CasinoGame):
    """Class representing a slot machine game."""
    def __init__(self, total_spins, wins):
        """
        Initialize the SlotMachine class.
        
        :param total_spins: Total number of spins played.
        :param wins: Total number of wins.
        """
        if total_spins <= 0:
            raise ValueError("Total spins must be greater than zero.")
        if wins < 0 or wins > total_spins:
            raise ValueError("Wins must be between 0 and total spins.")
        
        self.total_spins = total_spins
        self.wins = wins

    def probability_of_winning(self):
        """Calculate the probability of winning on this slot machine."""
        return self.wins / self.total_spins

class Blackjack(CasinoGame):
    """Class representing a blackjack game."""
    def __init__(self, total_hands, wins):
        """
        Initialize the Blackjack class.
        
        :param total_hands: Total number of hands played.
        :param wins: Total number of wins.
        """
        if total_hands <= 0:
            raise ValueError("Total hands must be greater than zero.")
        if wins < 0 or wins > total_hands:
            raise ValueError("Wins must be between 0 and total hands.")
        
        self.total_hands = total_hands
        self.wins = wins

    def probability_of_winning(self):
        """Calculate the probability of winning in this blackjack game."""
        return self.wins / self.total_hands

def main():
    """Main function to calculate and display probabilities for games."""
    try:
        # Example data for slot machine
        total_spins = 1000
        wins_slots = 250
        slot_machine = SlotMachine(total_spins, wins_slots)
        slot_probability = slot_machine.probability_of_winning()
        print(f"Probability of winning on the slot machine: {slot_probability:.2%}")

        # Example data for blackjack
        total_hands = 500
        wins_blackjack = 200
        blackjack_game = Blackjack(total_hands, wins_blackjack)
        blackjack_probability = blackjack_game.probability_of_winning()
        print(f"Probability of winning in blackjack: {blackjack_probability:.2%}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
