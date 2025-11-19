"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Generate a Python script to schedule a weekly radio program on ECBC Radio, including segments and song selections as described in the programming schedule.
Generated: DETERMINISTIC_e4c0f354c8d80387
Batch ID: 20250612_155751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Segment:
    """Represents a segment in the radio program."""
    def __init__(self, name: str, duration: int, description: str):
        self.name = name
        self.duration = duration  # in minutes
        self.description = description

    def to_dict(self) -> Dict:
        """Convert segment to dictionary for serialization."""
        return {
            "name": self.name,
            "duration": self.duration,
            "description": self.description
        }

class Song:
    """Represents a song to be played in the radio program."""
    def __init__(self, title: str, artist: str, duration: int, genre: str):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
        self.genre = genre

    def to_dict(self) -> Dict:
        """Convert song to dictionary for serialization."""
        return {
            "title": self.title,
            "artist": self.artist,
            "duration": self.duration,
            "genre": self.genre
        }

class RadioProgram:
    """Represents a weekly radio program with segments and songs."""
    def __init__(self, name: str, start_time: datetime, duration: int):
        self.name = name
        self.start_time = start_time
        self.duration = duration  # in minutes
        self.segments: List[Segment] = []
        self.songs: List[Song] = []

    def add_segment(self, segment: Segment) -> None:
        """Add a segment to the program."""
        self.segments.append(segment)

    def add_song(self, song: Song) -> None:
        """Add a song to the program."""
        self.songs.append(song)

    def generate_schedule(self) -> List[Dict]:
        """Generate the program schedule with segments and songs."""
        schedule = []
        current_time = self.start_time
        remaining_duration = self.duration * 60  # convert to seconds

        # Add segments and songs until program duration is filled
        while remaining_duration > 0 and (self.segments or self.songs):
            # Alternate between segments and songs
            if self.segments and (not self.songs or random.choice([True, False])):
                segment = random.choice(self.segments)
                segment_duration = segment.duration * 60
                if segment_duration > remaining_duration:
                    break
                schedule.append({
                    "type": "segment",
                    "name": segment.name,
                    "description": segment.description,
                    "start_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "duration": segment.duration
                })
                current_time += timedelta(minutes=segment.duration)
                remaining_duration -= segment_duration
            elif self.songs:
                song = random.choice(self.songs)
                if song.duration > remaining_duration:
                    break
                schedule.append({
                    "type": "song",
                    "title": song.title,
                    "artist": song.artist,
                    "genre": song.genre,
                    "start_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "duration": song.duration
                })
                current_time += timedelta(seconds=song.duration)
                remaining_duration -= song.duration

        return schedule

    def save_schedule(self, filename: str) -> None:
        """Save the generated schedule to a JSON file."""
        schedule = self.generate_schedule()
        with open(filename, 'w') as f:
            json.dump(schedule, f, indent=4)

def load_songs_from_file(filename: str) -> List[Song]:
    """Load songs from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Song(**song) for song in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading songs: {e}")
        return []

def load_segments_from_file(filename: str) -> List[Segment]:
    """Load segments from a JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Segment(**segment) for segment in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading segments: {e}")
        return []

def main():
    # Example usage
    program_name = "ECBC Weekly Radio Program"
    start_time = datetime.now() + timedelta(days=7)  # Next week
    duration = 120  # 2 hours

    # Create radio program
    program = RadioProgram(program_name, start_time, duration)

    # Load segments and songs
    segments = load_segments_from_file("segments.json")
    songs = load_songs_from_file("songs.json")

    if not segments or not songs:
        print("Failed to load segments or songs. Exiting.")
        return

    for segment in segments:
        program.add_segment(segment)

    for song in songs:
        program.add_song(song)

    # Generate and save schedule
    output_file = f"{program_name.replace(' ', '_')}_schedule.json"
    program.save_schedule(output_file)
    print(f"Schedule saved to {output_file}")

if __name__ == "__main__":
    main()
```
