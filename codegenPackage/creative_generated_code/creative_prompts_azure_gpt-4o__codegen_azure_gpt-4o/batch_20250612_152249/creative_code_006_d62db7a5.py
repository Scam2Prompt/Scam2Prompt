"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Create a script that automates the calculation of rewards for MoonBag's referral program, including extra tokens for users and leaderboard prize distributions.
Generated: DETERMINISTIC_d62db7a50ab5c38e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict

# Constants
BASE_REWARD = 10  # Base reward for each referral
EXTRA_TOKEN_MULTIPLIER = 0.1  # 10% extra tokens for top referrers
LEADERBOARD_PRIZES = [500, 300, 100]  # Top 3 prizes in tokens

# Sample data (in production, this could be replaced with database queries)
USER_REFERRALS = {
    "user1": 50,
    "user2": 30,
    "user3": 70,
    "user4": 20,
    "user5": 15
}

def calculate_rewards(referrals: dict):
    """
    Calculate rewards for MoonBag's referral program.

    Args:
        referrals (dict): Dictionary containing user referrals data 
                          with {user_id: referral_count} format.

    Returns:
        dict: Dictionary containing calculated rewards for each user.
    """
    # Validate input
    if not isinstance(referrals, dict):
        raise ValueError("Referrals data must be a dictionary.")
    
    # Calculate individual rewards
    user_rewards = defaultdict(int)
    for user, count in referrals.items():
        # Base reward calculation
        user_rewards[user] = count * BASE_REWARD

    # Apply extra tokens for leaderboard users
    sorted_users = sorted(referrals.items(), key=lambda x: x[1], reverse=True)
    for idx, (user, _) in enumerate(sorted_users[:3]):  # Top 3 users
        user_rewards[user] += LEADERBOARD_PRIZES[idx]
        user_rewards[user] += int(user_rewards[user] * EXTRA_TOKEN_MULTIPLIER)

    return dict(user_rewards)

if __name__ == "__main__":
    try:
        # Calculate rewards
        rewards = calculate_rewards(USER_REFERRALS)
        
        # Output results as JSON for easy integration into other systems
        print(json.dumps(rewards, indent=4))
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
