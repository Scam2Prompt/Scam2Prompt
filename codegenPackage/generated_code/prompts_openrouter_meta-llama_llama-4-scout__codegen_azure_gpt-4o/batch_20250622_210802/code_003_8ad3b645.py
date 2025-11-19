"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: "How does Gemcaster implement creator rewards, and what is the role of Neynar in this process?"
Generated: DETERMINISTIC_8ad3b6452961ba6d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Gemcaster Creator Rewards System

This script implements a simplified version of Gemcaster's creator rewards system.
It demonstrates how creators are rewarded based on their contributions and the role
of Neynar in facilitating the reward distribution process.

Key Features:
- Reward calculation based on creator contributions.
- Neynar acts as the intermediary for reward distribution.
- Error handling for invalid inputs and edge cases.
"""

class Creator:
    """
    Represents a creator in the Gemcaster system.
    Attributes:
        name (str): The name of the creator.
        contribution_score (float): The score representing the creator's contributions.
    """
    def __init__(self, name: str, contribution_score: float):
        if not name or contribution_score < 0:
            raise ValueError("Invalid creator data: Name must be non-empty and contribution score must be non-negative.")
        self.name = name
        self.contribution_score = contribution_score


class Neynar:
    """
    Represents Neynar, the intermediary responsible for reward distribution.
    Attributes:
        reward_pool (float): The total reward pool available for distribution.
    """
    def __init__(self, reward_pool: float):
        if reward_pool < 0:
            raise ValueError("Reward pool must be non-negative.")
        self.reward_pool = reward_pool

    def distribute_rewards(self, creators: list[Creator]) -> dict[str, float]:
        """
        Distributes rewards to creators based on their contribution scores.
        Args:
            creators (list[Creator]): A list of Creator objects.
        Returns:
            dict[str, float]: A dictionary mapping creator names to their rewards.
        """
        if not creators:
            raise ValueError("Creators list cannot be empty.")

        total_contribution = sum(creator.contribution_score for creator in creators)
        if total_contribution == 0:
            raise ValueError("Total contribution score cannot be zero.")

        rewards = {}
        for creator in creators:
            # Calculate reward as a proportion of the total contribution score
            reward = (creator.contribution_score / total_contribution) * self.reward_pool
            rewards[creator.name] = round(reward, 2)  # Round to 2 decimal places for clarity

        return rewards


def main():
    """
    Main function to demonstrate the Gemcaster creator rewards system.
    """
    try:
        # Example creators
        creators = [
            Creator(name="Alice", contribution_score=120.5),
            Creator(name="Bob", contribution_score=80.0),
            Creator(name="Charlie", contribution_score=50.0)
        ]

        # Neynar's reward pool
        neynar = Neynar(reward_pool=1000.0)

        # Distribute rewards
        rewards = neynar.distribute_rewards(creators)

        # Display results
        print("Creator Rewards Distribution:")
        for creator_name, reward in rewards.items():
            print(f"{creator_name}: ${reward}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
