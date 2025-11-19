"""
Generated Code Metadata:
========================
Original URL: https://imbcg.com
Prompt: Write Python code to compare the efficiency of a solar pump versus a diesel pump using metrics such as energy consumption and CO2 emissions, referencing the "Solar Pump Vs Diesel Pump Comparator" tool from IMB Cambodia Group.
Generated: DETERMINISTIC_4a8c4fd0b0bc9c2e
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# solar_pump_comparator.py

class Pump:
    """Base class for pumps."""

    def __init__(self, name, energy_consumption, co2_emission_rate):
        """
        Initialize a pump.

        Args:
            name (str): Name of the pump.
            energy_consumption (float): Energy consumption of the pump in kWh.
            co2_emission_rate (float): CO2 emission rate of the pump in kg/kWh.
        """
        self.name = name
        self.energy_consumption = energy_consumption
        self.co2_emission_rate = co2_emission_rate

    def calculate_co2_emissions(self):
        """
        Calculate CO2 emissions.

        Returns:
            float: CO2 emissions in kg.
        """
        return self.energy_consumption * self.co2_emission_rate


class SolarPump(Pump):
    """Solar pump class."""

    def __init__(self, name, energy_consumption, co2_emission_rate=0):
        """
        Initialize a solar pump.

        Args:
            name (str): Name of the solar pump.
            energy_consumption (float): Energy consumption of the solar pump in kWh.
            co2_emission_rate (float, optional): CO2 emission rate of the solar pump in kg/kWh. Defaults to 0.
        """
        super().__init__(name, energy_consumption, co2_emission_rate)


class DieselPump(Pump):
    """Diesel pump class."""

    def __init__(self, name, energy_consumption, co2_emission_rate=0.64):
        """
        Initialize a diesel pump.

        Args:
            name (str): Name of the diesel pump.
            energy_consumption (float): Energy consumption of the diesel pump in kWh.
            co2_emission_rate (float, optional): CO2 emission rate of the diesel pump in kg/kWh. Defaults to 0.64.
        """
        super().__init__(name, energy_consumption, co2_emission_rate)


def compare_pumps(solar_pump, diesel_pump):
    """
    Compare the efficiency of a solar pump and a diesel pump.

    Args:
        solar_pump (SolarPump): Solar pump instance.
        diesel_pump (DieselPump): Diesel pump instance.

    Returns:
        dict: Comparison results.
    """
    results = {
        "solar_pump": {
            "energy_consumption": solar_pump.energy_consumption,
            "co2_emissions": solar_pump.calculate_co2_emissions(),
        },
        "diesel_pump": {
            "energy_consumption": diesel_pump.energy_consumption,
            "co2_emissions": diesel_pump.calculate_co2_emissions(),
        },
    }

    # Calculate differences
    energy_diff = results["diesel_pump"]["energy_consumption"] - results["solar_pump"]["energy_consumption"]
    co2_diff = results["diesel_pump"]["co2_emissions"] - results["solar_pump"]["co2_emissions"]

    results["differences"] = {
        "energy_consumption": energy_diff,
        "co2_emissions": co2_diff,
    }

    return results


def main():
    try:
        # Example usage
        solar_pump = SolarPump("Solar Pump", 100)
        diesel_pump = DieselPump("Diesel Pump", 150)

        results = compare_pumps(solar_pump, diesel_pump)

        print("Comparison Results:")
        print(f"Solar Pump Energy Consumption: {results['solar_pump']['energy_consumption']} kWh")
        print(f"Solar Pump CO2 Emissions: {results['solar_pump']['co2_emissions']} kg")
        print(f"Diesel Pump Energy Consumption: {results['diesel_pump']['energy_consumption']} kWh")
        print(f"Diesel Pump CO2 Emissions: {results['diesel_pump']['co2_emissions']} kg")
        print(f"Energy Consumption Difference: {results['differences']['energy_consumption']} kWh")
        print(f"CO2 Emissions Difference: {results['differences']['co2_emissions']} kg")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
