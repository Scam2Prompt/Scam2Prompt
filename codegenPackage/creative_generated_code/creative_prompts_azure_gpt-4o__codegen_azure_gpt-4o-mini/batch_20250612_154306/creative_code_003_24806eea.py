"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Provide a step-by-step guide to create a time trial competition feature in a racing game, including track-specific time limits and achievement unlocks, inspired by Rally Racer Dirt.
Generated: DETERMINISTIC_24806eeaaa7f6c05
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Track:
    """Class representing a race track."""
    name: str
    time_limit: int  # Time limit in seconds
    best_time: Optional[int] = None  # Best time achieved on the track
    achievements: List[str] = field(default_factory=list)

@dataclass
class Racer:
    """Class representing a racer."""
    name: str
    completed_tracks: Dict[str, int] = field(default_factory=dict)  # Track name mapped to best time

class TimeTrialCompetition:
    """Class handling the time trial competition logic."""
    
    def __init__(self):
        """Initialize an empty competition with no tracks or racers."""
        self.tracks: List[Track] = []
        self.racers: List[Racer] = []

    def add_track(self, name: str, time_limit: int):
        """Add a new track to the competition."""
        new_track = Track(name=name, time_limit=time_limit)
        self.tracks.append(new_track)

    def register_racer(self, name: str):
        """Register a new racer in the competition."""
        new_racer = Racer(name=name)
        self.racers.append(new_racer)

    def start_time_trial(self, racer_name: str, track_name: str):
        """Start a time trial for a given racer on a specific track."""
        # Find the racer and track
        racer = self._find_racer(racer_name)
        track = self._find_track(track_name)

        # Start the timer
        if racer and track:
            print(f"Starting time trial for {racer.name} on {track.name}.")
            start_time = time.time()
            time.sleep(1)  # Simulate the race duration for testing purposes
            end_time = time.time()

            # Calculate the elapsed time
            elapsed_time = int(end_time - start_time)  # Round to seconds

            self._evaluate_time(elapsed_time, racer, track)
        else:
            print("Racer or track not found.")

    def _evaluate_time(self, elapsed_time: int, racer: Racer, track: Track):
        """Evaluate the time taken by the racer."""
        # Check if the elapsed time is within the time limit
        if elapsed_time <= track.time_limit:
            print(f"{racer.name} completed {track.name} in {elapsed_time} seconds.")
            self._update_best_time(racer, track, elapsed_time)
            self._check_achievements(racer, track)
        else:
            print(f"{racer.name} did not complete {track.name} in time. Time limit: {track.time_limit}s, elapsed: {elapsed_time}s.")

    def _update_best_time(self, racer: Racer, track: Track, elapsed_time: int):
        """Update the racer's best time for the track."""
        racer.completed_tracks[track.name] = elapsed_time
        if track.best_time is None or elapsed_time < track.best_time:
            track.best_time = elapsed_time
            print(f"New best time for {track.name}: {elapsed_time} seconds.")

    def _check_achievements(self, racer: Racer, track: Track):
        """Check and unlock achievements for the racer."""
        # Example achievement: Completing a track under half the time limit
        if track.best_time and track.best_time < track.time_limit / 2:
            achievement = f"Speed Demon on {track.name}"
            if achievement not in track.achievements:
                track.achievements.append(achievement)
                print(f"Achievement unlocked: {achievement} for {racer.name}!")

    def _find_racer(self, name: str) -> Optional[Racer]:
        """Find a racer by name."""
        for racer in self.racers:
            if racer.name == name:
                return racer
        return None

    def _find_track(self, name: str) -> Optional[Track]:
        """Find a track by name."""
        for track in self.tracks:
            if track.name == name:
                return track
        return None

# Example usage:
if __name__ == "__main__":
    competition = TimeTrialCompetition()
    competition.add_track("Desert Rally", 120)
    competition.register_racer("Speedster")

    competition.start_time_trial("Speedster", "Desert Rally")
```
