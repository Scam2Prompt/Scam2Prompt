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
import json
import csv
from typing import List, Dict, Optional
from dataclasses import dataclass
import heapq
from enum import Enum

class Condition(Enum):
    """Enum representing the condition of a building."""
    EXCELLENT = 5
    GOOD = 4
    FAIR = 3
    POOR = 2
    DERELICT = 1

class Priority(Enum):
    """Enum representing priority levels for redevelopment."""
    HIGH = 3
    MEDIUM = 2
    LOW = 1

@dataclass
class Building:
    """Represents a vacant building with relevant attributes."""
    id: str
    address: str
    location_score: float  # 0-10, higher is better
    condition: Condition
    square_meters: float
    community_needs_score: float  # 0-10, higher means more needed
    ownership_status: str
    historical_significance: bool

class BuildingPrioritizer:
    """Prioritizes buildings based on multiple factors."""
    
    def __init__(self, buildings: List[Building]):
        self.buildings = buildings
    
    def calculate_priority_score(self, building: Building) -> float:
        """Calculate a priority score for a building.
        
        Args:
            building: The building to score
            
        Returns:
            float: Priority score (higher means higher priority)
        """
        # Weighted factors (adjust weights as needed)
        location_weight = 0.3
        condition_weight = 0.2
        community_needs_weight = 0.4
        size_weight = 0.1
        
        # Normalize condition to 0-1 scale
        condition_score = building.condition.value / Condition.EXCELLENT.value
        
        score = (
            (building.location_score / 10 * location_weight) +
            (condition_score * condition_weight) +
            (building.community_needs_score / 10 * community_needs_weight) +
            (min(building.square_meters / 1000, 1) * size_weight)  # Cap size influence
        )
        
        # Bonus for historical significance
        if building.historical_significance:
            score *= 1.2
            
        return score
    
    def prioritize(self, top_n: Optional[int] = None) -> List[Building]:
        """Prioritize buildings based on calculated scores.
        
        Args:
            top_n: Optional number of top buildings to return
            
        Returns:
            List of buildings sorted by priority (highest first)
        """
        scored_buildings = [
            (self.calculate_priority_score(building), building)
            for building in self.buildings
        ]
        
        # Sort by score descending
        scored_buildings.sort(reverse=True, key=lambda x: x[0])
        
        if top_n is not None:
            scored_buildings = scored_buildings[:top_n]
        
        return [building for score, building in scored_buildings]
    
    def get_priority_category(self, building: Building) -> Priority:
        """Categorize a building's priority level.
        
        Args:
            building: The building to categorize
            
        Returns:
            Priority level (HIGH, MEDIUM, LOW)
        """
        score = self.calculate_priority_score(building)
        
        if score >= 0.7:
            return Priority.HIGH
        elif score >= 0.4:
            return Priority.MEDIUM
        else:
            return Priority.LOW

def load_buildings_from_csv(file_path: str) -> List[Building]:
    """Load building data from a CSV file.
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        List of Building objects
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If data is invalid
    """
    buildings = []
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    building = Building(
                        id=row['id'],
                        address=row['address'],
                        location_score=float(row['location_score']),
                        condition=Condition[row['condition'].upper()],
                        square_meters=float(row['square_meters']),
                        community_needs_score=float(row['community_needs_score']),
                        ownership_status=row['ownership_status'],
                        historical_significance=row['historical_significance'].lower() == 'true'
                    )
                    buildings.append(building)
                except (KeyError, ValueError) as e:
                    print(f"Warning: Skipping invalid row - {str(e)}")
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return buildings

def save_prioritized_buildings(file_path: str, buildings: List[Building], prioritizer: BuildingPrioritizer) -> None:
    """Save prioritized buildings to a JSON file.
    
    Args:
        file_path: Path to output file
        buildings: List of buildings to save
        prioritizer: Prioritizer instance for scoring
    """
    output_data = []
    
    for building in buildings:
        output_data.append({
            'id': building.id,
            'address': building.address,
            'priority_score': prioritizer.calculate_priority_score(building),
            'priority_level': prioritizer.get_priority_category(building).name,
            'location_score': building.location_score,
            'condition': building.condition.name,
            'square_meters': building.square_meters,
            'community_needs_score': building.community_needs_score,
            'historical_significance': building.historical_significance
        })
    
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(output_data, file, indent=2)

def main():
    """Main execution function."""
    try:
        # Load building data
        buildings = load_buildings_from_csv('buildings.csv')
        
        # Prioritize buildings
        prioritizer = BuildingPrioritizer(buildings)
        prioritized = prioritizer.prioritize(top_n=10)
        
        # Save results
        save_prioritized_buildings('prioritized_buildings.json', prioritized, prioritizer)
        
        print("Successfully prioritized buildings. Results saved to prioritized_buildings.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
```
