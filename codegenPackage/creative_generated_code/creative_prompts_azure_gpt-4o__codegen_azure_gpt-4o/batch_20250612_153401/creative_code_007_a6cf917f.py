"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playgorund.pages.dev
Prompt: Write a function to calculate contribution levels based on Twitter engagement data and return corresponding $BEYOND rewards.
Generated: DETERMINISTIC_a6cf917fdfd39378
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_beyond_rewards(engagement_data):
    """
    Calculate $BEYOND rewards based on Twitter engagement data.

    Parameters:
    engagement_data (dict): A dictionary containing engagement metrics:
                            - 'likes': int
                            - 'retweets': int
                            - 'comments': int
                            - 'shares': int

    Returns:
    float: The calculated $BEYOND rewards.
    """
    # Define weights for each engagement metric
    WEIGHTS = {
        'likes': 0.1,      # Each like contributes 0.1 points
        'retweets': 0.5,   # Each retweet contributes 0.5 points
        'comments': 0.3,   # Each comment contributes 0.3 points
        'shares': 0.4      # Each share contributes 0.4 points
    }
    
    # Validate engagement_data
    if not isinstance(engagement_data, dict):
        raise ValueError("engagement_data must be a dictionary with engagement metrics.")
    
    for metric in WEIGHTS.keys():
        if metric not in engagement_data:
            raise KeyError(f"Missing required engagement metric: {metric}")
        if not isinstance(engagement_data[metric], int) or engagement_data[metric] < 0:
            raise ValueError(f"{metric} must be a non-negative integer.")
    
    # Calculate engagement score
    engagement_score = sum(
        engagement_data[metric] * WEIGHTS[metric] for metric in WEIGHTS
    )
    
    # Apply a reward scaling formula to convert score into $BEYOND rewards
    # Using logarithmic scaling to ensure diminishing returns for higher scores
    REWARD_MULTIPLIER = 10  # Multiplier to adjust reward scaling
    beyond_rewards = REWARD_MULTIPLIER * math.log1p(engagement_score)  # log1p(x) = log(1 + x)
    
    return round(beyond_rewards, 2)  # Round to 2 decimal places for reward precision


# Example usage:
if __name__ == '__main__':
    try:
        # Sample engagement data
        sample_data = {
            'likes': 120,
            'retweets': 30,
            'comments': 15,
            'shares': 20
        }

        # Calculate rewards
        rewards = calculate_beyond_rewards(sample_data)
        print(f"Calculated $BEYOND rewards: {rewards}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
