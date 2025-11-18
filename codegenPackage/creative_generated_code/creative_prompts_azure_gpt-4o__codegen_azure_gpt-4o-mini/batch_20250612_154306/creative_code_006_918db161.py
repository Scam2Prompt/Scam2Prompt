"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gendis.energia.misiones.gob.ar
Prompt: Create a program to estimate the cost savings of a solar photovoltaic installation based on energy tariffs in Misiones, Argentina.
Generated: DETERMINISTIC_918db16105d2eea8
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SolarSavingsEstimator:
    """
    A class to estimate cost savings from a solar photovoltaic installation.

    Attributes:
        energy_tariff (float): The cost per kilowatt-hour (kWh) in Argentine Pesos.
        solar_panel_output (float): The expected energy output of the solar panels in kWh.
    """

    def __init__(self, energy_tariff: float, solar_panel_output: float):
        """
        Initializes the SolarSavingsEstimator with the provided energy tariff and solar panel output.

        Args:
            energy_tariff (float): The energy tariff in Argentine Pesos.
            solar_panel_output (float): The expected output of solar panels per month in kWh.
        """
        if energy_tariff < 0 or solar_panel_output < 0:
            raise ValueError("Energy tariff and solar panel output must be non-negative.")

        self.energy_tariff = energy_tariff
        self.solar_panel_output = solar_panel_output

    def calculate_monthly_savings(self) -> float:
        """
        Calculates the monthly savings from the solar photovoltaic installation.

        Returns:
            float: The estimated savings in Argentine Pesos.
        """
        savings = self.solar_panel_output * self.energy_tariff
        return savings

    def calculate_annual_savings(self) -> float:
        """
        Calculates the annual savings from the solar photovoltaic installation.

        Returns:
            float: The estimated annual savings in Argentine Pesos.
        """
        monthly_savings = self.calculate_monthly_savings()
        annual_savings = monthly_savings * 12
        return annual_savings


def main():
    """
    Main function to run the solar savings estimator.
    """
    try:
        # User inputs for energy tariff and solar panel output
        energy_tariff = float(input("Enter the energy tariff (in ARS/kWh): "))
        solar_panel_output = float(input("Enter the expected solar panel output (in kWh/month): "))

        # Creating an instance of SolarSavingsEstimator
        estimator = SolarSavingsEstimator(energy_tariff, solar_panel_output)

        # Calculating savings
        monthly_savings = estimator.calculate_monthly_savings()
        annual_savings = estimator.calculate_annual_savings()

        # Displaying results
        print(f"Estimated Monthly Savings: ARS {monthly_savings:.2f}")
        print(f"Estimated Annual Savings: ARS {annual_savings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
