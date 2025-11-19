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
class BioethanolFireplace:
    """
    A class to represent a bioethanol fireplace using Planika BEV Technology™.
    """

    def __init__(self, fuel_capacity: float, burn_rate: float, efficiency: float):
        """
        Initializes the BioethanolFireplace with the given parameters.

        :param fuel_capacity: The maximum fuel capacity in liters.
        :param burn_rate: The rate of fuel consumption in liters per hour.
        :param efficiency: The energy efficiency of the fireplace as a decimal (0 to 1).
        """
        if fuel_capacity <= 0:
            raise ValueError("Fuel capacity must be greater than zero.")
        if burn_rate <= 0:
            raise ValueError("Burn rate must be greater than zero.")
        if not (0 <= efficiency <= 1):
            raise ValueError("Efficiency must be between 0 and 1.")

        self.fuel_capacity = fuel_capacity
        self.burn_rate = burn_rate
        self.efficiency = efficiency

    def calculate_heat_output(self) -> float:
        """
        Calculates the heat output of the fireplace.

        :return: The heat output in kilowatts (kW).
        """
        # Energy content of bioethanol in MJ/L (megajoules per liter)
        energy_content_per_liter = 26.8  # MJ/L
        # Convert MJ to kWh (1 MJ = 0.277778 kWh)
        energy_content_per_liter_kWh = energy_content_per_liter * 0.277778

        # Calculate the heat output based on burn rate and energy content
        heat_output = self.burn_rate * energy_content_per_liter_kWh
        return heat_output

    def calculate_energy_efficiency(self) -> float:
        """
        Calculates the energy efficiency of the fireplace.

        :return: The energy efficiency as a percentage.
        """
        return self.efficiency * 100

    def simulate_burn_time(self) -> float:
        """
        Simulates the burn time based on the fuel capacity and burn rate.

        :return: The burn time in hours.
        """
        burn_time = self.fuel_capacity / self.burn_rate
        return burn_time

    def display_info(self):
        """
        Displays the fireplace information including heat output, energy efficiency, and burn time.
        """
        try:
            heat_output = self.calculate_heat_output()
            efficiency = self.calculate_energy_efficiency()
            burn_time = self.simulate_burn_time()

            print(f"Heat Output: {heat_output:.2f} kW")
            print(f"Energy Efficiency: {efficiency:.2f}%")
            print(f"Estimated Burn Time: {burn_time:.2f} hours")
        except Exception as e:
            print(f"An error occurred while calculating fireplace information: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a BioethanolFireplace instance with example parameters
        fireplace = BioethanolFireplace(fuel_capacity=5.0, burn_rate=0.5, efficiency=0.85)
        fireplace.display_info()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
