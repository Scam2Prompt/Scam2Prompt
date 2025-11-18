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
import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class SoundProfileAnalyzer:
    """
    A class to analyze sound profiles of audio tracks.
    
    Attributes:
        directory (str): The path to the directory containing audio files.
    """

    def __init__(self, directory):
        """
        Initializes the SoundProfileAnalyzer with a directory of audio files.

        Parameters:
            directory (str): The directory path to analyze.
        """
        self.directory = directory
        self.tracks_data = []

    def analyze_tracks(self):
        """Analyzes all audio tracks in the specified directory."""
        # Check if the directory exists
        if not os.path.isdir(self.directory):
            raise ValueError(f"The directory '{self.directory}' does not exist.")
        
        # Iterate through each audio file in the directory
        for filename in os.listdir(self.directory):
            if filename.endswith(('.wav', '.mp3', '.flac')):  # Check for audio file extensions
                file_path = os.path.join(self.directory, filename)
                try:
                    # Load the audio file
                    y, sr = librosa.load(file_path, sr=None)
                    # Extract features
                    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
                    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
                    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=y))

                    # Store the track's data
                    self.tracks_data.append({
                        'filename': filename,
                        'tempo': tempo,
                        'spectral_centroid': spectral_centroid,
                        'zero_crossing_rate': zero_crossing_rate
                    })

                except Exception as e:
                    print(f"Error processing file '{filename}': {e}")

    def generate_report(self):
        """Generates a report of the analyzed tracks."""
        if not self.tracks_data:
            print("No tracks analyzed. Please run analyze_tracks() first.")
            return
        
        df = pd.DataFrame(self.tracks_data)
        print("Analyzed Tracks:")
        print(df)

        # Plotting the results
        plt.figure(figsize=(14, 7))
        plt.subplot(3, 1, 1)
        plt.title('Spectral Centroid')
        plt.bar(df['filename'], df['spectral_centroid'], color='cyan')
        plt.xticks(rotation=45)

        plt.subplot(3, 1, 2)
        plt.title('Tempo')
        plt.bar(df['filename'], df['tempo'], color='magenta')
        plt.xticks(rotation=45)

        plt.subplot(3, 1, 3)
        plt.title('Zero Crossing Rate')
        plt.bar(df['filename'], df['zero_crossing_rate'], color='yellow')
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        directory_path = "path/to/comet_records"  # Specify the path to the audio files directory
        analyzer = SoundProfileAnalyzer(directory_path)
        analyzer.analyze_tracks()
        analyzer.generate_report()
    except Exception as e:
        print(f"An error occurred: {e}")
```
