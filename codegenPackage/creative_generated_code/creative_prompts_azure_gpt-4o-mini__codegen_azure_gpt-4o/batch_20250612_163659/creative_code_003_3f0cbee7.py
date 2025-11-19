"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartnetrewardls.pages.dev
Prompt: Generate a function that calculates the total value of tokens a user can claim based on their activity, inspired by the rewards structure on the SmartNet Rewards page.
Generated: DETERMINISTIC_3f0cbee73326b0c7
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

# Define a function to calculate the total reward value based on user activity
def calculate_reward(tokens: List[Dict[str, float]]) -> float:
    """
    Calculates the total reward tokens a user can claim based on activity.

    Args:
        tokens (List[Dict[str, float]]): A list of dictionaries where each dictionary 
                                         represents a reward activity. Each dictionary 
                                         contains:
                                         - 'activity_points' (float): The points earned for an activity.
                                         - 'conversion_rate' (float): The rate at which points are converted to tokens.

    Returns:
        float: The total value of tokens the user can claim.

    Raises:
        ValueError: If the input data structure is invalid or contains negative values.
    """

    # Input validation
    if not isinstance(tokens, list) or not all(isinstance(token, dict) for token in tokens):
        raise ValueError("Invalid input: 'tokens' must be a list of dictionaries.")

    total_tokens = 0.0

    for token in tokens:
        # Validate each token dictionary's structure
        if 'activity_points' not in token or 'conversion_rate' not in token:
            raise ValueError("Invalid token dictionary: Missing required keys 'activity_points' or 'conversion_rate'.")

        activity_points = token.get('activity_points')
        conversion_rate = token.get('conversion_rate')

        # Validate data types and values
        if not isinstance(activity_points, (int, float)) or not isinstance(conversion_rate, (int, float)):
            raise ValueError("Invalid values: 'activity_points' and 'conversion_rate' must be numeric.")

        if activity_points < 0 or conversion_rate < 0:
            raise ValueError("Invalid values: 'activity_points' and 'conversion_rate' cannot be negative.")

        # Calculate tokens for this activity and add to the total
        total_tokens += activity_points * conversion_rate

    return total_tokens

# Example Usage
if __name__ == "__main__":
    # Example list of activity data
    activities = [
        {"activity_points": 100, "conversion_rate": 0.5},
        {"activity_points": 200, "conversion_rate": 0.75},
        {"activity_points": 50, "conversion_rate": 1.0}
    ]

    try:
        total = calculate_reward(activities)
        print(f"Total reward tokens: {total}")
    except ValueError as e:
        print(f"Error: {e}")
```
