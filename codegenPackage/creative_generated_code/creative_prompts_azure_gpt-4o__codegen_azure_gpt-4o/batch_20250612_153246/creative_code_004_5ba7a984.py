"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cometrecords.co.uk
Prompt: Suggest a library or tool to analyze the sound profiles of tracks produced by Comet Records, focusing on progressive house and melodic techno genres.
Generated: DETERMINISTIC_5ba7a9843accff5e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the `librosa` library to analyze the sound profiles of audio tracks produced by Comet Records,
focusing on characteristics relevant to progressive house and melodic techno genres.

Dependencies:
- librosa: A Python library for audio and music analysis.
- numpy: Used for numerical computations.
- matplotlib: Optional, used for plotting spectrograms for visualization.

Usage:
Place your audio tracks in the `audio_files` folder and run the script.
The script extracts audio features and prints a summary for each track.
"""

import os
import librosa
import numpy as np

# Folder containing audio files
AUDIO_FOLDER = "audio_files"

# Function to analyze a single audio file
def analyze_audio(file_path):
    """
    Analyze the sound profile of an audio file.

    Parameters:
    file_path (str): Path to the audio file.

    Returns:
    dict: A dictionary containing extracted audio features.
    """
    try:
        # Load the audio file
        y, sr = librosa.load(file_path, sr=None)
        
        # Extract audio features
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)  # Estimated tempo
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)  # Harmonic content
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)  # Brightness
        spectral_rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)  # Roll-off frequency
        rms = librosa.feature.rms(y=y)  # Energy

        # Prepare a summary of features
        audio_features = {
            "tempo": tempo,
            "mean_spectral_centroid": np.mean(spectral_centroid),
            "mean_spectral_rolloff": np.mean(spectral_rolloff),
            "mean_rms": np.mean(rms),
            "mean_chroma": np.mean(chroma, axis=1).tolist()  # Average chroma per pitch class
        }

        return audio_features

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Main function to analyze all audio files in the specified folder
def analyze_all_tracks(audio_folder):
    """
    Analyze all audio tracks in a specified folder.

    Parameters:
    audio_folder (str): Path to the folder containing audio files.

    Returns:
    None
    """
    if not os.path.exists(audio_folder):
        print(f"The folder '{audio_folder}' does not exist.")
        return

    # Iterate through all files in the folder
    for file_name in os.listdir(audio_folder):
        file_path = os.path.join(audio_folder, file_name)
        if os.path.isfile(file_path) and file_name.endswith(('.wav', '.mp3', '.flac')):
            print(f"Analyzing {file_name}...")
            result = analyze_audio(file_path)
            if result:
                print(f"Analysis for {file_name}: {result}\n")
            else:
                print(f"Failed to analyze {file_name}\n")
        else:
            print(f"Skipping unsupported file: {file_name}")

# Run the script
if __name__ == "__main__":
    analyze_all_tracks(AUDIO_FOLDER)
```

To use this script, ensure you have the required libraries (`librosa`, `numpy`, `matplotlib`) installed in your environment. You can install them using pip:

```bash
pip install librosa numpy matplotlib
```

Place your audio files in the `audio_files` folder and execute the script. It extracts features like tempo, spectral centroid, spectral rolloff, RMS energy, and chroma values, which are particularly relevant for analyzing progressive house and melodic techno tracks.
