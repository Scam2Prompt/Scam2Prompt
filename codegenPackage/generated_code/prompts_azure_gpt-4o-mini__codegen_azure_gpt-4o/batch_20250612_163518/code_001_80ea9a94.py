"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Write a Python script to create a multiplayer matchmaking system for a game similar to Moon Tropica.
Generated: DETERMINISTIC_80ea9a94d7ad38c7
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import uuid
from typing import List, Dict, Optional

class Player:
    """
    Represents a player in the matchmaking system.
    """
    def __init__(self, username: str, skill_level: int):
        self.id = str(uuid.uuid4())  # Unique identifier for the player
        self.username = username
        self.skill_level = skill_level  # Skill level of the player (e.g., 1-100)

    def __repr__(self):
        return f"Player(username={self.username}, skill_level={self.skill_level})"


class Match:
    """
    Represents a match between players.
    """
    def __init__(self, players: List[Player]):
        self.id = str(uuid.uuid4())  # Unique identifier for the match
        self.players = players

    def __repr__(self):
        return f"Match(id={self.id}, players={[player.username for player in self.players]})"


class MatchmakingSystem:
    """
    A matchmaking system for multiplayer games.
    """
    def __init__(self):
        self.waiting_players: List[Player] = []  # Players waiting for a match
        self.matches: List[Match] = []  # Active matches

    def add_player(self, player: Player):
        """
        Adds a player to the matchmaking queue.
        """
        self.waiting_players.append(player)
        print(f"Player {player.username} added to the queue.")

    def find_match(self, max_skill_difference: int = 10) -> Optional[Match]:
        """
        Attempts to find a match for players in the queue.
        Players are matched based on their skill level.
        :param max_skill_difference: Maximum allowed skill level difference between players in a match.
        :return: A Match object if a match is found, otherwise None.
        """
        if len(self.waiting_players) < 2:
            print("Not enough players to create a match.")
            return None

        # Sort players by skill level for easier matchmaking
        self.waiting_players.sort(key=lambda p: p.skill_level)

        for i in range(len(self.waiting_players) - 1):
            player1 = self.waiting_players[i]
            player2 = self.waiting_players[i + 1]

            # Check if the skill level difference is within the allowed range
            if abs(player1.skill_level - player2.skill_level) <= max_skill_difference:
                # Create a match and remove players from the queue
                match = Match(players=[player1, player2])
                self.matches.append(match)
                self.waiting_players.remove(player1)
                self.waiting_players.remove(player2)
                print(f"Match created: {match}")
                return match

        print("No suitable match found.")
        return None

    def list_active_matches(self) -> List[Match]:
        """
        Lists all active matches.
        :return: A list of Match objects.
        """
        return self.matches

    def remove_match(self, match_id: str):
        """
        Removes a match from the active matches list.
        :param match_id: The ID of the match to remove.
        """
        self.matches = [match for match in self.matches if match.id != match_id]
        print(f"Match {match_id} removed.")


# Example usage
if __name__ == "__main__":
    # Create the matchmaking system
    matchmaking_system = MatchmakingSystem()

    # Add players to the queue
    matchmaking_system.add_player(Player(username="Player1", skill_level=50))
    matchmaking_system.add_player(Player(username="Player2", skill_level=55))
    matchmaking_system.add_player(Player(username="Player3", skill_level=30))
    matchmaking_system.add_player(Player(username="Player4", skill_level=35))

    # Attempt to find matches
    matchmaking_system.find_match()
    matchmaking_system.find_match()

    # List active matches
    print("Active matches:", matchmaking_system.list_active_matches())

    # Remove a match
    if matchmaking_system.matches:
        matchmaking_system.remove_match(matchmaking_system.matches[0].id)

    # List active matches after removal
    print("Active matches after removal:", matchmaking_system.list_active_matches())
```
