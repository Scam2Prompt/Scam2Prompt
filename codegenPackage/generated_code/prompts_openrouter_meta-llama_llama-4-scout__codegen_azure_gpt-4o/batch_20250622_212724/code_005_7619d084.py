"""
Generated Code Metadata:
========================
Original URL: https://vempire-opal.vercel.app
Prompt: Develop a function to convert earned points to VEMP Tokens, considering the multipliers and challenges mentioned in the VEMP Hunt platform.
Generated: DETERMINISTIC_7619d0840341550e
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Union

# Define constants for multipliers
BASE_MULTIPLIER = 0.1  # Base multiplier for points to tokens conversion
CHALLENGE_MULTIPLIERS = {
    "easy": 1.0,  # Easy challenge multiplier
    "medium": 1.5,  # Medium challenge multiplier
    "hard": 2.0,  # Hard challenge multiplier
}

def convert_points_to_vemp(points: Union[int, float], challenge_level: str) -> Union[float, str]:
    """
    Converts earned points to VEMP Tokens based on challenge level multipliers.

    Args:
        points (Union[int, float]): The number of points earned by the user.
        challenge_level (str): The difficulty level of the challenge ("easy", "medium", "hard").

    Returns:
        Union[float, str]: The equivalent VEMP Tokens or an error message if inputs are invalid.
    """
    try:
        # Validate points input
        if not isinstance(points, (int, float)) or points < 0:
            return "Error: Points must be a non-negative number."

        # Validate challenge level input
        if challenge_level not in CHALLENGE_MULTIPLIERS:
            return "Error: Invalid challenge level. Choose from 'easy', 'medium', or 'hard'."

        # Calculate VEMP Tokens
        multiplier = CHALLENGE_MULTIPLIERS[challenge_level]
        vemp_tokens = points * BASE_MULTIPLIER * multiplier

        return round(vemp_tokens, 2)  # Return rounded value for better readability

    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # Test cases
    print(convert_points_to_vemp(100, "easy"))    # Expected output: 10.0
    print(convert_points_to_vemp(200, "medium"))  # Expected output: 30.0
    print(convert_points_to_vemp(300, "hard"))    # Expected output: 60.0
    print(convert_points_to_vemp(-50, "easy"))    # Expected output: Error message
    print(convert_points_to_vemp(150, "invalid")) # Expected output: Error message
```
