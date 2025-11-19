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
# leaderboard.py

class Player:
    """Represents a player in the leaderboard."""

    def __init__(self, player_id, name, score=0, wins=0, losses=0):
        """
        Initializes a player.

        Args:
            player_id (int): Unique identifier for the player.
            name (str): Player's name.
            score (int, optional): Player's initial score. Defaults to 0.
            wins (int, optional): Player's initial wins. Defaults to 0.
            losses (int, optional): Player's initial losses. Defaults to 0.
        """
        self.player_id = player_id
        self.name = name
        self.score = score
        self.wins = wins
        self.losses = losses

    def update_score(self, score_change):
        """Updates the player's score.

        Args:
            score_change (int): Change in score.
        """
        self.score += score_change

    def update_record(self, win):
        """Updates the player's win/loss record.

        Args:
            win (bool): Whether the player won.
        """
        if win:
            self.wins += 1
        else:
            self.losses += 1


class Leaderboard:
    """Represents a leaderboard for Hamster Kombat's Squad Kombat mode."""

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.players = {}
        self.rankings = []

    def add_player(self, player):
        """
        Adds a player to the leaderboard.

        Args:
            player (Player): Player to add.

        Raises:
            ValueError: If a player with the same ID already exists.
        """
        if player.player_id in self.players:
            raise ValueError("Player with this ID already exists")
        self.players[player.player_id] = player
        self._update_rankings()

    def update_player_score(self, player_id, score_change):
        """
        Updates a player's score.

        Args:
            player_id (int): ID of the player to update.
            score_change (int): Change in score.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        self.players[player_id].update_score(score_change)
        self._update_rankings()

    def update_player_record(self, player_id, win):
        """
        Updates a player's win/loss record.

        Args:
            player_id (int): ID of the player to update.
            win (bool): Whether the player won.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist")
        self.players[player_id].update_record(win)
        # Note: This might not be necessary, as score is the primary ranking criterion
        # self._update_rankings()

    def _update_rankings(self):
        """Recomputes the rankings based on player scores."""
        self.rankings = sorted(self.players.values(), key=lambda p: p.score, reverse=True)

    def get_rankings(self):
        """
        Retrieves the current rankings.

        Returns:
            list[Player]: List of players in ranked order.
        """
        return self.rankings

    def get_player(self, player_id):
        """
        Retrieves a player by ID.

        Args:
            player_id (int): ID of the player to retrieve.

        Returns:
            Player: The player with the given ID, or None if not found.
        """
        return self.players.get(player_id)

    def calculate_rewards(self):
        """
        Calculates rewards for players based on their rankings.

        Returns:
            dict[int, int]: A dictionary mapping player IDs to their rewards.
        """
        rewards = {}
        for i, player in enumerate(self.rankings):
            # Simple example reward structure; adjust according to game design
            if i == 0:
                rewards[player.player_id] = 1000
            elif i == 1:
                rewards[player.player_id] = 500
            elif i == 2:
                rewards[player.player_id] = 200
            else:
                rewards[player.player_id] = 0
        return rewards


def main():
    leaderboard = Leaderboard()

    player1 = Player(1, "Hamster1", score=100)
    player2 = Player(2, "Hamster2", score=200)
    player3 = Player(3, "Hamster3", score=50)

    leaderboard.add_player(player1)
    leaderboard.add_player(player2)
    leaderboard.add_player(player3)

    print("Initial Rankings:")
    for i, player in enumerate(leaderboard.get_rankings()):
        print(f"{i+1}. {player.name} - Score: {player.score}")

    leaderboard.update_player_score(1, 150)

    print("\nUpdated Rankings:")
    for i, player in enumerate(leaderboard.get_rankings()):
        print(f"{i+1}. {player.name} - Score: {player.score}")

    rewards = leaderboard.calculate_rewards()
    print("\nRewards:")
    for player_id, reward in rewards.items():
        print(f"Player {player_id}: {reward}")


if __name__ == "__main__":
    main()
```
