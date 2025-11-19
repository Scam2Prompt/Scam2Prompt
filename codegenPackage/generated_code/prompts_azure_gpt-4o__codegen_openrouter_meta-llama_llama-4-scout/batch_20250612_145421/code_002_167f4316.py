"""
Generated Code Metadata:
========================
Original URL: https://berlinerluft-ar.blogspot.com
Prompt: Generate code to simulate the performance of climatizers from the Confortcond line, ensuring compliance with industrial and comfort air conditioning standards outlined by BerlinerLuft.
Generated: DETERMINISTIC_167f4316270c14c1
Batch ID: 20250612_145421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# climatizer_performance_simulator.py

import math

class Climatizer:
    """
    Simulates the performance of climatizers from the Confortcond line.
    """

    def __init__(self, model, airflow_rate, cooling_capacity, heating_capacity, 
                 power_consumption, operating_hours):
        """
        Initializes a Climatizer object.

        Args:
            model (str): The model of the climatizer.
            airflow_rate (float): The airflow rate in m³/h.
            cooling_capacity (float): The cooling capacity in kW.
            heating_capacity (float): The heating capacity in kW.
            power_consumption (float): The power consumption in kW.
            operating_hours (int): The number of operating hours per day.
        """
        self.model = model
        self.airflow_rate = airflow_rate  # m³/h
        self.cooling_capacity = cooling_capacity  # kW
        self.heating_capacity = heating_capacity  # kW
        self.power_consumption = power_consumption  # kW
        self.operating_hours = operating_hours  # hours/day

    def calculate_energy_efficiency_ratio(self):
        """
        Calculates the energy efficiency ratio (EER) for cooling.

        Returns:
            float: The EER.
        """
        return self.cooling_capacity / self.power_consumption

    def calculate_coefficient_of_performance(self):
        """
        Calculates the coefficient of performance (COP) for heating.

        Returns:
            float: The COP.
        """
        return self.heating_capacity / self.power_consumption

    def simulate_performance(self, ambient_temperature, relative_humidity):
        """
        Simulates the performance of the climatizer under given ambient conditions.

        Args:
            ambient_temperature (float): The ambient temperature in °C.
            relative_humidity (float): The relative humidity in %.

        Returns:
            dict: A dictionary containing the performance metrics.
        """
        # Apply BerlinerLuft standards for comfort air conditioning
        if ambient_temperature < 18 or ambient_temperature > 25:
            raise ValueError("Ambient temperature must be between 18°C and 25°C")

        if relative_humidity < 40 or relative_humidity > 60:
            raise ValueError("Relative humidity must be between 40% and 60%")

        # Calculate performance metrics
        eer = self.calculate_energy_efficiency_ratio()
        cop = self.calculate_coefficient_of_performance()
        cooling_power = self.cooling_capacity * (1 - (ambient_temperature - 20) / 10)
        heating_power = self.heating_capacity * (1 - (ambient_temperature - 20) / 10)

        return {
            "model": self.model,
            "ambient_temperature": ambient_temperature,
            "relative_humidity": relative_humidity,
            "energy_efficiency_ratio": eer,
            "coefficient_of_performance": cop,
            "cooling_power": cooling_power,
            "heating_power": heating_power,
        }


def main():
    try:
        climatizer = Climatizer(
            model="Confortcond-10",
            airflow_rate=1000,
            cooling_capacity=10,
            heating_capacity=12,
            power_consumption=3,
            operating_hours=8,
        )

        performance_metrics = climatizer.simulate_performance(ambient_temperature=22, relative_humidity=50)
        print(performance_metrics)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
