"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Write code to simulate the drainage efficiency of Engel coolers' precision-tapered channels, ensuring no water pooling on the cooler floor.
Generated: DETERMINISTIC_092519c3144dfdda
Batch ID: 20250612_151408
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

class EngelCooler:
    def __init__(self, channel_length, channel_width, taper_angle, floor_length, floor_width):
        """
        Initialize the Engel cooler with its geometric parameters.

        Args:
        - channel_length (float): Length of the channel.
        - channel_width (float): Width of the channel at the inlet.
        - taper_angle (float): Taper angle of the channel in degrees.
        - floor_length (float): Length of the cooler floor.
        - floor_width (float): Width of the cooler floor.
        """
        self.channel_length = channel_length
        self.channel_width = channel_width
        self.taper_angle = np.deg2rad(taper_angle)  # Convert to radians
        self.floor_length = floor_length
        self.floor_width = floor_width

    def calculate_channel_widths(self):
        """
        Calculate the widths of the channel along its length.

        Returns:
        - widths (numpy array): Array of widths at each point along the channel.
        """
        widths = self.channel_width - self.channel_length * np.tan(self.taper_angle) * np.linspace(0, 1, 100)
        return widths

    def simulate_water_flow(self, water_volume, viscosity=0.001):
        """
        Simulate the water flow through the channel.

        Args:
        - water_volume (float): Volume of water.
        - viscosity (float, optional): Viscosity of water. Defaults to 0.001.

        Returns:
        - water_height (float): Height of water on the floor.
        - pooling (bool): Whether water pooling occurs.
        """
        # Calculate the channel widths
        widths = self.calculate_channel_widths()

        # Calculate the cross-sectional area of the channel
        areas = widths * 0.01  # Assuming a constant height of 0.01 units

        # Calculate the flow rate using the Hagen-Poiseuille equation
        flow_rate = (water_volume / (self.channel_length * viscosity)) * np.mean(areas**2)

        # Calculate the water height on the floor
        water_height = water_volume / (self.floor_length * self.floor_width)

        # Check for water pooling
        pooling = water_height > 0.01  # Assuming a threshold height of 0.01 units

        return water_height, pooling

    def optimize_channel_design(self, max_water_height, max_pooling_probability):
        """
        Optimize the channel design to prevent water pooling.

        Args:
        - max_water_height (float): Maximum allowed water height.
        - max_pooling_probability (float): Maximum allowed probability of water pooling.

        Returns:
        - optimal_taper_angle (float): Optimal taper angle.
        """
        taper_angles = np.linspace(0, np.pi/2, 100)
        pooling_probabilities = []

        for taper_angle in taper_angles:
            self.taper_angle = taper_angle
            water_height, pooling = self.simulate_water_flow(1.0)
            pooling_probabilities.append(pooling)

        optimal_taper_angle = taper_angles[np.argmin(np.array(pooling_probabilities) - max_pooling_probability)]

        return np.rad2deg(optimal_taper_angle)


# Example usage
if __name__ == "__main__":
    cooler = EngelCooler(channel_length=10, channel_width=1, taper_angle=10, floor_length=10, floor_width=10)
    water_height, pooling = cooler.simulate_water_flow(1.0)
    print(f"Water height: {water_height:.4f}, Pooling: {pooling}")

    optimal_taper_angle = cooler.optimize_channel_design(max_water_height=0.1, max_pooling_probability=0.1)
    print(f"Optimal taper angle: {optimal_taper_angle:.2f} degrees")

    # Plot the channel widths
    widths = cooler.calculate_channel_widths()
    plt.plot(widths)
    plt.xlabel("Distance along channel")
    plt.ylabel("Width")
    plt.title("Channel Widths")
    plt.show()
```
