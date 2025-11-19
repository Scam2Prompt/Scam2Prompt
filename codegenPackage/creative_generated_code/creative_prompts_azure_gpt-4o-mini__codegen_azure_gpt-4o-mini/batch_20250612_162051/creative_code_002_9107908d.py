"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Write a Python script that utilizes a library for audio processing, reflecting the techniques of sound design described by Jérémie Frémont in his work for video games.
Generated: DETERMINISTIC_9107908d81298878
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

class SoundDesigner:
    def __init__(self, sample_rate=44100):
        """Initialize the Sound Designer with a specified sample rate."""
        self.sample_rate = sample_rate

    def load_audio(self, file_path):
        """Load an audio file.

        Args:
            file_path (str): The path to the audio file to be loaded.

        Returns:
            numpy.ndarray: The audio data.
            int: The sample rate of the audio file.
        """
        try:
            audio_data, sr = sf.read(file_path)
            return audio_data, sr
        except Exception as e:
            raise RuntimeError(f"Error loading audio file: {e}")

    def save_audio(self, audio_data, file_path):
        """Save audio data to a file.

        Args:
            audio_data (numpy.ndarray): The audio data to save.
            file_path (str): The path where the audio file will be saved.
        """
        try:
            sf.write(file_path, audio_data, self.sample_rate)
        except Exception as e:
            raise RuntimeError(f"Error saving audio file: {e}")

    def apply_filter(self, data, cutoff, btype='low', order=5):
        """Apply a Butterworth filter to the audio data.

        Args:
            data (numpy.ndarray): The audio data to filter.
            cutoff (float): Cutoff frequency in Hz.
            btype (str): The type of filter ('low', 'high', 'band').
            order (int): The order of the filter.

        Returns:
            numpy.ndarray: Filtered audio data.
        """
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype=btype, analog=False)
        filtered_data = lfilter(b, a, data)
        return filtered_data

    def visualize_audio(self, data):
        """Visualize the audio data using a waveform plot.

        Args:
            data (numpy.ndarray): The audio data to visualize.
        """
        plt.figure(figsize=(10, 4))
        plt.plot(data)
        plt.title('Audio Waveform')
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

def main():
    """Main function to demonstrate audio processing."""
    sound_designer = SoundDesigner()

    # Load audio file
    input_file = 'input_audio.wav'
    try:
        audio_data, sr = sound_designer.load_audio(input_file)
        print(f"Loaded audio file: {input_file} with sample rate: {sr}")
    except RuntimeError as e:
        print(e)
        return

    # Visualize original audio
    sound_designer.visualize_audio(audio_data)

    # Apply low-pass filter
    cutoff_frequency = 1000  # Hz
    filtered_audio = sound_designer.apply_filter(audio_data, cutoff_frequency)

    # Visualize filtered audio
    sound_designer.visualize_audio(filtered_audio)

    # Save the filtered audio
    output_file = 'output_audio.wav'
    try:
        sound_designer.save_audio(filtered_audio, output_file)
        print(f"Filtered audio saved to: {output_file}")
    except RuntimeError as e:
        print(e)

if __name__ == '__main__':
    main()
```
