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
# Import necessary libraries
import hashlib
import random
from typing import Dict, List, Union

# Define constants
MAX_PLAYERS_PER_PARTY = 10
MAX_PLAYERS_PER_TOURNAMENT = 100
DEFAULT_MATCHMAKING_TIMEOUT = 300  # seconds

# Error classes
class MatchmakingError(Exception):
    pass

class PartyFullError(MatchmakingError):
    pass

class TournamentFullError(MatchmakingError):
    pass

class PlayerNotFoundError(MatchmakingError):
    pass

class PartyNotFoundError(MatchmakingError):
    pass

class TournamentNotFoundError(MatchmakingError):
    pass

# Player class
class Player:
    def __init__(self, username: str, blockchain_id: str):
        self.username = username
        self.blockchain_id = blockchain_id

    def __repr__(self):
        return f"Player(username={self.username}, blockchain_id={self.blockchain_id})"

# Party class
class Party:
    def __init__(self, host: Player):
        self.party_id = self._generate_unique_id()
        self.host = host
        self.players = [host]

    def _generate_unique_id(self) -> str:
        return hashlib.sha256(f"{self.host.username}{random.random()}".encode('utf-8')).hexdigest()

    def add_player(self, player: Player):
        if len(self.players) >= MAX_PLAYERS_PER_PARTY:
            raise PartyFullError("Party is full.")
        self.players.append(player)

    def remove_player(self, player: Player):
        if player not in self.players:
            raise PlayerNotFoundError("Player not found in the party.")
        self.players.remove(player)

    def __repr__(self):
        return f"Party(party_id={self.party_id}, host={self.host}, players={self.players})"

# Tournament class
class Tournament:
    def __init__(self, organizer: Player):
        self.tournament_id = self._generate_unique_id()
        self.organizer = organizer
        self.players = [organizer]

    def _generate_unique_id(self) -> str:
        return hashlib.sha256(f"{self.organizer.username}{random.random()}".encode('utf-8')).hexdigest()

    def add_player(self, player: Player):
        if len(self.players) >= MAX_PLAYERS_PER_TOURNAMENT:
            raise TournamentFullError("Tournament is full.")
        self.players.append(player)

    def remove_player(self, player: Player):
        if player not in self.players:
            raise PlayerNotFoundError("Player not found in the tournament.")
        self.players.remove(player)

    def __repr__(self):
        return f"Tournament(tournament_id={self.tournament_id}, organizer={self.organizer}, players={self.players})"

# Matchmaking system
class MatchmakingSystem:
    def __init__(self):
        self.parties: Dict[str, Party] = {}
        self.tournaments: Dict[str, Tournament] = {}

    def create_party(self, host: Player) -> Party:
        party = Party(host)
        self.parties[party.party_id] = party
        return party

    def join_party(self, party_id: str, player: Player):
        if party_id not in self.parties:
            raise PartyNotFoundError("Party not found.")
        party = self.parties[party_id]
        party.add_player(player)

    def leave_party(self, party_id: str, player: Player):
        if party_id not in self.parties:
            raise PartyNotFoundError("Party not found.")
        party = self.parties[party_id]
        party.remove_player(player)

    def create_tournament(self, organizer: Player) -> Tournament:
        tournament = Tournament(organizer)
        self.tournaments[tournament.tournament_id] = tournament
        return tournament

    def join_tournament(self, tournament_id: str, player: Player):
        if tournament_id not in self.tournaments:
            raise TournamentNotFoundError("Tournament not found.")
        tournament = self.tournaments[tournament_id]
        tournament.add_player(player)

    def leave_tournament(self, tournament_id: str, player: Player):
        if tournament_id not in self.tournaments:
            raise TournamentNotFoundError("Tournament not found.")
        tournament = self.tournaments[tournament_id]
        tournament.remove_player(player)

    def __repr__(self):
        return f"MatchmakingSystem(parties={self.parties}, tournaments={self.tournaments})"

# Example usage
if __name__ == "__main__":
    try:
        system = MatchmakingSystem()

        # Create players
        alice = Player("Alice", "abc123")
        bob = Player("Bob", "def456")

        # Create a party and add players
        party = system.create_party(alice)
        print(f"Created party: {party}")

        system.join_party(party.party_id, bob)
        print(f"Party after Bob joined: {party}")

        # Create a tournament
        tournament = system.create_tournament(alice)
        print(f"Created tournament: {tournament}")

        system.join_tournament(tournament.tournament_id, bob)
        print(f"Tournament after Bob joined: {tournament}")

    except MatchmakingError as e:
        print(f"Error: {e}")
```
