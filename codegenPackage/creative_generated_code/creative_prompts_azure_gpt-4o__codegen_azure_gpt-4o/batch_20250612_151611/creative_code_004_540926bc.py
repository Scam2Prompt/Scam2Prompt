"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Suggest a library or tool for ultrasonic cleaning simulation, and write code to model the cleaning of pintle valves and filter baskets in fuel injectors, as described on the site.
Generated: DETERMINISTIC_540926bcd22865c1
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the UltrasonicCleaningSimulation class
class UltrasonicCleaningSimulation:
    """
    A class to model ultrasonic cleaning for pintle valves and filter baskets in fuel injectors.
    """

    def __init__(self, frequency, amplitude, cleaning_duration):
        """
        Initialize the simulation parameters.
        
        :param frequency: Frequency of ultrasonic waves in kHz
        :param amplitude: Amplitude of ultrasonic waves in microns
        :param cleaning_duration: Cleaning duration in seconds
        """
        self.frequency = frequency  # kHz
        self.amplitude = amplitude  # microns
        self.cleaning_duration = cleaning_duration  # seconds

    def simulate_cleaning(self, object_type):
        """
        Simulate the cleaning process for different objects.
        
        :param object_type: Type of object to clean ("pintle_valve" or "filter_basket")
        :return: A dictionary containing cleaning efficiency data
        """
        try:
            # Validate object type
            if object_type not in ["pintle_valve", "filter_basket"]:
                raise ValueError("Invalid object type. Must be 'pintle_valve' or 'filter_basket'.")

            # Define cleaning efficiency model
            time_steps = np.linspace(0, self.cleaning_duration, 100)
            if object_type == "pintle_valve":
                # Pintle valves have higher surface area-to-volume ratio
                efficiency = self.amplitude * np.sin(2 * np.pi * self.frequency * time_steps) * 0.8
            elif object_type == "filter_basket":
                # Filter baskets require higher intensity cleaning due to finer debris
                efficiency = self.amplitude * np.sin(2 * np.pi * self.frequency * time_steps) * 1.2

            # Clip efficiency to a maximum value of 100%
            efficiency = np.clip(efficiency, 0, 100)

            # Package the results
            cleaning_data = {
                "time_steps": time_steps,
                "efficiency": efficiency,
                "object_type": object_type
            }
            return cleaning_data

        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

    def plot_efficiency(self, cleaning_data):
        """
        Plot cleaning efficiency over time.
        
        :param cleaning_data: Dictionary containing cleaning efficiency data
        """
        try:
            # Extract data for plotting
            time_steps = cleaning_data["time_steps"]
            efficiency = cleaning_data["efficiency"]
            object_type = cleaning_data["object_type"]

            # Create the plot
            plt.figure(figsize=(10, 6))
            plt.plot(time_steps, efficiency, label=f'{object_type.capitalize()} Cleaning Efficiency')
            plt.xlabel('Time (s)')
            plt.ylabel('Efficiency (%)')
            plt.title('Ultrasonic Cleaning Efficiency Over Time')
            plt.legend()
            plt.grid(True)
            plt.show()

        except KeyError as e:
            print(f"Error: Missing key in cleaning_data dictionary - {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred while plotting: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize simulation parameters
    frequency = 40  # kHz
    amplitude = 10  # microns
    cleaning_duration = 10  # seconds

    # Create an instance of the simulation class
    simulation = UltrasonicCleaningSimulation(frequency, amplitude, cleaning_duration)

    # Simulate cleaning for pintle valves
    pintle_valve_data = simulation.simulate_cleaning("pintle_valve")

    if pintle_valve_data:
        simulation.plot_efficiency(pintle_valve_data)

    # Simulate cleaning for filter baskets
    filter_basket_data = simulation.simulate_cleaning("filter_basket")

    if filter_basket_data:
        simulation.plot_efficiency(filter_basket_data)
```
