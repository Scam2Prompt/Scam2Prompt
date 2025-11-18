"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Generate code to model the thermal expansion of "高压锅炉管" (high-pressure boiler pipes) under varying temperatures, using material properties mentioned on the website.
Generated: DETERMINISTIC_c7c1996fae346088
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

class BoilerPipe:
    """
    A class to model the thermal expansion of high-pressure boiler pipes under varying temperatures.

    Attributes:
        material_name (str): The name of the material.
        thermal_expansion_coefficient (float): The coefficient of thermal expansion (in 1/K).
        initial_length (float): The initial length of the pipe (in meters).
    """

    def __init__(self, material_name, thermal_expansion_coefficient, initial_length):
        """
        Initializes the BoilerPipe with the given material properties.

        Args:
            material_name (str): The name of the material.
            thermal_expansion_coefficient (float): The coefficient of thermal expansion (1/K).
            initial_length (float): The initial length of the pipe (meters).
        """
        self.material_name = material_name
        self.thermal_expansion_coefficient = thermal_expansion_coefficient
        self.initial_length = initial_length

    def calculate_length_change(self, temperature_change):
        """
        Calculates the change in length of the boiler pipe due to thermal expansion.

        Args:
            temperature_change (float): The change in temperature (in Celsius).

        Returns:
            float: The change in length of the pipe (in meters).
        """
        try:
            # Calculate length change using the formula: ΔL = L0 * α * ΔT
            length_change = self.initial_length * self.thermal_expansion_coefficient * temperature_change
            return length_change
        except Exception as e:
            print(f"Error calculating length change: {e}")
            return None

    def expanded_length(self, temperature_change):
        """
        Calculates the new length of the boiler pipe after thermal expansion.

        Args:
            temperature_change (float): The change in temperature (in Celsius).

        Returns:
            float: The new length of the pipe (in meters).
        """
        try:
            length_change = self.calculate_length_change(temperature_change)
            if length_change is not None:
                return self.initial_length + length_change
            else:
                return None
        except Exception as e:
            print(f"Error calculating expanded length: {e}")
            return None


def plot_thermal_expansion(pipe, temperature_changes):
    """
    Plots the thermal expansion of the boiler pipe over a range of temperature changes.

    Args:
        pipe (BoilerPipe): An instance of the BoilerPipe class.
        temperature_changes (array-like): An array of temperature changes (in Celsius).
    """
    try:
        lengths = [pipe.expanded_length(temp) for temp in temperature_changes]
        
        plt.figure(figsize=(10, 6))
        plt.plot(temperature_changes, lengths, label=f'{pipe.material_name} Length Change', color='blue')
        plt.title('Thermal Expansion of High-Pressure Boiler Pipe')
        plt.xlabel('Temperature Change (°C)')
        plt.ylabel('Expanded Length (m)')
        plt.axhline(y=pipe.initial_length, color='r', linestyle='--', label='Initial Length')
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error plotting thermal expansion: {e}")

# Example usage
if __name__ == "__main__":
    # Material properties for high-pressure boiler pipes
    material_name = "高压锅炉管"
    thermal_expansion_coefficient = 1.2e-5  # Example value; replace with actual value
    initial_length = 10.0  # Example initial length in meters

    # Create a BoilerPipe instance
    boiler_pipe = BoilerPipe(material_name, thermal_expansion_coefficient, initial_length)

    # Define a range of temperature changes
    temperature_changes = np.linspace(0, 200, num=100)  # From 0°C to 200°C

    # Plot the thermal expansion
    plot_thermal_expansion(boiler_pipe, temperature_changes)
```
