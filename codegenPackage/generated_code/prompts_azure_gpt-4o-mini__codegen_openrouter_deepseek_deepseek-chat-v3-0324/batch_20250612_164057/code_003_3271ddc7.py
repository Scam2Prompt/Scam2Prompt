"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: Develop a script that recommends the best time to visit Tanzania for a Serengeti Migration Safari, considering factors like weather and wildlife activity.
Generated: DETERMINISTIC_3271ddc70c2755fd
Batch ID: 20250612_164057
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

class Month(Enum):
    """Enum representing months of the year."""
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Season(Enum):
    """Enum representing seasons in Tanzania."""
    DRY = "Dry Season"
    WET = "Wet Season"
    SHORT_RAINS = "Short Rains"
    LONG_RAINS = "Long Rains"

class WildlifeActivity(Enum):
    """Enum representing wildlife activity levels."""
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class MigrationPhase(Enum):
    """Enum representing Serengeti migration phases."""
    CALVING = "Calving (Southern Serengeti)"
    GRUMETI = "Grumeti River Crossing"
    MARA = "Mara River Crossing"
    DISPERSED = "Dispersed (Central/Western Serengeti)"

class SafariRecommendation:
    """Class representing a recommendation for the best time to visit."""
    
    def __init__(
        self,
        months: List[Month],
        season: Season,
        wildlife_activity: WildlifeActivity,
        migration_phase: MigrationPhase,
        description: str
    ):
        self.months = months
        self.season = season
        self.wildlife_activity = wildlife_activity
        self.migration_phase = migration_phase
        self.description = description
    
    def to_dict(self) -> Dict:
        """Convert the recommendation to a dictionary."""
        return {
            "months": [month.name for month in self.months],
            "season": self.season.value,
            "wildlife_activity": self.wildlife_activity.value,
            "migration_phase": self.migration_phase.value,
            "description": self.description
        }

def get_recommendations() -> List[SafariRecommendation]:
    """Get a list of recommendations for the best times to visit Serengeti."""
    return [
        SafariRecommendation(
            months=[Month.JANUARY, Month.FEBRUARY, Month.MARCH],
            season=Season.WET,
            wildlife_activity=WildlifeActivity.HIGH,
            migration_phase=MigrationPhase.CALVING,
            description="Best for calving season in Southern Serengeti. High wildlife activity with predator-prey interactions."
        ),
        SafariRecommendation(
            months=[Month.JUNE, Month.JULY],
            season=Season.DRY,
            wildlife_activity=WildlifeActivity.HIGH,
            migration_phase=MigrationPhase.GRUMETI,
            description="Ideal for Grumeti River crossings. Dry weather and high concentration of wildlife."
        ),
        SafariRecommendation(
            months=[Month.AUGUST, Month.SEPTEMBER, Month.OCTOBER],
            season=Season.DRY,
            wildlife_activity=WildlifeActivity.HIGH,
            migration_phase=MigrationPhase.MARA,
            description="Peak for Mara River crossings. Dramatic wildlife scenes with migrating herds."
        ),
        SafariRecommendation(
            months=[Month.NOVEMBER, Month.DECEMBER],
            season=Season.SHORT_RAINS,
            wildlife_activity=WildlifeActivity.MEDIUM,
            migration_phase=MigrationPhase.DISPERSED,
            description="Short rains with dispersed herds. Fewer crowds and lush landscapes."
        )
    ]

def recommend_best_time(
    preferred_season: Optional[Season] = None,
    preferred_activity: Optional[WildlifeActivity] = None
) -> List[Dict]:
    """
    Recommend the best time to visit Serengeti based on preferences.
    
    Args:
        preferred_season: Optional preferred season filter.
        preferred_activity: Optional preferred wildlife activity level filter.
    
    Returns:
        List of recommendation dictionaries matching the criteria.
    """
    recommendations = get_recommendations()
    
    filtered = []
    for rec in recommendations:
        if preferred_season and rec.season != preferred_season:
            continue
        if preferred_activity and rec.wildlife_activity != preferred_activity:
            continue
        filtered.append(rec.to_dict())
    
    return filtered

def main():
    """Main function to demonstrate recommendation functionality."""
    print("Serengeti Migration Safari Recommendations")
    print("=" * 40)
    
    # Get all recommendations
    all_recommendations = recommend_best_time()
    print("\nAll Recommendations:")
    print(json.dumps(all_recommendations, indent=2))
    
    # Filter by dry season
    dry_season_recommendations = recommend_best_time(preferred_season=Season.DRY)
    print("\nDry Season Recommendations:")
    print(json.dumps(dry_season_recommendations, indent=2))
    
    # Filter by high wildlife activity
    high_activity_recommendations = recommend_best_time(preferred_activity=WildlifeActivity.HIGH)
    print("\nHigh Wildlife Activity Recommendations:")
    print(json.dumps(high_activity_recommendations, indent=2))

if __name__ == "__main__":
    main()
```
