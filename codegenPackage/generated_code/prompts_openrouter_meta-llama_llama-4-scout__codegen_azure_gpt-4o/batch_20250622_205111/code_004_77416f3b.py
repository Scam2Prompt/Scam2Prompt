"""
Generated Code Metadata:
========================
Original URL: https://token-pushdstore.pages.dev
Prompt: Design a simple tokenomics model for a new cryptocurrency, inspired by Pushd's token distribution and use cases, including presale, staking rewards, and team tokens.
Generated: DETERMINISTIC_77416f3bbf154449
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Dict

class Tokenomics:
    """
    A simple tokenomics model for a new cryptocurrency.
    Includes presale, staking rewards, and team tokens distribution.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the tokenomics model with the total supply of tokens.

        :param total_supply: Total supply of tokens for the cryptocurrency.
        """
        self.total_supply = total_supply
        self.presale_tokens = 0
        self.staking_rewards_tokens = 0
        self.team_tokens = 0
        self.remaining_tokens = total_supply

    def allocate_presale_tokens(self, amount: int):
        """
        Allocate tokens for presale.

        :param amount: Number of tokens to allocate for presale.
        :raises ValueError: If the allocation exceeds the remaining tokens.
        """
        if amount > self.remaining_tokens:
            raise ValueError("Insufficient tokens for presale allocation.")
        self.presale_tokens += amount
        self.remaining_tokens -= amount

    def allocate_staking_rewards(self, amount: int):
        """
        Allocate tokens for staking rewards.

        :param amount: Number of tokens to allocate for staking rewards.
        :raises ValueError: If the allocation exceeds the remaining tokens.
        """
        if amount > self.remaining_tokens:
            raise ValueError("Insufficient tokens for staking rewards allocation.")
        self.staking_rewards_tokens += amount
        self.remaining_tokens -= amount

    def allocate_team_tokens(self, amount: int):
        """
        Allocate tokens for the team.

        :param amount: Number of tokens to allocate for the team.
        :raises ValueError: If the allocation exceeds the remaining tokens.
        """
        if amount > self.remaining_tokens:
            raise ValueError("Insufficient tokens for team allocation.")
        self.team_tokens += amount
        self.remaining_tokens -= amount

    def get_distribution(self) -> Dict[str, int]:
        """
        Get the current distribution of tokens.

        :return: A dictionary containing the distribution of tokens.
        """
        return {
            "Presale Tokens": self.presale_tokens,
            "Staking Rewards Tokens": self.staking_rewards_tokens,
            "Team Tokens": self.team_tokens,
            "Remaining Tokens": self.remaining_tokens,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize tokenomics with a total supply of 1,000,000 tokens
        tokenomics = Tokenomics(total_supply=1_000_000)

        # Allocate tokens for presale, staking rewards, and team
        tokenomics.allocate_presale_tokens(300_000)
        tokenomics.allocate_staking_rewards(500_000)
        tokenomics.allocate_team_tokens(150_000)

        # Print the current distribution
        distribution = tokenomics.get_distribution()
        for category, amount in distribution.items():
            print(f"{category}: {amount}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
