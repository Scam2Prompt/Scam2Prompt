"""
Generated Code Metadata:
========================
Original URL: https://duckchain.world
Prompt: Write Python code to simulate a portable music player interface with customizable playlists and support for major audio formats, inspired by the features described on Duckchain.world.
Generated: DETERMINISTIC_a2b27ea3aadb1ea5
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import time
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict, Optional, Tuple
import pygame
import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE
from pathlib import Path


class AudioFormat(Enum):
    """Supported audio formats for the music player."""
    MP3 = auto()
    FLAC = auto()
    OGG = auto()
    WAV = auto()


@dataclass
class Song:
    """Represents a song with metadata."""
    title: str
    artist: str
    album: str
    duration: float  # in seconds
    file_path: str
    audio_format: AudioFormat


@dataclass
class Playlist:
    """Represents a playlist containing songs."""
    name: str
    songs: List[Song] = field(default_factory=list)
    current_index: int = 0

    def add_song(self, song: Song) -> None:
        """Add a song to the playlist."""
        self.songs.append(song)

    def remove_song(self, index: int) -> None:
        """Remove a song from the playlist by index."""
        if 0 <= index < len(self.songs):
            self.songs.pop(index)
            if self.current_index >= len(self.songs):
                self.current_index = max(0, len(self.songs) - 1)

    def next_song(self) -> Optional[Song]:
        """Get the next song in the playlist."""
        if not self.songs:
            return None
        self.current_index = (self.current_index + 1) % len(self.songs)
        return self.songs[self.current_index]

    def previous_song(self) -> Optional[Song]:
        """Get the previous song in the playlist."""
        if not self.songs:
            return None
        self.current_index = (self.current_index - 1) % len(self.songs)
        return self.songs[self.current_index]

    def shuffle(self) -> None:
        """Shuffle the playlist songs."""
        random.shuffle(self.songs)
        self.current_index = 0

    def get_current_song(self) -> Optional[Song]:
        """Get the current song."""
        if not self.songs:
            return None
        return self.songs[self.current_index]


class MusicPlayer:
    """Portable music player with playlist support."""
    
    def __init__(self):
        pygame.mixer.init()
        self.playlists: Dict[str, Playlist] = {}
        self.current_playlist: Optional[Playlist] = None
        self.volume: float = 0.7  # Default volume (0.0 to 1.0)
        self.is_playing: bool = False
        self.is_paused: bool = False

    def create_playlist(self, name: str) -> bool:
        """Create a new playlist."""
        if name in self.playlists:
            return False
        self.playlists[name] = Playlist(name=name)
        return True

    def delete_playlist(self, name: str) -> bool:
        """Delete an existing playlist."""
        if name not in self.playlists:
            return False
        if self.current_playlist and self.current_playlist.name == name:
            self.stop()
            self.current_playlist = None
        del self.playlists[name]
        return True

    def select_playlist(self, name: str) -> bool:
        """Select a playlist to play."""
        if name not in self.playlists:
            return False
        self.current_playlist = self.playlists[name]
        return True

    def load_song(self, file_path: str) -> Optional[Song]:
        """Load a song from file and extract metadata."""
        try:
            path = Path(file_path)
            if not path.exists():
                return None

            audio_file = None
            audio_format = None

            if file_path.lower().endswith('.mp3'):
                audio_file = MP3(file_path)
                audio_format = AudioFormat.MP3
            elif file_path.lower().endswith('.flac'):
                audio_file = FLAC(file_path)
                audio_format = AudioFormat.FLAC
            elif file_path.lower().endswith('.ogg'):
                audio_file = OggVorbis(file_path)
                audio_format = AudioFormat.OGG
            elif file_path.lower().endswith('.wav'):
                audio_file = WAVE(file_path)
                audio_format = AudioFormat.WAV
            else:
                return None

            title = audio_file.get('title', [os.path.basename(file_path)])[0]
            artist = audio_file.get('artist', ['Unknown Artist'])[0]
            album = audio_file.get('album', ['Unknown Album'])[0]
            duration = audio_file.info.length

            return Song(
                title=title,
                artist=artist,
                album=album,
                duration=duration,
                file_path=file_path,
                audio_format=audio_format
            )
        except Exception:
            return None

    def add_song_to_playlist(self, playlist_name: str, file_path: str) -> bool:
        """Add a song to a playlist."""
        if playlist_name not in self.playlists:
            return False
        
        song = self.load_song(file_path)
        if not song:
            return False
        
        self.playlists[playlist_name].add_song(song)
        return True

    def play(self) -> bool:
        """Play the current song in the selected playlist."""
        if not self.current_playlist or not self.current_playlist.songs:
            return False
        
        current_song = self.current_playlist.get_current_song()
        if not current_song:
            return False
        
        try:
            pygame.mixer.music.load(current_song.file_path)
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused = False
            return True
        except Exception:
            return False

    def pause(self) -> bool:
        """Pause the current song."""
        if not self.is_playing:
            return False
        
        pygame.mixer.music.pause()
        self.is_paused = True
        return True

    def resume(self) -> bool:
        """Resume the paused song."""
        if not self.is_paused:
            return False
        
        pygame.mixer.music.unpause()
        self.is_paused = False
        return True

    def stop(self) -> bool:
        """Stop playback."""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        return True

    def next(self) -> bool:
        """Play the next song in the playlist."""
        if not self.current_playlist:
            return False
        
        self.stop()
        song = self.current_playlist.next_song()
        if not song:
            return False
        
        return self.play()

    def previous(self) -> bool:
        """Play the previous song in the playlist."""
        if not self.current_playlist:
            return False
        
        self.stop()
        song = self.current_playlist.previous_song()
        if not song:
            return False
        
        return self.play()

    def set_volume(self, volume: float) -> bool:
        """Set the player volume (0.0 to 1.0)."""
        if volume < 0 or volume > 1:
            return False
        
        self.volume = volume
        pygame.mixer.music.set_volume(volume)
        return True

    def shuffle_playlist(self, playlist_name: str) -> bool:
        """Shuffle a playlist."""
        if playlist_name not in self.playlists:
            return False
        
        self.playlists[playlist_name].shuffle()
        return True

    def get_current_song_info(self) -> Optional[Tuple[str, str, str, float]]:
        """Get info about the currently playing song."""
        if not self.current_playlist or not self.is_playing:
            return None
        
        current_song = self.current_playlist.get_current_song()
        if not current_song:
            return None
        
        return (
            current_song.title,
            current_song.artist,
            current_song.album,
            current_song.duration
        )

    def get_playback_status(self) -> str:
        """Get current playback status."""
        if not self.is_playing:
            return "stopped"
        elif self.is_paused:
            return "paused"
        else:
            return "playing"


# Example usage
if __name__ == "__main__":
    player = MusicPlayer()
    player.create_playlist("My Favorites")
    player.add_song_to_playlist("My Favorites", "example.mp3")  # Replace with actual file
    player.select_playlist("My Favorites")
    player.play()
    
    # Simulate playback
    time.sleep(5)
    player.pause()
    time.sleep(2)
    player.resume()
    time.sleep(3)
    player.next()
    time.sleep(5)
    player.stop()
```
