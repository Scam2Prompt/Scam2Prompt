"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namestajnovidom.com
Prompt: Write a program to simulate small-scale betting games with quick results, inspired by the 미니게임 사이트 features outlined on the 토토플레이 webpage.
Generated: DETERMINISTIC_6037b528141cf46b
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class BettingGame:
    def __init__(self):
        # Initialize the player's balance
        self.balance = 100  # Starting balance
        self.games = ['Heads', 'Tails']  # Possible game outcomes

    def place_bet(self, amount, prediction):
        """
        Places a bet on the game outcome.
        
        :param amount: The amount to bet
        :param prediction: The player's prediction ('Heads' or 'Tails')
        :return: Result of the game
        """
        if amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance to place this bet.")
        if prediction not in self.games:
            raise ValueError("Invalid prediction. Choose 'Heads' or 'Tails'.")

        # Simulate game result
        result = random.choice(self.games)
        print(f"Game result: {result}")

        # Determine win or loss
        if prediction == result:
            self.balance += amount  # Win: add to balance
            print(f"You won! New balance: {self.balance}")
        else:
            self.balance -= amount  # Lose: subtract from balance
            print(f"You lost! New balance: {self.balance}")

        return result

    def display_balance(self):
        """Displays the current balance of the player."""
        print(f"Current balance: {self.balance}")

    def reset_game(self):
        """Resets the player's balance to the starting amount."""
        self.balance = 100
        print("Game reset. Starting balance has been restored to 100.")

def main():
    """Main function to run the betting game."""
    game = BettingGame()

    while True:
        game.display_balance()

        # Get user input for betting
        try:
            bet_amount = float(input("Enter your bet amount (or 0 to exit): "))
            if bet_amount == 0:
                print("Exiting the game. Thank you for playing!")
                break

            prediction = input("Predict the outcome (Heads/Tails): ").capitalize()
            game.place_bet(bet_amount, prediction)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # Add a brief pause before the next round
        time.sleep(1)

if __name__ == "__main__":
    main()
```
