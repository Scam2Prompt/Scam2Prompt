"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the cost of playing multiple games of foosball at Playland Kenya, considering both the 5-ball and 10-ball options.
Generated: DETERMINISTIC_dec7f42a7f795f76
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# foosball_cost_calculator.py

class FoosballGameCostCalculator:
    """
    A class to calculate the cost of playing foosball at Playland Kenya.
    This class supports both 5-ball and 10-ball game options.
    """

    # Pricing constants
    PRICE_PER_5_BALL = 100  # Price for 5-ball game
    PRICE_PER_10_BALL = 180  # Price for 10-ball game

    def __init__(self):
        """
        Initializes the FoosballGameCostCalculator instance.
        """
        self.total_cost = 0

    def calculate_cost(self, num_games: int, ball_type: str) -> float:
        """
        Calculate the total cost based on the number of games and ball type.

        Parameters:
        num_games (int): The number of games to be played.
        ball_type (str): Type of game ('5-ball' or '10-ball').

        Returns:
        float: Total cost for the specified number of games.

        Raises:
        ValueError: If the ball_type is not '5-ball' or '10-ball', or if num_games is less than 1.
        """
        if num_games < 1:
            raise ValueError("Number of games must be at least 1.")
        
        if ball_type not in ('5-ball', '10-ball'):
            raise ValueError("ball_type must be either '5-ball' or '10-ball'.")

        if ball_type == '5-ball':
            self.total_cost = num_games * self.PRICE_PER_5_BALL
        elif ball_type == '10-ball':
            self.total_cost = num_games * self.PRICE_PER_10_BALL

        return self.total_cost

def main():
    """
    Main function to run the Foosball Game Cost Calculator.
    """
    calculator = FoosballGameCostCalculator()

    try:
        num_games = int(input("Enter the number of games you want to play: "))
        ball_type = input("Enter the type of game ('5-ball' or '10-ball'): ")

        # Calculate the cost
        total_cost = calculator.calculate_cost(num_games, ball_type)
        print(f"Total cost for {num_games} games of {ball_type}: Ksh {total_cost}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
