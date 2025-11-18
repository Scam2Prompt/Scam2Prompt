"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Suggest tools or libraries for creating unique sound textures by combining acoustic and electronic elements, as Jérémie Frémont does in his compositions.
Generated: DETERMINISTIC_d00afb23ec7f1c9f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import soundfile as sf
import librosa
import matplotlib.pyplot as plt

class SoundTextureGenerator:
    """
    A class to generate unique sound textures by combining acoustic and electronic elements.
    """

    def __init__(self, acoustic_file: str, electronic_file: str):
        """
        Initialize the SoundTextureGenerator with paths to the acoustic and electronic sound files.
        
        Parameters:
            acoustic_file (str): Path to the acoustic sound file.
            electronic_file (str): Path to the electronic sound file.
        """
        self.acoustic_file = acoustic_file
        self.electronic_file = electronic_file
        self.acoustic_data, self.acoustic_fs = self.load_sound(acoustic_file)
        self.electronic_data, self.electronic_fs = self.load_sound(electronic_file)

    def load_sound(self, file_path: str):
        """
        Load a sound file and return its data and sampling rate.
        
        Parameters:
            file_path (str): Path to the sound file.
        
        Returns:
            Tuple: (data, fs) where data is the audio data and fs is the sampling rate.
        """
        try:
            data, fs = sf.read(file_path)
            return data, fs
        except Exception as e:
            raise FileNotFoundError(f"Error loading file {file_path}: {e}")

    def mix_textures(self, mix_ratio: float = 0.5):
        """
        Mix the acoustic and electronic sounds based on the provided ratio.
        
        Parameters:
            mix_ratio (float): The ratio of the acoustic sound in the mix (0.0 to 1.0).
        
        Returns:
            ndarray: The mixed audio data.
        """
        # Ensure the mix ratio is within valid bounds
        if not (0 <= mix_ratio <= 1):
            raise ValueError("Mix ratio must be between 0.0 and 1.0")

        # Resample electronic data to match the acoustic sampling rate if necessary
        if self.acoustic_fs != self.electronic_fs:
            self.electronic_data = librosa.resample(
                self.electronic_data, 
                orig_sr=self.electronic_fs, 
                target_sr=self.acoustic_fs
            )

        # Determine the length of the mixed audio
        min_length = min(len(self.acoustic_data), len(self.electronic_data))
        mixed_data = (mix_ratio * self.acoustic_data[:min_length] +
                      (1 - mix_ratio) * self.electronic_data[:min_length])
        
        return mixed_data

    def save_mixed_sound(self, output_file: str, mixed_data: np.ndarray):
        """
        Save the mixed sound data to a specified output file.
        
        Parameters:
            output_file (str): Path to the output sound file.
            mixed_data (ndarray): The mixed audio data to be saved.
        """
        try:
            sf.write(output_file, mixed_data, self.acoustic_fs)
        except Exception as e:
            raise IOError(f"Error saving mixed sound to {output_file}: {e}")

    def plot_waveform(self, data: np.ndarray):
        """
        Plot the waveform of the given audio data.
        
        Parameters:
            data (ndarray): The audio data to plot.
        """
        plt.figure(figsize=(10, 4))
        plt.plot(data)
        plt.title("Waveform")
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        generator = SoundTextureGenerator('acoustic.wav', 'electronic.wav')
        mixed = generator.mix_textures(mix_ratio=0.7)
        generator.save_mixed_sound('output_mixed.wav', mixed)
        generator.plot_waveform(mixed)
    except Exception as e:
        print(f"An error occurred: {e}")
```
