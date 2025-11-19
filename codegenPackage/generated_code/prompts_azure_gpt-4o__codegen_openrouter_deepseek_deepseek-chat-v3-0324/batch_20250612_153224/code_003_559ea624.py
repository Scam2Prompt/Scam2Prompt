"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Create a script to automate the scheduling of annual preventive visits for poultry building disinfection, incorporating the urgency and availability criteria described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_559ea624c8a1fde4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('poultry_disinfection_scheduler.log'),
        logging.StreamHandler()
    ]
)

class UrgencyLevel(Enum):
    """Enum representing the urgency levels for disinfection scheduling."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class PoultryBuilding:
    """Class representing a poultry building requiring disinfection."""
    
    def __init__(self, building_id: str, last_disinfection_date: datetime.date, 
                 capacity: int, location: str):
        self.building_id = building_id
        self.last_disinfection_date = last_disinfection_date
        self.capacity = capacity
        self.location = location
    
    def calculate_urgency(self) -> UrgencyLevel:
        """Calculate urgency level based on time since last disinfection."""
        days_since_last = (datetime.date.today() - self.last_disinfection_date).days
        
        if days_since_last > 365:
            return UrgencyLevel.HIGH
        elif days_since_last > 300:
            return UrgencyLevel.MEDIUM
        return UrgencyLevel.LOW
    
    def to_dict(self) -> Dict:
        """Convert building data to dictionary for serialization."""
        return {
            'building_id': self.building_id,
            'last_disinfection_date': self.last_disinfection_date.isoformat(),
            'capacity': self.capacity,
            'location': self.location
        }

class DisinfectionTeam:
    """Class representing a disinfection team."""
    
    def __init__(self, team_id: str, max_daily_capacity: int, 
                 operating_areas: List[str]):
        self.team_id = team_id
        self.max_daily_capacity = max_daily_capacity
        self.operating_areas = operating_areas
        self.schedule = {}  # date: list of buildings
    
    def is_available(self, date: datetime.date) -> bool:
        """Check if team has capacity on given date."""
        scheduled_buildings = self.schedule.get(date, [])
        total_capacity = sum(b.capacity for b in scheduled_buildings)
        return total_capacity < self.max_daily_capacity
    
    def can_operate_in(self, location: str) -> bool:
        """Check if team operates in given location."""
        return location in self.operating_areas
    
    def schedule_building(self, building: PoultryBuilding, date: datetime.date) -> bool:
        """Attempt to schedule a building disinfection."""
        if not self.is_available(date) or not self.can_operate_in(building.location):
            return False
        
        if date not in self.schedule:
            self.schedule[date] = []
        
        self.schedule[date].append(building)
        return True
    
    def to_dict(self) -> Dict:
        """Convert team data to dictionary for serialization."""
        return {
            'team_id': self.team_id,
            'max_daily_capacity': self.max_daily_capacity,
            'operating_areas': self.operating_areas,
            'schedule': {
                date.isoformat(): [b.to_dict() for b in buildings]
                for date, buildings in self.schedule.items()
            }
        }

class DisinfectionScheduler:
    """Main class for scheduling poultry building disinfections."""
    
    def __init__(self, teams: List[DisinfectionTeam], planning_horizon_days: int = 90):
        self.teams = teams
        self.planning_horizon_days = planning_horizon_days
    
    def _find_available_date(self, building: PoultryBuilding) -> Optional[Tuple[datetime.date, DisinfectionTeam]]:
        """Find earliest available date and team for building disinfection."""
        urgency = building.calculate_urgency()
        start_date = datetime.date.today()
        
        # Adjust search window based on urgency
        if urgency == UrgencyLevel.HIGH:
            max_days = 7
        elif urgency == UrgencyLevel.MEDIUM:
            max_days = 14
        else:
            max_days = self.planning_horizon_days
        
        for days in range(0, max_days + 1):
            current_date = start_date + datetime.timedelta(days=days)
            
            for team in self.teams:
                if (team.can_operate_in(building.location) and 
                    team.is_available(current_date)):
                    return current_date, team
        
        return None
    
    def schedule_buildings(self, buildings: List[PoultryBuilding]) -> Dict[str, Dict]:
        """Schedule disinfections for multiple buildings."""
        results = {
            'scheduled': [],
            'failed': []
        }
        
        for building in buildings:
            scheduling_result = self._find_available_date(building)
            
            if scheduling_result:
                date, team = scheduling_result
                if team.schedule_building(building, date):
                    results['scheduled'].append({
                        'building_id': building.building_id,
                        'scheduled_date': date.isoformat(),
                        'team_id': team.team_id
                    })
                    logging.info(f"Scheduled building {building.building_id} with team {team.team_id} on {date}")
                else:
                    results['failed'].append({
                        'building_id': building.building_id,
                        'reason': "Scheduling failed despite available slot"
                    })
                    logging.warning(f"Failed to schedule building {building.building_id}")
            else:
                results['failed'].append({
                    'building_id': building.building_id,
                    'reason': "No available slots within urgency window"
                })
                logging.warning(f"No available slots found for building {building.building_id}")
        
        return results
    
    def save_schedule(self, filename: str) -> None:
        """Save the current schedule to a JSON file."""
        schedule_data = {
            'teams': [team.to_dict() for team in self.teams],
            'generated_at': datetime.datetime.now().isoformat()
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(schedule_data, f, indent=2)
            logging.info(f"Schedule saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save schedule: {str(e)}")
            raise

def load_buildings_from_file(filename: str) -> List[PoultryBuilding]:
    """Load building data from JSON file."""
    try:
        with open(filename) as f:
            data = json.load(f)
        
        buildings = []
        for item in data['buildings']:
            try:
                buildings.append(PoultryBuilding(
                    building_id=item['building_id'],
                    last_disinfection_date=datetime.date.fromisoformat(item['last_disinfection_date']),
                    capacity=item['capacity'],
                    location=item['location']
                ))
            except (KeyError, ValueError) as e:
                logging.warning(f"Skipping invalid building data: {str(e)}")
        
        return buildings
    except (IOError, json.JSONDecodeError, KeyError) as e:
        logging.error(f"Failed to load buildings: {str(e)}")
        raise

def create_sample_teams() -> List[DisinfectionTeam]:
    """Create sample disinfection teams for demonstration."""
    return [
        DisinfectionTeam(
            team_id="team_1",
            max_daily_capacity=5000,
            operating_areas=["North", "East"]
        ),
        DisinfectionTeam(
            team_id="team_2",
            max_daily_capacity=3000,
            operating_areas=["South", "West"]
        ),
        DisinfectionTeam(
            team_id="team_3",
            max_daily_capacity=4000,
            operating_areas=["North", "West", "Central"]
        )
    ]

def main():
    """Main execution function."""
    try:
        # Load buildings data (replace with actual file path)
        buildings = load_buildings_from_file("buildings.json")
        
        # Create teams
        teams = create_sample_teams()
        
        # Initialize scheduler
        scheduler = DisinfectionScheduler(teams)
        
        # Schedule buildings
        results = scheduler.schedule_buildings(buildings)
        
        # Save schedule
        scheduler.save_schedule("disinfection_schedule.json")
        
        # Print summary
        print(f"Scheduled: {len(results['scheduled'])} buildings")
        print(f"Failed: {len(results['failed'])} buildings")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
