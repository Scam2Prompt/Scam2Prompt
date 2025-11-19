"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Develop a function to calculate and display player achievements based on track completion times and drifting performance, inspired by Rally Racer Dirt's achievement system.
Generated: DETERMINISTIC_a93125d6caa0b95e
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class AchievementLevel(Enum):
    """Enum representing different achievement levels."""
    BRONZE = auto()
    SILVER = auto()
    GOLD = auto()
    PLATINUM = auto()

@dataclass
class Achievement:
    """Data class representing an achievement."""
    name: str
    description: str
    level: AchievementLevel
    unlocked: bool = False

class TrackType(Enum):
    """Enum representing different track types."""
    FOREST = "Forest"
    DESERT = "Desert"
    MOUNTAIN = "Mountain"
    CITY = "City"

@dataclass
class TrackPerformance:
    """Data class representing player performance on a track."""
    track_name: str
    track_type: TrackType
    completion_time: float  # in seconds
    drift_score: float
    perfect_drift_count: int
    crash_count: int

class AchievementSystem:
    """System for managing and calculating player achievements."""
    
    def __init__(self):
        self.achievements: List[Achievement] = []
        self._initialize_achievements()
    
    def _initialize_achievements(self):
        """Initialize the default set of achievements."""
        self.achievements = [
            Achievement(
                name="Speed Demon",
                description="Complete any track under the target time",
                level=AchievementLevel.BRONZE
            ),
            Achievement(
                name="Drift King",
                description="Achieve a high drift score on any track",
                level=AchievementLevel.SILVER
            ),
            Achievement(
                name="Perfect Drifter",
                description="Complete a track with perfect drifts and no crashes",
                level=AchievementLevel.GOLD
            ),
            Achievement(
                name="Track Master",
                description="Complete all track types under target time with perfect drifts",
                level=AchievementLevel.PLATINUM
            )
        ]
    
    def calculate_achievements(self, performances: List[TrackPerformance]) -> List[Achievement]:
        """
        Calculate which achievements should be unlocked based on track performances.
        
        Args:
            performances: List of TrackPerformance objects representing player's performance
            
        Returns:
            List of updated achievements with unlocked status
        """
        # Make a copy of achievements to avoid modifying the original
        updated_achievements = [Achievement(**a.__dict__) for a in self.achievements]
        
        # Check each achievement condition
        for achievement in updated_achievements:
            if achievement.name == "Speed Demon" and not achievement.unlocked:
                achievement.unlocked = any(
                    self._is_fast_time(performance.completion_time, performance.track_type)
                    for performance in performances
                )
            
            elif achievement.name == "Drift King" and not achievement.unlocked:
                achievement.unlocked = any(
                    performance.drift_score >= 5000
                    for performance in performances
                )
            
            elif achievement.name == "Perfect Drifter" and not achievement.unlocked:
                achievement.unlocked = any(
                    performance.perfect_drift_count >= 10 and performance.crash_count == 0
                    for performance in performances
                )
            
            elif achievement.name == "Track Master" and not achievement.unlocked:
                track_types_completed = set()
                for performance in performances:
                    if (self._is_fast_time(performance.completion_time, performance.track_type) and
                        performance.perfect_drift_count >= 10 and
                        performance.crash_count == 0):
                        track_types_completed.add(performance.track_type)
                
                achievement.unlocked = len(track_types_completed) == len(TrackType)
        
        return updated_achievements
    
    def _is_fast_time(self, time: float, track_type: TrackType) -> bool:
        """Check if completion time is fast enough for the track type."""
        target_times = {
            TrackType.FOREST: 120.0,
            TrackType.DESERT: 150.0,
            TrackType.MOUNTAIN: 180.0,
            TrackType.CITY: 90.0
        }
        return time <= target_times[track_type]
    
    def display_achievements(self, achievements: List[Achievement]):
        """Display the achievements in a formatted way."""
        print("\n=== PLAYER ACHIEVEMENTS ===\n")
        for achievement in achievements:
            status = "UNLOCKED" if achievement.unlocked else "Locked"
            print(f"{achievement.name} ({achievement.level.name}) - {status}")
            print(f"  {achievement.description}\n")
    
    def save_achievements(self, achievements: List[Achievement], filename: str):
        """Save achievements to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([a.__dict__ for a in achievements], f, indent=2)
        except IOError as e:
            print(f"Error saving achievements: {e}")
    
    def load_achievements(self, filename: str) -> Optional[List[Achievement]]:
        """Load achievements from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return [Achievement(**item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading achievements: {e}")
            return None

# Example usage
if __name__ == "__main__":
    system = AchievementSystem()
    
    # Sample track performances
    performances = [
        TrackPerformance(
            track_name="Forest Rush",
            track_type=TrackType.FOREST,
            completion_time=115.5,
            drift_score=4500,
            perfect_drift_count=8,
            crash_count=1
        ),
        TrackPerformance(
            track_name="Desert Storm",
            track_type=TrackType.DESERT,
            completion_time=145.0,
            drift_score=5200,
            perfect_drift_count=12,
            crash_count=0
        ),
        TrackPerformance(
            track_name="Mountain Peak",
            track_type=TrackType.MOUNTAIN,
            completion_time=175.0,
            drift_score=6000,
            perfect_drift_count=15,
            crash_count=0
        ),
        TrackPerformance(
            track_name="City Sprint",
            track_type=TrackType.CITY,
            completion_time=85.0,
            drift_score=4800,
            perfect_drift_count=10,
            crash_count=0
        )
    ]
    
    # Calculate and display achievements
    updated_achievements = system.calculate_achievements(performances)
    system.display_achievements(updated_achievements)
    
    # Save achievements to file
    system.save_achievements(updated_achievements, "player_achievements.json")
```
