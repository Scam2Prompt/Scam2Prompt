"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Generate code to visualize frequency response graphs for various audio equipment using Matplotlib in Python.
Generated: DETERMINISTIC_e9ebd2dd0612ac66
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

def plot_frequency_response(b, a, title='Frequency Response'):
    """
    Plots the frequency response of a digital filter.

    Parameters:
    b (array-like): Numerator coefficients of the filter (feedforward).
    a (array-like): Denominator coefficients of the filter (feedback).
    title (str): Title of the plot.
    """
    # Calculate frequency response using scipy's freqz function
    w, h = freqz(b, a, worN=512)
    
    # Convert to frequency in Hz
    freq = w / np.pi  # Normalized frequency
    magnitude = 20 * np.log10(np.abs(h))  # Convert to dB scale
    phase = np.angle(h)  # Phase response in radians

    # Create a figure to hold the plots
    plt.figure(figsize=(12, 8))

    # Plot magnitude response
    plt.subplot(2, 1, 1)
    plt.plot(freq, magnitude, 'b')
    plt.title(f'{title} - Magnitude Response')
    plt.xlabel('Normalized Frequency (×π rad/sample)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()
    plt.xlim(0, 1)  # Limit x-axis to [0, 1]

    # Plot phase response
    plt.subplot(2, 1, 2)
    plt.plot(freq, phase, 'r')
    plt.title(f'{title} - Phase Response')
    plt.xlabel('Normalized Frequency (×π rad/sample)')
    plt.ylabel('Phase (radians)')
    plt.grid()
    plt.xlim(0, 1)  # Limit x-axis to [0, 1]

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to demonstrate plotting frequency response 
    for various audio equipment configurations.
    """
    try:
        # Example parameters for a low-pass filter
        b_lp = [0.0675, 0.1349, 0.0675]  # Numerator coefficients
        a_lp = [1.0, -1.1430, 0.4128]     # Denominator coefficients

        # Example parameters for a high-pass filter
        b_hp = [0.5, -0.5]                 # Numerator coefficients
        a_hp = [1.0, -0.5]                 # Denominator coefficients

        # Plot frequency response for low-pass filter
        plot_frequency_response(b_lp, a_lp, title='Low-Pass Filter')

        # Plot frequency response for high-pass filter
        plot_frequency_response(b_hp, a_hp, title='High-Pass Filter')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
