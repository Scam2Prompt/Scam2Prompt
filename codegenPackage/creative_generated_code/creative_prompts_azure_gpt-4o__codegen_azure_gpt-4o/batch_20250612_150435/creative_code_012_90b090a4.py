"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Write a program to calculate the rewards for players participating in TG.Casino's seasonal airdrops based on their wagering activity.
Generated: DETERMINISTIC_90b090a420e136a6
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Player:
    """
    Represents a player in the TG.Casino system.
    """
    def __init__(self, player_id, total_wager):
        """
        Initializes a Player object.

        :param player_id: Unique identifier for the player.
        :param total_wager: Total amount the player has wagered.
        """
        self.player_id = player_id
        self.total_wager = total_wager
        self.reward = 0

    def calculate_reward(self, total_pool, global_wager):
        """
        Calculates the reward for the player based on their wagering activity.

        :param total_pool: Total reward pool for the airdrop.
        :param global_wager: Total wagering activity of all players.
        """
        if global_wager > 0:
            self.reward = (self.total_wager / global_wager) * total_pool
        else:
            self.reward = 0

    def to_dict(self):
        """
        Converts the player object to a dictionary for serialization.

        :return: Dictionary representation of the player object.
        """
        return {
            "player_id": self.player_id,
            "total_wager": self.total_wager,
            "reward": round(self.reward, 2)
        }


class AirdropCalculator:
    """
    Calculates rewards for TG.Casino seasonal airdrops.
    """
    def __init__(self, reward_pool):
        """
        Initializes an AirdropCalculator object.

        :param reward_pool: Total amount of rewards available for the airdrop.
        """
        self.reward_pool = reward_pool
        self.players = []

    def add_player(self, player_id, total_wager):
        """
        Adds a player to the airdrop pool.

        :param player_id: Unique identifier for the player.
        :param total_wager: Total amount the player has wagered.
        """
        if total_wager < 0:
            raise ValueError("Total wager cannot be negative.")
        self.players.append(Player(player_id, total_wager))

    def calculate_rewards(self):
        """
        Calculates rewards for all players based on their wagering activity.
        """
        global_wager = sum(player.total_wager for player in self.players)
        for player in self.players:
            player.calculate_reward(self.reward_pool, global_wager)

    def export_rewards(self, file_path="rewards.json"):
        """
        Exports the calculated rewards to a JSON file.

        :param file_path: Path to the file where rewards will be saved.
        """
        try:
            rewards_data = [player.to_dict() for player in self.players]
            with open(file_path, "w") as file:
                json.dump(rewards_data, file, indent=4)
        except Exception as e:
            print(f"Error exporting rewards: {e}")


# Example usage if this were a standalone script:
if __name__ == "__main__":
    try:
        reward_pool = 10000  # Total pool amount for rewards
        airdrop_calculator = AirdropCalculator(reward_pool)

        # Add players and their wagering activity
        airdrop_calculator.add_player("player1", 500)
        airdrop_calculator.add_player("player2", 1500)
        airdrop_calculator.add_player("player3", 1000)

        # Calculate rewards
        airdrop_calculator.calculate_rewards()

        # Export rewards to a file
        airdrop_calculator.export_rewards()

        print("Rewards calculation completed and exported to rewards.json.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
