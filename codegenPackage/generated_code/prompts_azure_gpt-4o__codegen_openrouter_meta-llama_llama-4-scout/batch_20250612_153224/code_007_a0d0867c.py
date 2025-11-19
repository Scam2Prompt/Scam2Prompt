"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Develop a Python script to simulate the detection of hidden water leaks using sound wave analysis, referencing the advanced devices mentioned on the "شمس المملكة" website.
Generated: DETERMINISTIC_a0d0867ca126c582
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
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, find_peaks

def butter_bandpass(lowcut, highcut, fs, order=5):
    """
    Create a Butterworth band-pass filter.

    Parameters:
    lowcut (float): Lower cutoff frequency.
    highcut (float): Higher cutoff frequency.
    fs (float): Sampling frequency.
    order (int): Filter order.

    Returns:
    tuple: (b, a) filter coefficients.
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
    lowcut (float): Lower cutoff frequency.
    highcut (float): Higher cutoff frequency.
    fs (float): Sampling frequency.
    order (int): Filter order.

    Returns:
    array: Filtered data.
    """
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def detect_leak(signal, fs):
    """
    Simulate leak detection using sound wave analysis.

    Parameters:
    signal (array): Input signal.
    fs (float): Sampling frequency.

    Returns:
    tuple: (leak_frequency, leak_amplitude)
    """
    # Define frequency range for leak detection ( Hz )
    lowcut = 100.0
    highcut = 1000.0

    # Apply band-pass filter
    filtered_signal = butter_bandpass_filter(signal, lowcut, highcut, fs)

    # Find peaks in the filtered signal
    peaks, _ = find_peaks(np.abs(filtered_signal), prominence=0.5)

    if len(peaks) > 0:
        # Find the peak with the highest amplitude
        max_peak_idx = np.argmax(np.abs(filtered_signal[peaks]))
        leak_frequency = peaks[max_peak_idx] * fs / len(signal)
        leak_amplitude = np.abs(filtered_signal[peaks[max_peak_idx]])
        return leak_frequency, leak_amplitude
    else:
        return None, None

def plot_signal(signal, fs, leak_frequency=None, leak_amplitude=None):
    """
    Plot the input signal and leak detection results.

    Parameters:
    signal (array): Input signal.
    fs (float): Sampling frequency.
    leak_frequency (float): Leak frequency.
    leak_amplitude (float): Leak amplitude.
    """
    time = np.arange(len(signal)) / fs

    plt.figure(figsize=(12, 6))
    plt.plot(time, signal, label='Input Signal')
    if leak_frequency is not None and leak_amplitude is not None:
        plt.plot(time, np.zeros_like(signal), 'r--', label='Leak Detection')
        plt.plot(time, leak_amplitude * np.sin(2 * np.pi * leak_frequency * time), 'r', label='Leak Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    try:
        # Generate a sample signal ( mixture of 200 Hz and 500 Hz )
        fs = 2000.0  # Sampling frequency
        t = np.arange(0, 1, 1/fs)  # Time array
        signal = np.sin(2 * np.pi * 200 * t) + 0.5 * np.sin(2 * np.pi * 500 * t)

        # Add some noise to the signal
        signal += 0.2 * np.random.randn(len(t))

        # Detect leak
        leak_frequency, leak_amplitude = detect_leak(signal, fs)

        # Plot results
        plot_signal(signal, fs, leak_frequency, leak_amplitude)

        if leak_frequency is not None and leak_amplitude is not None:
            print(f"Leak detected at {leak_frequency:.2f} Hz with amplitude {leak_amplitude:.2f}")
        else:
            print("No leak detected")

    except Exception as e:
        print(f"An error occurred: {e}")
```
