"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Provide a list of Python libraries for processing audio files and explain how they can be used to evaluate the performance of music equipment.
Generated: DETERMINISTIC_087ace5f5c3aab73
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import librosa  # A powerful library for audio analysis
import soundfile as sf  # For reading and writing sound files
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting waveforms and spectrograms

def load_audio(file_path):
    """
    Load an audio file and return the audio time series and its sample rate.
    
    Parameters:
    file_path (str): The path to the audio file.
    
    Returns:
    tuple: A tuple containing the audio time series (numpy array) and sample rate (int).
    """
    try:
        audio_data, sample_rate = librosa.load(file_path, sr=None)
        return audio_data, sample_rate
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None, None

def plot_waveform(audio_data, sample_rate):
    """
    Plot the waveform of the audio signal.
    
    Parameters:
    audio_data (numpy array): The audio time series.
    sample_rate (int): The sample rate of the audio file.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data)), audio_data)
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

def plot_spectrogram(audio_data, sample_rate):
    """
    Plot the spectrogram of the audio signal.
    
    Parameters:
    audio_data (numpy array): The audio time series.
    sample_rate (int): The sample rate of the audio file.
    """
    plt.figure(figsize=(12, 4))
    D = librosa.amplitude_to_db(np.abs(librosa.stft(audio_data)), ref=np.max)
    librosa.display.specshow(D, sr=sample_rate, x_axis='time', y_axis='log', cmap='coolwarm')
    plt.title('Spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.show()

def save_audio(file_path, audio_data, sample_rate):
    """
    Save the audio data to a file.
    
    Parameters:
    file_path (str): The path where the audio file will be saved.
    audio_data (numpy array): The audio time series to save.
    sample_rate (int): The sample rate of the audio file.
    """
    try:
        sf.write(file_path, audio_data, sample_rate)
        print(f"Audio saved to {file_path}")
    except Exception as e:
        print(f"Error saving audio file: {e}")

# Example usage:
if __name__ == "__main__":
    audio_file = "example.wav"  # Replace with your audio file path
    audio_data, sample_rate = load_audio(audio_file)
    
    if audio_data is not None:
        plot_waveform(audio_data, sample_rate)
        plot_spectrogram(audio_data, sample_rate)
        # Modify audio data here if necessary (e.g., apply effects)
        save_audio("output.wav", audio_data, sample_rate)  # Save modified audio
```
