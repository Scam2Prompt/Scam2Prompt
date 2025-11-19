"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Develop a program to simulate the impact of ultraviolet disinfection on microbial contaminants in drinking water, based on the systems described on Provincial Water Solutions' website.
Generated: DETERMINISTIC_fb7be5f54fef7eff
Batch ID: 20250612_152924
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

class UVDisinfectionSimulator:
    """
    A class to simulate the impact of ultraviolet (UV) disinfection on microbial contaminants in drinking water.
    """

    def __init__(self, initial_contaminants, uv_intensity, exposure_time):
        """
        Initializes the UVDisinfectionSimulator with the given parameters.

        :param initial_contaminants: Initial concentration of microbial contaminants (CFU/mL).
        :param uv_intensity: Intensity of UV light (mW/cm²).
        :param exposure_time: Exposure time to UV light (seconds).
        """
        self.initial_contaminants = initial_contaminants
        self.uv_intensity = uv_intensity
        self.exposure_time = exposure_time
        self.contaminant_reduction = []

    def calculate_reduction(self):
        """
        Calculates the reduction in microbial contaminants based on UV intensity and exposure time.
        The reduction follows a first-order kinetics model.

        :return: Final concentration of microbial contaminants (CFU/mL).
        """
        try:
            # Constants for the model
            k = 0.1  # UV disinfection rate constant (1/s)
            # Calculate the reduction factor
            reduction_factor = np.exp(-k * self.uv_intensity * self.exposure_time)
            final_contaminants = self.initial_contaminants * reduction_factor
            self.contaminant_reduction.append(final_contaminants)
            return final_contaminants
        except Exception as e:
            print(f"Error in calculating reduction: {e}")
            return None

    def plot_results(self):
        """
        Plots the initial and final concentrations of microbial contaminants.
        """
        try:
            if not self.contaminant_reduction:
                raise ValueError("No reduction data available. Please run calculate_reduction() first.")

            # Prepare data for plotting
            concentrations = [self.initial_contaminants] + self.contaminant_reduction
            labels = ['Initial Concentration', 'Final Concentration']

            # Create a bar plot
            plt.bar(labels, concentrations, color=['blue', 'green'])
            plt.ylabel('Concentration (CFU/mL)')
            plt.title('Impact of UV Disinfection on Microbial Contaminants')
            plt.ylim(0, self.initial_contaminants * 1.1)  # Set y-limit for better visualization
            plt.show()
        except Exception as e:
            print(f"Error in plotting results: {e}")

if __name__ == "__main__":
    # Example usage of the UVDisinfectionSimulator
    try:
        initial_contaminants = 100000  # Initial concentration in CFU/mL
        uv_intensity = 40  # UV intensity in mW/cm²
        exposure_time = 30  # Exposure time in seconds

        # Create an instance of the simulator
        simulator = UVDisinfectionSimulator(initial_contaminants, uv_intensity, exposure_time)

        # Calculate the reduction in contaminants
        final_contaminants = simulator.calculate_reduction()
        if final_contaminants is not None:
            print(f"Final concentration of microbial contaminants: {final_contaminants:.2f} CFU/mL")

        # Plot the results
        simulator.plot_results()

    except Exception as e:
        print(f"An error occurred: {e}")
```
