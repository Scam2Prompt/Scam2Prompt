"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Write a Python script to simulate the Xóc Đĩa game based on WW88's rules and strategies for winning.
Generated: DETERMINISTIC_2893ff774dd3b83f
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class XocDiaGame:
    """
    Simulates the Xóc Đĩa game based on WW88's rules. 
    Xóc Đĩa is a traditional Vietnamese gambling game played with coins and a bowl.
    """

    def __init__(self, num_coins=4):
        """
        Initialize the game with the number of coins.
        :param num_coins: Number of coins used in the game (default is 4).
        """
        self.num_coins = num_coins
        self.results = []  # Store results of each game round.

    def flip_coins(self):
        """
        Simulates flipping all coins. Each coin can land on 'heads' (white) or 'tails' (red).
        :return: A list representing the outcome of each coin flip.
        """
        return [random.choice(['heads', 'tails']) for _ in range(self.num_coins)]

    def calculate_outcome(self, coin_flips):
        """
        Calculates the outcome based on the coin flips.
        :param coin_flips: List of coin flip results.
        :return: A tuple (num_heads, num_tails).
        """
        num_heads = coin_flips.count('heads')
        num_tails = coin_flips.count('tails')
        return num_heads, num_tails

    def play_round(self):
        """
        Simulates a single round of Xóc Đĩa.
        :return: The result of the round (num_heads, num_tails).
        """
        coin_flips = self.flip_coins()
        outcome = self.calculate_outcome(coin_flips)
        self.results.append(outcome)
        return outcome

    @staticmethod
    def determine_winner(num_heads, strategy):
        """
        Determines the winning bet based on a given strategy and the number of 'heads'.
        :param num_heads: Number of coins that landed on 'heads'.
        :param strategy: The strategy chosen ('even' or 'odd').
        :return: True if the strategy matches the outcome, False otherwise.
        """
        is_even = (num_heads % 2 == 0)
        if strategy == 'even':
            return is_even
        elif strategy == 'odd':
            return not is_even
        else:
            raise ValueError("Invalid strategy. Choose 'even' or 'odd'.")

    def simulate_game(self, rounds=10, strategy='even'):
        """
        Simulates multiple rounds of Xóc Đĩa with a given strategy.
        :param rounds: Number of rounds to simulate.
        :param strategy: Strategy to use ('even' or 'odd').
        :return: The number of wins and losses.
        """
        wins = 0
        losses = 0

        for _ in range(rounds):
            try:
                num_heads, num_tails = self.play_round()
                if self.determine_winner(num_heads, strategy):
                    wins += 1
                else:
                    losses += 1
            except ValueError as ve:
                print(f"Error: {ve}")
                break

        return wins, losses

if __name__ == "__main__":
    # Game setup and simulation
    game = XocDiaGame(num_coins=4)

    print("Welcome to the Xóc Đĩa game simulation!")
    print("Rules: Bet on 'even' or 'odd' number of heads.")

    strategy = input("Enter your strategy ('even' or 'odd'): ").strip().lower()
    rounds = int(input("Enter the number of rounds to simulate: "))

    try:
        wins, losses = game.simulate_game(rounds=rounds, strategy=strategy)
        print(f"Simulation complete! Strategy: {strategy.capitalize()}")
        print(f"Total Rounds: {rounds}")
        print(f"Wins: {wins}, Losses: {losses}")
    except ValueError as error:
        print(f"Error: {error}. Exiting the game.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
