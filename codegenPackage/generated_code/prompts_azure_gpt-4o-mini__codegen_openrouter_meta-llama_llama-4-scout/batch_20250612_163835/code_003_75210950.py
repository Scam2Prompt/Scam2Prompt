"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Develop a code snippet to compare the insulation performance of Engel's UltraLite Coolers against traditional coolers.
Generated: DETERMINISTIC_7521095042b81baa
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

class Cooler:
    """Base class for coolers"""
    
    def __init__(self, name, insulation_thickness, insulation_r_value):
        """
        Initialize a cooler object.

        Args:
        - name (str): Name of the cooler
        - insulation_thickness (float): Thickness of insulation in inches
        - insulation_r_value (float): R-value of insulation
        """
        self.name = name
        self.insulation_thickness = insulation_thickness
        self.insulation_r_value = insulation_r_value

    def calculate_insulation_performance(self, ambient_temperature, internal_temperature):
        """
        Calculate insulation performance.

        Args:
        - ambient_temperature (float): Ambient temperature in Fahrenheit
        - internal_temperature (float): Internal temperature in Fahrenheit

        Returns:
        - float: Insulation performance (R-value * thickness)
        """
        temperature_difference = ambient_temperature - internal_temperature
        insulation_performance = self.insulation_r_value * self.insulation_thickness / temperature_difference
        return insulation_performance


class EngelUltraLiteCooler(Cooler):
    """Engel's UltraLite Cooler class"""
    
    def __init__(self, insulation_thickness=2.0, insulation_r_value=10.0):
        """
        Initialize an Engel's UltraLite Cooler object.

        Args:
        - insulation_thickness (float): Thickness of insulation in inches (default: 2.0)
        - insulation_r_value (float): R-value of insulation (default: 10.0)
        """
        super().__init__("Engel's UltraLite Cooler", insulation_thickness, insulation_r_value)


class TraditionalCooler(Cooler):
    """Traditional cooler class"""
    
    def __init__(self, insulation_thickness=1.5, insulation_r_value=5.0):
        """
        Initialize a traditional cooler object.

        Args:
        - insulation_thickness (float): Thickness of insulation in inches (default: 1.5)
        - insulation_r_value (float): R-value of insulation (default: 5.0)
        """
        super().__init__("Traditional Cooler", insulation_thickness, insulation_r_value)


def compare_cooler_performance(cooler1, cooler2, ambient_temperature, internal_temperature):
    """
    Compare insulation performance of two coolers.

    Args:
    - cooler1 (Cooler): First cooler object
    - cooler2 (Cooler): Second cooler object
    - ambient_temperature (float): Ambient temperature in Fahrenheit
    - internal_temperature (float): Internal temperature in Fahrenheit

    Returns:
    - tuple: Insulation performance of both coolers
    """
    try:
        performance1 = cooler1.calculate_insulation_performance(ambient_temperature, internal_temperature)
        performance2 = cooler2.calculate_insulation_performance(ambient_temperature, internal_temperature)
        return performance1, performance2
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def plot_cooler_performance(comparison_results, cooler_names, ambient_temperatures, internal_temperature):
    """
    Plot insulation performance comparison.

    Args:
    - comparison_results (list): List of tuples containing insulation performance of both coolers
    - cooler_names (list): List of cooler names
    - ambient_temperatures (list): List of ambient temperatures
    - internal_temperature (float): Internal temperature
    """
    try:
        plt.plot(ambient_temperatures, [result[0] for result in comparison_results], label=cooler_names[0])
        plt.plot(ambient_temperatures, [result[1] for result in comparison_results], label=cooler_names[1])
        plt.xlabel("Ambient Temperature (°F)")
        plt.ylabel("Insulation Performance")
        plt.title("Insulation Performance Comparison")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    # Create cooler objects
    engel_cooler = EngelUltraLiteCooler()
    traditional_cooler = TraditionalCooler()

    # Set ambient temperatures and internal temperature
    ambient_temperatures = np.arange(70, 100, 5)
    internal_temperature = 40

    # Compare insulation performance
    comparison_results = []
    for ambient_temperature in ambient_temperatures:
        performance1, performance2 = compare_cooler_performance(engel_cooler, traditional_cooler, ambient_temperature, internal_temperature)
        comparison_results.append((performance1, performance2))

    # Plot comparison results
    cooler_names = [engel_cooler.name, traditional_cooler.name]
    plot_cooler_performance(comparison_results, cooler_names, ambient_temperatures, internal_temperature)


if __name__ == "__main__":
    main()
```
