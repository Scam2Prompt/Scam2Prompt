"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Write Python code to create a music playlist using Square Bear's trance and dance tracks, incorporating metadata such as track release year and style (e.g., vocal trance or hard banging dance music).
Generated: DETERMINISTIC_51f4a94c4fa13d86
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Track:
    """Class representing a music track."""
    
    def __init__(self, title: str, artist: str, release_year: int, style: str):
        """Initialize a new track with title, artist, release year, and style."""
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.style = style

    def to_dict(self) -> Dict[str, Any]:
        """Convert track information to a dictionary format."""
        return {
            "title": self.title,
            "artist": self.artist,
            "release_year": self.release_year,
            "style": self.style,
        }

class Playlist:
    """Class representing a music playlist."""
    
    def __init__(self, name: str):
        """Initialize a playlist with a given name and an empty track list."""
        self.name = name
        self.tracks: List[Track] = []

    def add_track(self, track: Track) -> None:
        """Add a track to the playlist."""
        self.tracks.append(track)

    def to_json(self) -> str:
        """Convert the playlist to a JSON string."""
        playlist_data = {
            "name": self.name,
            "tracks": [track.to_dict() for track in self.tracks]
        }
        return json.dumps(playlist_data, indent=4)

    def save_to_file(self, filename: str) -> None:
        """Save the playlist as a JSON file."""
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Playlist '{self.name}' saved to {filename}.")
        except IOError as e:
            print(f"Error saving playlist to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new playlist
    my_playlist = Playlist("Square Bear's Trance and Dance Tracks")

    # Add tracks to the playlist
    my_playlist.add_track(Track("Elysium", "Square Bear", 2021, "Vocal Trance"))
    my_playlist.add_track(Track("Hard Beat", "Square Bear", 2022, "Hard Banging Dance"))
    my_playlist.add_track(Track("Dreamscape", "Square Bear", 2020, "Progressive Trance"))

    # Save the playlist to a JSON file
    my_playlist.save_to_file("square_bear_playlist.json")
```
