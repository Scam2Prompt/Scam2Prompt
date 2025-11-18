"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Write a program to simulate the acoustic insulation performance of UPVC windows, referencing the specifications provided by Dexodoor.
Generated: DETERMINISTIC_ca13114fdd6fe4bb
Batch ID: 20250612_152441
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

class UPVCWindow:
    def __init__(self, thickness: float, lamination_factor: float, noise_reduction_index: float):
        """
        Initialize the UPVC Window specifications.

        :param thickness: Thickness of the window (in mm)
        :param lamination_factor: Factor accounting for lamination effects
        :param noise_reduction_index: Rw (Weighted Sound Reduction Index) in dB
        """
        self.thickness = thickness  # Window thickness
        self.lamination_factor = lamination_factor  # Lamination effect
        self.noise_reduction_index = noise_reduction_index  # Noise reduction index

    def calculate_acoustic_insulation(self, frequency: np.ndarray) -> np.ndarray:
        """
        Calculate the acoustic insulation performance (in dB) for given frequencies.

        :param frequency: Numpy array of frequencies (in Hz)
        :return: Numpy array of calculated insulation performance (in dB)
        """
        if not isinstance(frequency, np.ndarray):
            raise ValueError("Frequency must be a NumPy array.")
        
        # Basic model based on frequency, thickness, and noise reduction index
        insulation_performance = (
            self.noise_reduction_index 
            - (20 * np.log10(frequency)) 
            + (self.lamination_factor * self.thickness / 100)
        )
        
        return insulation_performance

    def plot_insulation_graph(self, frequency: np.ndarray):
        """
        Plot the acoustic insulation performance graph.

        :param frequency: Numpy array of frequencies (in Hz)
        """
        insulation = self.calculate_acoustic_insulation(frequency)

        plt.figure(figsize=(10, 6))
        plt.plot(frequency, insulation, label='Acoustic Insulation', color='blue')
        plt.title('Acoustic Insulation Performance of UPVC Windows')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Insulation Performance (dB)')
        plt.grid()
        plt.legend()
        plt.xscale('log')  # Logarithmic scale for frequency
        plt.xlim(frequency[0], frequency[-1])
        plt.ylim(min(insulation) - 10, max(insulation) + 10)
        plt.axhline(0, color='red', linestyle='--', label='Reference Level')
        plt.legend()
        plt.show()

def main():
    # Example specifications for a UPVC window
    thickness_mm = 32.0  # Example thickness in mm
    lamination_factor = 1.5  # Example lamination factor
    noise_reduction_index = 35.0  # Example Rw in dB

    # Create a UPVC window object
    upvc_window = UPVCWindow(thickness_mm, lamination_factor, noise_reduction_index)

    # Frequency range for simulation (20 Hz to 20 kHz)
    frequency = np.logspace(1, 4, num=400)  # 10^1 to 10^4 Hz

    try:
        # Plot the insulation performance
        upvc_window.plot_insulation_graph(frequency)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
