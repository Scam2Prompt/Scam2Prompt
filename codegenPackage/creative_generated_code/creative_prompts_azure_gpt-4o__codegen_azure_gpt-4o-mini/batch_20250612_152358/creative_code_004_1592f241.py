"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Write a function to calculate token rewards allocation (2% of total supply) for $PLENA Quest participants based on their leaderboard ranking.
Generated: DETERMINISTIC_1592f241ff9dc45c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenRewardsAllocator:
    def __init__(self, total_supply: float):
        """
        Initialize the TokenRewardsAllocator with the total supply of tokens.
        
        :param total_supply: Total supply of tokens available for allocation.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.reward_pool = self.calculate_reward_pool()

    def calculate_reward_pool(self) -> float:
        """
        Calculate the total reward pool available for allocation (2% of total supply).
        
        :return: The calculated reward pool.
        """
        return self.total_supply * 0.02

    def allocate_rewards(self, leaderboard: list) -> dict:
        """
        Allocate token rewards to participants based on their leaderboard ranking.
        
        :param leaderboard: A list of tuples containing participant names and their ranks.
                           Example: [('Alice', 1), ('Bob', 2), ('Charlie', 3)]
        :return: A dictionary mapping participant names to their allocated rewards.
        """
        if not leaderboard or not isinstance(leaderboard, list):
            raise ValueError("Leaderboard must be a non-empty list.")

        # Calculate total ranks for distribution
        total_ranks = sum(rank for _, rank in leaderboard)
        rewards_distribution = {}

        for participant, rank in leaderboard:
            if rank <= 0:
                raise ValueError("Rank must be a positive integer.")
            # Calculate reward based on rank
            reward = (rank / total_ranks) * self.reward_pool
            rewards_distribution[participant] = reward

        return rewards_distribution


# Example usage
if __name__ == "__main__":
    try:
        total_supply = 1000000  # Example total supply
        allocator = TokenRewardsAllocator(total_supply)
        
        # Example leaderboard participants with their ranks
        leaderboard = [('Alice', 1), ('Bob', 2), ('Charlie', 3)]
        rewards = allocator.allocate_rewards(leaderboard)
        
        print("Token rewards allocation:", rewards)
    except Exception as e:
        print("Error:", str(e))
```
