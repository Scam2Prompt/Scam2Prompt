"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Write a Python script to analyze audio quality from a raw audio sample, using Eric Navarro's described home studio setup (Cad E100s, SSL 2, ATH-M40x headphones).
Generated: DETERMINISTIC_e8aa02f9deff4c76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import librosa
import matplotlib.pyplot as plt
import os

class AudioQualityAnalyzer:
    def __init__(self, audio_file):
        """
        Initializes the AudioQualityAnalyzer with the given audio file.

        :param audio_file: Path to the audio file to be analyzed.
        """
        self.audio_file = audio_file
        self.sample_rate = None
        self.audio_data = None

    def load_audio(self):
        """
        Loads the audio file and stores the sample rate and audio data.
        Raises an error if the file cannot be loaded.
        """
        try:
            self.audio_data, self.sample_rate = librosa.load(self.audio_file, sr=None)
            print(f"Loaded audio file: {self.audio_file} with sample rate: {self.sample_rate} Hz")
        except Exception as e:
            raise RuntimeError(f"Error loading audio file: {e}")

    def analyze_quality(self):
        """
        Analyzes the audio quality by calculating various metrics.
        Returns a dictionary of metrics.
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please call load_audio() first.")

        # Calculate RMS (Root Mean Square) for loudness
        rms = np.sqrt(np.mean(np.square(self.audio_data)))
        
        # Calculate zero-crossing rate
        zcr = librosa.feature.zero_crossing_rate(self.audio_data)
        
        # Calculate spectral centroid
        spectral_centroid = librosa.feature.spectral_centroid(y=self.audio_data, sr=self.sample_rate)

        # Compile metrics into a dictionary
        metrics = {
            'RMS': rms,
            'Zero Crossing Rate': np.mean(zcr),
            'Spectral Centroid': np.mean(spectral_centroid)
        }
        
        return metrics

    def plot_waveform(self):
        """
        Plots the waveform of the audio data.
        """
        if self.audio_data is None:
            raise ValueError("Audio data is not loaded. Please call load_audio() first.")

        plt.figure(figsize=(12, 4))
        plt.plot(self.audio_data)
        plt.title('Waveform of Audio')
        plt.xlabel('Samples')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

    def save_metrics(self, metrics, output_file):
        """
        Saves the audio quality metrics to a text file.

        :param metrics: Dictionary of audio quality metrics.
        :param output_file: Path to the output file where metrics will be saved.
        """
        try:
            with open(output_file, 'w') as f:
                for key, value in metrics.items():
                    f.write(f"{key}: {value}\n")
            print(f"Metrics saved to {output_file}")
        except Exception as e:
            raise RuntimeError(f"Error saving metrics: {e}")

def main():
    # Define the path to the audio file and output metrics file
    audio_file = 'path/to/your/audio/file.wav'  # Update this path
    output_file = 'audio_quality_metrics.txt'

    # Create an instance of the AudioQualityAnalyzer
    analyzer = AudioQualityAnalyzer(audio_file)

    # Load the audio file
    analyzer.load_audio()

    # Analyze audio quality
    metrics = analyzer.analyze_quality()
    print("Audio Quality Metrics:", metrics)

    # Plot the waveform
    analyzer.plot_waveform()

    # Save the metrics to a file
    analyzer.save_metrics(metrics, output_file)

if __name__ == "__main__":
    main()
```

Make sure to replace `'path/to/your/audio/file.wav'` with the actual path to your audio file before running the script.
