"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the cost of playing multiple games of foosball at Playland Kenya, considering both the 5-ball and 10-ball options.
Generated: DETERMINISTIC_dec7f42a7f795f76
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# foosball_cost_calculator.py

class FoosballGame:
    """Represents a game of foosball with a specific ball option."""

    def __init__(self, ball_option):
        """
        Initializes a FoosballGame instance.

        Args:
            ball_option (str): The ball option, either '5-ball' or '10-ball'.

        Raises:
            ValueError: If the ball option is not '5-ball' or '10-ball'.
        """
        if ball_option not in ['5-ball', '10-ball']:
            raise ValueError("Invalid ball option. Must be '5-ball' or '10-ball'.")
        self.ball_option = ball_option

    def get_cost(self):
        """
        Gets the cost of the game based on the ball option.

        Returns:
            float: The cost of the game.
        """
        # Cost in KES
        costs = {
            '5-ball': 200,
            '10-ball': 400
        }
        return costs[self.ball_option]


class FoosballSession:
    """Represents a session of multiple foosball games."""

    def __init__(self):
        """Initializes a FoosballSession instance."""
        self.games = []

    def add_game(self, game):
        """
        Adds a game to the session.

        Args:
            game (FoosballGame): The game to add.
        """
        self.games.append(game)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the session.

        Returns:
            float: The total cost of the session.
        """
        return sum(game.get_cost() for game in self.games)


def main():
    try:
        session = FoosballSession()

        num_5_ball_games = int(input("Enter the number of 5-ball games: "))
        num_10_ball_games = int(input("Enter the number of 10-ball games: "))

        for _ in range(num_5_ball_games):
            session.add_game(FoosballGame('5-ball'))

        for _ in range(num_10_ball_games):
            session.add_game(FoosballGame('10-ball'))

        total_cost = session.calculate_total_cost()

        print(f"Total cost: KES {total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
