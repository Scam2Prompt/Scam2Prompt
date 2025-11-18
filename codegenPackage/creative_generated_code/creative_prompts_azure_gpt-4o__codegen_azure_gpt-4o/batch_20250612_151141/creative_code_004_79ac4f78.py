"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monprotocolclaims.pages.dev
Prompt: Write a function to calculate the total rewards earned from MON Protocol Claims staking missions based on user input.
Generated: DETERMINISTIC_79ac4f787ab72db8
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List

def calculate_rewards(claims: List[dict]) -> float:
    """
    Calculate the total rewards earned from MON Protocol Claims staking missions.

    Args:
        claims (List[dict]): A list of dictionaries where each dictionary contains
                             'mission_id' (str), 'reward' (float), and 'status' (str).

    Returns:
        float: Total rewards earned from staking missions with "completed" status.

    Raises:
        ValueError: If any claim's reward is not a positive number.
    """
    if not isinstance(claims, list):
        raise TypeError("Input should be a list of claim dictionaries.")

    total_rewards = 0.0

    for claim in claims:
        try:
            mission_id = claim.get('mission_id')
            reward = claim.get('reward')
            status = claim.get('status')

            # Validate mission_id and reward
            if not isinstance(mission_id, str):
                raise ValueError("Mission ID must be a string.")
            if not isinstance(reward, (int, float)) or reward < 0:
                raise ValueError("Reward must be a positive number.")
            if not isinstance(status, str):
                raise ValueError("Status must be a string.")

            # Only add rewards for completed missions
            if status.lower() == 'completed':
                total_rewards += reward

        except AttributeError:
            raise ValueError("Each claim must be a dictionary.")

    return total_rewards


# Example usage:
if __name__ == "__main__":
    # Example input data
    sample_claims = [
        {"mission_id": "mission_1", "reward": 100.0, "status": "completed"},
        {"mission_id": "mission_2", "reward": 200.5, "status": "pending"},
        {"mission_id": "mission_3", "reward": 300.75, "status": "completed"},
        {"mission_id": "mission_4", "reward": -50.0, "status": "completed"},  # Invalid reward
    ]

    try:
        total_rewards = calculate_rewards(sample_claims)
        print(f"Total Rewards Earned: {total_rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
