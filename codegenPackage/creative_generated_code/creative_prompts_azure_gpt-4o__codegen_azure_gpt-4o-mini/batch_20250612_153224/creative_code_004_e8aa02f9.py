"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Write a Python script to analyze audio quality from a raw audio sample, using Eric Navarro's described home studio setup (Cad E100s, SSL 2, ATH-M40x headphones).
Generated: DETERMINISTIC_e8aa02f9deff4c76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import librosa
import matplotlib.pyplot as plt
import soundfile as sf
import os

class AudioAnalyzer:
    """
    A class to analyze the quality of audio samples.

    Attributes:
        audio_file (str): Path to the audio file to be analyzed.
        sample_rate (int): Sample rate of the audio file.
        audio_data (numpy.ndarray): Audio data loaded from the audio file.
    """

    def __init__(self, audio_file: str):
        """
        Initialize the AudioAnalyzer with the path to the audio file.

        Args:
            audio_file (str): Path to the audio file.
        """
        self.audio_file = audio_file
        self.sample_rate = None
        self.audio_data = None

        self.load_audio()

    def load_audio(self):
        """
        Loads audio data from the specified file.
        """
        try:
            self.audio_data, self.sample_rate = librosa.load(self.audio_file, sr=None)
            print(f"Loaded audio file: {self.audio_file}")
            print(f"Sample Rate: {self.sample_rate} Hz")
            print(f"Audio Duration: {librosa.get_duration(y=self.audio_data, sr=self.sample_rate)} seconds")
        except Exception as e:
            print(f"Error loading audio file: {e}")
            raise

    def analyze(self):
        """
        Analyzes the audio quality metrics.
        This method computes and plots the waveform, spectrogram, and other metrics.
        """
        self.plot_waveform()
        self.plot_spectrogram()

    def plot_waveform(self):
        """
        Plots the waveform of the audio signal.
        """
        plt.figure(figsize=(12, 4))
        plt.plot(self.audio_data, color='blue')
        plt.title('Waveform')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

    def plot_spectrogram(self):
        """
        Plots the spectrogram of the audio signal.
        """
        plt.figure(figsize=(12, 4))
        D = librosa.amplitude_to_db(np.abs(librosa.stft(self.audio_data)), ref=np.max)
        plt.imshow(D, sr=self.sample_rate, hop_length=512, x_axis='time', y_axis='log', cmap='gray_r')
        plt.title('Spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (s)')
        plt.show()

def main():
    """
    Main function to run the audio quality analysis.
    """
    # Define the path to the audio file (modify as necessary)
    audio_file_path = 'path/to/your/audio/file.wav'

    # Check if the audio file exists
    if not os.path.isfile(audio_file_path):
        print(f"Audio file does not exist: {audio_file_path}")
        return

    # Instantiate the AudioAnalyzer and analyze the audio quality
    try:
        audio_analyzer = AudioAnalyzer(audio_file_path)
        audio_analyzer.analyze()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
