"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Provide a Python script to simulate gameplay for a table game offered by Pelangi189, including random win/loss outcomes and bonus triggers.
Generated: DETERMINISTIC_5e058d7be04595b3
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class TableGame:
    def __init__(self, player_name):
        """
        Initialize the TableGame with a player's name.
        
        :param player_name: str - The name of the player
        """
        self.player_name = player_name
        self.balance = 100  # Starting balance for the player
        self.bonus_triggered = False

    def play_round(self):
        """
        Simulate a single round of the game.
        
        :return: str - Outcome of the round
        """
        # Simulate win/loss outcome
        outcome = random.choice(['win', 'loss'])
        if outcome == 'win':
            winnings = random.randint(10, 50)  # Random winnings between 10 and 50
            self.balance += winnings
            result = f"{self.player_name} won {winnings}! New balance: {self.balance}"
        else:
            loss = random.randint(5, 30)  # Random loss between 5 and 30
            self.balance -= loss
            result = f"{self.player_name} lost {loss}. New balance: {self.balance}"

        # Check for bonus trigger
        self.check_bonus()

        return result

    def check_bonus(self):
        """
        Check if a bonus is triggered based on the current balance.
        If the balance is a multiple of 50, trigger a bonus.
        """
        if self.balance % 50 == 0 and self.balance > 0 and not self.bonus_triggered:
            bonus_amount = 20  # Fixed bonus amount
            self.balance += bonus_amount
            self.bonus_triggered = True
            print(f"Bonus triggered! {self.player_name} received an additional {bonus_amount}. New balance: {self.balance}")
        elif self.balance % 50 != 0:
            self.bonus_triggered = False  # Reset bonus trigger if not a multiple of 50

    def play_game(self, rounds):
        """
        Play a specified number of rounds of the game.
        
        :param rounds: int - Number of rounds to play
        """
        for round_number in range(1, rounds + 1):
            print(f"Round {round_number}:")
            outcome = self.play_round()
            print(outcome)
            time.sleep(1)  # Pause for a second between rounds

        print(f"Game over! Final balance for {self.player_name}: {self.balance}")

if __name__ == "__main__":
    try:
        player_name = input("Enter your name: ")
        game = TableGame(player_name)
        number_of_rounds = int(input("Enter the number of rounds you want to play: "))
        
        if number_of_rounds <= 0:
            raise ValueError("Number of rounds must be a positive integer.")
        
        game.play_game(number_of_rounds)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
