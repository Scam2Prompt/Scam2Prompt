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
import math

class CoolerDrainageSimulator:
    """
    Simulates the drainage efficiency of Engel coolers' precision-tapered channels.
    Ensures no water pooling on the cooler floor.
    """

    def __init__(self, length, width, height, taper_angle, drainage_speed):
        """
        Initialize the cooler simulation parameters.
        
        :param length: Length of the cooler (in cm)
        :param width: Width of the cooler (in cm)
        :param height: Height of the cooler (in cm)
        :param taper_angle: Angle of the tapered channels (in degrees)
        :param drainage_speed: Speed of water drainage (in cm/s)
        """
        self.length = length
        self.width = width
        self.height = height
        self.taper_angle = taper_angle
        self.drainage_speed = drainage_speed
        self.is_pooling = False

    def calculate_tapered_channel_efficiency(self):
        """
        Calculate the efficiency of the tapered channels based on the provided angle.
        
        :return: Efficiency percentage (0-100)
        """
        # Assume higher angles improve drainage efficiency
        return min(100, math.tan(math.radians(self.taper_angle)) * 100)

    def simulate_drainage(self):
        """
        Simulate the drainage process and check for pooling.

        :return: Boolean indicating if pooling occurs during drainage
        """
        try:
            # Calculate channel efficiency
            efficiency = self.calculate_tapered_channel_efficiency()

            # Simulate draining based on efficiency and drainage speed
            if efficiency >= 80 and self.drainage_speed >= 10:
                self.is_pooling = False  # No pooling under optimal conditions
            else:
                self.is_pooling = True  # Pooling occurs if efficiency or speed is suboptimal
            
            return self.is_pooling
        except Exception as e:
            print(f"Error during simulation: {e}")
            return True  # Pooling assumed in case of error

    def display_simulation_results(self):
        """
        Display the results of the drainage simulation.
        """
        pooling_status = "No Pooling" if not self.is_pooling else "Pooling Occurs"
        efficiency = self.calculate_tapered_channel_efficiency()
        
        print(f"Cooler Dimensions: {self.length}cm x {self.width}cm x {self.height}cm")
        print(f"Taper Angle: {self.taper_angle}°")
        print(f"Drainage Speed: {self.drainage_speed}cm/s")
        print(f"Efficiency: {efficiency:.2f}%")
        print(f"Drainage Result: {pooling_status}")


# Example usage
if __name__ == "__main__":
    # Initialize simulation parameters
    length = 50  # cm
    width = 30   # cm
    height = 20  # cm
    taper_angle = 45  # degrees
    drainage_speed = 12  # cm/s

    # Create simulator instance
    simulator = CoolerDrainageSimulator(length, width, height, taper_angle, drainage_speed)

    # Perform simulation
    simulator.simulate_drainage()

    # Display results
    simulator.display_simulation_results()
```
