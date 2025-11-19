"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: Write a Python function that simulates a Togel HK game, allowing users to select numbers and check against winning combinations.
Generated: DETERMINISTIC_70672591b9b1a9a4
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def generate_winning_numbers():
    """
    Generate 6 unique random winning numbers between 1 and 49.
    
    Returns:
        list: A list of 6 unique random numbers.
    """
    return random.sample(range(1, 50), 6)

def get_user_numbers():
    """
    Get 6 unique numbers from the user.
    
    Returns:
        list: A list of 6 unique numbers selected by the user.
    """
    while True:
        try:
            user_numbers = [int(num) for num in input("Enter 6 numbers separated by space (1-49): ").split()]
            if len(user_numbers) != 6:
                print("Please enter 6 numbers.")
                continue
            if not all(1 <= num <= 49 for num in user_numbers):
                print("Numbers must be between 1 and 49.")
                continue
            if len(set(user_numbers)) != 6:
                print("Numbers must be unique.")
                continue
            return user_numbers
        except ValueError:
            print("Invalid input. Please enter numbers separated by space.")

def check_numbers(user_numbers, winning_numbers):
    """
    Check the user's numbers against the winning numbers.
    
    Args:
        user_numbers (list): The user's selected numbers.
        winning_numbers (list): The winning numbers.
    
    Returns:
        int: The number of matching numbers.
    """
    return len(set(user_numbers) & set(winning_numbers))

def play_togel_hk():
    """
    Simulate a Togel HK game.
    """
    print("Welcome to Togel HK game!")
    user_numbers = get_user_numbers()
    winning_numbers = generate_winning_numbers()
    print(f"\nYour numbers: {sorted(user_numbers)}")
    print(f"Winning numbers: {sorted(winning_numbers)}")
    matches = check_numbers(user_numbers, winning_numbers)
    print(f"\nYou matched {matches} numbers.")
    if matches == 6:
        print("Congratulations, you won!")
    elif matches == 5:
        print("You won a smaller prize!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_togel_hk()
```
