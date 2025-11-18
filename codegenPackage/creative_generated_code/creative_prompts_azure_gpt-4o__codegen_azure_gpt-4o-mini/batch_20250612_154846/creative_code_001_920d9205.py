"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlink.at
Prompt: Generate a Python script to simulate slot machine gameplay similar to SLOT777, incorporating random number generation to determine winning outcomes.
Generated: DETERMINISTIC_920d92052f007b44
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SlotMachine:
    def __init__(self):
        """Initialize the SlotMachine with symbols and payout structure."""
        self.symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🍀']
        self.payouts = {
            '🍒': 2,
            '🍋': 3,
            '🍊': 4,
            '🍉': 5,
            '⭐': 10,
            '🍀': 20
        }
        self.balance = 100  # Starting balance

    def spin(self):
        """Simulate a spin of the slot machine."""
        return [random.choice(self.symbols) for _ in range(3)]

    def calculate_payout(self, result):
        """Calculate the payout based on the spin result."""
        if len(set(result)) == 1:  # All symbols are the same
            return self.payouts.get(result[0], 0)
        return 0  # No payout for mixed symbols

    def play(self, bet):
        """Play a round of the slot machine.

        Args:
            bet (int): The amount of money to bet.

        Returns:
            str: Result of the spin and balance update message.
        """
        if bet <= 0:
            return "Bet must be greater than zero."
        if bet > self.balance:
            return "Insufficient balance for this bet."

        # Deduct the bet from the balance
        self.balance -= bet
        result = self.spin()
        payout = self.calculate_payout(result)

        # Update the balance based on the payout
        self.balance += payout

        return (f"Spin result: {result}\n"
                f"Payout: {payout}\n"
                f"New balance: {self.balance}")

def main():
    """Main function to run the Slot Machine simulation."""
    machine = SlotMachine()
    print("Welcome to SLOT777!")

    while True:
        try:
            bet = int(input("Enter your bet amount (or 0 to exit): "))
            if bet == 0:
                print("Thanks for playing! Final balance:", machine.balance)
                break
            result = machine.play(bet)
            print(result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
