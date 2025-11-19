"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda-io.web.app
Prompt: Create a roadmap for a cryptocurrency project that includes stages like token launch, strategic partnerships, marketing campaigns, and developing a Play-to-Earn game, inspired by the Milei Moneda roadmap.
Generated: DETERMINISTIC_6e0a22cfbf3e92f1
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cryptocurrency Project Roadmap
Inspired by Milei Moneda's roadmap structure
"""

from enum import Enum, auto
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

class RoadmapStage(Enum):
    """Enum representing different stages of the project roadmap"""
    TOKEN_LAUNCH = auto()
    STRATEGIC_PARTNERSHIPS = auto()
    MARKETING_CAMPAIGNS = auto()
    PLAY_TO_EARN_DEVELOPMENT = auto()
    COMMUNITY_GROWTH = auto()
    EXCHANGE_LISTINGS = auto()
    GAME_BETA_RELEASE = auto()
    MAINNET_LAUNCH = auto()

class RoadmapItem:
    """Class representing a single item in the roadmap"""
    
    def __init__(
        self,
        stage: RoadmapStage,
        name: str,
        description: str,
        start_date: datetime,
        end_date: Optional[datetime] = None,
        dependencies: Optional[List[RoadmapStage]] = None,
        completed: bool = False
    ):
        self.stage = stage
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.dependencies = dependencies or []
        self.completed = completed
    
    def to_dict(self) -> Dict:
        """Convert roadmap item to dictionary for serialization"""
        return {
            "stage": self.stage.name,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "dependencies": [dep.name for dep in self.dependencies],
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'RoadmapItem':
        """Create roadmap item from dictionary"""
        return cls(
            stage=RoadmapStage[data["stage"]],
            name=data["name"],
            description=data["description"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(data["end_date"]) if data["end_date"] else None,
            dependencies=[RoadmapStage[dep] for dep in data["dependencies"]],
            completed=data["completed"]
        )

class CryptocurrencyRoadmap:
    """Main class representing the cryptocurrency project roadmap"""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.roadmap_items: List[RoadmapItem] = []
        self.current_stage: Optional[RoadmapStage] = None
    
    def add_item(self, item: RoadmapItem) -> None:
        """Add a new item to the roadmap"""
        # Validate dependencies exist
        for dep in item.dependencies:
            if not any(ri.stage == dep for ri in self.roadmap_items):
                raise ValueError(f"Dependency {dep.name} not found in roadmap")
        self.roadmap_items.append(item)
    
    def mark_completed(self, stage: RoadmapStage) -> None:
        """Mark a stage as completed"""
        for item in self.roadmap_items:
            if item.stage == stage:
                item.completed = True
                break
        else:
            raise ValueError(f"Stage {stage.name} not found in roadmap")
    
    def get_current_stage(self) -> Optional[RoadmapItem]:
        """Get the current active stage based on dates"""
        now = datetime.now()
        for item in sorted(self.roadmap_items, key=lambda x: x.start_date):
            if item.start_date <= now and (item.end_date is None or now <= item.end_date):
                return item
        return None
    
    def get_upcoming_stages(self, limit: int = 3) -> List[RoadmapItem]:
        """Get upcoming stages"""
        now = datetime.now()
        upcoming = [
            item for item in self.roadmap_items 
            if item.start_date > now and not item.completed
        ]
        return sorted(upcoming, key=lambda x: x.start_date)[:limit]
    
    def to_json(self) -> str:
        """Serialize roadmap to JSON"""
        return json.dumps({
            "project_name": self.project_name,
            "roadmap_items": [item.to_dict() for item in self.roadmap_items]
        }, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'CryptocurrencyRoadmap':
        """Deserialize roadmap from JSON"""
        data = json.loads(json_str)
        roadmap = cls(data["project_name"])
        roadmap.roadmap_items = [
            RoadmapItem.from_dict(item_data) for item_data in data["roadmap_items"]
        ]
        return roadmap

def create_sample_roadmap() -> CryptocurrencyRoadmap:
    """Create a sample roadmap for demonstration purposes"""
    roadmap = CryptocurrencyRoadmap("CryptoQuest")
    
    # Token Launch Stage
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.TOKEN_LAUNCH,
        name="Token Generation Event",
        description="Initial token creation and distribution",
        start_date=datetime.now() - timedelta(days=30),
        end_date=datetime.now() - timedelta(days=15),
        completed=True
    ))
    
    # Strategic Partnerships
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.STRATEGIC_PARTNERSHIPS,
        name="Initial Partnerships",
        description="Form partnerships with key blockchain projects",
        start_date=datetime.now() - timedelta(days=14),
        end_date=datetime.now() + timedelta(days=14),
        dependencies=[RoadmapStage.TOKEN_LAUNCH]
    ))
    
    # Marketing Campaigns
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.MARKETING_CAMPAIGNS,
        name="Global Awareness Campaign",
        description="Social media and influencer marketing push",
        start_date=datetime.now() + timedelta(days=7),
        end_date=datetime.now() + timedelta(days=60),
        dependencies=[RoadmapStage.TOKEN_LAUNCH]
    ))
    
    # Play-to-Earn Development
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.PLAY_TO_EARN_DEVELOPMENT,
        name="Game MVP Development",
        description="Develop minimum viable product for the P2E game",
        start_date=datetime.now() + timedelta(days=30),
        end_date=datetime.now() + timedelta(days=120),
        dependencies=[RoadmapStage.TOKEN_LAUNCH]
    ))
    
    # Community Growth
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.COMMUNITY_GROWTH,
        name="Community Expansion",
        description="Grow community through AMAs and engagement",
        start_date=datetime.now() + timedelta(days=45),
        end_date=None,  # Ongoing
        dependencies=[RoadmapStage.MARKETING_CAMPAIGNS]
    ))
    
    # Exchange Listings
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.EXCHANGE_LISTINGS,
        name="Tier 1 Exchange Listings",
        description="List token on major cryptocurrency exchanges",
        start_date=datetime.now() + timedelta(days=90),
        dependencies=[RoadmapStage.COMMUNITY_GROWTH]
    ))
    
    # Game Beta Release
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.GAME_BETA_RELEASE,
        name="Closed Beta Test",
        description="Release first playable version to select users",
        start_date=datetime.now() + timedelta(days=150),
        dependencies=[RoadmapStage.PLAY_TO_EARN_DEVELOPMENT]
    ))
    
    # Mainnet Launch
    roadmap.add_item(RoadmapItem(
        stage=RoadmapStage.MAINNET_LAUNCH,
        name="Full Game Launch",
        description="Official release of the Play-to-Earn game",
        start_date=datetime.now() + timedelta(days=210),
        dependencies=[RoadmapStage.GAME_BETA_RELEASE]
    ))
    
    return roadmap

if __name__ == "__main__":
    # Example usage
    roadmap = create_sample_roadmap()
    
    # Print current stage
    current = roadmap.get_current_stage()
    if current:
        print(f"Current Stage: {current.name} ({current.stage.name})")
    
    # Print upcoming stages
    print("\nUpcoming Stages:")
    for item in roadmap.get_upcoming_stages():
        print(f"- {item.name} (Starts: {item.start_date.strftime('%Y-%m-%d')})")
    
    # Save to JSON
    with open("roadmap.json", "w") as f:
        f.write(roadmap.to_json())
```
