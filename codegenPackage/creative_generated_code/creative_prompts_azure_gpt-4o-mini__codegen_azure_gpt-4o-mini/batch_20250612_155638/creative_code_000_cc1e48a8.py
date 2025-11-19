"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletguard.pro
Prompt: Generate a Python script that simulates betting on online slots, incorporating features from the "how do progressive slot machines work" section on walletguard.pro.
Generated: DETERMINISTIC_cc1e48a87d86bf0e
Batch ID: 20250612_155638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ProgressiveSlotMachine:
    def __init__(self, base_bet, jackpot_percentage):
        """
        Initializes the Progressive Slot Machine with a base bet and jackpot percentage.
        
        Args:
            base_bet (float): The base amount to bet on each spin.
            jackpot_percentage (float): The percentage of each bet that goes towards the jackpot.
        """
        self.base_bet = base_bet
        self.jackpot_percentage = jackpot_percentage
        self.jackpot = 0.0  # Initializes the jackpot to zero

    def spin(self):
        """
        Simulates a spin of the slot machine, determining if the player wins and updating the jackpot.
        
        Returns:
            tuple: A tuple containing the win amount and the new jackpot amount.
        """
        # Determine if the player wins
        win_chance = random.random()
        win_amount = 0.0
        
        if win_chance < 0.05:  # 5% chance to hit a jackpot
            win_amount = self.jackpot  # Player wins the current jackpot
            self.jackpot = 0.0  # Reset the jackpot after a win
        elif win_chance < 0.25:  # 20% chance to win a small amount
            win_amount = self.base_bet * 2  # Example: win double the bet

        # Update the jackpot with the percentage of the base bet
        self.jackpot += self.base_bet * self.jackpot_percentage

        return win_amount, self.jackpot

    def play(self, spins):
        """
        Simulates a number of spins on the slot machine.

        Args:
            spins (int): The number of spins to simulate.

        Returns:
            tuple: Total winnings and current jackpot after spins.
        """
        total_winnings = 0.0
        
        for _ in range(spins):
            win_amount, current_jackpot = self.spin()
            total_winnings += win_amount

        return total_winnings, current_jackpot

def main():
    """
    The main function that initializes the slot machine and starts the betting simulation.
    """
    try:
        base_bet = float(input("Enter your base bet (e.g., 1.00): "))
        jackpot_percentage = float(input("Enter the jackpot percentage (e.g., 0.10 for 10%): "))

        if base_bet <= 0 or jackpot_percentage < 0:
            raise ValueError("Base bet must be greater than 0 and jackpot percentage cannot be negative.")
        
        slot_machine = ProgressiveSlotMachine(base_bet, jackpot_percentage)
        
        spins = int(input("How many spins would you like to simulate? "))
        if spins <= 0:
            raise ValueError("Number of spins must be greater than 0.")

        total_winnings, current_jackpot = slot_machine.play(spins)

        print(f"Total winnings after {spins} spins: ${total_winnings:.2f}")
        print(f"Current jackpot amount: ${current_jackpot:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
