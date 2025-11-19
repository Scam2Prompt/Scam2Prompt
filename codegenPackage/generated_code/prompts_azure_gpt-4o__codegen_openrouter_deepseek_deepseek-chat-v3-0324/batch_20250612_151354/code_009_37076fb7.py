"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Develop a tournament lobby system for a blockchain FPS game, referencing ev.io's ability to host minigames and tournaments.
Generated: DETERMINISTIC_37076fb7dafe6c05
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from typing import List, Dict, Optional
from enum import Enum
from dataclasses import dataclass
import hashlib
import uuid
from datetime import datetime, timedelta

# Blockchain interaction mock (would be replaced with actual blockchain calls)
class Blockchain:
    @staticmethod
    def verify_signature(player_id: str, signature: str) -> bool:
        """Mock verification of player's blockchain signature"""
        return True  # In production, would verify against blockchain

    @staticmethod
    def transfer_tokens(from_addr: str, to_addr: str, amount: float) -> bool:
        """Mock token transfer between addresses"""
        return True  # In production, would execute on blockchain

# Enums for tournament states and types
class TournamentState(Enum):
    REGISTRATION = "registration"
    COUNTDOWN = "countdown"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TournamentType(Enum):
    SOLO = "solo"
    TEAM = "team"
    BATTLE_ROYALE = "battle_royale"

class GameMode(Enum):
    DEATHMATCH = "deathmatch"
    CAPTURE_THE_FLAG = "capture_the_flag"
    KING_OF_THE_HILL = "king_of_the_hill"

# Data classes for tournament entities
@dataclass
class Player:
    id: str
    wallet_address: str
    username: str
    rating: int = 1000

@dataclass
class Team:
    id: str
    name: str
    members: List[Player]
    captain: Player

@dataclass
class TournamentConfig:
    entry_fee: float
    prize_pool: float
    max_players: int
    min_players: int = 2
    duration_minutes: int = 30
    game_mode: GameMode = GameMode.DEATHMATCH

@dataclass
class Tournament:
    id: str
    name: str
    tournament_type: TournamentType
    config: TournamentConfig
    state: TournamentState = TournamentState.REGISTRATION
    participants: List[Union[Player, Team]] = field(default_factory=list)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    winners: List[Union[Player, Team]] = field(default_factory=list)

# Main tournament lobby system
class TournamentLobby:
    def __init__(self):
        self.active_tournaments: Dict[str, Tournament] = {}
        self.pending_registrations: Dict[str, List[Dict]] = {}
        self.player_stats: Dict[str, Dict] = {}  # Would be populated from game data

    def create_tournament(
        self,
        name: str,
        tournament_type: TournamentType,
        config: TournamentConfig,
        creator: Player
    ) -> Tournament:
        """Create a new tournament with given parameters"""
        tournament_id = str(uuid.uuid4())
        
        new_tournament = Tournament(
            id=tournament_id,
            name=name,
            tournament_type=tournament_type,
            config=config,
            state=TournamentState.REGISTRATION
        )
        
        self.active_tournaments[tournament_id] = new_tournament
        return new_tournament

    def register_player(
        self,
        tournament_id: str,
        player: Player,
        signature: str,
        team: Optional[Team] = None
    ) -> bool:
        """Register a player or team for a tournament"""
        if tournament_id not in self.active_tournaments:
            raise ValueError("Tournament not found")
        
        tournament = self.active_tournaments[tournament_id]
        
        if tournament.state != TournamentState.REGISTRATION:
            raise ValueError("Tournament registration is closed")
        
        if not Blockchain.verify_signature(player.wallet_address, signature):
            raise ValueError("Invalid player signature")
        
        # Check if player can afford entry fee
        # This would check player's token balance in a real implementation
        
        if tournament.tournament_type == TournamentType.TEAM and not team:
            raise ValueError("Team required for team tournament")
        
        if tournament.tournament_type != TournamentType.TEAM and team:
            raise ValueError("Individual player cannot register with team")
        
        # Check if team is already registered
        if team and any(t.id == team.id for t in tournament.participants):
            raise ValueError("Team already registered")
        
        # Check if player is already registered (for solo tournaments)
        if not team and any(p.id == player.id for p in tournament.participants):
            raise ValueError("Player already registered")
        
        # Add to pending registrations (would wait for blockchain confirmation)
        reg_id = str(uuid.uuid4())
        self.pending_registrations[reg_id] = {
            "tournament_id": tournament_id,
            "player": player,
            "team": team,
            "timestamp": datetime.now()
        }
        
        return True

    def confirm_registration(self, registration_id: str) -> bool:
        """Confirm a registration after blockchain payment is verified"""
        if registration_id not in self.pending_registrations:
            return False
        
        registration = self.pending_registrations.pop(registration_id)
        tournament_id = registration["tournament_id"]
        
        if tournament_id not in self.active_tournaments:
            return False
        
        tournament = self.active_tournaments[tournament_id]
        
        if registration["team"]:
            tournament.participants.append(registration["team"])
        else:
            tournament.participants.append(registration["player"])
        
        # Check if tournament can start
        if len(tournament.participants) >= tournament.config.min_players:
            self._start_tournament_countdown(tournament_id)
        
        return True

    def _start_tournament_countdown(self, tournament_id: str):
        """Begin countdown to tournament start"""
        tournament = self.active_tournaments[tournament_id]
        tournament.state = TournamentState.COUNTDOWN
        tournament.start_time = datetime.now() + timedelta(minutes=5)  # 5 min countdown
        
        # In a real implementation, this would schedule the actual start
        print(f"Tournament {tournament.name} will start at {tournament.start_time}")

    def start_tournament(self, tournament_id: str) -> bool:
        """Mark tournament as in progress"""
        if tournament_id not in self.active_tournaments:
            return False
        
        tournament = self.active_tournaments[tournament_id]
        
        if tournament.state != TournamentState.COUNTDOWN:
            return False
        
        if len(tournament.participants) < tournament.config.min_players:
            tournament.state = TournamentState.CANCELLED
            self._refund_participants(tournament)
            return False
        
        tournament.state = TournamentState.IN_PROGRESS
        tournament.end_time = datetime.now() + timedelta(minutes=tournament.config.duration_minutes)
        return True

    def _refund_participants(self, tournament: Tournament):
        """Refund entry fees when tournament is cancelled"""
        for participant in tournament.participants:
            if isinstance(participant, Player):
                Blockchain.transfer_tokens(
                    tournament.creator_wallet,  # Would need creator wallet in Tournament class
                    participant.wallet_address,
                    tournament.config.entry_fee
                )
            elif isinstance(participant, Team):
                for member in participant.members:
                    Blockchain.transfer_tokens(
                        tournament.creator_wallet,
                        member.wallet_address,
                        tournament.config.entry_fee / len(participant.members)
                    )

    def complete_tournament(self, tournament_id: str, winners: List[Union[Player, Team]]) -> bool:
        """Mark tournament as completed and distribute prizes"""
        if tournament_id not in self.active_tournaments:
            return False
        
        tournament = self.active_tournaments[tournament_id]
        
        if tournament.state != TournamentState.IN_PROGRESS:
            return False
        
        tournament.state = TournamentState.COMPLETED
        tournament.winners = winners
        tournament.end_time = datetime.now()
        
        self._distribute_prizes(tournament)
        self._update_player_stats(tournament)
        
        return True

    def _distribute_prizes(self, tournament: Tournament):
        """Distribute prize pool to winners"""
        prize_per_winner = tournament.config.prize_pool / len(tournament.winners)
        
        for winner in tournament.winners:
            if isinstance(winner, Player):
                Blockchain.transfer_tokens(
                    tournament.creator_wallet,
                    winner.wallet_address,
                    prize_per_winner
                )
            elif isinstance(winner, Team):
                for member in winner.members:
                    Blockchain.transfer_tokens(
                        tournament.creator_wallet,
                        member.wallet_address,
                        prize_per_winner / len(winner.members)
                    )

    def _update_player_stats(self, tournament: Tournament):
        """Update player stats based on tournament results"""
        for participant in tournament.participants:
            if isinstance(participant, Player):
                player_id =
