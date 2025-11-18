"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Generate code for a staking rewards system in a blockchain gaming platform, aligning with MetaLeagues' roadmap Phase 2 goals. Include functionality for calculating and distributing rewards based on player activity.
Generated: DETERMINISTIC_84eac013323324ea
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Staking Rewards System for a Blockchain Gaming Platform
# This code implements a basic staking rewards system that calculates and
# distributes rewards based on player activity.

class Player:
    def __init__(self, address):
        self.address = address
        self.staked_amount = 0.0
        self.activity_score = 0
        self.rewards = 0.0

    def stake(self, amount):
        """Stake an amount to earn rewards."""
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        self.staked_amount += amount
        print(f"{self.address} has staked {amount}. Total staked: {self.staked_amount}.")

    def update_activity_score(self, score):
        """Update the player's activity score."""
        if score < 0:
            raise ValueError("Activity score must be non-negative.")
        self.activity_score = score
        print(f"{self.address} activity score updated to {self.activity_score}.")

class StakingRewards:
    def __init__(self, reward_rate):
        self.reward_rate = reward_rate  # Reward rate per stake per score
        self.players = {}

    def add_player(self, player):
        """Add a player to the staking rewards system."""
        if player.address in self.players:
            raise ValueError("Player already exists in the rewards system.")
        self.players[player.address] = player
        print(f"Player {player.address} added to the rewards system.")

    def calculate_rewards(self):
        """Calculate rewards for all players based on their stake and activity score."""
        for player in self.players.values():
            if player.staked_amount > 0 and player.activity_score > 0:
                player.rewards = player.staked_amount * self.reward_rate * player.activity_score
                print(f"Calculated rewards for {player.address}: {player.rewards}.")
            else:
                player.rewards = 0
                print(f"No rewards for {player.address} due to insufficient stake or activity.")

    def distribute_rewards(self):
        """Distribute rewards to all players."""
        for player in self.players.values():
            if player.rewards > 0:
                print(f"Distributing {player.rewards} to {player.address}.")
                # Placeholder for actual distribution logic (e.g., transfer tokens)
                # transfer_tokens(player.address, player.rewards)
                player.rewards = 0  # Reset rewards after distribution
                print(f"Rewards distributed for {player.address}. Current rewards reset to {player.rewards}.")
            else:
                print(f"No rewards to distribute for {player.address}.")

# Example usage
if __name__ == "__main__":
    # Initialize the staking rewards system
    reward_system = StakingRewards(reward_rate=0.01)

    # Create players
    player1 = Player(address="0xPlayer1")
    player2 = Player(address="0xPlayer2")

    # Add players to the system
    try:
        reward_system.add_player(player1)
        reward_system.add_player(player2)
    except ValueError as e:
        print(f"Error adding player: {e}")

    # Players stake and update activity scores
    try:
        player1.stake(100.0)
        player1.update_activity_score(10)
        player2.stake(50.0)
        player2.update_activity_score(5)
    except ValueError as e:
        print(f"Error updating player: {e}")

    # Calculate and distribute rewards
    reward_system.calculate_rewards()
    reward_system.distribute_rewards()
```
