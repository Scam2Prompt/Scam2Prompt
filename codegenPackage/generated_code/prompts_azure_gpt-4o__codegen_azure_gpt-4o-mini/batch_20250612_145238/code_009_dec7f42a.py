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

class FoosballCostCalculator:
    """
    A class to calculate the cost of playing foosball games at Playland Kenya.
    """

    def __init__(self, price_per_game_5_ball, price_per_game_10_ball):
        """
        Initializes the calculator with the prices for 5-ball and 10-ball games.

        :param price_per_game_5_ball: Price for a 5-ball game
        :param price_per_game_10_ball: Price for a 10-ball game
        """
        self.price_per_game_5_ball = price_per_game_5_ball
        self.price_per_game_10_ball = price_per_game_10_ball

    def calculate_cost(self, num_games_5_ball, num_games_10_ball):
        """
        Calculates the total cost for the given number of 5-ball and 10-ball games.

        :param num_games_5_ball: Number of 5-ball games played
        :param num_games_10_ball: Number of 10-ball games played
        :return: Total cost of the games
        :raises ValueError: If the number of games is negative
        """
        if num_games_5_ball < 0 or num_games_10_ball < 0:
            raise ValueError("Number of games cannot be negative.")

        total_cost = (num_games_5_ball * self.price_per_game_5_ball) + \
                     (num_games_10_ball * self.price_per_game_10_ball)
        return total_cost


def main():
    """
    Main function to execute the cost calculation for foosball games.
    """
    # Prices for the games
    price_per_game_5_ball = 100  # Example price for 5-ball game
    price_per_game_10_ball = 150  # Example price for 10-ball game

    # Create an instance of the calculator
    calculator = FoosballCostCalculator(price_per_game_5_ball, price_per_game_10_ball)

    # Input: Number of games played
    try:
        num_games_5_ball = int(input("Enter the number of 5-ball games played: "))
        num_games_10_ball = int(input("Enter the number of 10-ball games played: "))

        # Calculate total cost
        total_cost = calculator.calculate_cost(num_games_5_ball, num_games_10_ball)

        # Output: Display the total cost
        print(f"Total cost for playing {num_games_5_ball} 5-ball games and "
              f"{num_games_10_ball} 10-ball games is: Ksh {total_cost}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid integer values for the number of games.")


if __name__ == "__main__":
    main()
```
