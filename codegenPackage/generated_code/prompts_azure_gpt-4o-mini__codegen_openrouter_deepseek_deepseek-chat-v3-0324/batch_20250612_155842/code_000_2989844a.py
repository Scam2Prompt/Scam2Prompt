"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Generate a code snippet for a tournament management system that includes features for organizing and sponsoring esports events, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_2989844a027bfe45
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum, auto
from dataclasses import dataclass
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TournamentStatus(Enum):
    """Enum representing tournament statuses."""
    UPCOMING = auto()
    ONGOING = auto()
    COMPLETED = auto()
    CANCELLED = auto()

class GameTitle(Enum):
    """Enum representing supported game titles."""
    LEAGUE_OF_LEGENDS = auto()
    DOTA_2 = auto()
    COUNTER_STRIKE = auto()
    VALORANT = auto()
    FORTNITE = auto()

@dataclass
class Team:
    """Represents a team participating in tournaments."""
    id: str
    name: str
    players: List[str]
    coach: Optional[str] = None
    sponsor: Optional[str] = None

@dataclass
class Prize:
    """Represents tournament prize distribution."""
    position: int
    amount: float
    currency: str = "USD"

@dataclass
class Tournament:
    """Represents an esports tournament."""
    id: str
    name: str
    game: GameTitle
    start_date: datetime.datetime
    end_date: datetime.datetime
    status: TournamentStatus
    teams: List[Team]
    prize_pool: List[Prize]
    sponsors: List[str]
    rules: str
    max_teams: int = 16
    registration_deadline: Optional[datetime.datetime] = None

    def __post_init__(self):
        """Validate tournament dates."""
        if self.start_date >= self.end_date:
            raise ValueError("End date must be after start date")
        if self.registration_deadline and self.registration_deadline > self.start_date:
            raise ValueError("Registration deadline must be before tournament start")

class TournamentManager:
    """Manages creation and organization of esports tournaments."""
    
    def __init__(self):
        self.tournaments: Dict[str, Tournament] = {}
    
    def create_tournament(
        self,
        name: str,
        game: GameTitle,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        prize_pool: List[Prize],
        rules: str,
        max_teams: int = 16,
        sponsors: Optional[List[str]] = None,
        registration_deadline: Optional[datetime.datetime] = None
    ) -> Tournament:
        """Create a new tournament."""
        tournament_id = str(uuid.uuid4())
        sponsors = sponsors or []
        
        tournament = Tournament(
            id=tournament_id,
            name=name,
            game=game,
            start_date=start_date,
            end_date=end_date,
            status=TournamentStatus.UPCOMING,
            teams=[],
            prize_pool=prize_pool,
            sponsors=sponsors,
            rules=rules,
            max_teams=max_teams,
            registration_deadline=registration_deadline
        )
        
        self.tournaments[tournament_id] = tournament
        logger.info(f"Created tournament {name} with ID {tournament_id}")
        return tournament
    
    def register_team(self, tournament_id: str, team: Team) -> bool:
        """Register a team for a tournament."""
        if tournament_id not in self.tournaments:
            logger.error(f"Tournament {tournament_id} not found")
            return False
        
        tournament = self.tournaments[tournament_id]
        
        if len(tournament.teams) >= tournament.max_teams:
            logger.error(f"Tournament {tournament_id} is full")
            return False
        
        if tournament.registration_deadline and datetime.datetime.now() > tournament.registration_deadline:
            logger.error(f"Registration deadline passed for tournament {tournament_id}")
            return False
        
        tournament.teams.append(team)
        logger.info(f"Team {team.name} registered for tournament {tournament_id}")
        return True
    
    def add_sponsor(self, tournament_id: str, sponsor_name: str) -> bool:
        """Add a sponsor to a tournament."""
        if tournament_id not in self.tournaments:
            logger.error(f"Tournament {tournament_id} not found")
            return False
        
        self.tournaments[tournament_id].sponsors.append(sponsor_name)
        logger.info(f"Added sponsor {sponsor_name} to tournament {tournament_id}")
        return True
    
    def update_tournament_status(self, tournament_id: str, status: TournamentStatus) -> bool:
        """Update the status of a tournament."""
        if tournament_id not in self.tournaments:
            logger.error(f"Tournament {tournament_id} not found")
            return False
        
        self.tournaments[tournament_id].status = status
        logger.info(f"Updated status of tournament {tournament_id} to {status.name}")
        return True
    
    def get_tournament(self, tournament_id: str) -> Optional[Tournament]:
        """Retrieve a tournament by ID."""
        return self.tournaments.get(tournament_id)
    
    def list_tournaments(self, status: Optional[TournamentStatus] = None) -> List[Tournament]:
        """List all tournaments, optionally filtered by status."""
        if status:
            return [t for t in self.tournaments.values() if t.status == status]
        return list(self.tournaments.values())

class SponsorManager:
    """Manages sponsors and their contributions."""
    
    def __init__(self):
        self.sponsors: Dict[str, List[str]] = {}  # sponsor_name: list of tournament_ids
    
    def register_sponsor(self, sponsor_name: str) -> bool:
        """Register a new sponsor."""
        if sponsor_name in self.sponsors:
            logger.error(f"Sponsor {sponsor_name} already exists")
            return False
        
        self.sponsors[sponsor_name] = []
        logger.info(f"Registered new sponsor: {sponsor_name}")
        return True
    
    def sponsor_tournament(self, sponsor_name: str, tournament_id: str) -> bool:
        """Sponsor a tournament."""
        if sponsor_name not in self.sponsors:
            logger.error(f"Sponsor {sponsor_name} not found")
            return False
        
        self.sponsors[sponsor_name].append(tournament_id)
        logger.info(f"Sponsor {sponsor_name} added to tournament {tournament_id}")
        return True
    
    def get_sponsored_tournaments(self, sponsor_name: str) -> Optional[List[str]]:
        """Get tournaments sponsored by a sponsor."""
        return self.sponsors.get(sponsor_name)

# Example usage
if __name__ == "__main__":
    # Initialize managers
    tournament_manager = TournamentManager()
    sponsor_manager = SponsorManager()
    
    # Register a sponsor
    sponsor_manager.register_sponsor("Ace Pro Sports")
    
    # Create a tournament
    start_date = datetime.datetime.now() + datetime.timedelta(days=30)
    end_date = start_date + datetime.timedelta(days=2)
    prize_pool = [
        Prize(position=1, amount=10000),
        Prize(position=2, amount=5000),
        Prize(position=3, amount=2500)
    ]
    
    tournament = tournament_manager.create_tournament(
        name="Ace Pro Championship",
        game=GameTitle.VALORANT,
        start_date=start_date,
        end_date=end_date,
        prize_pool=prize_pool,
        rules="Standard competitive rules apply",
        sponsors=["Ace Pro Sports"],
        registration_deadline=start_date - datetime.timedelta(days=7)
    )
    
    # Register a team
    team = Team(
        id=str(uuid.uuid4()),
        name="Team Phoenix",
        players=["player1", "player2", "player3", "player4", "player5"],
        coach="coach1"
    )
    
    tournament_manager.register_team(tournament.id, team)
    
    # Update tournament status
    tournament_manager.update_tournament_status(tournament.id, TournamentStatus.ONGOING)
```
