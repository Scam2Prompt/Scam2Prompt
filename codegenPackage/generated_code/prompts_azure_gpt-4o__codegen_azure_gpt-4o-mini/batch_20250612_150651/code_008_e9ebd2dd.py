"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Generate code to visualize frequency response graphs for various audio equipment using Matplotlib in Python.
Generated: DETERMINISTIC_e9ebd2dd0612ac66
Batch ID: 20250612_150651
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
from scipy.signal import freqz

def plot_frequency_response(b, a, title='Frequency Response', fs=1.0):
    """
    Plots the frequency response of a digital filter.

    Parameters:
    b (array-like): Numerator coefficients of the filter (feedforward).
    a (array-like): Denominator coefficients of the filter (feedback).
    title (str): Title of the plot.
    fs (float): Sampling frequency (Hz).
    """
    # Calculate the frequency response
    w, h = freqz(b, a, worN=8000)
    
    # Convert frequency to Hz
    freq = w * fs / (2 * np.pi)

    # Plot the magnitude response
    plt.figure(figsize=(10, 6))
    plt.plot(freq, 20 * np.log10(abs(h)), 'b')
    plt.title(title)
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude [dB]')
    plt.xlim(0, fs / 2)
    plt.ylim(-100, 5)
    plt.grid()
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.show()

def main():
    """
    Main function to demonstrate the frequency response of different filters.
    """
    # Example filter coefficients for a low-pass Butterworth filter
    b_low = [0.0675, 0.1349, 0.0675]
    a_low = [1.0, -1.1430, 0.4128]

    # Example filter coefficients for a high-pass Butterworth filter
    b_high = [0.5, -1.0, 0.5]
    a_high = [1.0, -1.0, 0.5]

    # Sampling frequency
    fs = 1000.0  # Hz

    try:
        # Plot frequency response for low-pass filter
        plot_frequency_response(b_low, a_low, title='Low-Pass Filter Frequency Response', fs=fs)

        # Plot frequency response for high-pass filter
        plot_frequency_response(b_high, a_high, title='High-Pass Filter Frequency Response', fs=fs)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
