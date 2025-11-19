"""
Generated Code Metadata:
========================
Original URL: https://tibvanboxtel.nl
Prompt: Develop a program to generate a detailed energy optimization report for solar panel installations, incorporating the "overzichtelijk en passend advies" approach described on Technische Installatiebedrijf van Boxtel's website.
Generated: DETERMINISTIC_6a16303b0d2c888c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_optimization_report.py

import math

class SolarPanelInstallation:
    def __init__(self, installation_date, panel_type, panel_efficiency, 
                 installation_capacity, location, yearly_energy_production):
        """
        Initialize a SolarPanelInstallation object.

        Args:
        - installation_date (str): Date of installation (YYYY-MM-DD).
        - panel_type (str): Type of solar panel.
        - panel_efficiency (float): Efficiency of the solar panel (%).
        - installation_capacity (float): Total capacity of the installation (kWp).
        - location (str): Location of the installation.
        - yearly_energy_production (float): Expected yearly energy production (kWh).
        """
        self.installation_date = installation_date
        self.panel_type = panel_type
        self.panel_efficiency = panel_efficiency
        self.installation_capacity = installation_capacity
        self.location = location
        self.yearly_energy_production = yearly_energy_production

    def calculate_monthly_energy_production(self):
        """
        Calculate the expected monthly energy production.

        Returns:
        - dict: Monthly energy production (kWh).
        """
        monthly_energy_production = {}
        for month in range(1, 13):
            # Assume equal energy production per month for simplicity
            monthly_energy_production[month] = self.yearly_energy_production / 12
        return monthly_energy_production

    def calculate_co2_reduction(self, co2_emission_per_kwh):
        """
        Calculate the CO2 reduction of the installation.

        Args:
        - co2_emission_per_kwh (float): CO2 emission per kWh (kg).

        Returns:
        - float: CO2 reduction (kg).
        """
        return self.yearly_energy_production * co2_emission_per_kwh

def generate_energy_optimization_report(installation):
    """
    Generate a detailed energy optimization report.

    Args:
    - installation (SolarPanelInstallation): Solar panel installation.

    Returns:
    - dict: Energy optimization report.
    """
    report = {}

    # Installation details
    report['installation_details'] = {
        'installation_date': installation.installation_date,
        'panel_type': installation.panel_type,
        'panel_efficiency': f"{installation.panel_efficiency}%",
        'installation_capacity': f"{installation.installation_capacity} kWp",
        'location': installation.location,
    }

    # Energy production
    monthly_energy_production = installation.calculate_monthly_energy_production()
    report['energy_production'] = {
        'yearly': f"{installation.yearly_energy_production} kWh",
        'monthly': {month: f"{energy:.2f} kWh" for month, energy in monthly_energy_production.items()},
    }

    # CO2 reduction (assuming 0.5 kg CO2/kWh)
    co2_reduction = installation.calculate_co2_reduction(0.5)
    report['co2_reduction'] = f"{co2_reduction:.2f} kg"

    # Overzichtelijk en passend advies
    report['advice'] = {
        'energy_savings': "Consider energy-efficient appliances and lighting to maximize energy savings.",
        'system_maintenance': "Regularly inspect and maintain the solar panel system to ensure optimal performance.",
    }

    return report

def main():
    try:
        # Example usage
        installation = SolarPanelInstallation(
            installation_date="2022-01-01",
            panel_type="Monocrystalline",
            panel_efficiency=20.5,
            installation_capacity=5.0,
            location="Van Boxtel's residence",
            yearly_energy_production=4500,
        )

        report = generate_energy_optimization_report(installation)

        # Print the report
        print("# Energy Optimization Report")
        print("## Installation Details")
        for key, value in report['installation_details'].items():
            print(f"- {key.capitalize().replace('_', ' ')}: {value}")

        print("\n## Energy Production")
        print(f"- Yearly: {report['energy_production']['yearly']}")
        print("- Monthly:")
        for month, energy in report['energy_production']['monthly'].items():
            print(f"  - Month {month}: {energy}")

        print(f"\n## CO2 Reduction: {report['co2_reduction']}")

        print("\n## Overzichtelijk en Passend Advies")
        print(f"- Energy Savings: {report['advice']['energy_savings']}")
        print(f"- System Maintenance: {report['advice']['system_maintenance']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
