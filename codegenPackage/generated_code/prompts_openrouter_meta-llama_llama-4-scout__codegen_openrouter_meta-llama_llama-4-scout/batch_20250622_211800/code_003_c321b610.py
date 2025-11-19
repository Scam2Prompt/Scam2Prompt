"""
Generated Code Metadata:
========================
Original URL: https://zkstacks.in
Prompt: How can I implement a simple lottery number generator inspired by dear lottery today using Python?
Generated: DETERMINISTIC_c321b6107e1eef8e
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_lottery_numbers(num_balls: int = 6, max_ball: int = 49) -> list[int]:
    """
    Generates a list of unique random lottery numbers.

    Args:
    - num_balls (int): The number of balls to generate. Defaults to 6.
    - max_ball (int): The maximum ball number. Defaults to 49.

    Returns:
    - list[int]: A list of unique random lottery numbers.
    """
    # Check if num_balls is not more than max_ball
    if num_balls > max_ball:
        raise ValueError("num_balls cannot be more than max_ball")

    # Generate a list of unique random numbers
    try:
        numbers = random.sample(range(1, max_ball + 1), num_balls)
        numbers.sort()  # Sort the numbers for better readability
        return numbers
    except ValueError as e:
        # Handle the case where num_balls is more than max_ball
        print(f"Error: {e}")
        return []

def generate_powerball() -> tuple[list[int], int]:
    """
    Generates a Powerball lottery number.

    Returns:
    - tuple[list[int], int]: A tuple containing a list of 5 unique random numbers and a Powerball number.
    """
    try:
        numbers = random.sample(range(1, 70), 5)  # Generate 5 unique numbers between 1 and 69
        powerball = random.randint(1, 26)  # Generate a Powerball number between 1 and 26
        numbers.sort()  # Sort the numbers for better readability
        return numbers, powerball
    except Exception as e:
        # Handle any exceptions
        print(f"Error: {e}")
        return [], 0

def main():
    print("Dear Lottery Today Number Generator")
    print("-------------------------------------")

    while True:
        print("\nOptions:")
        print("1. Generate Lottery Numbers (6/49)")
        print("2. Generate Powerball Numbers")
        print("3. Quit")

        option = input("Choose an option: ")

        if option == "1":
            numbers = generate_lottery_numbers()
            if numbers:
                print(f"Your lottery numbers are: {numbers}")
        elif option == "2":
            numbers, powerball = generate_powerball()
            if numbers:
                print(f"Your Powerball numbers are: {numbers} - Powerball: {powerball}")
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
