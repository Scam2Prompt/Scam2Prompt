"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-illuvium.net
Prompt: Write code to implement a matchmaking system for multiplayer games, referencing the community features described on the 4399 gaming site.
Generated: DETERMINISTIC_0888c46105344eb1
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict, Tuple
from queue import PriorityQueue

# Define constants for the matchmaking system
MAX_WAIT_TIME = 30  # Maximum waiting time in seconds before matching players
SKILL_TOLERANCE = 100  # Allowable skill gap for matchmaking

# Class representing a player in the matchmaking system
class Player:
    def __init__(self, player_id: str, skill_level: int) -> None:
        self.player_id = player_id
        self.skill_level = skill_level
        self.queue_time = time.time()  # Time when the player joined the queue

    def __repr__(self) -> str:
        return f"Player({self.player_id}, Skill: {self.skill_level})"

# Class representing the matchmaking system
class MatchmakingSystem:
    def __init__(self) -> None:
        self.waiting_queue = PriorityQueue()  # Queue to hold players waiting for a match
        self.matches: List[Tuple[Player, Player]] = []  # List of matched pairs

    def add_player_to_queue(self, player: Player) -> None:
        """
        Adds a player to the matchmaking queue.
        """
        self.waiting_queue.put((player.skill_level, player))
        print(f"Player {player.player_id} added to the matchmaking queue.")

    def match_players(self) -> None:
        """
        Attempts to match players based on skill level and queue time.
        """
        while not self.waiting_queue.empty():
            try:
                _, player1 = self.waiting_queue.get()  # Get the first player
                if self.waiting_queue.empty():
                    # No other players to match with
                    self.waiting_queue.put((player1.skill_level, player1))
                    break
                
                _, player2 = self.waiting_queue.get()  # Get the second player

                # Check if skill levels are within acceptable range
                if abs(player1.skill_level - player2.skill_level) <= SKILL_TOLERANCE:
                    self.matches.append((player1, player2))
                    print(f"Matched {player1.player_id} with {player2.player_id}.")
                else:
                    # Return player2 to queue if mismatch
                    self.waiting_queue.put((player2.skill_level, player2))
                    self.waiting_queue.put((player1.skill_level, player1))
                    break
            except Exception as e:
                print(f"Error occurred during matching: {e}")

    def get_matches(self) -> List[Tuple[Player, Player]]:
        """
        Returns the list of matched players.
        """
        return self.matches


# Example usage
if __name__ == "__main__":
    # Initialize matchmaking system
    matchmaking_system = MatchmakingSystem()

    # Create players with random skill levels
    players = [
        Player("Player1", random.randint(800, 1200)),
        Player("Player2", random.randint(800, 1200)),
        Player("Player3", random.randint(800, 1200)),
        Player("Player4", random.randint(800, 1200)),
    ]

    # Add players to the matchmaking queue
    for player in players:
        matchmaking_system.add_player_to_queue(player)

    # Attempt to match players
    matchmaking_system.match_players()

    # Display matches
    print("Matches:")
    for match in matchmaking_system.get_matches():
        print(f"{match[0]} vs {match[1]}")
```
