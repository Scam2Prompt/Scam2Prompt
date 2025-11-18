"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Develop a program to calculate the heat output and energy efficiency of bioethanol fireplaces using Planika BEV Technology™.
Generated: DETERMINISTIC_0b5ded63d116ecda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BioethanolFireplace:
    """
    A class to represent a bioethanol fireplace using Planika BEV Technology™.
    """

    def __init__(self, fuel_capacity, energy_per_unit, burn_time):
        """
        Initializes a BioethanolFireplace instance.

        :param fuel_capacity: The capacity of the fuel tank in liters.
        :param energy_per_unit: The energy output per liter of bioethanol in MJ.
        :param burn_time: The burn time in hours for the full tank of fuel.
        """
        self.fuel_capacity = fuel_capacity  # in liters
        self.energy_per_unit = energy_per_unit  # in MJ per liter
        self.burn_time = burn_time  # in hours

    def calculate_heat_output(self):
        """
        Calculates the total heat output of the fireplace.

        :return: Total heat output in MJ.
        """
        try:
            heat_output = self.fuel_capacity * self.energy_per_unit
            return heat_output
        except Exception as e:
            print(f"Error calculating heat output: {e}")
            return 0

    def calculate_energy_efficiency(self):
        """
        Calculates the energy efficiency of the fireplace.

        :return: Energy efficiency in MJ/h.
        """
        try:
            heat_output = self.calculate_heat_output()
            efficiency = heat_output / self.burn_time if self.burn_time > 0 else 0
            return efficiency
        except Exception as e:
            print(f"Error calculating energy efficiency: {e}")
            return 0

def main():
    """
    Main function to demonstrate the usage of the BioethanolFireplace class.
    """
    # Example parameters for the fireplace
    fuel_capacity = 1.5  # in liters
    energy_per_unit = 26.8  # in MJ per liter (average for bioethanol)
    burn_time = 3  # in hours

    # Create an instance of BioethanolFireplace
    fireplace = BioethanolFireplace(fuel_capacity, energy_per_unit, burn_time)

    # Calculate and display heat output
    heat_output = fireplace.calculate_heat_output()
    print(f"Total Heat Output: {heat_output:.2f} MJ")

    # Calculate and display energy efficiency
    energy_efficiency = fireplace.calculate_energy_efficiency()
    print(f"Energy Efficiency: {energy_efficiency:.2f} MJ/h")

if __name__ == "__main__":
    main()
```
