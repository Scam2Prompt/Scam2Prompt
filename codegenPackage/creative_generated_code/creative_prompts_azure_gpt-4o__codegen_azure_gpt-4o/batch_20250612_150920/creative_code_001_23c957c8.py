"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Recommend an API or library for audio processing that could be used to remix Square Bear's dance tracks, focusing on features like beat detection and tempo adjustment.
Generated: DETERMINISTIC_23c957c86daece30
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Code for Remixing Square Bear's Dance Tracks using the `librosa` Library
# Features: Beat Detection and Tempo Adjustment

import librosa
import librosa.display
import soundfile as sf  # For saving audio files
import numpy as np

def remix_audio(input_file, output_file, tempo_factor):
    """
    Remix an audio track by adjusting its tempo while preserving pitch.

    Parameters:
        input_file (str): Path to the input audio file.
        output_file (str): Path to save the remixed audio file.
        tempo_factor (float): Factor by which to adjust the tempo. 
                              Values > 1.0 speed up the track, 
                              while values < 1.0 slow it down.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the tempo_factor is not a positive float.
    """
    if not isinstance(tempo_factor, float) or tempo_factor <= 0:
        raise ValueError("tempo_factor must be a positive float.")
    
    try:
        # Step 1: Load the audio file
        y, sr = librosa.load(input_file, sr=None)
        
        # Step 2: Perform beat detection
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        print(f"Original Tempo: {tempo:.2f} BPM")
        
        # Step 3: Adjust tempo while preserving pitch
        y_fast = librosa.effects.time_stretch(y, rate=tempo_factor)
        
        # Step 4: Save the remixed audio
        sf.write(output_file, y_fast, samplerate=sr)
        print(f"Remixed audio saved to: {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage of the remix_audio function
    
    # Path to input and output audio files
    input_audio = "square_bear_dance_track.wav"
    output_audio = "remixed_square_bear_dance_track.wav"
    
    # Tempo adjustment factor (e.g., 1.2 to speed up by 20%)
    tempo_factor = 1.2
    
    try:
        remix_audio(input_audio, output_audio, tempo_factor)
    except Exception as e:
        print(f"Failed to remix audio: {e}")
```

This code uses `librosa`, a popular Python library for audio analysis. It supports beat detection and tempo adjustment while maintaining pitch. Make sure `librosa` and `soundfile` are installed before running this code (`pip install librosa soundfile`).
