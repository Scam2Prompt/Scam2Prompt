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
import matplotlib.pyplot as plt
import numpy as np

def plot_frequency_response(frequencies, gains, phase_shifts, title, xlabel='Frequency (Hz)', ylabel='Gain (dB)'):
    """
    Plot the frequency response graph.

    Parameters:
    frequencies (list): List of frequency values.
    gains (list): List of gain values corresponding to frequencies.
    phase_shifts (list): List of phase shift values corresponding to frequencies.
    title (str): Title of the plot.
    xlabel (str): Label for the x-axis. Defaults to 'Frequency (Hz)'.
    ylabel (str): Label for the y-axis. Defaults to 'Gain (dB)'.
    """

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(2, figsize=(10, 6))

    # Plot the frequency response (gain)
    axs[0].plot(frequencies, gains)
    axs[0].set_title('Frequency Response (Gain)')
    axs[0].set_xlabel(xlabel)
    axs[0].set_ylabel(ylabel)

    # Plot the phase response
    axs[1].plot(frequencies, phase_shifts)
    axs[1].set_title('Phase Response')
    axs[1].set_xlabel(xlabel)
    axs[1].set_ylabel('Phase Shift (degrees)')

    # Layout so plots do not overlap
    fig.tight_layout()

    # Set the title of the plot
    fig.suptitle(title)

    # Display the plot
    plt.show()

def generate_frequency_response(frequencies, equipment):
    """
    Generate frequency response data for various audio equipment.

    Parameters:
    frequencies (list): List of frequency values.
    equipment (str): Type of audio equipment.

    Returns:
    tuple: Tuple containing lists of gain and phase shift values.
    """

    # Define the frequency response characteristics for different equipment
    equipment_characteristics = {
        'microphone': {'gain': 20, 'phase_shift': 0},
        'speaker': {'gain': 10, 'phase_shift': 30},
        'headphone': {'gain': 15, 'phase_shift': 20},
        'amplifier': {'gain': 30, 'phase_shift': 10}
    }

    # Check if equipment is supported
    if equipment not in equipment_characteristics:
        raise ValueError(f"Unsupported equipment: {equipment}")

    # Generate gain and phase shift values
    gain = [equipment_characteristics[equipment]['gain'] + 5 * np.sin(2 * np.pi * f / 1000) for f in frequencies]
    phase_shift = [equipment_characteristics[equipment]['phase_shift'] + 2 * np.sin(2 * np.pi * f / 500) for f in frequencies]

    return gain, phase_shift

def main():
    try:
        # Generate frequency values
        frequencies = np.logspace(20, 20000, 1000)

        # Generate frequency response data for different equipment
        equipment_types = ['microphone', 'speaker', 'headphone', 'amplifier']

        for equipment in equipment_types:
            gain, phase_shift = generate_frequency_response(frequencies, equipment)
            plot_frequency_response(frequencies, gain, phase_shift, f'Frequency Response of {equipment.capitalize()}')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
