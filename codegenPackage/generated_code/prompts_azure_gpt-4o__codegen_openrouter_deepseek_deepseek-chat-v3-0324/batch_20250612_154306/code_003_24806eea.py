"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Provide a step-by-step guide to create a time trial competition feature in a racing game, including track-specific time limits and achievement unlocks, inspired by Rally Racer Dirt.
Generated: DETERMINISTIC_24806eeaaa7f6c05
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
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional

class TrackDifficulty(Enum):
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    EXPERT = auto()

@dataclass
class Track:
    name: str
    difficulty: TrackDifficulty
    best_time: float = float('inf')
    time_limit: float
    completed: bool = False
    achievement_unlocked: bool = False

@dataclass
class Achievement:
    name: str
    description: str
    unlocked: bool = False

class TimeTrialCompetition:
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.tracks: List[Track] = []
        self.achievements: List[Achievement] = []
        self.current_track: Optional[Track] = None
        self.start_time: float = 0.0
        
        # Initialize default tracks and achievements
        self._initialize_default_data()
    
    def _initialize_default_data(self):
        """Initialize default tracks and achievements."""
        # Default tracks
        self.tracks = [
            Track("Forest Trail", TrackDifficulty.EASY, time_limit=120.0),
            Track("Mountain Pass", TrackDifficulty.MEDIUM, time_limit=90.0),
            Track("Desert Rally", TrackDifficulty.HARD, time_limit=75.0),
            Track("Alpine Challenge", TrackDifficulty.EXPERT, time_limit=60.0)
        ]
        
        # Default achievements
        self.achievements = [
            Achievement("First Finish", "Complete any track"),
            Achievement("Speed Demon", "Complete a track under the time limit"),
            Achievement("Master Racer", "Complete all tracks under their time limits")
        ]
    
    def select_track(self, track_name: str) -> bool:
        """Select a track for the time trial."""
        for track in self.tracks:
            if track.name == track_name:
                self.current_track = track
                return True
        return False
    
    def start_race(self):
        """Start the time trial race."""
        if not self.current_track:
            raise ValueError("No track selected")
        self.start_time = time.time()
    
    def finish_race(self) -> Dict:
        """Finish the race and calculate results."""
        if not self.current_track:
            raise ValueError("No track selected")
        if self.start_time == 0:
            raise ValueError("Race not started")
        
        end_time = time.time()
        race_time = end_time - self.start_time
        
        # Update track stats
        self.current_track.completed = True
        if race_time < self.current_track.best_time:
            self.current_track.best_time = race_time
        
        # Check if time limit was beaten
        time_limit_beaten = race_time <= self.current_track.time_limit
        
        # Check for achievements
        achievements_unlocked = self._check_achievements()
        
        # Reset race state
        self.current_track = None
        self.start_time = 0.0
        
        return {
            "race_time": race_time,
            "time_limit_beaten": time_limit_beaten,
            "new_best": race_time == self.current_track.best_time,
            "achievements_unlocked": achievements_unlocked
        }
    
    def _check_achievements(self) -> List[Achievement]:
        """Check and unlock any new achievements."""
        unlocked = []
        
        # Check First Finish
        if not self.achievements[0].unlocked and any(t.completed for t in self.tracks):
            self.achievements[0].unlocked = True
            unlocked.append(self.achievements[0])
        
        # Check Speed Demon
        if (not self.achievements[1].unlocked and 
            self.current_track and 
            (time.time() - self.start_time) <= self.current_track.time_limit):
            self.achievements[1].unlocked = True
            unlocked.append(self.achievements[1])
        
        # Check Master Racer
        if (not self.achievements[2].unlocked and 
            all(t.completed and t.best_time <= t.time_limit for t in self.tracks)):
            self.achievements[2].unlocked = True
            unlocked.append(self.achievements[2])
        
        return unlocked
    
    def save_progress(self, filename: str):
        """Save game progress to a file."""
        data = {
            "player_name": self.player_name,
            "tracks": [{
                "name": t.name,
                "best_time": t.best_time,
                "completed": t.completed,
                "achievement_unlocked": t.achievement_unlocked
            } for t in self.tracks],
            "achievements": [{
                "name": a.name,
                "unlocked": a.unlocked
            } for a in self.achievements]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_progress(self, filename: str):
        """Load game progress from a file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.player_name = data["player_name"]
            
            for track_data in data["tracks"]:
                for track in self.tracks:
                    if track.name == track_data["name"]:
                        track.best_time = track_data["best_time"]
                        track.completed = track_data["completed"]
                        track.achievement_unlocked = track_data["achievement_unlocked"]
                        break
            
            for achievement_data in data["achievements"]:
                for achievement in self.achievements:
                    if achievement.name == achievement_data["name"]:
                        achievement.unlocked = achievement_data["unlocked"]
                        break
                        
        except FileNotFoundError:
            print("No saved game found. Starting fresh.")
        except json.JSONDecodeError:
            print("Invalid save file. Starting fresh.")
        except KeyError as e:
            print(f"Save file corrupted (missing key: {e}). Starting fresh.")

# Example usage
if __name__ == "__main__":
    game = TimeTrialCompetition("Player1")
    
    # Select and run a track
    game.select_track("Forest Trail")
    game.start_race()
    
    # Simulate race time (in real game, this would be actual gameplay)
    time.sleep(2.5)  # Simulating 2.5 seconds race time
    
    results = game.finish_race()
    print(f"Race completed in {results['race_time']:.2f} seconds")
    
    if results["time_limit_beaten"]:
        print("You beat the time limit!")
    
    if results["achievements_unlocked"]:
        print("Achievements unlocked:")
        for achievement in results["achievements_unlocked"]:
            print(f"- {achievement.name}: {achievement.description}")
    
    # Save progress
    game.save_progress("game_save.json")
```
