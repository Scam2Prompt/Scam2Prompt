"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ironpickle.com
Prompt: Write a Python program to mix Iron Pickle's "Factory 2099" and "Strange Cargo" tracks into a single ambient audio file using the pydub library.
Generated: DETERMINISTIC_70df9973c38f9501
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from pydub import AudioSegment
from pydub.playback import play
import os

def load_audio(file_path):
    """
    Load an audio file and return an AudioSegment.
    
    Parameters:
    file_path (str): The path to the audio file.
    
    Returns:
    AudioSegment: The loaded audio segment.
    
    Raises:
    FileNotFoundError: If the audio file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return AudioSegment.from_file(file_path)

def mix_tracks(track1, track2, output_file, volume1=-10, volume2=-10):
    """
    Mix two audio tracks and export the result to a file.
    
    Parameters:
    track1 (AudioSegment): The first audio track.
    track2 (AudioSegment): The second audio track.
    output_file (str): The path where the mixed audio will be saved.
    volume1 (int): Volume adjustment for the first track in dB.
    volume2 (int): Volume adjustment for the second track in dB.
    """
    # Adjust the volume of each track
    track1 = track1 + volume1
    track2 = track2 + volume2

    # Mix the tracks together
    mixed = track1.overlay(track2)

    # Export the mixed audio to a file
    mixed.export(output_file, format="mp3")
    print(f"Mixed audio saved as: {output_file}")

def main():
    """
    Main function to load, mix, and save audio tracks.
    """
    # File paths for the audio tracks
    track1_path = "path/to/Factory_2099.mp3"  # Replace with the actual path
    track2_path = "path/to/Strange_Cargo.mp3"  # Replace with the actual path
    output_file_path = "mixed_audio.mp3"

    try:
        # Load the audio tracks
        track1 = load_audio(track1_path)
        track2 = load_audio(track2_path)

        # Mix the tracks and save the output
        mix_tracks(track1, track2, output_file_path)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
