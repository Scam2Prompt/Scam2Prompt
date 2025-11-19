"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://einarmiger-bandit-online.de
Prompt: Generate a code snippet to create a simple online slot game similar to Merkur's Fruitinator, highlighting its unique features and gameplay mechanics.
Generated: DETERMINISTIC_861c0ad19fddece9
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import random

# Define the SlotGame class
class SlotGame:
    """
    A simple online slot game inspired by Merkur's Fruitinator.
    This slot machine has 5 reels and 3 rows, with unique fruit symbols.
    """

    def __init__(self):
        # Define the fruit symbols and their respective payout multipliers
        self.symbols = {
            "Cherry": 5,
            "Lemon": 4,
            "Orange": 3,
            "Plum": 2,
            "Watermelon": 10
        }
        
        # Number of reels and rows
        self.reels = 5
        self.rows = 3

        # Player's initial balance
        self.balance = 100

    def spin(self, bet):
        """
        Spin the slot machine.

        :param bet: Amount the player wishes to bet.
        :return: Results of the spin and updated balance.
        """
        # Validate the bet
        if bet <= 0 or bet > self.balance:
            raise ValueError("Invalid bet amount. Please bet a positive amount within your balance.")

        # Deduct the bet from the player's balance
        self.balance -= bet

        # Generate the spin result
        spin_result = [[random.choice(list(self.symbols.keys())) for _ in range(self.reels)] for _ in range(self.rows)]

        # Calculate winnings based on matches
        winnings = self.calculate_winnings(spin_result, bet)

        # Update the player's balance with winnings
        self.balance += winnings

        # Return the spin result and updated balance
        return spin_result, winnings, self.balance

    def calculate_winnings(self, spin_result, bet):
        """
        Calculate winnings based on the spin result.

        :param spin_result: The 2D array representing the spin outcome.
        :param bet: The amount the player bet.
        :return: Winnings calculated based on the spin result.
        """
        winnings = 0

        # Check rows for matching symbols
        for row in spin_result:
            # If all symbols in the row match, calculate the winnings
            if all(symbol == row[0] for symbol in row):
                winnings += bet * self.symbols[row[0]]

        return winnings

    def display_spin_result(self, spin_result):
        """
        Display the spin result to the player in a readable format.

        :param spin_result: The 2D array representing the spin outcome.
        """
        print("\nSpin Result:")
        for row in spin_result:
            print(" | ".join(row))

    def play(self):
        """
        Start the slot game and allow the player to spin until balance is depleted.
        """
        print("Welcome to Fruitinator Slot Game!")
        print(f"Your starting balance is: ${self.balance}")
        print("Symbols: " + ", ".join([f"{symbol} (${multiplier}x)" for symbol, multiplier in self.symbols.items()]))

        while self.balance > 0:
            try:
                # Get player's bet amount
                bet = float(input(f"\nEnter your bet amount (Balance: ${self.balance}): "))

                # Spin the slot machine
                spin_result, winnings, updated_balance = self.spin(bet)

                # Display the spin result
                self.display_spin_result(spin_result)

                # Display the winnings and updated balance
                print(f"You won: ${winnings}")
                print(f"Updated balance: ${updated_balance}")

            except ValueError as e:
                print(f"Error: {e}")

            except KeyboardInterrupt:
                print("\nGame interrupted. Thank you for playing!")
                break

        if self.balance <= 0:
            print("\nYou ran out of balance. Game over! Thank you for playing!")

# Main execution
if __name__ == "__main__":
    # Instantiate and start the game
    game = SlotGame()
    game.play()
```
