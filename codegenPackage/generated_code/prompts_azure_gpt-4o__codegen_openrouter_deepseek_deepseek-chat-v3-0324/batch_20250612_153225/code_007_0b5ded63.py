"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Develop a program to calculate the heat output and energy efficiency of bioethanol fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_0b5ded63d116ecda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Program to calculate the heat output and energy efficiency of bioethanol fireplaces
using Planika BEV Technology™.

This module provides functions to calculate:
- Heat output (in kW)
- Energy efficiency (as a percentage)
- Fuel consumption rate (in liters per hour)

Assumptions:
- Bioethanol has an energy content of ~6.5 kWh per liter
- Planika BEV Technology™ has an efficiency range of 85-95%
"""

class BioethanolFireplace:
    """
    A class representing a bioethanol fireplace with Planika BEV Technology™.

    Attributes:
        model (str): The model name of the fireplace
        max_fuel_consumption (float): Maximum fuel consumption in liters/hour
        efficiency (float): Energy efficiency percentage (0-100)
    """

    def __init__(self, model: str, max_fuel_consumption: float, efficiency: float = 90.0):
        """
        Initialize the bioethanol fireplace.

        Args:
            model: Model name of the fireplace
            max_fuel_consumption: Maximum fuel consumption in liters/hour
            efficiency: Energy efficiency percentage (85-95% typical for Planika BEV)
        
        Raises:
            ValueError: If efficiency is not between 85 and 95 or fuel consumption is negative
        """
        if not 85 <= efficiency <= 95:
            raise ValueError("Efficiency must be between 85% and 95% for Planika BEV Technology™")
        if max_fuel_consumption < 0:
            raise ValueError("Fuel consumption cannot be negative")
        
        self.model = model
        self.max_fuel_consumption = max_fuel_consumption
        self.efficiency = efficiency

    def calculate_heat_output(self, fuel_consumption_rate: float) -> float:
        """
        Calculate the heat output in kW based on current fuel consumption rate.

        Args:
            fuel_consumption_rate: Current fuel consumption in liters/hour

        Returns:
            Heat output in kilowatts (kW)

        Raises:
            ValueError: If fuel consumption exceeds max capacity or is negative
        """
        if fuel_consumption_rate < 0:
            raise ValueError("Fuel consumption rate cannot be negative")
        if fuel_consumption_rate > self.max_fuel_consumption:
            raise ValueError(f"Fuel consumption exceeds max capacity of {self.max_fuel_consumption} l/h")
        
        # Energy content of bioethanol: 6.5 kWh per liter
        energy_content = 6.5  # kWh/l
        return fuel_consumption_rate * energy_content * (self.efficiency / 100)

    def calculate_energy_efficiency(self, actual_output: float, fuel_consumption_rate: float) -> float:
        """
        Calculate the actual energy efficiency based on measured output.

        Args:
            actual_output: Measured heat output in kW
            fuel_consumption_rate: Current fuel consumption in liters/hour

        Returns:
            Calculated efficiency percentage

        Raises:
            ValueError: If inputs are invalid (negative or zero fuel consumption)
        """
        if fuel_consumption_rate <= 0:
            raise ValueError("Fuel consumption must be positive")
        
        theoretical_output = fuel_consumption_rate * 6.5  # kWh
        return (actual_output / theoretical_output) * 100

    def calculate_fuel_consumption(self, desired_output: float) -> float:
        """
        Calculate required fuel consumption to achieve desired heat output.

        Args:
            desired_output: Desired heat output in kW

        Returns:
            Required fuel consumption in liters/hour

        Raises:
            ValueError: If desired output exceeds maximum possible output
        """
        max_output = self.calculate_heat_output(self.max_fuel_consumption)
        if desired_output > max_output:
            raise ValueError(f"Desired output exceeds maximum possible output of {max_output:.2f} kW")
        
        return desired_output / (6.5 * (self.efficiency / 100))


def main():
    """Example usage of the BioethanolFireplace class."""
    try:
        # Create a fireplace instance
        fireplace = BioethanolFireplace(
            model="Planika BEV-2000",
            max_fuel_consumption=0.5,  # liters/hour
            efficiency=92.0  # percentage
        )

        # Calculate heat output at 0.3 l/h fuel consumption
        heat_output = fireplace.calculate_heat_output(0.3)
        print(f"Heat output at 0.3 l/h: {heat_output:.2f} kW")

        # Calculate required fuel for 1.5 kW output
        fuel_needed = fireplace.calculate_fuel_consumption(1.5)
        print(f"Fuel needed for 1.5 kW output: {fuel_needed:.2f} l/h")

        # Calculate actual efficiency
        actual_efficiency = fireplace.calculate_energy_efficiency(1.4, 0.25)
        print(f"Actual efficiency: {actual_efficiency:.1f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
