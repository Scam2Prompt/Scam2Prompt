"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Write code to implement a leaderboard system for a Play-to-Earn game, allowing users to track rankings and earn rewards, as described in Kangamoon's community engagement features.
Generated: DETERMINISTIC_1cf1a636b10c29c3
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Tuple
import heapq


class Leaderboard:
    """
    A class to implement a leaderboard system for a Play-to-Earn game.
    Tracks player rankings and allows rewards allocation.
    """

    def __init__(self):
        # Dictionary to store player scores: {player_id: score}
        self.scores = {}

    def add_score(self, player_id: str, score: int) -> None:
        """
        Add or update a player's score.

        :param player_id: Unique identifier for the player
        :param score: Score to be added to the player
        """
        if player_id in self.scores:
            self.scores[player_id] += score
        else:
            self.scores[player_id] = score

    def get_top_n_players(self, n: int) -> List[Tuple[str, int]]:
        """
        Get the top N players based on their scores.

        :param n: Number of top players to fetch
        :return: List of tuples containing (player_id, score) sorted by score descending
        """
        if n <= 0:
            return []

        # Use a min-heap to efficiently get the top N players
        top_players = heapq.nlargest(n, self.scores.items(), key=lambda x: x[1])
        return top_players

    def reset_player_score(self, player_id: str) -> None:
        """
        Reset a player's score to 0.

        :param player_id: Unique identifier for the player
        """
        if player_id in self.scores:
            self.scores[player_id] = 0

    def allocate_rewards(self, reward_thresholds: Dict[int, int]) -> Dict[str, int]:
        """
        Allocate rewards to players based on their rankings.

        :param reward_thresholds: A dictionary where keys are ranking positions
                                  and values are reward amounts (e.g., {1: 100, 2: 50})
        :return: A dictionary mapping player_id to earned rewards
        """
        rewards = {}
        # Get players sorted by score (highest first)
        sorted_players = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

        # Assign rewards based on ranking
        for rank, (player_id, _) in enumerate(sorted_players, start=1):
            if rank in reward_thresholds:
                rewards[player_id] = reward_thresholds[rank]

        return rewards


# Example Usage
if __name__ == "__main__":
    # Initialize the leaderboard
    leaderboard = Leaderboard()

    # Add scores for players
    leaderboard.add_score("player1", 150)
    leaderboard.add_score("player2", 200)
    leaderboard.add_score("player3", 100)

    # Fetch the top 2 players
    top_players = leaderboard.get_top_n_players(2)
    print("Top 2 Players:", top_players)

    # Allocate rewards based on ranking
    rewards = leaderboard.allocate_rewards({1: 100, 2: 50})
    print("Rewards Allocation:", rewards)

    # Reset a player's score
    leaderboard.reset_player_score("player2")
    print("Scores After Reset:", leaderboard.scores)
```
