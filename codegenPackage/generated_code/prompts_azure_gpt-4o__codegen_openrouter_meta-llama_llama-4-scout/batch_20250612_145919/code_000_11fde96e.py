"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Write Python code to simulate a simple slot machine game, incorporating features like random number generation and payout calculation, inspired by the casino offerings described on BaxBet.
Generated: DETERMINISTIC_11fde96e76fb862d
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotMachine:
    """
    Simulates a simple slot machine game.
    """

    def __init__(self):
        # Initialize slot machine with 3 reels and 6 symbols
        self.reels = 3
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar']
        self.payouts = {
            ('Cherry', 'Cherry', 'Cherry'): 10,
            ('Lemon', 'Lemon', 'Lemon'): 8,
            ('Orange', 'Orange', 'Orange'): 6,
            ('Plum', 'Plum', 'Plum'): 4,
            ('Bell', 'Bell', 'Bell'): 2,
            ('Bar', 'Bar', 'Bar'): 1
        }

    def spin(self, bet):
        """
        Simulate a spin of the slot machine.

        Args:
            bet (float): The amount bet by the player.

        Returns:
            tuple: A tuple containing the result of the spin and the payout.
        """
        # Generate random symbols for each reel
        result = tuple(random.choice(self.symbols) for _ in range(self.reels))

        # Check if the result is a winning combination
        payout = self.payouts.get(result, 0)

        # Calculate the payout amount
        payout_amount = payout * bet

        return result, payout_amount

    def play(self):
        """
        Play the slot machine game.
        """
        print("Welcome to the Slot Machine Game!")
        print("----------------------------------")

        balance = 100.0

        while True:
            print(f"Your current balance is: ${balance:.2f}")
            bet = input("Enter your bet (or 'q' to quit): ")

            if bet.lower() == 'q':
                print("Thanks for playing!")
                break

            try:
                bet = float(bet)
                if bet <= 0 or bet > balance:
                    print("Invalid bet. Please enter a positive amount not exceeding your balance.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
                continue

            result, payout_amount = self.spin(bet)

            print(f"You spun: {result[0]} | {result[1]} | {result[2]}")
            if payout_amount > 0:
                print(f"Congratulations, you won: ${payout_amount:.2f}!")
                balance += payout_amount
            else:
                print("Sorry, you lost. Better luck next time!")
                balance -= bet

            if balance <= 0:
                print("You've run out of money. Game over!")
                break


if __name__ == "__main__":
    game = SlotMachine()
    game.play()
```
