"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-ie.web.app
Prompt: Create a function that calculates the potential rewards from participating in Kangamoon's weekly challenges based on user activity and engagement levels.
Generated: DETERMINISTIC_e31f2c1d0847bed8
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# kangamoon_rewards_calculator.py

def calculate_rewards(activity_level, engagement_score):
    """
    Calculates potential rewards for participating in Kangamoon's weekly challenges.

    Parameters:
        activity_level (int): A numeric value representing the user's activity level (1-10).
                              Higher values indicate greater activity.
        engagement_score (int): A numeric value representing the user's engagement score (1-100).
                                Higher scores indicate better engagement.

    Returns:
        float: The calculated reward based on user activity and engagement levels.

    Raises:
        ValueError: If activity_level is not between 1 and 10, or engagement_score is not between 1 and 100.
    """

    # Validate input ranges
    if not (1 <= activity_level <= 10):
        raise ValueError("activity_level must be between 1 and 10.")
    if not (1 <= engagement_score <= 100):
        raise ValueError("engagement_score must be between 1 and 100.")

    # Base reward multiplier
    BASE_REWARD_MULTIPLIER = 5.0

    # Weight factors for activity and engagement
    ACTIVITY_WEIGHT = 0.4
    ENGAGEMENT_WEIGHT = 0.6

    # Calculate weighted contributions
    activity_contribution = activity_level * ACTIVITY_WEIGHT
    engagement_contribution = engagement_score * ENGAGEMENT_WEIGHT

    # Final reward calculation
    total_reward = (activity_contribution + engagement_contribution) * BASE_REWARD_MULTIPLIER

    return round(total_reward, 2)  # Round to 2 decimal places for better readability


if __name__ == "__main__":
    # Example usage
    try:
        activity_level = int(input("Enter your activity level (1-10): "))
        engagement_score = int(input("Enter your engagement score (1-100): "))
        rewards = calculate_rewards(activity_level, engagement_score)
        print(f"Your potential rewards are: {rewards}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
