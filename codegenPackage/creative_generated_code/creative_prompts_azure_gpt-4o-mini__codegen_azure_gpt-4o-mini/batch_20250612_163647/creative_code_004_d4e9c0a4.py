"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://play-gamer.com
Prompt: Provide an example of how to design a track layout for an off-road racing game that challenges players, as seen in Rally Racer Dirt.
Generated: DETERMINISTIC_d4e9c0a410daa97d
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class TrackSegment:
    """Class representing a segment of the track."""
    
    def __init__(self, terrain: str, length: float, difficulty: int):
        """
        Initialize a track segment.

        Parameters:
        terrain (str): The type of terrain (e.g., 'mud', 'gravel', 'sand').
        length (float): The length of the segment in meters.
        difficulty (int): Difficulty level of the segment (1-10).
        """
        self.terrain = terrain
        self.length = length
        self.difficulty = difficulty

    def __str__(self):
        return f"Segment(terrain={self.terrain}, length={self.length}m, difficulty={self.difficulty})"


class TrackLayout:
    """Class to design the layout of the racing track."""
    
    def __init__(self):
        """Initialize an empty track layout."""
        self.segments: List[TrackSegment] = []
    
    def add_segment(self, terrain: str, length: float, difficulty: int):
        """
        Add a new segment to the track layout.

        Parameters:
        terrain (str): The type of terrain for the segment.
        length (float): The length of the segment.
        difficulty (int): Difficulty level of the segment.

        Raises:
        ValueError: If the difficulty is out of range or length is negative.
        """
        if not (1 <= difficulty <= 10):
            raise ValueError("Difficulty must be between 1 and 10.")
        if length < 0:
            raise ValueError("Length must be non-negative.")

        segment = TrackSegment(terrain, length, difficulty)
        self.segments.append(segment)
    
    def generate_random_track(self, num_segments: int):
        """
        Generate a random track with a specified number of segments.

        Parameters:
        num_segments (int): The number of segments to generate.
        """
        terrains = ['mud', 'gravel', 'sand', 'rock', 'forest']
        for _ in range(num_segments):
            terrain = random.choice(terrains)
            length = random.uniform(100, 1000)  # Length between 100m to 1000m
            difficulty = random.randint(1, 10)
            self.add_segment(terrain, length, difficulty)

    def display_track(self):
        """Display the track layout segments."""
        print("Track Layout:")
        for segment in self.segments:
            print(segment)


# Example usage
if __name__ == "__main__":
    try:
        track = TrackLayout()
        track.generate_random_track(num_segments=5)
        track.display_track()
    except ValueError as e:
        print(f"Error: {e}")
```
