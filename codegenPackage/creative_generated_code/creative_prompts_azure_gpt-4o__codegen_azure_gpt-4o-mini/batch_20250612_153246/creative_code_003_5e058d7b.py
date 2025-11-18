"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blogdotrabalhadordigital.com
Prompt: Provide a Python script to simulate gameplay for a table game offered by Pelangi189, including random win/loss outcomes and bonus triggers.
Generated: DETERMINISTIC_5e058d7be04595b3
Batch ID: 20250612_153246
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

class TableGame:
    """
    A class to simulate a table game offered by Pelangi189.
    """

    def __init__(self, player_name: str, starting_balance: float):
        """
        Initializes the TableGame with a player's name and starting balance.

        :param player_name: Name of the player.
        :param starting_balance: Starting balance for the player.
        """
        self.player_name = player_name
        self.balance = starting_balance
        self.rounds_played = 0

    def simulate_round(self) -> dict:
        """
        Simulates a single round of the game, returning the outcome.

        :return: A dictionary containing the outcome of the round.
        """
        outcome = random.choice(["win", "loss"])
        bonus_triggered = random.choice([True, False])
        winnings = 0

        # Determine winnings and balance based on the outcome
        if outcome == "win":
            winnings = random.uniform(10, 100)  # Random win amount
            self.balance += winnings
        else:
            loss = random.uniform(5, 50)  # Random loss amount
            self.balance -= loss

        # Ensure balance does not go negative
        self.balance = max(self.balance, 0)

        # Log round details
        self.rounds_played += 1
        return {
            "round": self.rounds_played,
            "outcome": outcome,
            "winnings": winnings,
            "balance": self.balance,
            "bonus_triggered": bonus_triggered
        }

    def play_game(self, total_rounds: int):
        """
        Plays a specified number of rounds of the game.

        :param total_rounds: Number of rounds to play.
        """
        for _ in range(total_rounds):
            result = self.simulate_round()
            self.display_result(result)
            time.sleep(1)  # Sleep to simulate time between rounds

    @staticmethod
    def display_result(result: dict):
        """
        Displays the result of a round.

        :param result: The result dictionary containing round details.
        """
        print(f"Round {result['round']}: You {result['outcome']}!")
        if result['outcome'] == 'win':
            print(f"You won: ${result['winnings']:.2f}")
        print(f"Current balance: ${result['balance']:.2f}")
        if result['bonus_triggered']:
            print("Bonus triggered! 🎉")
        print("-" * 30)

def main():
    """
    Main function to run the table game simulation.
    """
    try:
        player_name = input("Enter your name: ")
        starting_balance = float(input("Enter your starting balance: $"))
        total_rounds = int(input("Enter the number of rounds to play: "))

        # Validate input
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        if total_rounds <= 0:
            raise ValueError("Number of rounds must be a positive integer.")

        game = TableGame(player_name, starting_balance)
        game.play_game(total_rounds)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
