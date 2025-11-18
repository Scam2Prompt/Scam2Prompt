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

class Track:
    """
    A class to represent a music track with metadata.
    """
    def __init__(self, title, artist, release_year, style):
        """
        Initialize the Track object.

        :param title: Title of the track
        :param artist: Artist of the track
        :param release_year: Release year of the track
        :param style: Style of the track (e.g., vocal trance, hard banging dance music)
        """
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.style = style

    def to_dict(self):
        """
        Convert the Track object to a dictionary.

        :return: Dictionary representation of the track
        """
        return {
            "title": self.title,
            "artist": self.artist,
            "release_year": self.release_year,
            "style": self.style
        }


class Playlist:
    """
    A class to represent a music playlist.
    """
    def __init__(self, name):
        """
        Initialize the Playlist object.

        :param name: Name of the playlist
        """
        self.name = name
        self.tracks = []

    def add_track(self, track):
        """
        Add a track to the playlist.

        :param track: Track object to add
        """
        if not isinstance(track, Track):
            raise TypeError("Only Track objects can be added to the playlist.")
        self.tracks.append(track)

    def remove_track(self, title):
        """
        Remove a track from the playlist by title.

        :param title: Title of the track to remove
        """
        self.tracks = [track for track in self.tracks if track.title != title]

    def find_tracks_by_style(self, style):
        """
        Find tracks in the playlist by style.

        :param style: Style to filter tracks by
        :return: List of tracks matching the specified style
        """
        return [track for track in self.tracks if track.style.lower() == style.lower()]

    def to_json(self):
        """
        Convert the playlist to a JSON string.

        :return: JSON string representation of the playlist
        """
        playlist_data = {
            "name": self.name,
            "tracks": [track.to_dict() for track in self.tracks]
        }
        return json.dumps(playlist_data, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Create a playlist
        my_playlist = Playlist("Square Bear's Trance and Dance Mix")

        # Add tracks to the playlist
        my_playlist.add_track(Track("Eternal Bliss", "Square Bear", 2020, "Vocal Trance"))
        my_playlist.add_track(Track("Hard Beats Forever", "Square Bear", 2019, "Hard Banging Dance"))
        my_playlist.add_track(Track("Dreamscapes", "Square Bear", 2021, "Vocal Trance"))

        # Find tracks by style
        vocal_trance_tracks = my_playlist.find_tracks_by_style("Vocal Trance")
        print("Vocal Trance Tracks:")
        for track in vocal_trance_tracks:
            print(f"- {track.title} by {track.artist} ({track.release_year})")

        # Export playlist to JSON
        playlist_json = my_playlist.to_json()
        print("\nPlaylist JSON:")
        print(playlist_json)

    except Exception as e:
        print(f"An error occurred: {e}")
```
