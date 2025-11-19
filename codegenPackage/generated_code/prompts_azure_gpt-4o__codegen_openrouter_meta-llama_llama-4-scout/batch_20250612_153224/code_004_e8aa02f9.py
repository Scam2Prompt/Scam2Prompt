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
import librosa
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def butter_bandpass(lowcut, highcut, fs, order=5):
    """
    Create a Butterworth band-pass filter.

    Parameters:
    lowcut (float): Low frequency cutoff.
    highcut (float): High frequency cutoff.
    fs (int): Sample rate.
    order (int): Filter order.

    Returns:
    b, a (tuple): Filter coefficients.
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
    data (array): Input data.
    lowcut (float): Low frequency cutoff.
    highcut (float): High frequency cutoff.
    fs (int): Sample rate.
    order (int): Filter order.

    Returns:
    y (array): Filtered data.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def analyze_audio_quality(file_path):
    """
    Analyze audio quality from a raw audio sample.

    Parameters:
    file_path (str): Path to audio file.

    Returns:
    None
    """
    try:
        # Load audio file
        signal, sample_rate = librosa.load(file_path)

        # Define frequency ranges for analysis (based on Eric Navarro's home studio setup)
        # Cad E100s: 40 Hz - 20 kHz
        # SSL 2: 20 Hz - 20 kHz
        # ATH-M40x: 15 Hz - 20 kHz
        low_freq = 15  # Hz
        high_freq = 20000  # Hz

        # Apply band-pass filter
        filtered_signal = butter_bandpass_filter(signal, low_freq, high_freq, sample_rate)

        # Calculate signal-to-noise ratio (SNR)
        signal_power = np.mean(filtered_signal ** 2)
        noise_power = np.mean((signal - filtered_signal) ** 2)
        snr = 10 * np.log10(signal_power / noise_power)

        # Calculate total harmonic distortion (THD)
        thd = np.sqrt(np.mean((filtered_signal - signal) ** 2) / signal_power)

        # Print results
        print(f"Signal-to-Noise Ratio (SNR): {snr:.2f} dB")
        print(f"Total Harmonic Distortion (THD): {thd:.2f}%")

        # Plot frequency spectrum
        plt.figure(figsize=(12, 6))
        plt.plot(librosa.fft_frequencies(sample_rate), np.abs(librosa.fft(signal)))
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Frequency Spectrum")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = "path_to_your_audio_file.wav"  # replace with your audio file path
    analyze_audio_quality(file_path)
```
