"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soundsource.tn
Prompt: Create a code snippet that simulates an immersive audio experience for an event, inspired by the projects showcased in Sound Source's portfolio.
Generated: DETERMINISTIC_09f63b69de3d95c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import os

# Initialize pygame's mixer for audio playback
pygame.mixer.init()

class ImmersiveAudioExperience:
    """
    Class to manage immersive audio experiences for events. 
    Allows layering and spatialization of multiple audio tracks.
    """
    
    def __init__(self):
        """
        Initializes the audio manager and prepares resources.
        """
        self.audio_tracks = {}  # Dictionary to store audio tracks and their metadata
        self.currently_playing = []  # List to keep track of playing sounds
    
    def load_audio(self, track_name, file_path):
        """
        Load an audio file into the system.

        :param track_name: A unique name for the audio track.
        :param file_path: Path to the audio file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Audio file not found: {file_path}")
        
        try:
            sound = pygame.mixer.Sound(file_path)
            self.audio_tracks[track_name] = sound
        except pygame.error as e:
            raise RuntimeError(f"Failed to load audio file: {file_path}. Error: {e}")
    
    def play_audio(self, track_name, loops=0, volume=1.0):
        """
        Play an audio track.

        :param track_name: The name of the audio track to play.
        :param loops: Number of times to loop the track (-1 for infinite).
        :param volume: Volume level (0.0 - 1.0).
        """
        if track_name not in self.audio_tracks:
            raise ValueError(f"Track '{track_name}' not found.")
        
        sound = self.audio_tracks[track_name]
        sound.set_volume(volume)
        channel = sound.play(loops=loops)
        if channel is None:
            raise RuntimeError(f"Failed to play track: {track_name}")
        
        self.currently_playing.append(track_name)
    
    def stop_audio(self, track_name):
        """
        Stop a specific audio track.

        :param track_name: The name of the audio track to stop.
        """
        if track_name not in self.audio_tracks:
            raise ValueError(f"Track '{track_name}' not found.")
        
        sound = self.audio_tracks[track_name]
        sound.stop()
        if track_name in self.currently_playing:
            self.currently_playing.remove(track_name)

    def fade_out_all(self, fade_time_ms=3000):
        """
        Gradually fade out all currently playing tracks.

        :param fade_time_ms: Duration of the fade-out in milliseconds.
        """
        for track_name in self.currently_playing:
            sound = self.audio_tracks[track_name]
            sound.fadeout(fade_time_ms)
        self.currently_playing = []

# Example usage:
if __name__ == "__main__":
    try:
        immersive_audio = ImmersiveAudioExperience()
        
        # Load audio files
        immersive_audio.load_audio("ambient", "ambient_sound.wav")
        immersive_audio.load_audio("music", "event_music.wav")
        
        # Play audio tracks
        immersive_audio.play_audio("ambient", loops=-1, volume=0.5)
        immersive_audio.play_audio("music", loops=-1, volume=0.7)
        
        # Simulate some experience duration
        input("Press Enter to stop audio and fade out...")
        
        # Fade out and stop all audio tracks
        immersive_audio.fade_out_all()
    except Exception as e:
        print(f"An error occurred: {e}")
```
