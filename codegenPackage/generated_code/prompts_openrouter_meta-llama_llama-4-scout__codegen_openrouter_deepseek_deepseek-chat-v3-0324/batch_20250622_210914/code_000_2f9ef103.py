"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Write a Python script to recommend trekking routes in Nepal based on a user's fitness level and preferred mountain range, considering routes like Everest Base Camp Trek and Annapurna Base Camp Trek.
Generated: DETERMINISTIC_2f9ef10302f442f6
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class FitnessLevel(Enum):
    """Enum representing user fitness levels."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class MountainRange(Enum):
    """Enum representing available mountain ranges in Nepal."""
    EVEREST = "everest"
    ANNAPURNA = "annapurna"
    LANGTANG = "langtang"
    MANASLU = "manaslu"

class TrekkingRoute:
    """Class representing a trekking route with its attributes."""
    
    def __init__(
        self,
        name: str,
        mountain_range: MountainRange,
        difficulty: FitnessLevel,
        duration_days: int,
        max_altitude: int,
        description: str
    ):
        self.name = name
        self.mountain_range = mountain_range
        self.difficulty = difficulty
        self.duration_days = duration_days
        self.max_altitude = max_altitude
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert route details to dictionary for easy serialization."""
        return {
            "name": self.name,
            "mountain_range": self.mountain_range.value,
            "difficulty": self.difficulty.value,
            "duration_days": self.duration_days,
            "max_altitude": self.max_altitude,
            "description": self.description
        }

class TrekkingRouteRecommender:
    """Main class for recommending trekking routes based on user preferences."""
    
    def __init__(self):
        self.routes = self._load_routes()
    
    def _load_routes(self) -> List[TrekkingRoute]:
        """Load and initialize trekking routes data."""
        return [
            TrekkingRoute(
                name="Everest Base Camp Trek",
                mountain_range=MountainRange.EVEREST,
                difficulty=FitnessLevel.INTERMEDIATE,
                duration_days=12,
                max_altitude=5545,
                description="Classic trek to the base of the world's highest peak."
            ),
            TrekkingRoute(
                name="Annapurna Base Camp Trek",
                mountain_range=MountainRange.ANNAPURNA,
                difficulty=FitnessLevel.INTERMEDIATE,
                duration_days=10,
                max_altitude=4130,
                description="Beautiful trek through diverse landscapes to Annapurna sanctuary."
            ),
            TrekkingRoute(
                name="Langtang Valley Trek",
                mountain_range=MountainRange.LANGTANG,
                difficulty=FitnessLevel.BEGINNER,
                duration_days=8,
                max_altitude=3870,
                description="Less crowded trek with stunning valley views and Tibetan culture."
            ),
            TrekkingRoute(
                name="Manaslu Circuit Trek",
                mountain_range=MountainRange.MANASLU,
                difficulty=FitnessLevel.ADVANCED,
                duration_days=14,
                max_altitude=5106,
                description="Challenging trek around the eighth highest mountain in the world."
            )
        ]
    
    def recommend_routes(
        self,
        fitness_level: str,
        mountain_range: Optional[str] = None
    ) -> List[Dict]:
        """
        Recommend routes based on fitness level and optional mountain range preference.
        
        Args:
            fitness_level: User's fitness level (beginner, intermediate, advanced)
            mountain_range: Preferred mountain range (optional)
            
        Returns:
            List of recommended routes matching the criteria
        """
        try:
            # Validate fitness level
            fitness = FitnessLevel(fitness_level.lower())
            
            # Filter routes by fitness level
            filtered_routes = [
                route for route in self.routes
                if route.difficulty.value == fitness.value
            ]
            
            # Further filter by mountain range if specified
            if mountain_range:
                try:
                    preferred_range = MountainRange(mountain_range.lower())
                    filtered_routes = [
                        route for route in filtered_routes
                        if route.mountain_range.value == preferred_range.value
                    ]
                except ValueError:
                    raise ValueError(f"Invalid mountain range. Available options: {[r.value for r in MountainRange]}")
            
            # Convert routes to dictionaries for output
            return [route.to_dict() for route in filtered_routes]
            
        except ValueError as e:
            raise ValueError(f"Invalid input: {str(e)}. Available fitness levels: {[l.value for l in FitnessLevel]}")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")

def main():
    """Main function to demonstrate the recommender system."""
    recommender = TrekkingRouteRecommender()
    
    print("Welcome to Nepal Trekking Route Recommender!")
    print("Available mountain ranges:", [r.value for r in MountainRange])
    print("Available fitness levels:", [l.value for l in FitnessLevel])
    
    try:
        fitness = input("Enter your fitness level (beginner/intermediate/advanced): ").strip()
        mountain_pref = input("Enter preferred mountain range (optional, press enter to skip): ").strip()
        
        recommendations = recommender.recommend_routes(
            fitness_level=fitness,
            mountain_range=mountain_pref if mountain_pref else None
        )
        
        if not recommendations:
            print("No routes match your criteria. Try different parameters.")
        else:
            print("\nRecommended Routes:")
            for idx, route in enumerate(recommendations, 1):
                print(f"\n{idx}. {route['name']}")
                print(f"Mountain Range: {route['mountain_range'].title()}")
                print(f"Difficulty: {route['difficulty'].title()}")
                print(f"Duration: {route['duration_days']} days")
                print(f"Max Altitude: {route['max_altitude']} meters")
                print(f"Description: {route['description']}")
    
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
