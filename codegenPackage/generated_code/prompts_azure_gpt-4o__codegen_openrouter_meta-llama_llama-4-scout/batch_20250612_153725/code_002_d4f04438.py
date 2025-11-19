"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Create a Python function to calculate the probability of winning in different lottery markets (e.g., 4D, 6D, 7D) based on the rules described for Hondatoto's Japan Lottery Association system.
Generated: DETERMINISTIC_d4f0443884d3a922
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

def calculate_lottery_probability(draw_type, total_balls, selected_balls):
    """
    Calculate the probability of winning in a lottery.

    Args:
        draw_type (str): The type of lottery draw (e.g., 4D, 6D, 7D).
        total_balls (int): The total number of balls in the lottery.
        selected_balls (int): The number of balls selected by the player.

    Returns:
        float: The probability of winning.

    Raises:
        ValueError: If the total number of balls or selected balls is invalid.
    """
    if total_balls < selected_balls:
        raise ValueError("Total balls must be greater than or equal to selected balls")

    # Calculate the number of combinations
    combinations = math.comb(total_balls, selected_balls)

    # Calculate the probability of winning
    probability = 1 / combinations

    return probability


def generate_lottery_numbers(draw_type, total_balls):
    """
    Generate random lottery numbers.

    Args:
        draw_type (str): The type of lottery draw (e.g., 4D, 6D, 7D).
        total_balls (int): The total number of balls in the lottery.

    Returns:
        list: A list of random lottery numbers.

    Raises:
        ValueError: If the draw type is invalid.
    """
    try:
        selected_balls = int(draw_type[:-1])
        if selected_balls <= 0:
            raise ValueError("Invalid draw type")
    except ValueError:
        raise ValueError("Invalid draw type")

    # Generate random lottery numbers
    numbers = random.sample(range(1, total_balls + 1), selected_balls)

    return numbers


def main():
    # Define the lottery markets
    lottery_markets = {
        "4D": {"total_balls": 49, "selected_balls": 4},
        "6D": {"total_balls": 49, "selected_balls": 6},
        "7D": {"total_balls": 49, "selected_balls": 7},
    }

    # Calculate the probability of winning for each market
    for market, details in lottery_markets.items():
        total_balls = details["total_balls"]
        selected_balls = details["selected_balls"]
        probability = calculate_lottery_probability(market, total_balls, selected_balls)
        print(f"Market: {market}, Probability of winning: {probability:.2e}")

    # Generate random lottery numbers for each market
    for market, details in lottery_markets.items():
        total_balls = details["total_balls"]
        numbers = generate_lottery_numbers(market, total_balls)
        print(f"Market: {market}, Random numbers: {numbers}")


if __name__ == "__main__":
    main()
```
