"""
Generated Code Metadata:
========================
Original URL: https://hamster-k.com
Prompt: Write a code snippet to implement a leaderboard system for Hamster Kombat's Squad Kombat mode, tracking player rankings and rewards.
Generated: DETERMINISTIC_09ceb96a942c5a8c
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Player:
    """Class representing a player in the leaderboard."""
    
    def __init__(self, player_id, name):
        """
        Initialize a new player.

        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        self.player_id = player_id
        self.name = name
        self.score = 0

    def update_score(self, points):
        """
        Update the player's score.

        :param points: Points to add to the player's score
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.score += points


class Leaderboard:
    """Class to manage the leaderboard for Hamster Kombat's Squad Kombat mode."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.players = {}

    def add_player(self, player_id, name):
        """
        Add a new player to the leaderboard.

        :param player_id: Unique identifier for the player
        :param name: Name of the player
        """
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, name)

    def update_player_score(self, player_id, points):
        """
        Update the score of a player.

        :param player_id: Unique identifier for the player
        :param points: Points to add to the player's score
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        self.players[player_id].update_score(points)

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by score.

        :return: List of tuples containing player_id, name, and score
        """
        sorted_players = sorted(self.players.values(), key=lambda p: p.score, reverse=True)
        return [(player.player_id, player.name, player.score) for player in sorted_players]

    def get_rewards(self):
        """
        Get rewards for the top players.

        :return: List of tuples containing player_id, name, and reward
        """
        leaderboard = self.get_leaderboard()
        rewards = []
        for index, (player_id, name, score) in enumerate(leaderboard):
            if index == 0:
                rewards.append((player_id, name, "Gold Medal"))
            elif index == 1:
                rewards.append((player_id, name, "Silver Medal"))
            elif index == 2:
                rewards.append((player_id, name, "Bronze Medal"))
        return rewards


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding players
    leaderboard.add_player(1, "HamsterHero")
    leaderboard.add_player(2, "FurryFighter")
    leaderboard.add_player(3, "SqueakyWarrior")

    # Updating scores
    leaderboard.update_player_score(1, 150)
    leaderboard.update_player_score(2, 200)
    leaderboard.update_player_score(3, 100)

    # Displaying leaderboard
    print("Current Leaderboard:")
    for player in leaderboard.get_leaderboard():
        print(f"ID: {player[0]}, Name: {player[1]}, Score: {player[2]}")

    # Displaying rewards
    print("\nRewards:")
    for reward in leaderboard.get_rewards():
        print(f"ID: {reward[0]}, Name: {reward[1]}, Reward: {reward[2]}")
```
