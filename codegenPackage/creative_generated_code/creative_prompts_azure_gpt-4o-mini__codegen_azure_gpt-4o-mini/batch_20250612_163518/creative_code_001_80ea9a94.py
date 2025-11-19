"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moontropica.pages.dev
Prompt: Write a Python script to create a multiplayer matchmaking system for a game similar to Moon Tropica.
Generated: DETERMINISTIC_80ea9a94d7ad38c7
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import socket
from typing import List, Dict, Tuple

class Player:
    """Represents a player in the matchmaking system."""
    def __init__(self, player_id: str, skill_level: int):
        self.player_id = player_id
        self.skill_level = skill_level

class MatchmakingSystem:
    """Handles matchmaking for players."""
    
    def __init__(self):
        self.players: List[Player] = []
        self.matches: List[List[Player]] = []

    def add_player(self, player_id: str, skill_level: int):
        """Adds a player to the matchmaking queue."""
        if self._is_player_in_queue(player_id):
            raise ValueError(f"Player {player_id} is already in the queue.")
        
        player = Player(player_id, skill_level)
        self.players.append(player)
        self._try_create_match(player)

    def _is_player_in_queue(self, player_id: str) -> bool:
        """Checks if a player is already in the matchmaking queue."""
        return any(player.player_id == player_id for player in self.players)

    def _try_create_match(self, new_player: Player):
        """Attempts to create a match with the new player."""
        potential_matches = [player for player in self.players if player != new_player]
        match = self._find_match(new_player, potential_matches)

        if match:
            self.players.remove(new_player)
            for player in match:
                self.players.remove(player)
            self.matches.append([new_player] + match)
            print(f"Match created: {[p.player_id for p in [new_player] + match]}")

    def _find_match(self, new_player: Player, potential_matches: List[Player]) -> List[Player]:
        """Finds a suitable match based on skill level."""
        skill_threshold = 10  # Define acceptable skill difference threshold
        matched_players = []
        
        for player in potential_matches:
            if abs(new_player.skill_level - player.skill_level) <= skill_threshold:
                matched_players.append(player)
                if len(matched_players) >= 3:  # Assume 4-player match
                    break

        return matched_players

    def get_matches(self) -> List[List[Player]]:
        """Returns the list of all created matches."""
        return self.matches

def main():
    """Main function to run the matchmaking system."""
    matchmaking_system = MatchmakingSystem()

    # Simulate adding players to the matchmaking queue
    player_data = [
        ("player1", 20),
        ("player2", 25),
        ("player3", 30),
        ("player4", 18),
        ("player5", 27),
        ("player6", 22),
    ]

    for player_id, skill_level in player_data:
        try:
            matchmaking_system.add_player(player_id, skill_level)
        except ValueError as e:
            print(e)

    # Output all matches created
    print("Final Matches:")
    for match in matchmaking_system.get_matches():
        print([player.player_id for player in match])

if __name__ == "__main__":
    main()
```
