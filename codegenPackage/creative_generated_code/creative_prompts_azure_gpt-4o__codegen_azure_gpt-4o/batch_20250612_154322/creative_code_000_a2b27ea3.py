"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Write Python code to simulate a portable music player interface with customizable playlists and support for major audio formats, inspired by the features described on Duckchain.world.
Generated: DETERMINISTIC_a2b27ea3aadb1ea5
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os


class AudioFile:
    """
    Represents an audio file with metadata such as name and file format.
    """

    SUPPORTED_FORMATS = {'mp3', 'wav', 'flac', 'aac', 'ogg'}

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.name = os.path.basename(file_path)
        self.format = self._get_file_format()

        if not self._is_supported_format():
            raise ValueError(f"Unsupported audio format: {self.format}")

    def _get_file_format(self):
        """
        Extracts the file format from the file name.
        """
        return self.name.split('.')[-1].lower()

    def _is_supported_format(self):
        """
        Checks if the audio file format is supported.
        """
        return self.format in self.SUPPORTED_FORMATS

    def __str__(self):
        return f"{self.name} ({self.format})"


class Playlist:
    """
    Represents a playlist containing multiple audio files.
    """

    def __init__(self, name: str):
        self.name = name
        self.tracks = []

    def add_track(self, audio_file: AudioFile):
        """
        Adds an audio file to the playlist.
        """
        self.tracks.append(audio_file)

    def remove_track(self, track_name: str):
        """
        Removes an audio file from the playlist by name.
        """
        self.tracks = [track for track in self.tracks if track.name != track_name]

    def list_tracks(self):
        """
        Lists all tracks in the playlist.
        """
        if not self.tracks:
            print(f"The playlist '{self.name}' is empty.")
        else:
            print(f"Playlist: {self.name}")
            for idx, track in enumerate(self.tracks, 1):
                print(f"{idx}. {track}")

    def __len__(self):
        """
        Returns the number of tracks in the playlist.
        """
        return len(self.tracks)


class MusicPlayer:
    """
    Represents a portable music player with support for playlists and playback.
    """

    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name: str):
        """
        Creates a new playlist.
        """
        if name in self.playlists:
            raise ValueError(f"A playlist named '{name}' already exists.")
        self.playlists[name] = Playlist(name)
        print(f"Playlist '{name}' created successfully.")

    def delete_playlist(self, name: str):
        """
        Deletes an existing playlist.
        """
        if name not in self.playlists:
            raise ValueError(f"No playlist named '{name}' exists.")
        del self.playlists[name]
        print(f"Playlist '{name}' deleted successfully.")

    def add_track_to_playlist(self, playlist_name: str, audio_file_path: str):
        """
        Adds a track to a specified playlist.
        """
        if playlist_name not in self.playlists:
            raise ValueError(f"No playlist named '{playlist_name}' exists.")
        try:
            audio_file = AudioFile(audio_file_path)
            self.playlists[playlist_name].add_track(audio_file)
            print(f"Track '{audio_file.name}' added to playlist '{playlist_name}'.")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_track_from_playlist(self, playlist_name: str, track_name: str):
        """
        Removes a track from a specified playlist.
        """
        if playlist_name not in self.playlists:
            raise ValueError(f"No playlist named '{playlist_name}' exists.")
        self.playlists[playlist_name].remove_track(track_name)
        print(f"Track '{track_name}' removed from playlist '{playlist_name}'.")

    def list_playlists(self):
        """
        Lists all playlists and their respective tracks.
        """
        if not self.playlists:
            print("No playlists available.")
        else:
            print("Available Playlists:")
            for playlist in self.playlists.values():
                playlist.list_tracks()

    def play_track(self, playlist_name: str, track_name: str):
        """
        Simulates playing a track from a specified playlist.
        """
        if playlist_name not in self.playlists:
            raise ValueError(f"No playlist named '{playlist_name}' exists.")
        playlist = self.playlists[playlist_name]
        for track in playlist.tracks:
            if track.name == track_name:
                print(f"Playing track: {track}")
                return
        print(f"Track '{track_name}' not found in playlist '{playlist_name}'.")


if __name__ == "__main__":
    # Example usage of the MusicPlayer class:
    player = MusicPlayer()
    player.create_playlist("Favorites")
    player.add_track_to_playlist("Favorites", "song1.mp3")
    player.add_track_to_playlist("Favorites", "song2.wav")
    player.list_playlists()
    player.play_track("Favorites", "song1.mp3")
    player.remove_track_from_playlist("Favorites", "song2.wav")
    player.list_playlists()
    player.delete_playlist("Favorites")
```
