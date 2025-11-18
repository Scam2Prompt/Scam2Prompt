"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Write code to simulate the corrosion resistance of "316不锈钢管" (316 stainless steel pipes) in a marine environment, using the technical details from the website.
Generated: DETERMINISTIC_0a7025121bafc453
Batch ID: 20250612_154905
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

class CorrosionResistanceSimulator:
    """
    A class to simulate the corrosion resistance of 316 stainless steel pipes in a marine environment.
    
    Attributes:
        exposure_time (float): Time of exposure to the marine environment in years.
        corrosion_rate (float): Corrosion rate of 316 stainless steel in mm/year.
    """

    def __init__(self, exposure_time: float, corrosion_rate: float = 0.1):
        """
        Initializes the simulator with exposure time and corrosion rate.
        
        Parameters:
            exposure_time (float): The time in years for which the pipes are exposed to the marine environment.
            corrosion_rate (float): The corrosion rate in mm/year. Default is set to 0.1 mm/year.
        """
        if exposure_time < 0:
            raise ValueError("Exposure time must be a non-negative value.")
        if corrosion_rate < 0:
            raise ValueError("Corrosion rate must be a non-negative value.")
        
        self.exposure_time = exposure_time
        self.corrosion_rate = corrosion_rate
        self.corrosion_depth = self.calculate_corrosion_depth()

    def calculate_corrosion_depth(self) -> float:
        """
        Calculates the total corrosion depth over the exposure time.
        
        Returns:
            float: Total corrosion depth in mm.
        """
        return self.corrosion_rate * self.exposure_time

    def plot_corrosion_progression(self):
        """
        Plots the corrosion progression over time.
        """
        years = np.arange(0, self.exposure_time + 1, 1)
        depths = [self.corrosion_rate * year for year in years]

        plt.figure(figsize=(10, 5))
        plt.plot(years, depths, marker='o')
        plt.title('Corrosion Progression of 316 Stainless Steel Pipes in Marine Environment')
        plt.xlabel('Years of Exposure')
        plt.ylabel('Corrosion Depth (mm)')
        plt.grid()
        plt.axhline(y=self.corrosion_depth, color='r', linestyle='--', label='Total Corrosion Depth')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        exposure_time = float(input("Enter exposure time in years: "))
        corrosion_simulator = CorrosionResistanceSimulator(exposure_time)
        print(f"Total corrosion depth after {exposure_time} years: {corrosion_simulator.corrosion_depth} mm")
        corrosion_simulator.plot_corrosion_progression()
    except ValueError as e:
        print(f"Error: {e}")
```
