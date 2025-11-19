"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Suggest tools or libraries for creating unique sound textures by combining acoustic and electronic elements, as Jérémie Frémont does in his compositions.
Generated: DETERMINISTIC_d00afb23ec7f1c9f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sound_texture_generator.py

import numpy as np
import librosa
import soundfile as sf
from scipy.signal import butter, lfilter
from pydub import AudioSegment

def butter_bandpass(lowcut, highcut, fs, order=5):
    """
    Create a Butterworth band-pass filter.

    Parameters:
    lowcut (float): Low frequency cutoff.
    highcut (float): High frequency cutoff.
    fs (int): Sample rate.
    order (int): Filter order.

    Returns:
    b, a (ndarray): Filter coefficients.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    """
    Apply a Butterworth band-pass filter.

    Parameters:
    data (ndarray): Audio data.
    lowcut (float): Low frequency cutoff.
    highcut (float): High cutoff.
    fs (int): Sample rate.
    order (int): Filter order.

    Returns:
    y (ndarray): Filtered audio data.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def generate_sound_texture(acoustic_file, electronic_file, output_file, 
                           lowcut=20, highcut=20000, 
                           acoustic_gain=1.0, electronic_gain=1.0):
    """
    Combine acoustic and electronic elements to create a unique sound texture.

    Parameters:
    acoustic_file (str): Path to acoustic audio file.
    electronic_file (str): Path to electronic audio file.
    output_file (str): Path to output audio file.
    lowcut (float): Low frequency cutoff. Defaults to 20 Hz.
    highcut (float): High frequency cutoff. Defaults to 20000 Hz.
    acoustic_gain (float): Acoustic audio gain. Defaults to 1.0.
    electronic_gain (float): Electronic audio gain. Defaults to 1.0.
    """
    try:
        # Load acoustic and electronic audio files
        acoustic_audio, acoustic_fs = librosa.load(acoustic_file)
        electronic_audio, electronic_fs = librosa.load(electronic_file)

        # Ensure both audio files have the same sample rate
        if acoustic_fs != electronic_fs:
            electronic_audio = librosa.resample(electronic_audio, electronic_fs, acoustic_fs)

        # Apply band-pass filter to acoustic audio
        acoustic_audio_filtered = butter_bandpass_filter(acoustic_audio, lowcut, highcut, acoustic_fs)

        # Apply gain to acoustic and electronic audio
        acoustic_audio_filtered *= acoustic_gain
        electronic_audio *= electronic_gain

        # Combine acoustic and electronic audio
        combined_audio = acoustic_audio_filtered + electronic_audio

        # Normalize combined audio to prevent clipping
        combined_audio_normalized = combined_audio / np.max(np.abs(combined_audio))

        # Save combined audio to file
        sf.write(output_file, combined_audio_normalized, acoustic_fs)

    except Exception as e:
        print(f"Error generating sound texture: {e}")

# Example usage
if __name__ == "__main__":
    acoustic_file = "acoustic.wav"
    electronic_file = "electronic.wav"
    output_file = "output.wav"

    generate_sound_texture(acoustic_file, electronic_file, output_file)
```

```python
# install required libraries
# pip install numpy librosa soundfile scipy pydub
```
