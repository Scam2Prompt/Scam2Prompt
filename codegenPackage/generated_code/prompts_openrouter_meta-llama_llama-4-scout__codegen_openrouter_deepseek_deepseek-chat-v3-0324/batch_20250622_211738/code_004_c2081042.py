"""
Generated Code Metadata:
========================
Original URL: https://tudopro.site
Prompt: Suggest a suitable format for delivering music playlists to users, considering compatibility with celulares, pendrives, and aparelhos de paredão e paredinha.
Generated: DETERMINISTIC_c208104215eaa1e1
Batch ID: 20250622_211738
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Union

class PlaylistGenerator:
    """
    A class to generate music playlists in various formats for compatibility with
    different devices (cellphones, pendrives, wall-mounted sound systems).
    Supported formats: M3U, PLS, JSON.
    """
    
    def __init__(self, playlist_name: str):
        """
        Initialize the PlaylistGenerator with a playlist name.
        
        Args:
            playlist_name (str): Name of the playlist.
        """
        self.playlist_name = playlist_name
        self.tracks: List[Dict[str, Union[str, int]]] = []
    
    def add_track(self, file_path: str, title: str, duration: int = 0) -> None:
        """
        Add a track to the playlist.
        
        Args:
            file_path (str): Path to the audio file.
            title (str): Title of the track.
            duration (int, optional): Duration in seconds. Defaults to 0.
        """
        self.tracks.append({
            'file_path': file_path,
            'title': title,
            'duration': duration
        })
    
    def generate_m3u(self, output_path: str) -> None:
        """
        Generate an M3U playlist file.
        
        Args:
            output_path (str): Path to save the M3U file.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("#EXTM3U\n")
                for track in self.tracks:
                    f.write(f"#EXTINF:{track['duration']},{track['title']}\n")
                    f.write(f"{track['file_path']}\n")
        except IOError as e:
            raise IOError(f"Failed to write M3U file: {e}")
    
    def generate_pls(self, output_path: str) -> None:
        """
        Generate a PLS playlist file.
        
        Args:
            output_path (str): Path to save the PLS file.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("[playlist]\n")
                for i, track in enumerate(self.tracks, 1):
                    f.write(f"File{i}={track['file_path']}\n")
                    f.write(f"Title{i}={track['title']}\n")
                    f.write(f"Length{i}={track['duration']}\n")
                f.write(f"NumberOfEntries={len(self.tracks)}\n")
                f.write("Version=2\n")
        except IOError as e:
            raise IOError(f"Failed to write PLS file: {e}")
    
    def generate_json(self, output_path: str) -> None:
        """
        Generate a JSON playlist file.
        
        Args:
            output_path (str): Path to save the JSON file.
        
        Raises:
            IOError: If file cannot be written.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'playlist_name': self.playlist_name,
                    'tracks': self.tracks
                }, f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Failed to write JSON file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        playlist = PlaylistGenerator("My Awesome Playlist")
        playlist.add_track("/music/song1.mp3", "Song One", 180)
        playlist.add_track("/music/song2.mp3", "Song Two", 200)
        
        # Generate all formats
        playlist.generate_m3u("playlist.m3u")
        playlist.generate_pls("playlist.pls")
        playlist.generate_json("playlist.json")
        
        print("Playlist files generated successfully.")
    except Exception as e:
        print(f"Error generating playlist: {e}")
```
