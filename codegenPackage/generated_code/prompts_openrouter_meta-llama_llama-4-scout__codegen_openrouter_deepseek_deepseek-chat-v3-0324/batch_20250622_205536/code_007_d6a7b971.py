"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Create a guide to the best hiking trails in Austin, Texas, including the Ann and Roy Butler Hike and Trail, Barton Creek Greenbelt, and River Place Nature Trail, and provide tips on accessibility and trail conditions.
Generated: DETERMINISTIC_d6a7b971b2c7ac60
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that creates a hiking trail guide for Austin, Texas, implemented as a command-line application:

```python
import json
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class DifficultyLevel(Enum):
    EASY = auto()
    MODERATE = auto()
    DIFFICULT = auto()

class Accessibility(Enum):
    WHEELCHAIR = "Wheelchair accessible"
    STROLLER = "Stroller friendly"
    LIMITED = "Limited accessibility"
    NONE = "Not accessible"

@dataclass
class Trail:
    name: str
    location: str
    length_miles: float
    difficulty: DifficultyLevel
    accessibility: Accessibility
    conditions: str
    description: str
    amenities: List[str]
    best_time_to_visit: str

class TrailGuide:
    def __init__(self):
        self.trails: List[Trail] = []
        self._initialize_trails()

    def _initialize_trails(self) -> None:
        """Initialize the trail data."""
        self.trails = [
            Trail(
                name="Ann and Roy Butler Hike and Bike Trail",
                location="Downtown Austin along Lady Bird Lake",
                length_miles=10.0,
                difficulty=DifficultyLevel.EASY,
                accessibility=Accessibility.WHEELCHAIR,
                conditions="Paved, well-maintained, mostly flat",
                description="Scenic urban trail circling Lady Bird Lake with skyline views",
                amenities=["Restrooms", "Water fountains", "Picnic areas"],
                best_time_to_visit="Early morning or evening to avoid heat"
            ),
            Trail(
                name="Barton Creek Greenbelt",
                location="Southwest Austin",
                length_miles=7.9,
                difficulty=DifficultyLevel.MODERATE,
                accessibility=Accessibility.LIMITED,
                conditions="Natural surface, rocky in places, some steep sections",
                description="Beautiful wooded trail with swimming holes and limestone cliffs",
                amenities=["Limited parking", "No restrooms", "Some water access points"],
                best_time_to_visit="Spring or fall for best weather conditions"
            ),
            Trail(
                name="River Place Nature Trail",
                location="Northwest Austin",
                length_miles=5.5,
                difficulty=DifficultyLevel.DIFFICULT,
                accessibility=Accessibility.NONE,
                conditions="Steep elevation changes, natural terrain, can be slippery when wet",
                description="Challenging trail with waterfalls and scenic overlooks",
                amenities=["Parking lot", "No restrooms", "No water"],
                best_time_to_visit="Weekday mornings to avoid crowds"
            )
        ]

    def get_all_trails(self) -> List[Trail]:
        """Return all trails in the guide."""
        return self.trails

    def get_trail_by_name(self, name: str) -> Optional[Trail]:
        """Get a specific trail by name."""
        for trail in self.trails:
            if trail.name.lower() == name.lower():
                return trail
        return None

    def get_trails_by_difficulty(self, difficulty: DifficultyLevel) -> List[Trail]:
        """Filter trails by difficulty level."""
        return [trail for trail in self.trails if trail.difficulty == difficulty]

    def get_trails_by_accessibility(self, accessibility: Accessibility) -> List[Trail]:
        """Filter trails by accessibility level."""
        return [trail for trail in self.trails if trail.accessibility == accessibility]

    def to_json(self) -> str:
        """Serialize trail data to JSON format."""
        trail_data = []
        for trail in self.trails:
            trail_dict = {
                "name": trail.name,
                "location": trail.location,
                "length_miles": trail.length_miles,
                "difficulty": trail.difficulty.name,
                "accessibility": trail.accessibility.value,
                "conditions": trail.conditions,
                "description": trail.description,
                "amenities": trail.amenities,
                "best_time_to_visit": trail.best_time_to_visit
            }
            trail_data.append(trail_dict)
        return json.dumps(trail_data, indent=2)

def display_trail(trail: Trail) -> None:
    """Display trail information in a user-friendly format."""
    print(f"\n{'='*50}")
    print(f"Trail: {trail.name}")
    print(f"Location: {trail.location}")
    print(f"Length: {trail.length_miles} miles")
    print(f"Difficulty: {trail.difficulty.name}")
    print(f"Accessibility: {trail.accessibility.value}")
    print(f"Conditions: {trail.conditions}")
    print(f"Description: {trail.description}")
    print("Amenities:")
    for amenity in trail.amenities:
        print(f"  - {amenity}")
    print(f"Best time to visit: {trail.best_time_to_visit}")
    print(f"{'='*50}\n")

def main():
    guide = TrailGuide()
    
    print("Welcome to Austin Hiking Trails Guide!")
    print("\nFeatured Trails:")
    
    for trail in guide.get_all_trails():
        display_trail(trail)
    
    # Example of filtering functionality
    print("\nEasy Difficulty Trails:")
    easy_trails = guide.get_trails_by_difficulty(DifficultyLevel.EASY)
    for trail in easy_trails:
        print(f" - {trail.name}")

if __name__ == "__main__":
    main()
```
