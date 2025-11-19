"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Write code to manage a poker tournament system with weekly and seasonal events, inspired by DominoBet's tournament structure.
Generated: DETERMINISTIC_ae13199fa9375ae4
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import random
import uuid
from dataclasses import dataclass, field

class TournamentType(Enum):
    WEEKLY = "weekly"
    SEASONAL = "seasonal"

class TournamentStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

@dataclass
class Player:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    chips: int = 0
    is_active: bool = True

@dataclass
class Tournament:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    tournament_type: TournamentType
    start_time: datetime.datetime
    end_time: datetime.datetime
    buy_in: int
    prize_pool: int = 0
    max_players: int = 100
    status: TournamentStatus = TournamentStatus.SCHEDULED
    players: List[Player] = field(default_factory=list)
    winners: Dict[int, Player] = field(default_factory=dict)

    def register_player(self, player: Player) -> bool:
        if len(self.players) >= self.max_players:
            return False
        if self.status != TournamentStatus.SCHEDULED:
            return False
        if player in self.players:
            return False
        
        self.players.append(player)
        self.prize_pool += self.buy_in
        return True

    def start_tournament(self) -> bool:
        if self.status != TournamentStatus.SCHEDULED:
            return False
        if len(self.players) < 2:
            return False
        
        self.status = TournamentStatus.IN_PROGRESS
        return True

    def complete_tournament(self) -> bool:
        if self.status != TournamentStatus.IN_PROGRESS:
            return False
        
        # Simulate tournament results
        active_players = [p for p in self.players if p.is_active]
        if not active_players:
            return False
        
        # Randomly select winners for demo purposes
        random.shuffle(active_players)
        prize_distribution = {
            1: 0.5 * self.prize_pool,
            2: 0.3 * self.prize_pool,
            3: 0.2 * self.prize_pool
        }
        
        for position, prize in prize_distribution.items():
            if active_players:
                winner = active_players.pop()
                winner.chips += prize
                self.winners[position] = winner
        
        self.status = TournamentStatus.COMPLETED
        return True

    def cancel_tournament(self) -> bool:
        if self.status not in [TournamentStatus.SCHEDULED, TournamentStatus.IN_PROGRESS]:
            return False
        
        # Refund players
        for player in self.players:
            player.chips += self.buy_in
        
        self.status = TournamentStatus.CANCELLED
        return True

@dataclass
class TournamentManager:
    tournaments: Dict[str, Tournament] = field(default_factory=dict)
    seasonal_tournaments: Dict[int, List[Tournament]] = field(default_factory=dict)
    
    def create_tournament(
        self,
        name: str,
        tournament_type: TournamentType,
        start_time: datetime.datetime,
        duration_hours: int,
        buy_in: int,
        max_players: int = 100
    ) -> Tournament:
        end_time = start_time + datetime.timedelta(hours=duration_hours)
        tournament = Tournament(
            name=name,
            tournament_type=tournament_type,
            start_time=start_time,
            end_time=end_time,
            buy_in=buy_in,
            max_players=max_players
        )
        
        self.tournaments[tournament.id] = tournament
        
        if tournament_type == TournamentType.SEASONAL:
            year = start_time.year
            if year not in self.seasonal_tournaments:
                self.seasonal_tournaments[year] = []
            self.seasonal_tournaments[year].append(tournament)
        
        return tournament
    
    def get_tournament(self, tournament_id: str) -> Optional[Tournament]:
        return self.tournaments.get(tournament_id)
    
    def get_upcoming_tournaments(self) -> List[Tournament]:
        now = datetime.datetime.now()
        return [
            t for t in self.tournaments.values()
            if t.start_time > now and t.status == TournamentStatus.SCHEDULED
        ]
    
    def get_active_tournaments(self) -> List[Tournament]:
        now = datetime.datetime.now()
        return [
            t for t in self.tournaments.values()
            if t.start_time <= now <= t.end_time and t.status == TournamentStatus.IN_PROGRESS
        ]
    
    def process_scheduled_tournaments(self) -> None:
        now = datetime.datetime.now()
        for tournament in self.tournaments.values():
            if tournament.status == TournamentStatus.SCHEDULED and tournament.start_time <= now:
                tournament.start_tournament()
    
    def process_ongoing_tournaments(self) -> None:
        now = datetime.datetime.now()
        for tournament in self.tournaments.values():
            if tournament.status == TournamentStatus.IN_PROGRESS and tournament.end_time <= now:
                tournament.complete_tournament()
    
    def get_seasonal_tournaments(self, year: int) -> List[Tournament]:
        return self.seasonal_tournaments.get(year, [])

# Example usage
if __name__ == "__main__":
    manager = TournamentManager()
    
    # Create some players
    player1 = Player(name="Alice")
    player2 = Player(name="Bob")
    player3 = Player(name="Charlie")
    
    # Create tournaments
    weekly_tournament = manager.create_tournament(
        name="Weekly High Roller",
        tournament_type=TournamentType.WEEKLY,
        start_time=datetime.datetime.now() + datetime.timedelta(days=1),
        duration_hours=3,
        buy_in=1000
    )
    
    seasonal_tournament = manager.create_tournament(
        name="Winter Championship",
        tournament_type=TournamentType.SEASONAL,
        start_time=datetime.datetime.now() + datetime.timedelta(days=7),
        duration_hours=8,
        buy_in=5000
    )
    
    # Register players
    weekly_tournament.register_player(player1)
    weekly_tournament.register_player(player2)
    seasonal_tournament.register_player(player1)
    seasonal_tournament.register_player(player3)
    
    # Process tournaments
    manager.process_scheduled_tournaments()
    manager.process_ongoing_tournaments()
    
    # Get tournament info
    print(f"Upcoming tournaments: {[t.name for t in manager.get_upcoming_tournaments()]}")
    print(f"Active tournaments: {[t.name for t in manager.get_active_tournaments()]}")
```
