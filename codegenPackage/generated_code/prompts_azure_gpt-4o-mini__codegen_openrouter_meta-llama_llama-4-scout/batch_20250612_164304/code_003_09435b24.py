"""
Generated Code Metadata:
========================
Original URL: https://bigtime-codes.pages.dev
Prompt: Generate a function that calculates the rewards from Prestige Portals based on completed challenges in Big Time.
Generated: DETERMINISTIC_09435b24c8a3c690
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class ChallengeType(str, Enum):
    """Enum for challenge types."""
    DAILY = "daily"
    WEEKLY = "weekly"
    SEASONAL = "seasonal"

class PrestigePortalRewards:
    """Calculates rewards from Prestige Portals based on completed challenges."""

    def __init__(self, challenge_rewards: Dict[ChallengeType, Dict[str, int]]):
        """
        Initializes PrestigePortalRewards with challenge rewards.

        Args:
        challenge_rewards (Dict[ChallengeType, Dict[str, int]]): 
            A dictionary of challenge types and their corresponding rewards.
        """
        self.challenge_rewards = challenge_rewards

    def calculate_rewards(self, completed_challenges: List[Dict[str, str]]) -> Dict[ChallengeType, int]:
        """
        Calculates rewards based on completed challenges.

        Args:
        completed_challenges (List[Dict[str, str]]): 
            A list of completed challenges with their types.

        Returns:
        Dict[ChallengeType, int]: A dictionary of challenge types and their total rewards.
        """
        rewards = {challenge_type: 0 for challenge_type in ChallengeType}

        for challenge in completed_challenges:
            try:
                challenge_type = ChallengeType(challenge["type"])
                reward = self.challenge_rewards[challenge_type].get(challenge["name"], 0)
                rewards[challenge_type] += reward
            except (KeyError, ValueError) as e:
                # Handle invalid challenge type or missing reward
                print(f"Error calculating reward for challenge {challenge}: {str(e)}")

        return rewards


def main():
    # Example usage
    challenge_rewards = {
        ChallengeType.DAILY: {"Daily Challenge 1": 100, "Daily Challenge 2": 200},
        ChallengeType.WEEKLY: {"Weekly Challenge 1": 500, "Weekly Challenge 2": 1000},
        ChallengeType.SEASONAL: {"Seasonal Challenge 1": 2000, "Seasonal Challenge 2": 5000},
    }

    completed_challenges = [
        {"name": "Daily Challenge 1", "type": "daily"},
        {"name": "Weekly Challenge 1", "type": "weekly"},
        {"name": "Seasonal Challenge 1", "type": "seasonal"},
        {"name": "Invalid Challenge", "type": "invalid"},  # Test error handling
    ]

    prestige_portal_rewards = PrestigePortalRewards(challenge_rewards)
    rewards = prestige_portal_rewards.calculate_rewards(completed_challenges)

    print("Rewards:")
    for challenge_type, reward in rewards.items():
        print(f"{challenge_type}: {reward}")


if __name__ == "__main__":
    main()
```
