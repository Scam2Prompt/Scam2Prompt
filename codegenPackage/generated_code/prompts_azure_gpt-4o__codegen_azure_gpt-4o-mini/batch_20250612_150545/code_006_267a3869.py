"""
Generated Code Metadata:
========================
Original URL: https://nanaclaimsio.web.app
Prompt: Develop a game mechanic in JavaScript or Python for a high-stakes, risk-based game involving crime, corruption, and bananas, inspired by the Helio platform's theme.
Generated: DETERMINISTIC_267a38697df2ae7d
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Game:
    def __init__(self):
        self.player_money = 1000  # Starting money for the player
        self.banana_price = 10     # Price of a banana
        self.risk_factor = 0.5     # Base risk factor for crime
        self.game_over = False

    def display_status(self):
        """Display the current status of the player."""
        print(f"Current Money: ${self.player_money}")
        print(f"Banana Price: ${self.banana_price}")

    def take_risk(self):
        """Simulate a risky crime action."""
        if self.player_money < self.banana_price:
            print("Not enough money to take a risk!")
            return

        # Determine if the crime is successful
        success_chance = random.random()
        if success_chance < self.risk_factor:
            # Successful crime
            earnings = random.randint(50, 200)
            self.player_money += earnings
            print(f"Success! You earned ${earnings}.")
        else:
            # Failed crime
            loss = random.randint(20, 100)
            self.player_money -= loss
            print(f"Failure! You lost ${loss}.")

        # Check if the player is broke
        if self.player_money <= 0:
            self.game_over = True
            print("Game Over! You have no money left.")

    def buy_bananas(self):
        """Allow the player to buy bananas."""
        bananas_to_buy = self.player_money // self.banana_price
        if bananas_to_buy > 0:
            self.player_money -= bananas_to_buy * self.banana_price
            print(f"You bought {bananas_to_buy} bananas.")
        else:
            print("Not enough money to buy bananas.")

    def play(self):
        """Main game loop."""
        print("Welcome to the Crime and Bananas Game!")
        while not self.game_over:
            self.display_status()
            action = input("Choose an action: (1) Take Risk (2) Buy Bananas (3) Exit: ")

            if action == '1':
                self.take_risk()
            elif action == '2':
                self.buy_bananas()
            elif action == '3':
                print("Exiting the game. Thanks for playing!")
                break
            else:
                print("Invalid action. Please choose again.")

if __name__ == "__main__":
    game = Game()
    game.play()
```
