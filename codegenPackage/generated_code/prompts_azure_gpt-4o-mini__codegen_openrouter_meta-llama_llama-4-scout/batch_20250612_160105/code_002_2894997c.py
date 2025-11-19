"""
Generated Code Metadata:
========================
Original URL: https://zkstacks.in
Prompt: Write a script that simulates a lottery draw based on the mechanics described on "dear lottery today."
Generated: DETERMINISTIC_2894997c38629aa8
Batch ID: 20250612_160105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_lottery_numbers():
    """
    Generates a set of lottery numbers based on the "Dear Lottery" mechanics.
    Typically, this involves 6 main numbers and 1 bonus ball.
    """
    # Generate 6 unique main numbers between 1 and 49
    main_numbers = random.sample(range(1, 50), 6)
    main_numbers.sort()  # Sort the numbers for consistency

    # Generate 1 bonus ball between 1 and 10
    bonus_ball = random.randint(1, 10)

    return main_numbers, bonus_ball

def print_lottery_numbers(main_numbers, bonus_ball):
    """
    Prints the lottery numbers in a readable format.
    """
    print("Main Numbers: ", main_numbers)
    print("Bonus Ball: ", bonus_ball)

def simulate_lottery_draw(num_draws=1):
    """
    Simulates multiple lottery draws.

    Args:
        num_draws (int): The number of draws to simulate.
    """
    for i in range(num_draws):
        print(f"Draw {i+1} Results:")
        main_numbers, bonus_ball = generate_lottery_numbers()
        print_lottery_numbers(main_numbers, bonus_ball)
        print()  # Empty line for readability

if __name__ == "__main__":
    try:
        num_draws = int(input("Enter the number of lottery draws to simulate: "))
        if num_draws <= 0:
            print("Please enter a positive integer.")
        else:
            simulate_lottery_draw(num_draws)
    except ValueError:
        print("Invalid input. Please enter an integer.")
```

```python
# Example usage:
# Run the script, enter the number of draws when prompted, and it will display the simulated lottery results.
```
