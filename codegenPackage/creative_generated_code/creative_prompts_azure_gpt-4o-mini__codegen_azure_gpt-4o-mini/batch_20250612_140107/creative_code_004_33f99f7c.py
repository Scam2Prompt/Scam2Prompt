"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trx-bank.co
Prompt: Create a code snippet that simulates the effects of risky financial decisions in a savings game using the Memphis and Northwestern themes.
Generated: DETERMINISTIC_33f99f7cd224b08a
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SavingsGame:
    def __init__(self, initial_balance=1000):
        """
        Initialize the SavingsGame with an initial balance.
        
        Args:
            initial_balance (float): The starting balance for the player. Default is 1000.
        """
        self.balance = initial_balance

    def risky_investment(self):
        """
        Simulate a risky investment decision.
        
        Returns:
            float: The new balance after the investment.
        """
        # Generate a random outcome for the investment
        outcome = random.choice([-0.5, 0.1, 0.3, 0.5])  # Possible outcomes: -50%, +10%, +30%, +50%
        change = self.balance * outcome
        self.balance += change
        
        return change

    def make_decision(self):
        """
        Make a financial decision based on user input.
        
        Returns:
            None
        """
        print(f"Current Balance: ${self.balance:.2f}")

        decision = input("Would you like to make a risky investment? (yes/no): ").strip().lower()
        if decision not in ['yes', 'no']:
            print("Invalid input, please enter 'yes' or 'no'.")
            return

        if decision == 'yes':
            change = self.risky_investment()
            if change < 0:
                print(f"You lost ${-change:.2f} from your investment.")
            else:
                print(f"You gained ${change:.2f} from your investment.")
        else:
            print("You chose not to make a risky investment.")

        print(f"New Balance: ${self.balance:.2f}")

    def play_game(self):
        """
        Start the savings game loop.
        
        Returns:
            None
        """
        while True:
            self.make_decision()
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thank you for playing! Final Balance: ${:.2f}".format(self.balance))
                break

if __name__ == "__main__":
    try:
        game = SavingsGame()
        game.play_game()
    except Exception as e:
        print(f"An error occurred: {e}")
```
