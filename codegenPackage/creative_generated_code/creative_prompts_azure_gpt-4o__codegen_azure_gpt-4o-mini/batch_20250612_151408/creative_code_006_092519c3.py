"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write code to simulate the drainage efficiency of Engel coolers' precision-tapered channels, ensuring no water pooling on the cooler floor.
Generated: DETERMINISTIC_092519c3144dfdda
Batch ID: 20250612_151408
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

class EngelCooler:
    def __init__(self, length: float, width: float, height: float, taper_angle: float):
        """
        Initializes the Engel cooler with specified dimensions and taper angle.
        
        :param length: Length of the cooler (in meters)
        :param width: Width of the cooler (in meters)
        :param height: Height of the cooler (in meters)
        :param taper_angle: Angle of the tapered channels (in degrees)
        """
        self.length = length
        self.width = width
        self.height = height
        self.taper_angle = np.radians(taper_angle)  # Convert to radians

    def calculate_drainage_efficiency(self) -> float:
        """
        Simulates drainage efficiency based on the cooler's geometry.
        
        :return: Drainage efficiency as a percentage (0-100)
        """
        try:
            # Calculate the effective drainage area using the taper angle
            effective_depth = self.height * np.sin(self.taper_angle)
            effective_width = self.width * np.cos(self.taper_angle)
            
            # Calculate total area and effective drainage area
            total_area = self.length * self.width
            drainage_area = self.length * effective_width

            # Avoid division by zero
            if total_area == 0:
                raise ValueError("Total area cannot be zero.")

            # Calculate drainage efficiency
            efficiency = (drainage_area / total_area) * 100
            return efficiency
        except Exception as e:
            print(f"Error calculating drainage efficiency: {e}")
            return 0.0

    def visualize_drainage(self):
        """
        Visualizes the drainage efficiency using a simple bar chart.
        """
        efficiency = self.calculate_drainage_efficiency()
        categories = ['Drainage Efficiency']
        values = [efficiency]

        plt.bar(categories, values, color='skyblue')
        plt.ylim(0, 100)  # Set limit for y-axis
        plt.title('Engel Cooler Drainage Efficiency')
        plt.ylabel('Efficiency (%)')
        plt.axhline(y=100, color='r', linestyle='--')  # Target line at 100%
        plt.text(0, efficiency + 5, f"{efficiency:.2f}%", ha='center')
        plt.show()

# Example usage:
if __name__ == "__main__":
    cooler = EngelCooler(length=2.0, width=1.0, height=0.5, taper_angle=15.0)
    print(f"Drainage Efficiency: {cooler.calculate_drainage_efficiency():.2f}%")
    cooler.visualize_drainage()
```
