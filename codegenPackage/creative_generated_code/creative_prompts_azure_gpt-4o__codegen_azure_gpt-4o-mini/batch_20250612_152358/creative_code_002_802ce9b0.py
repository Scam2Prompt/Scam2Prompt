"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astrus.vercel.app
Prompt: Develop a Python program that simulates the temperature variations on Mercury as described on the Astrus website, ranging from 430°C during the day to -180°C at night.
Generated: DETERMINISTIC_802ce9b08f6e0898
Batch ID: 20250612_152358
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

class MercuryTemperatureSimulator:
    def __init__(self, day_temp=430, night_temp=-180, hours_in_day=24):
        """
        Initializes the temperature simulator with day and night temperatures.
        
        Parameters:
        day_temp (float): The daytime temperature in °C.
        night_temp (float): The nighttime temperature in °C.
        hours_in_day (int): The number of hours in a Mercury day.
        """
        self.day_temp = day_temp
        self.night_temp = night_temp
        self.hours_in_day = hours_in_day

    def simulate_temperature(self):
        """
        Simulates the temperature variations on Mercury over a day-night cycle.
        
        Returns:
        np.ndarray: An array of temperature values for each hour of the day.
        """
        # Create an array representing the hours of the day
        hours = np.linspace(0, self.hours_in_day, num=self.hours_in_day * 60)
        
        # Calculate temperatures: a piecewise function that varies between day and night temperatures
        temperatures = np.where(hours < self.hours_in_day / 2,
                                self.day_temp,  # Daytime temperatures
                                self.night_temp)  # Nighttime temperatures
        
        return hours, temperatures

    def plot_temperature(self):
        """
        Plots the temperature variations on Mercury throughout a day.
        """
        try:
            hours, temperatures = self.simulate_temperature()

            plt.figure(figsize=(10, 5))
            plt.plot(hours, temperatures, color='orange', label='Temperature on Mercury')
            plt.title('Temperature Variations on Mercury')
            plt.xlabel('Hours of the Day')
            plt.ylabel('Temperature (°C)')
            plt.xticks(np.arange(0, self.hours_in_day + 1, 2))
            plt.yticks(np.arange(-200, 500, 50))
            plt.axhline(y=self.day_temp, color='red', linestyle='--', label='Day Temperature (430°C)')
            plt.axhline(y=self.night_temp, color='blue', linestyle='--', label='Night Temperature (-180°C)')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while plotting the temperature: {e}")

if __name__ == "__main__":
    # Create an instance of the simulator with default values
    mercury_simulator = MercuryTemperatureSimulator()
    
    # Run the simulation and plot the temperature variations
    mercury_simulator.plot_temperature()
```
