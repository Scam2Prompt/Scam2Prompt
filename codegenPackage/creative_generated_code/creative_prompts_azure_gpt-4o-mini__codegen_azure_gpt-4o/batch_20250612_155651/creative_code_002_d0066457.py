"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a.aciumreward.com
Prompt: Write a Python function to calculate user rewards based on points earned, inspired by Acium Reward's system.
Generated: DETERMINISTIC_d00664572ca5e137
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict

def calculate_rewards(points: int) -> Dict[str, float]:
    """
    Calculates user rewards based on points earned.

    Reward tiers:
    - Bronze: 0-999 points, reward rate 0.5%
    - Silver: 1000-4999 points, reward rate 1.0%
    - Gold: 5000+ points, reward rate 2.0%

    Args:
        points (int): The number of points earned by the user.

    Returns:
        Dict[str, float]: A dictionary containing:
            - tier: The reward tier (Bronze, Silver, Gold).
            - reward: The calculated reward based on points.
    """
    try:
        if points < 0:
            raise ValueError("Points cannot be negative.")

        # Determine reward tier and rate
        if points <= 999:
            tier = "Bronze"
            rate = 0.005  # 0.5%
        elif points <= 4999:
            tier = "Silver"
            rate = 0.01  # 1.0%
        else:
            tier = "Gold"
            rate = 0.02  # 2.0%

        # Calculate rewards
        reward = points * rate

        return {"tier": tier, "reward": reward}

    except TypeError:
        raise TypeError("Points must be an integer.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating rewards: {e}")

# Example usage:
# result = calculate_rewards(3500)
# print(result)  # Output: {'tier': 'Silver', 'reward': 35.0}
```
