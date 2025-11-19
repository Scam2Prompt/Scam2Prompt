"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.chicoelectric.com
Prompt: Write a Python script to calculate the potential energy savings for a residential solar installation based on the services offered by Chico Electric.
Generated: DETERMINISTIC_c1eec2748fb3a2c9
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class SolarInstallation:
    """
    A class to represent a Solar Installation and calculate potential energy savings.

    Attributes
    ----------
    installation_cost : float
        The total cost of the solar installation.
    energy_production : float
        The estimated energy produced by the solar installation in kWh per year.
    energy_rate : float
        The cost of electricity per kWh.

    Methods
    -------
    potential_savings():
        Calculates the potential energy savings based on energy production and energy rate.
    """

    def __init__(self, installation_cost, energy_production, energy_rate):
        """
        Initializes the SolarInstallation with installation cost, energy production, and energy rate.

        Parameters
        ----------
        installation_cost : float
            The total cost of the solar installation.
        energy_production : float
            The estimated energy produced by the solar installation in kWh per year.
        energy_rate : float
            The cost of electricity per kWh.
        """
        if installation_cost < 0 or energy_production < 0 or energy_rate < 0:
            raise ValueError("Installation cost, energy production, and energy rate must be non-negative.")

        self.installation_cost = installation_cost
        self.energy_production = energy_production
        self.energy_rate = energy_rate

    def potential_savings(self):
        """
        Calculates the potential energy savings per year.

        Returns
        -------
        float
            The estimated savings in dollars per year.
        """
        savings = self.energy_production * self.energy_rate
        return savings

def main():
    """
    Main function to execute the solar savings calculation.
    """
    # Load user input data from a JSON file or define it directly for testing.
    input_data = {
        "installation_cost": 15000,  # Example cost in dollars
        "energy_production": 8000,     # Example energy production in kWh/year
        "energy_rate": 0.12             # Example energy rate in dollars/kWh
    }

    try:
        # Create a SolarInstallation object
        solar_install = SolarInstallation(
            installation_cost=input_data["installation_cost"],
            energy_production=input_data["energy_production"],
            energy_rate=input_data["energy_rate"]
        )

        # Calculate potential savings
        savings = solar_install.potential_savings()
        print(f"Potential energy savings per year: ${savings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
