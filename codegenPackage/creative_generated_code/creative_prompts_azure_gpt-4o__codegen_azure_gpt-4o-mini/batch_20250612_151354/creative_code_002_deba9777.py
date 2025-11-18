"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Develop a matchmaking system for a blockchain FPS game like ev.io, allowing players to create or join private parties and tournaments.
Generated: DETERMINISTIC_deba9777575c6570
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# matchmaking_system.py

import uuid
from typing import List, Dict, Optional

class Player:
    """Class representing a player in the matchmaking system."""
    
    def __init__(self, player_id: str, username: str):
        self.player_id = player_id
        self.username = username

class Party:
    """Class representing a party of players."""
    
    def __init__(self, party_id: str, host: Player):
        self.party_id = party_id
        self.host = host
        self.members: List[Player] = [host]

    def add_member(self, player: Player) -> None:
        """Add a player to the party."""
        if player not in self.members:
            self.members.append(player)
        else:
            raise ValueError(f"Player {player.username} is already in the party.")

    def remove_member(self, player: Player) -> None:
        """Remove a player from the party."""
        if player in self.members:
            self.members.remove(player)
        else:
            raise ValueError(f"Player {player.username} is not in the party.")

class Tournament:
    """Class representing a tournament."""
    
    def __init__(self, tournament_id: str):
        self.tournament_id = tournament_id
        self.parties: List[Party] = []

    def add_party(self, party: Party) -> None:
        """Add a party to the tournament."""
        if party not in self.parties:
            self.parties.append(party)
        else:
            raise ValueError(f"Party {party.party_id} is already in the tournament.")

class MatchmakingSystem:
    """Matchmaking system for managing parties and tournaments."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.parties: Dict[str, Party] = {}
        self.tournaments: Dict[str, Tournament] = {}

    def register_player(self, username: str) -> Player:
        """Register a new player and return their Player object."""
        player_id = str(uuid.uuid4())
        new_player = Player(player_id, username)
        self.players[player_id] = new_player
        return new_player

    def create_party(self, host: Player) -> Party:
        """Create a new party with a host player."""
        party_id = str(uuid.uuid4())
        party = Party(party_id, host)
        self.parties[party_id] = party
        return party

    def join_party(self, party_id: str, player: Player) -> None:
        """Allow a player to join an existing party."""
        if party_id in self.parties:
            self.parties[party_id].add_member(player)
        else:
            raise KeyError(f"Party with ID {party_id} does not exist.")

    def leave_party(self, party_id: str, player: Player) -> None:
        """Allow a player to leave a party."""
        if party_id in self.parties:
            self.parties[party_id].remove_member(player)
        else:
            raise KeyError(f"Party with ID {party_id} does not exist.")

    def create_tournament(self) -> Tournament:
        """Create a new tournament."""
        tournament_id = str(uuid.uuid4())
        tournament = Tournament(tournament_id)
        self.tournaments[tournament_id] = tournament
        return tournament

    def add_party_to_tournament(self, tournament_id: str, party: Party) -> None:
        """Add a party to a specified tournament."""
        if tournament_id in self.tournaments:
            self.tournaments[tournament_id].add_party(party)
        else:
            raise KeyError(f"Tournament with ID {tournament_id} does not exist.")

# Example usage (this should be removed or commented out in production)
if __name__ == "__main__":
    matchmaking_system = MatchmakingSystem()
    
    # Register players
    player1 = matchmaking_system.register_player("PlayerOne")
    player2 = matchmaking_system.register_player("PlayerTwo")
    
    # Create a party
    party = matchmaking_system.create_party(player1)
    
    # Join the party
    matchmaking_system.join_party(party.party_id, player2)

    # Create a tournament
    tournament = matchmaking_system.create_tournament()
    
    # Add party to tournament
    matchmaking_system.add_party_to_tournament(tournament.tournament_id, party)

    print(f"Tournament ID: {tournament.tournament_id} created with Party ID: {party.party_id}")
```
