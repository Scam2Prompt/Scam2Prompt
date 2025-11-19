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

def simulate_togel_hk(user_numbers):
    """
    Simulates a Togel HK game where users select numbers and check against winning combinations.

    Args:
        user_numbers (list): A list of integers representing the user's selected numbers (4 numbers).

    Returns:
        dict: A dictionary containing the winning numbers, user's numbers, and the result.
    """
    # Validate user input
    if not isinstance(user_numbers, list) or len(user_numbers) != 4:
        raise ValueError("You must provide a list of exactly 4 numbers.")
    if not all(isinstance(num, int) and 1 <= num <= 49 for num in user_numbers):
        raise ValueError("All numbers must be integers between 1 and 49.")

    # Generate 4 random winning numbers between 1 and 49
    winning_numbers = random.sample(range(1, 50), 4)

    # Check how many numbers match
    matches = set(user_numbers) & set(winning_numbers)

    # Prepare the result
    result = {
        "winning_numbers": winning_numbers,
        "user_numbers": user_numbers,
        "matches": len(matches),
        "matched_numbers": list(matches),
        "is_winner": len(matches) == 4  # User wins if all 4 numbers match
    }

    return result


# Example usage:
if __name__ == "__main__":
    try:
        # User selects 4 numbers
        user_selection = [5, 12, 23, 34]
        game_result = simulate_togel_hk(user_selection)

        # Display the result
        print("Winning Numbers:", game_result["winning_numbers"])
        print("Your Numbers:", game_result["user_numbers"])
        print("Matched Numbers:", game_result["matched_numbers"])
        print("Total Matches:", game_result["matches"])
        print("Congratulations, You Won!" if game_result["is_winner"] else "Better luck next time!")
    except ValueError as e:
        print(f"Error: {e}")
```
