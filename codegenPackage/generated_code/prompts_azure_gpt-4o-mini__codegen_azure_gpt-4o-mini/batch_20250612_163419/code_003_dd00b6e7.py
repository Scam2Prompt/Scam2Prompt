"""
Generated Code Metadata:
========================
Original URL: https://nyanheroes-9f5.pages.dev
Prompt: Generate code to manage mission completions and reward distribution in a game environment like Nyan Heroes.
Generated: DETERMINISTIC_dd00b6e7c6969ddb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Mission:
    """Class representing a game mission."""

    def __init__(self, mission_id, description, reward):
        """
        Initialize a new mission.

        Args:
            mission_id (int): Unique identifier for the mission.
            description (str): Description of the mission.
            reward (int): Reward points for completing the mission.
        """
        self.mission_id = mission_id
        self.description = description
        self.reward = reward
        self.completed = False

    def complete_mission(self):
        """Mark the mission as completed."""
        if not self.completed:
            self.completed = True
            return self.reward
        else:
            raise ValueError("Mission already completed.")


class Player:
    """Class representing a player in the game."""

    def __init__(self, player_id, name):
        """
        Initialize a new player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Name of the player.
        """
        self.player_id = player_id
        self.name = name
        self.total_rewards = 0

    def add_reward(self, reward):
        """
        Add reward points to the player's total.

        Args:
            reward (int): Reward points to add.
        """
        if reward < 0:
            raise ValueError("Reward cannot be negative.")
        self.total_rewards += reward


class MissionManager:
    """Class to manage missions and reward distribution."""

    def __init__(self):
        """Initialize the mission manager with an empty mission list."""
        self.missions = {}

    def add_mission(self, mission):
        """
        Add a new mission to the manager.

        Args:
            mission (Mission): The mission to add.
        """
        if mission.mission_id in self.missions:
            raise ValueError("Mission ID already exists.")
        self.missions[mission.mission_id] = mission

    def complete_mission(self, player, mission_id):
        """
        Complete a mission for a player and distribute rewards.

        Args:
            player (Player): The player completing the mission.
            mission_id (int): The ID of the mission to complete.

        Raises:
            ValueError: If the mission is not found or already completed.
        """
        if mission_id not in self.missions:
            raise ValueError("Mission not found.")
        
        mission = self.missions[mission_id]
        reward = mission.complete_mission()
        player.add_reward(reward)
        print(f"Player {player.name} completed mission '{mission.description}' and earned {reward} points.")


# Example usage
if __name__ == "__main__":
    # Create a mission manager
    mission_manager = MissionManager()

    # Create missions
    mission1 = Mission(1, "Collect 10 coins", 100)
    mission2 = Mission(2, "Defeat the dragon", 500)

    # Add missions to the manager
    mission_manager.add_mission(mission1)
    mission_manager.add_mission(mission2)

    # Create a player
    player1 = Player(1, "NyanCat")

    # Complete missions and distribute rewards
    try:
        mission_manager.complete_mission(player1, 1)
        mission_manager.complete_mission(player1, 2)
    except ValueError as e:
        print(f"Error: {e}")

    # Display total rewards for the player
    print(f"Total rewards for {player1.name}: {player1.total_rewards}")
```
