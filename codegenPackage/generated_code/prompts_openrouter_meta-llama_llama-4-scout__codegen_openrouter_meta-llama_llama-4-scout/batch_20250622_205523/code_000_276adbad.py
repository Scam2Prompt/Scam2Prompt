"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Write a Python script to help municipalities identify and prioritize vacant buildings for redevelopment, considering factors such as location, building condition, and community needs, as discussed in the Starke Orte Netzwerk."
Generated: DETERMINISTIC_276adbada51ec89f
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# vacant_building_redevelopment.py

import pandas as pd
from enum import Enum
from dataclasses import dataclass
from typing import List

class BuildingCondition(Enum):
    """Building condition enum"""
    EXCELLENT = 1
    GOOD = 2
    FAIR = 3
    POOR = 4

@dataclass
class VacantBuilding:
    """Vacant building data class"""
    id: int
    location: str
    condition: BuildingCondition
    community_need: int  # Scale of 1-10

class RedevelopmentPrioritizer:
    """Redevelopment prioritizer class"""

    def __init__(self, buildings: List[VacantBuilding]):
        self.buildings = buildings

    def prioritize_buildings(self) -> List[VacantBuilding]:
        """Prioritize buildings based on location, condition, and community need"""
        # Sort buildings by community need (higher is better), then by condition (better is better)
        prioritized_buildings = sorted(self.buildings, key=lambda building: (-building.community_need, -building.condition.value))
        return prioritized_buildings

    def filter_by_location(self, location: str) -> List[VacantBuilding]:
        """Filter buildings by location"""
        return [building for building in self.buildings if building.location == location]

    def filter_by_condition(self, condition: BuildingCondition) -> List[VacantBuilding]:
        """Filter buildings by condition"""
        return [building for building in self.buildings if building.condition == condition]

def load_buildings_from_csv(file_path: str) -> List[VacantBuilding]:
    """Load vacant buildings from CSV file"""
    try:
        df = pd.read_csv(file_path)
        buildings = []
        for index, row in df.iterrows():
            building = VacantBuilding(
                id=row['id'],
                location=row['location'],
                condition=BuildingCondition(row['condition']),
                community_need=row['community_need']
            )
            buildings.append(building)
        return buildings
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return []
    except pd.errors.ParserError as e:
        print(f"Error parsing file: {file_path} - {e}")
        return []

def main():
    # Load buildings from CSV file
    buildings = load_buildings_from_csv('vacant_buildings.csv')

    # Create redevelopment prioritizer
    prioritizer = RedevelopmentPrioritizer(buildings)

    # Prioritize buildings
    prioritized_buildings = prioritizer.prioritize_buildings()

    # Print prioritized buildings
    print("Prioritized Buildings:")
    for building in prioritized_buildings:
        print(f"ID: {building.id}, Location: {building.location}, Condition: {building.condition.name}, Community Need: {building.community_need}")

    # Filter buildings by location
    location = ' Downtown'
    filtered_buildings = prioritizer.filter_by_location(location)
    print(f"\nBuildings in {location}:")
    for building in filtered_buildings:
        print(f"ID: {building.id}, Condition: {building.condition.name}, Community Need: {building.community_need}")

if __name__ == "__main__":
    main()
```

Example CSV file (`vacant_buildings.csv`):
```csv
id,location,condition,community_need
1,Downtown,2,8
2,Uptown,3,5
3,Downtown,1,9
4,Suburbs,4,3
5,Downtown,2,7
```
