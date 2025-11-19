"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Develop a matchmaking system for a blockchain FPS game like ev.io, allowing players to create or join private parties and tournaments.
Generated: DETERMINISTIC_deba9777575c6570
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from typing import List, Dict, Optional

class Player:
    """Class representing a player in the matchmaking system."""
    
    def __init__(self, player_id: str, username: str):
        self.player_id = player_id
        self.username = username

class Party:
    """Class representing a party of players."""
    
    def __init__(self, party_id: str):
        self.party_id = party_id
        self.players: List[Player] = []
    
    def add_player(self, player: Player) -> None:
        """Add a player to the party."""
        if len(self.players) < 5:  # Assuming max 5 players per party
            self.players.append(player)
        else:
            raise ValueError("Party is full. Cannot add more players.")
    
    def remove_player(self, player_id: str) -> None:
        """Remove a player from the party."""
        self.players = [p for p in self.players if p.player_id != player_id]

class Tournament:
    """Class representing a tournament."""
    
    def __init__(self, tournament_id: str):
        self.tournament_id = tournament_id
        self.parties: List[Party] = []
    
    def add_party(self, party: Party) -> None:
        """Add a party to the tournament."""
        self.parties.append(party)

class MatchmakingSystem:
    """Class to manage matchmaking for players, parties, and tournaments."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.parties: Dict[str, Party] = {}
        self.tournaments: Dict[str, Tournament] = {}
    
    def register_player(self, username: str) -> Player:
        """Register a new player and return the Player object."""
        player_id = str(uuid.uuid4())
        player = Player(player_id, username)
        self.players[player_id] = player
        return player
    
    def create_party(self) -> Party:
        """Create a new party and return the Party object."""
        party_id = str(uuid.uuid4())
        party = Party(party_id)
        self.parties[party_id] = party
        return party
    
    def join_party(self, party_id: str, player_id: str) -> None:
        """Allow a player to join a specified party."""
        if party_id not in self.parties:
            raise ValueError("Party does not exist.")
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        
        party = self.parties[party_id]
        player = self.players[player_id]
        party.add_player(player)
    
    def leave_party(self, party_id: str, player_id: str) -> None:
        """Allow a player to leave a specified party."""
        if party_id not in self.parties:
            raise ValueError("Party does not exist.")
        
        party = self.parties[party_id]
        party.remove_player(player_id)
    
    def create_tournament(self) -> Tournament:
        """Create a new tournament and return the Tournament object."""
        tournament_id = str(uuid.uuid4())
        tournament = Tournament(tournament_id)
        self.tournaments[tournament_id] = tournament
        return tournament
    
    def add_party_to_tournament(self, tournament_id: str, party_id: str) -> None:
        """Add a party to a specified tournament."""
        if tournament_id not in self.tournaments:
            raise ValueError("Tournament does not exist.")
        if party_id not in self.parties:
            raise ValueError("Party does not exist.")
        
        tournament = self.tournaments[tournament_id]
        party = self.parties[party_id]
        tournament.add_party(party)

# Example usage
if __name__ == "__main__":
    matchmaking_system = MatchmakingSystem()
    
    # Register players
    player1 = matchmaking_system.register_player("PlayerOne")
    player2 = matchmaking_system.register_player("PlayerTwo")
    
    # Create a party
    party = matchmaking_system.create_party()
    
    # Players join the party
    matchmaking_system.join_party(party.party_id, player1.player_id)
    matchmaking_system.join_party(party.party_id, player2.player_id)
    
    # Create a tournament
    tournament = matchmaking_system.create_tournament()
    
    # Add party to tournament
    matchmaking_system.add_party_to_tournament(tournament.tournament_id, party.party_id)
    
    print("Matchmaking system initialized successfully.")
```
