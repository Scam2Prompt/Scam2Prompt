"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyanheroes-9f5.pages.dev
Prompt: Generate code to manage mission completions and reward distribution in a game environment like Nyan Heroes.
Generated: DETERMINISTIC_dd00b6e7c6969ddb
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MissionManager:
    """
    A class to manage mission completions and reward distribution
    in a game environment like Nyan Heroes.
    """

    def __init__(self):
        # Initialize with an empty list of missions.
        self.missions = []
        self.player_rewards = {}

    def add_mission(self, mission_id, mission_name, reward):
        """
        Add a new mission to the manager.
        
        :param mission_id: Unique identifier for the mission
        :param mission_name: Name of the mission
        :param reward: Reward associated with the mission
        """
        if mission_id in [mission['id'] for mission in self.missions]:
            raise ValueError(f"Mission ID {mission_id} already exists.")
        
        mission = {
            'id': mission_id,
            'name': mission_name,
            'reward': reward,
            'completed': False
        }
        self.missions.append(mission)

    def complete_mission(self, mission_id, player_id):
        """
        Mark a mission as completed and distribute rewards to the player.
        
        :param mission_id: Unique identifier for the mission
        :param player_id: Unique identifier for the player
        """
        mission = self.get_mission(mission_id)
        if mission is None:
            raise ValueError(f"Mission ID {mission_id} does not exist.")
        if mission['completed']:
            raise RuntimeError(f"Mission ID {mission_id} is already completed.")
        
        # Mark the mission as completed
        mission['completed'] = True

        # Distribute reward to the player
        if player_id not in self.player_rewards:
            self.player_rewards[player_id] = 0
        self.player_rewards[player_id] += mission['reward']

    def get_mission(self, mission_id):
        """
        Retrieve a mission by its ID.
        
        :param mission_id: Unique identifier for the mission
        :return: Mission details or None if not found
        """
        for mission in self.missions:
            if mission['id'] == mission_id:
                return mission
        return None

    def get_player_rewards(self, player_id):
        """
        Get total rewards for a specific player.
        
        :param player_id: Unique identifier for the player
        :return: Total rewards for the player
        """
        return self.player_rewards.get(player_id, 0)

    def reset_mission(self, mission_id):
        """
        Reset a completed mission back to its initial state.
        
        :param mission_id: Unique identifier for the mission
        """
        mission = self.get_mission(mission_id)
        if mission is None:
            raise ValueError(f"Mission ID {mission_id} does not exist.")
        
        mission['completed'] = False

# Example usage:
if __name__ == "__main__":
    manager = MissionManager()
    try:
        # Adding missions
        manager.add_mission(1, "Collect 10 Nyan Coins", 100)
        manager.add_mission(2, "Defeat the Cat Boss", 250)

        # Completing missions
        manager.complete_mission(1, "player1")
        print(f"Player 1 Rewards: {manager.get_player_rewards('player1')}")  # Output: 100

        # Attempting to complete a mission that is already completed
        # manager.complete_mission(1, "player1")  # Uncomment to see error

        # Resetting a mission
        manager.reset_mission(1)
        manager.complete_mission(1, "player1")
        print(f"Player 1 Rewards after reset: {manager.get_player_rewards('player1')}")  # Output: 200

    except Exception as e:
        print(f"Error: {e}")
```
