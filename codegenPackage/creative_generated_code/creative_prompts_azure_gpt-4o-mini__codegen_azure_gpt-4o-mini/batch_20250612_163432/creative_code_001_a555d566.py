"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pandas-dsp.pages.dev
Prompt: Write code to create a leaderboard system for tracking NFT Panda stakers and their rewards, inspired by the PandaVerse platform.
Generated: DETERMINISTIC_a555d5668dfc2eb1
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# leaderboard.py

from typing import Dict, List

class PandaStaker:
    """Class to represent a Panda staker and their rewards."""

    def __init__(self, username: str):
        self.username = username
        self.staked_amount = 0  # Amount of NFT Pandas staked
        self.rewards = 0        # Rewards earned

    def stake(self, amount: int) -> None:
        """Stake a specified amount of NFT Pandas."""
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        self.staked_amount += amount

    def claim_rewards(self, amount: int) -> None:
        """Claim a specified amount of rewards."""
        if amount < 0:
            raise ValueError("Claimed rewards must be non-negative.")
        if amount > self.rewards:
            raise ValueError("Cannot claim more rewards than earned.")
        self.rewards -= amount

    def add_rewards(self, amount: int) -> None:
        """Add rewards to the staker."""
        if amount <= 0:
            raise ValueError("Amount of rewards to add must be greater than zero.")
        self.rewards += amount


class Leaderboard:
    """Class to manage the leaderboard of Panda stakers."""

    def __init__(self):
        self.stakers: Dict[str, PandaStaker] = {}  # Dictionary of stakers by username

    def register_staker(self, username: str) -> None:
        """Register a new staker."""
        if username in self.stakers:
            raise ValueError("Staker with this username already exists.")
        self.stakers[username] = PandaStaker(username)

    def stake_nft(self, username: str, amount: int) -> None:
        """Allow a user to stake NFT Pandas."""
        if username not in self.stakers:
            raise ValueError("Staker not found.")
        self.stakers[username].stake(amount)

    def add_rewards(self, username: str, amount: int) -> None:
        """Add rewards to a staker's account."""
        if username not in self.stakers:
            raise ValueError("Staker not found.")
        self.stakers[username].add_rewards(amount)

    def claim_rewards(self, username: str, amount: int) -> None:
        """Allow a user to claim their rewards."""
        if username not in self.stakers:
            raise ValueError("Staker not found.")
        self.stakers[username].claim_rewards(amount)

    def get_leaderboard(self) -> List[Dict[str, int]]:
        """Retrieve the leaderboard sorted by rewards earned."""
        leaderboard = sorted(self.stakers.values(), key=lambda x: x.rewards, reverse=True)
        return [{"username": staker.username, "staked_amount": staker.staked_amount, "rewards": staker.rewards} for staker in leaderboard]


if __name__ == "__main__":
    # Example usage
    leaderboard = Leaderboard()

    # Register stakers
    leaderboard.register_staker("Alice")
    leaderboard.register_staker("Bob")

    # Staking NFT Pandas
    leaderboard.stake_nft("Alice", 5)
    leaderboard.stake_nft("Bob", 3)

    # Adding rewards
    leaderboard.add_rewards("Alice", 100)
    leaderboard.add_rewards("Bob", 50)

    # Claiming rewards
    leaderboard.claim_rewards("Alice", 30)

    # Display leaderboard
    print("Current Leaderboard:")
    for entry in leaderboard.get_leaderboard():
        print(entry)
```
