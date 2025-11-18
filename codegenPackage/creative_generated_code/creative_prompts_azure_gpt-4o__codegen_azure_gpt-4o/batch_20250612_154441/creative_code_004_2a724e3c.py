"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ironpickle.com
Prompt: Provide code to analyze the audio features (e.g., tempo, mood) of Iron Pickle's "Strange Cargo - Space Ambient Music" using the librosa Python library.
Generated: DETERMINISTIC_2a724e3ca1b0f600
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import librosa
import librosa.display
import numpy as np

def analyze_audio_features(audio_file_path):
    """
    Analyzes audio features such as tempo and mood of an audio file.
    
    Parameters:
        audio_file_path (str): Path to the audio file to be analyzed.
        
    Returns:
        dict: A dictionary containing analyzed features including tempo, 
              spectral centroid, and tonality/mood-related metrics.
    """
    results = {}

    try:
        # Load the audio file
        # sr=None ensures librosa uses the file's native sampling rate
        y, sr = librosa.load(audio_file_path, sr=None)

        # Extract tempo
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        results['tempo'] = tempo

        # Extract spectral centroid (represents brightness)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        results['spectral_centroid_mean'] = np.mean(spectral_centroid)

        # Extract chroma features (tonality/mood)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        results['chroma_mean'] = np.mean(chroma)

        # Extract spectral contrast (helps infer mood and dynamics)
        spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
        results['spectral_contrast_mean'] = np.mean(spectral_contrast)

        # Extract zero-crossing rate (can be used to infer percussiveness)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)
        results['zero_crossing_rate_mean'] = np.mean(zero_crossing_rate)

    except FileNotFoundError:
        print("Error: The specified audio file was not found.")
    except Exception as e:
        print(f"An error occurred while processing the audio file: {e}")
    
    return results


if __name__ == "__main__":
    # Example usage
    # Replace with the actual path to "Strange Cargo - Space Ambient Music"
    audio_path = "path_to_audio_file.mp3"
    
    # Analyze the audio features
    features = analyze_audio_features(audio_path)
    
    # Print the extracted features
    if features:
        print("Extracted Audio Features:")
        for feature, value in features.items():
            print(f"{feature}: {value}")
```
