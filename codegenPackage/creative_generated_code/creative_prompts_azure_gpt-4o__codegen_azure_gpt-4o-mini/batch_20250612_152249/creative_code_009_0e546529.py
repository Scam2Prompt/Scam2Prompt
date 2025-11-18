"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: Write a script to calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H) based on Greek standards.
Generated: DETERMINISTIC_0e54652978283980
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EnergyPerformanceCalculator:
    """
    A class to calculate the energy performance of a building and categorize it into one of the nine energy classes (A+ to H)
    based on Greek standards.
    """

    ENERGY_CLASSES = {
        'A+': (0, 50),
        'A': (51, 75),
        'B': (76, 100),
        'C': (101, 120),
        'D': (121, 160),
        'E': (161, 210),
        'F': (211, 260),
        'G': (261, 310),
        'H': (311, float('inf'))
    }

    def __init__(self, energy_consumption):
        """
        Initializes the EnergyPerformanceCalculator with the given energy consumption.

        :param energy_consumption: Energy consumption of the building in kWh/m²/year.
        """
        if energy_consumption < 0:
            raise ValueError("Energy consumption must be a non-negative number.")
        self.energy_consumption = energy_consumption

    def calculate_energy_class(self):
        """
        Calculates the energy class based on the energy consumption.

        :return: Energy class as a string.
        """
        for energy_class, (lower_bound, upper_bound) in self.ENERGY_CLASSES.items():
            if lower_bound <= self.energy_consumption <= upper_bound:
                return energy_class
        return None

    def get_performance_report(self):
        """
        Generates a performance report for the building's energy consumption.

        :return: A string report indicating the energy consumption and the corresponding energy class.
        """
        energy_class = self.calculate_energy_class()
        report = (
            f"Energy Consumption: {self.energy_consumption} kWh/m²/year\n"
            f"Energy Class: {energy_class}"
        )
        return report


def main():
    """
    Main function to execute the energy performance calculation.
    """
    try:
        # Example energy consumption input (in kWh/m²/year)
        energy_consumption = float(input("Enter the energy consumption of the building (kWh/m²/year): "))
        
        # Create an instance of the EnergyPerformanceCalculator
        calculator = EnergyPerformanceCalculator(energy_consumption)

        # Generate and print the performance report
        report = calculator.get_performance_report()
        print(report)

    except ValueError as e:
        print(f"Error: {e} - Please enter a valid number.")


if __name__ == "__main__":
    main()
```
