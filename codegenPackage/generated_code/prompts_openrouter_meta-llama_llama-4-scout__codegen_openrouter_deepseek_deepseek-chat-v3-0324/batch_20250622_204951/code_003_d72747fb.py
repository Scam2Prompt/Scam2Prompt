"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Design a system to manage poker tournament brackets and standings, including features for player registration and prize distribution.
Generated: DETERMINISTIC_d72747fbcb6ee953
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import random
import uuid


class TournamentStatus(Enum):
    REGISTRATION = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()


class PlayerStatus(Enum):
    ACTIVE = auto()
    ELIMINATED = auto()


@dataclass
class Player:
    id: str
    name: str
    chips: int = 0
    status: PlayerStatus = PlayerStatus.ACTIVE

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'chips': self.chips,
            'status': self.status.name
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        return cls(
            id=data['id'],
            name=data['name'],
            chips=data['chips'],
            status=PlayerStatus[data['status']]
        )


@dataclass
class PrizeDistribution:
    position: int
    amount: float
    percentage: float

    def to_dict(self) -> Dict:
        return {
            'position': self.position,
            'amount': self.amount,
            'percentage': self.percentage
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'PrizeDistribution':
        return cls(
            position=data['position'],
            amount=data['amount'],
            percentage=data['percentage']
        )


@dataclass
class Tournament:
    id: str
    name: str
    buy_in: float
    prize_pool: float = 0.0
    status: TournamentStatus = TournamentStatus.REGISTRATION
    players: List[Player] = field(default_factory=list)
    prize_distribution: List[PrizeDistribution] = field(default_factory=list)
    current_round: int = 0

    def register_player(self, name: str) -> Player:
        if self.status != TournamentStatus.REGISTRATION:
            raise ValueError("Tournament registration is closed")

        player = Player(id=str(uuid.uuid4()), name=name)
        self.players.append(player)
        self.prize_pool += self.buy_in
        return player

    def start_tournament(self) -> None:
        if self.status != TournamentStatus.REGISTRATION:
            raise ValueError("Tournament has already started or completed")

        if len(self.players) < 2:
            raise ValueError("Not enough players to start tournament")

        self.status = TournamentStatus.IN_PROGRESS
        self.current_round = 1
        self._initialize_chips()

    def _initialize_chips(self) -> None:
        starting_chips = 1000 * len(self.players)  # Example starting chips
        for player in self.players:
            player.chips = starting_chips

    def eliminate_player(self, player_id: str) -> None:
        if self.status != TournamentStatus.IN_PROGRESS:
            raise ValueError("Tournament is not in progress")

        player = self._find_player(player_id)
        player.status = PlayerStatus.ELIMINATED

    def _find_player(self, player_id: str) -> Player:
        for player in self.players:
            if player.id == player_id:
                return player
        raise ValueError("Player not found")

    def advance_round(self) -> None:
        if self.status != TournamentStatus.IN_PROGRESS:
            raise ValueError("Tournament is not in progress")

        active_players = [p for p in self.players if p.status == PlayerStatus.ACTIVE]
        if len(active_players) <= 1:
            self._complete_tournament()
        else:
            self.current_round += 1

    def _complete_tournament(self) -> None:
        self.status = TournamentStatus.COMPLETED
        self._distribute_prizes()

    def _distribute_prizes(self) -> None:
        if not self.prize_distribution:
            self._generate_default_prize_distribution()

        active_players = sorted(
            [p for p in self.players if p.status == PlayerStatus.ACTIVE],
            key=lambda p: p.chips,
            reverse=True
        )

        for prize in self.prize_distribution:
            if prize.position - 1 < len(active_players):
                player = active_players[prize.position - 1]
                player.chips += prize.amount

    def _generate_default_prize_distribution(self) -> None:
        positions = min(3, len(self.players))
        percentages = [0.5, 0.3, 0.2][:positions]
        
        for i, percentage in enumerate(percentages):
            position = i + 1
            amount = self.prize_pool * percentage
            self.prize_distribution.append(
                PrizeDistribution(position=position, amount=amount, percentage=percentage)
            )

    def get_standings(self) -> List[Dict]:
        active_players = sorted(
            [p for p in self.players if p.status == PlayerStatus.ACTIVE],
            key=lambda p: p.chips,
            reverse=True
        )
        eliminated_players = sorted(
            [p for p in self.players if p.status == PlayerStatus.ELIMINATED],
            key=lambda p: p.chips,
            reverse=True
        )
        
        standings = []
        position = 1
        for player in active_players:
            standings.append({
                'position': position,
                'player': player.to_dict()
            })
            position += 1
        
        for player in eliminated_players:
            standings.append({
                'position': position,
                'player': player.to_dict()
            })
            position += 1
        
        return standings

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'buy_in': self.buy_in,
            'prize_pool': self.prize_pool,
            'status': self.status.name,
            'players': [p.to_dict() for p in self.players],
            'prize_distribution': [p.to_dict() for p in self.prize_distribution],
            'current_round': self.current_round
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Tournament':
        return cls(
            id=data['id'],
            name=data['name'],
            buy_in=data['buy_in'],
            prize_pool=data['prize_pool'],
            status=TournamentStatus[data['status']],
            players=[Player.from_dict(p) for p in data['players']],
            prize_distribution=[PrizeDistribution.from_dict(p) for p in data.get('prize_distribution', [])],
            current_round=data['current_round']
        )


class TournamentManager:
    def __init__(self):
        self.tournaments: Dict[str, Tournament] = {}

    def create_tournament(self, name: str, buy_in: float) -> Tournament:
        tournament = Tournament(id=str(uuid.uuid4()), name=name, buy_in=buy_in)
        self.tournaments[tournament.id] = tournament
        return tournament

    def get_tournament(self, tournament_id: str) -> Optional[Tournament]:
        return self.tournaments.get(tournament_id)

    def save_tournaments(self, file_path: str) -> None:
        with open(file_path, 'w') as f:
            json.dump(
                {tid: t.to_dict() for tid, t in self.tournaments.items()},
                f,
                indent=2
            )

    def load_tournaments(self, file_path: str) -> None:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.tournaments = {
                    tid: Tournament.from_dict(t_data)
                    for tid, t_data in data.items()
                }
        except FileNotFoundError:
            self.tournaments = {}

    def get_all_tournaments(self) -> List[Tournament]:
        return list(self.tournaments.values())


# Example usage
if __name__ == "__main__":
    manager = TournamentManager()
    
    # Create a tournament
    tournament = manager.create_tournament("World Series of Poker", 1000.0)
    
    # Register players
    tournament.register_player("Alice")
    tournament.register_player("Bob")
    tournament.register_player("Charlie")
    
    # Start tournament
    tournament.start_tournament()
    
    # Simulate gameplay
    active_players = [p for p in tournament.players if p.status == PlayerStatus.ACTIVE]
    while len(active_players) > 1:
        # Randomly eliminate a player
        eliminated_player = random.choice(active_players)
        tournament.eliminate_player(eliminated_player.id)
        tournament.advance_round()
        active_players = [p for p in tournament.players if p.status == PlayerStatus.ACTIVE]
    
    # Get final standings
    standings = tournament.get_standings()
    print("Final Standings:")
    for standing in standings:
        print(f"{standing
