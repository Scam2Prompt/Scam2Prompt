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
import soundfile as sf
import matplotlib.pyplot as plt

def analyze_audio_quality(audio_file: str):
    """
    Analyze the audio quality of the given audio file using Eric Navarro's home studio setup.

    Parameters:
        audio_file (str): Path to the raw audio file.

    Returns:
        dict: A dictionary containing audio analysis metrics.
    """
    try:
        # Load audio file
        audio_data, sample_rate = librosa.load(audio_file, sr=None)  # Load with original sample rate
        
        # Compute basic metrics
        duration = librosa.get_duration(y=audio_data, sr=sample_rate)
        rms = librosa.feature.rms(y=audio_data).mean()
        zero_crossings = librosa.zero_crossings(audio_data).sum()
        
        # Compute spectral metrics
        spectral_centroid = librosa.feature.spectral_centroid(y=audio_data, sr=sample_rate).mean()
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio_data, sr=sample_rate).mean()
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio_data, sr=sample_rate).mean()
        
        # Visualization: Plot waveform and spectrogram
        plt.figure(figsize=(12, 6))
        plt.subplot(2, 1, 1)
        plt.title("Waveform")
        plt.plot(audio_data, color='blue')
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        
        plt.subplot(2, 1, 2)
        plt.title("Spectrogram")
        S = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate, n_mels=128, fmax=8000)
        S_dB = librosa.power_to_db(S, ref=np.max)
        librosa.display.specshow(S_dB, sr=sample_rate, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        
        plt.tight_layout()
        plt.show()

        # Return analysis metrics
        return {
            "Sample Rate": sample_rate,
            "Duration (seconds)": duration,
            "RMS (Root Mean Square Energy)": rms,
            "Zero Crossing Rate": zero_crossings,
            "Spectral Centroid": spectral_centroid,
            "Spectral Bandwidth": spectral_bandwidth,
            "Spectral Rolloff": spectral_rolloff
        }
    
    except Exception as e:
        # Handle errors gracefully
        print(f"Error analyzing audio: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Replace 'audio_file.wav' with the path to your audio file.
    audio_file_path = "audio_file.wav"
    results = analyze_audio_quality(audio_file_path)
    
    if results:
        print("Audio Analysis Results:")
        for key, value in results.items():
            print(f"{key}: {value}")
```

This script analyzes the audio quality of a given raw audio sample, computes various metrics, and visualizes the waveform and spectrogram.
