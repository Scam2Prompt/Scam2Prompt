"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Using the tokenomics structure provided on the Dopawing website, write a Python function to calculate the bonus percentage for presale participants based on follower milestones (e.g., 100%, 150%, 200%).
Generated: DETERMINISTIC_59efe3b9ed4db836
Batch ID: 20250612_155037
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

def calculate_bonus_percentage(followers: int, milestones: Dict[int, int]) -> int:
    """
    Calculate the bonus percentage for presale participants based on follower milestones.

    Args:
        followers (int): The number of followers achieved.
        milestones (Dict[int, int]): A dictionary where keys are follower milestones 
                                     and values are bonus percentages.

    Returns:
        int: The bonus percentage based on the achieved followers. If no exact milestone
             is met, the closest lower milestone's bonus is applied. Default is 0 if no
             milestone is applicable.
    """
    try:
        # Validate input arguments
        if not isinstance(followers, int) or followers < 0:
            raise ValueError("Followers must be a non-negative integer.")
        if not isinstance(milestones, dict) or not all(isinstance(k, int) and isinstance(v, int) for k, v in milestones.items()):
            raise ValueError("Milestones must be a dictionary with integer keys and values.")

        # Sort milestones by follower count in ascending order
        sorted_milestones = sorted(milestones.items())

        # Initialize bonus percentage to 0
        bonus_percentage = 0

        # Determine the bonus percentage based on milestones
        for milestone, bonus in sorted_milestones:
            if followers >= milestone:
                bonus_percentage = bonus
            else:
                break

        return bonus_percentage

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {e}")
        return 0

# Example usage:
if __name__ == "__main__":
    # Define follower milestones and corresponding bonus percentages
    follower_milestones = {
        100: 100,  # 100 followers = 100% bonus
        150: 150,  # 150 followers = 150% bonus
        200: 200   # 200 followers = 200% bonus
    }

    followers_achieved = 175
    bonus = calculate_bonus_percentage(followers_achieved, follower_milestones)
    print(f"Bonus percentage for {followers_achieved} followers: {bonus}%")
```
