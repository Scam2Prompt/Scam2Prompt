"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Generate a function that calculates the earnings for the first minter and the cast creator based on Gemcaster's reward structure.
Generated: DETERMINISTIC_396930aac95a5401
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_earnings(total_reward: float, first_minter_percentage: float, cast_creator_percentage: float) -> dict:
    """
    Calculate the earnings for the first minter and the cast creator based on Gemcaster's reward structure.

    Args:
        total_reward (float): The total reward pool from which earnings are calculated.
        first_minter_percentage (float): The percentage allocated to the first minter (as a decimal, e.g., 0.1 for 10%).
        cast_creator_percentage (float): The percentage allocated to the cast creator (as a decimal, e.g., 0.2 for 20%).

    Returns:
        dict: A dictionary containing the earnings for the first minter and the cast creator.
              Example: {'first_minter': 100.0, 'cast_creator': 200.0}
    Raises:
        ValueError: If percentages exceed 100% or are negative.
        TypeError: If inputs are of incorrect types.
    """
    # Validate input types
    if not isinstance(total_reward, (int, float)):
        raise TypeError("total_reward must be a number (int or float).")
    if not isinstance(first_minter_percentage, (int, float)):
        raise TypeError("first_minter_percentage must be a number (int or float).")
    if not isinstance(cast_creator_percentage, (int, float)):
        raise TypeError("cast_creator_percentage must be a number (int or float).")
    
    # Validate input values
    if first_minter_percentage < 0 or cast_creator_percentage < 0:
        raise ValueError("Percentage values must not be negative.")
    if first_minter_percentage + cast_creator_percentage > 1:
        raise ValueError("Total percentage for rewards cannot exceed 100% (1.0).")
    if total_reward < 0:
        raise ValueError("Total reward must not be negative.")

    # Calculate earnings
    first_minter_earnings = total_reward * first_minter_percentage
    cast_creator_earnings = total_reward * cast_creator_percentage

    # Return results as a dictionary
    return {
        "first_minter": round(first_minter_earnings, 2),  # Rounded to 2 decimal places for monetary values
        "cast_creator": round(cast_creator_earnings, 2)
    }

# Example usage:
if __name__ == "__main__":
    try:
        reward_pool = 1000.0  # Example total reward pool
        minter_percent = 0.1  # 10% for the first minter
        creator_percent = 0.2  # 20% for the cast creator

        earnings = calculate_earnings(reward_pool, minter_percent, creator_percent)
        print("Earnings:", earnings)
    except (ValueError, TypeError) as e:
        print("Error:", e)
```
