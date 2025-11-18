"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Suggest APIs or libraries for integrating multi-format audio support into a portable music player, as highlighted on Duckchain.world.
Generated: DETERMINISTIC_284ea72384bd474e
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s production-ready Python code that uses the `pydub` library for multi-format audio support in a portable music player. This code demonstrates how to load, play, and manipulate audio files in various formats.

```python
# Import necessary libraries
from pydub import AudioSegment
from pydub.playback import play
import os

# Define a class for the portable music player
class PortableMusicPlayer:
    """
    A portable music player that supports multi-format audio playback.
    Supported formats: mp3, wav, ogg, flac, etc.
    """

    def __init__(self):
        """
        Initialize the music player.
        """
        self.current_track = None

    def load_audio(self, file_path):
        """
        Load an audio file into the music player.

        :param file_path: Path to the audio file.
        :return: None
        """
        try:
            # Detect file format dynamically and load the audio file
            self.current_track = AudioSegment.from_file(file_path)
            print(f"Loaded audio file: {os.path.basename(file_path)}")
        except FileNotFoundError:
            print("Error: File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: Unable to load audio file. Details: {e}")

    def play_audio(self):
        """
        Play the currently loaded audio track.

        :return: None
        """
        if self.current_track:
            try:
                print("Playing audio...")
                play(self.current_track)
            except Exception as e:
                print(f"Error: Unable to play audio. Details: {e}")
        else:
            print("No audio track is loaded. Use the `load_audio` method first.")

    def get_audio_info(self):
        """
        Retrieve information about the loaded audio track (duration, format).

        :return: None
        """
        if self.current_track:
            duration_in_seconds = len(self.current_track) / 1000.0
            print(f"Audio info - Duration: {duration_in_seconds:.2f}s")
        else:
            print("No audio track is loaded. Use the `load_audio` method first.")

# Main function demonstrating usage
if __name__ == "__main__":
    # Initialize the music player
    player = PortableMusicPlayer()

    # Load an audio file (update the path to your audio file)
    audio_file_path = "sample_audio.mp3"
    player.load_audio(audio_file_path)

    # Display audio info
    player.get_audio_info()

    # Play the audio
    player.play_audio()

# Notes:
# - Install required libraries using `pip install pydub`
# - Ensure you have FFmpeg installed for multi-format support (e.g., MP3, WAV, etc.)
# - Replace "sample_audio.mp3" with the path to your actual audio file.
# - Always validate file paths and handle errors gracefully in production systems.
```
