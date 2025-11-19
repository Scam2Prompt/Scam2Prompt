"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://downtownspokanehotels.com
Prompt: Write a Python function that simulates a Togel HK game, allowing users to select numbers and check against winning combinations.
Generated: DETERMINISTIC_70672591b9b1a9a4
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_togel_hk(user_numbers):
    """
    Simulates a Togel HK game where users select numbers and check against winning combinations.

    Args:
        user_numbers (list of int): List of numbers (4 digits) selected by the user.

    Returns:
        dict: A dictionary containing the user's numbers, winning numbers, and result.
    """
    # Validate user input
    if not isinstance(user_numbers, list) or len(user_numbers) != 4:
        raise ValueError("User numbers must be a list of exactly 4 integers.")

    if not all(isinstance(num, int) and 0 <= num <= 9 for num in user_numbers):
        raise ValueError("Each number must be an integer between 0 and 9.")

    # Generate the winning numbers (4 random digits)
    winning_numbers = [random.randint(0, 9) for _ in range(4)]

    # Determine if the user has won
    result = {
        "Exact_Match": user_numbers == winning_numbers,
        "Partial_Match_Count": sum(1 for num in user_numbers if num in winning_numbers),
    }

    # Return game results
    return {
        "user_numbers": user_numbers,
        "winning_numbers": winning_numbers,
        "result": result
    }


# Example usage:
if __name__ == "__main__":
    try:
        # User selects 4 numbers (example input)
        user_selection = [1, 2, 3, 4]
        game_result = simulate_togel_hk(user_selection)

        # Display the result
        print("User Numbers:", game_result["user_numbers"])
        print("Winning Numbers:", game_result["winning_numbers"])
        print("Game Result:", game_result["result"])
    except Exception as e:
        print("Error:", e)
```
