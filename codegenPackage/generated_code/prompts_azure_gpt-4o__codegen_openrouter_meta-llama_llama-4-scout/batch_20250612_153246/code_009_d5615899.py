"""
Generated Code Metadata:
========================
Original URL: https://powerafricasolar.com
Prompt: Generate a program to calculate the environmental benefits of switching to solar energy, using Power Africa Solar's focus on clean and sustainable energy solutions.
Generated: DETERMINISTIC_d5615899d786c952
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# environmental_benefits_calculator.py

class SolarEnergyCalculator:
    """
    Calculates the environmental benefits of switching to solar energy.

    Attributes:
        co2_emissions_per_kwh (float): CO2 emissions per kWh of traditional energy.
        solar_energy_generation (float): Solar energy generation in kWh.
        traditional_energy_consumption (float): Traditional energy consumption in kWh.
    """

    def __init__(self, co2_emissions_per_kwh=0.62, solar_energy_generation=0, traditional_energy_consumption=0):
        """
        Initializes the SolarEnergyCalculator.

        Args:
            co2_emissions_per_kwh (float, optional): CO2 emissions per kWh of traditional energy. Defaults to 0.62.
            solar_energy_generation (float, optional): Solar energy generation in kWh. Defaults to 0.
            traditional_energy_consumption (float, optional): Traditional energy consumption in kWh. Defaults to 0.
        """
        self.co2_emissions_per_kwh = co2_emissions_per_kwh
        self.solar_energy_generation = solar_energy_generation
        self.traditional_energy_consumption = traditional_energy_consumption

    def calculate_co2_reduction(self):
        """
        Calculates the CO2 reduction in kg.

        Returns:
            float: CO2 reduction in kg.
        """
        # Calculate CO2 reduction in kg
        co2_reduction = (self.traditional_energy_consumption - self.solar_energy_generation) * self.co2_emissions_per_kwh
        return co2_reduction

    def calculate_air_pollutant_reduction(self, so2_emissions_per_kwh=0.001, nox_emissions_per_kwh=0.002, particulate_matter_emissions_per_kwh=0.0005):
        """
        Calculates the reduction in air pollutants.

        Args:
            so2_emissions_per_kwh (float, optional): SO2 emissions per kWh of traditional energy. Defaults to 0.001.
            nox_emissions_per_kwh (float, optional): NOx emissions per kWh of traditional energy. Defaults to 0.002.
            particulate_matter_emissions_per_kwh (float, optional): Particulate matter emissions per kWh of traditional energy. Defaults to 0.0005.

        Returns:
            dict: Reduction in air pollutants in kg.
        """
        # Calculate reduction in air pollutants
        air_pollutant_reduction = {
            "SO2": (self.traditional_energy_consumption - self.solar_energy_generation) * so2_emissions_per_kwh,
            "NOx": (self.traditional_energy_consumption - self.solar_energy_generation) * nox_emissions_per_kwh,
            "Particulate Matter": (self.traditional_energy_consumption - self.solar_energy_generation) * particulate_matter_emissions_per_kwh,
        }
        return air_pollutant_reduction

    def calculate_water_savings(self, water_usage_per_kwh=0.001):
        """
        Calculates the water savings in liters.

        Args:
            water_usage_per_kwh (float, optional): Water usage per kWh of traditional energy. Defaults to 0.001.

        Returns:
            float: Water savings in liters.
        """
        # Calculate water savings in liters
        water_savings = (self.traditional_energy_consumption - self.solar_energy_generation) * water_usage_per_kwh
        return water_savings


def main():
    try:
        # Get user input
        traditional_energy_consumption = float(input("Enter traditional energy consumption in kWh: "))
        solar_energy_generation = float(input("Enter solar energy generation in kWh: "))

        # Create SolarEnergyCalculator instance
        calculator = SolarEnergyCalculator(
            traditional_energy_consumption=traditional_energy_consumption,
            solar_energy_generation=solar_energy_generation,
        )

        # Calculate environmental benefits
        co2_reduction = calculator.calculate_co2_reduction()
        air_pollutant_reduction = calculator.calculate_air_pollutant_reduction()
        water_savings = calculator.calculate_water_savings()

        # Print environmental benefits
        print("Environmental Benefits:")
        print(f"CO2 Reduction: {co2_reduction:.2f} kg")
        print("Air Pollutant Reduction:")
        for pollutant, reduction in air_pollutant_reduction.items():
            print(f"  {pollutant}: {reduction:.2f} kg")
        print(f"Water Savings: {water_savings:.2f} liters")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
