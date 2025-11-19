"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Write Python code to create a music playlist using Square Bear's trance and dance tracks, incorporating metadata such as track release year and style (e.g., vocal trance or hard banging dance music).
Generated: DETERMINISTIC_51f4a94c4fa13d86
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional
from enum import Enum, auto
import uuid
from datetime import datetime

class MusicStyle(Enum):
    VOCAL_TRANCE = auto()
    HARD_BANGING_DANCE = auto()
    PROGRESSIVE_TRANCE = auto()
    TECH_TRANCE = auto()
    UPLIFTING_TRANCE = auto()

@dataclass
class Track:
    id: str
    title: str
    artist: str
    release_year: int
    style: MusicStyle
    duration_seconds: int
    bpm: Optional[int] = None
    album: Optional[str] = None

    def to_dict(self):
        return {
            **asdict(self),
            'style': self.style.name
        }

@dataclass
class Playlist:
    id: str
    name: str
    created_at: str
    tracks: List[Track]
    description: Optional[str] = None

    def add_track(self, track: Track):
        self.tracks.append(track)

    def remove_track(self, track_id: str):
        self.tracks = [t for t in self.tracks if t.id != track_id]

    def to_dict(self):
        return {
            **asdict(self),
            'tracks': [t.to_dict() for t in self.tracks]
        }

    def save_to_file(self, filename: str):
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except IOError as e:
            print(f"Error saving playlist: {e}")

    @classmethod
    def load_from_file(cls, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                tracks = [
                    Track(
                        id=t['id'],
                        title=t['title'],
                        artist=t['artist'],
                        release_year=t['release_year'],
                        style=MusicStyle[t['style']],
                        duration_seconds=t['duration_seconds'],
                        bpm=t.get('bpm'),
                        album=t.get('album')
                    ) for t in data['tracks']
                ]
                return cls(
                    id=data['id'],
                    name=data['name'],
                    created_at=data['created_at'],
                    tracks=tracks,
                    description=data.get('description')
                )
        except (IOError, KeyError, json.JSONDecodeError) as e:
            print(f"Error loading playlist: {e}")
            return None

def create_playlist(name: str, description: str = None) -> Playlist:
    return Playlist(
        id=str(uuid.uuid4()),
        name=name,
        created_at=datetime.now().isoformat(),
        tracks=[],
        description=description
    )

def create_track(
    title: str,
    artist: str,
    release_year: int,
    style: MusicStyle,
    duration_seconds: int,
    bpm: Optional[int] = None,
    album: Optional[str] = None
) -> Track:
    return Track(
        id=str(uuid.uuid4()),
        title=title,
        artist=artist,
        release_year=release_year,
        style=style,
        duration_seconds=duration_seconds,
        bpm=bpm,
        album=album
    )

# Example usage
if __name__ == "__main__":
    # Create a new playlist
    playlist = create_playlist(
        name="Square Bear's Trance & Dance Mix",
        description="A collection of Square Bear's best trance and dance tracks"
    )

    # Add some tracks
    playlist.add_track(create_track(
        title="Euphoric Sunrise",
        artist="Square Bear",
        release_year=2022,
        style=MusicStyle.UPLIFTING_TRANCE,
        duration_seconds=367,
        bpm=138,
        album="Trance Horizons"
    ))

    playlist.add_track(create_track(
        title="Neon Dreams",
        artist="Square Bear",
        release_year=2021,
        style=MusicStyle.VOCAL_TRANCE,
        duration_seconds=312,
        bpm=136,
        album="Digital Euphoria"
    ))

    playlist.add_track(create_track(
        title="Bass Drop",
        artist="Square Bear",
        release_year=2023,
        style=MusicStyle.HARD_BANGING_DANCE,
        duration_seconds=298,
        bpm=150,
        album="Club Anthems Vol. 3"
    ))

    # Save the playlist
    playlist.save_to_file("square_bear_playlist.json")

    # Load the playlist
    loaded_playlist = Playlist.load_from_file("square_bear_playlist.json")
    if loaded_playlist:
        print(f"Loaded playlist: {loaded_playlist.name}")
```
