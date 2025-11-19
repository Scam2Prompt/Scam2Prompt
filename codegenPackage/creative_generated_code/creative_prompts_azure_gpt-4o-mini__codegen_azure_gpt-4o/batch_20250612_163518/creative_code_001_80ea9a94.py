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
import uuid
import threading
import time
from typing import List, Dict, Optional

# Constants
MAX_PLAYERS_PER_MATCH = 4  # Max number of players in a match
MAX_WAIT_TIME = 10         # Max wait time before creating a match, even if not full

class Player:
    """
    Represents a player in the matchmaking system.
    """
    def __init__(self, player_id: str, skill_level: int):
        self.player_id = player_id
        self.skill_level = skill_level


class Match:
    """
    Represents a match with multiple players.
    """
    def __init__(self, match_id: str, players: List[Player]):
        self.match_id = match_id
        self.players = players


class MatchmakingSystem:
    """
    Handles player queuing and matchmaking.
    """
    def __init__(self):
        self.player_queue: List[Player] = []  # Queue for players waiting for a match
        self.matches: List[Match] = []       # Completed matches
        self.lock = threading.Lock()         # Thread-safety for matchmaking operations

    def add_player_to_queue(self, player: Player):
        """
        Adds a player to the matchmaking queue.
        """
        with self.lock:
            self.player_queue.append(player)
            print(f"Player {player.player_id} added to the queue.")

    def create_match(self) -> Optional[Match]:
        """
        Creates a match if enough players are in the queue.
        """
        with self.lock:
            if len(self.player_queue) >= MAX_PLAYERS_PER_MATCH:
                players_for_match = self._get_players_for_match(MAX_PLAYERS_PER_MATCH)
                match_id = str(uuid.uuid4())
                match = Match(match_id, players_for_match)
                self.matches.append(match)
                print(f"Match {match_id} created with players: {[p.player_id for p in players_for_match]}")
                return match
        return None

    def _get_players_for_match(self, count: int) -> List[Player]:
        """
        Retrieves players from the queue for a match.
        """
        players_for_match = self.player_queue[:count]
        self.player_queue = self.player_queue[count:]  # Remove players from queue
        return players_for_match

    def start_matchmaking(self):
        """
        Continuously processes the player queue and creates matches.
        """
        def matchmaking_loop():
            while True:
                with self.lock:
                    if len(self.player_queue) >= MAX_PLAYERS_PER_MATCH:
                        self.create_match()  # Create match if enough players
                    elif len(self.player_queue) > 0:
                        # Check if players have been waiting too long
                        time_elapsed = MAX_WAIT_TIME  # Simulated wait time
                        if time_elapsed >= MAX_WAIT_TIME:
                            players_for_match = self._get_players_for_match(min(len(self.player_queue), MAX_PLAYERS_PER_MATCH))
                            match_id = str(uuid.uuid4())
                            match = Match(match_id, players_for_match)
                            self.matches.append(match)
                            print(f"Match {match_id} created with players (due to timeout): {[p.player_id for p in players_for_match]}")

                time.sleep(1)  # Avoid busy-waiting

        threading.Thread(target=matchmaking_loop, daemon=True).start()

    def get_matches(self) -> List[Dict]:
        """
        Returns all completed matches.
        """
        with self.lock:
            return [{'match_id': match.match_id, 'players': [player.player_id for player in match.players]} for match in self.matches]


# Example Usage
if __name__ == "__main__":
    # Create matchmaking system
    matchmaking_system = MatchmakingSystem()
    matchmaking_system.start_matchmaking()

    # Simulate adding players to queue
    for i in range(10):
        player = Player(player_id=str(uuid.uuid4()), skill_level=random.randint(1, 100))
        matchmaking_system.add_player_to_queue(player)
        time.sleep(random.uniform(0.5, 2))  # Simulate random arrival times

    # Wait for matches to be created
    time.sleep(15)

    # Retrieve and print matches
    matches = matchmaking_system.get_matches()
    print("Completed Matches:")
    for match in matches:
        print(match)
```
