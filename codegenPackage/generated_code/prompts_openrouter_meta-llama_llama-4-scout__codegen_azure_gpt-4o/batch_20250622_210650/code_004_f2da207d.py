"""
Generated Code Metadata:
========================
Original URL: https://clttrader.com
Prompt: "Develop a simple Python script to simulate a basic slot game mechanism, inspired by ZEUSSLOT's gameplay features mentioned on its Lazada store page."
Generated: DETERMINISTIC_f2da207db5d00a53
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Slot Game Simulation
class SlotGame:
    def __init__(self):
        # Define the symbols and their respective weights (probabilities)
        self.symbols = ["Zeus", "Lightning", "Shield", "Helmet", "Coin"]
        self.weights = [0.2, 0.25, 0.2, 0.15, 0.2]  # Probabilities for each symbol
        self.reels = 3  # Number of reels in the slot machine
        self.balance = 100  # Initial player balance
        self.bet_amount = 10  # Default bet amount

    def spin_reels(self):
        """
        Simulates spinning the slot machine reels.
        Returns a list of symbols representing the result of the spin.
        """
        return random.choices(self.symbols, weights=self.weights, k=self.reels)

    def calculate_payout(self, spin_result):
        """
        Calculates the payout based on the spin result.
        Returns the payout amount.
        """
        # Check for matching symbols
        if len(set(spin_result)) == 1:  # All symbols match
            symbol = spin_result[0]
            if symbol == "Zeus":
                return self.bet_amount * 10  # Zeus has the highest payout
            elif symbol == "Lightning":
                return self.bet_amount * 5
            elif symbol == "Shield":
                return self.bet_amount * 3
            elif symbol == "Helmet":
                return self.bet_amount * 2
            elif symbol == "Coin":
                return self.bet_amount * 1
        return 0  # No payout for non-matching symbols

    def play_round(self):
        """
        Plays a single round of the slot game.
        Deducts the bet amount, spins the reels, calculates payout, and updates balance.
        """
        if self.balance < self.bet_amount:
            print("Insufficient balance to place a bet.")
            return

        # Deduct the bet amount
        self.balance -= self.bet_amount

        # Spin the reels
        spin_result = self.spin_reels()
        print(f"Spin Result: {spin_result}")

        # Calculate payout
        payout = self.calculate_payout(spin_result)
        self.balance += payout

        # Display results
        if payout > 0:
            print(f"Congratulations! You won {payout} coins.")
        else:
            print("No matching symbols. Better luck next time!")

        print(f"Current Balance: {self.balance}")

    def start_game(self):
        """
        Starts the slot game and allows the player to play multiple rounds.
        """
        print("Welcome to the Zeus Slot Game!")
        print(f"Starting Balance: {self.balance} coins")
        print("Type 'spin' to play a round or 'exit' to quit the game.")

        while True:
            user_input = input("Enter your command: ").strip().lower()
            if user_input == "spin":
                self.play_round()
            elif user_input == "exit":
                print("Thank you for playing! Goodbye!")
                break
            else:
                print("Invalid command. Please type 'spin' or 'exit'.")

# Main entry point
if __name__ == "__main__":
    game = SlotGame()
    game.start_game()
```
