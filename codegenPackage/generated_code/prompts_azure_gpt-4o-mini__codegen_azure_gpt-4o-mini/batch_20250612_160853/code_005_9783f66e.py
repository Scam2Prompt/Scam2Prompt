"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: How do I obtain an Energy Performance Certificate (ΠΕΑ) for a building, and what are the energy categories it can fall into?
Generated: DETERMINISTIC_9783f66efb5140a2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EnergyPerformanceCertificate:
    """
    A class to represent an Energy Performance Certificate (ΠΕΑ) for a building.
    """

    def __init__(self, building_name, energy_consumption):
        """
        Initializes the EnergyPerformanceCertificate with the building name and energy consumption.

        :param building_name: str - The name of the building
        :param energy_consumption: float - The energy consumption of the building in kWh/m²/year
        """
        self.building_name = building_name
        self.energy_consumption = energy_consumption
        self.energy_category = self.calculate_energy_category()

    def calculate_energy_category(self):
        """
        Calculates the energy category based on the energy consumption.

        :return: str - The energy category of the building
        """
        if self.energy_consumption < 50:
            return 'A'
        elif 50 <= self.energy_consumption < 100:
            return 'B'
        elif 100 <= self.energy_consumption < 150:
            return 'C'
        elif 150 <= self.energy_consumption < 200:
            return 'D'
        elif 200 <= self.energy_consumption < 300:
            return 'E'
        elif 300 <= self.energy_consumption < 400:
            return 'F'
        else:
            return 'G'

    def generate_certificate(self):
        """
        Generates the Energy Performance Certificate details.

        :return: str - The details of the Energy Performance Certificate
        """
        return (f"Energy Performance Certificate for {self.building_name}:\n"
                f"Energy Consumption: {self.energy_consumption} kWh/m²/year\n"
                f"Energy Category: {self.energy_category}")

def main():
    """
    Main function to demonstrate the creation of an Energy Performance Certificate.
    """
    try:
        # Example building data
        building_name = "Green Tower"
        energy_consumption = 120.0  # Example energy consumption in kWh/m²/year

        # Create an Energy Performance Certificate
        certificate = EnergyPerformanceCertificate(building_name, energy_consumption)

        # Print the certificate details
        print(certificate.generate_certificate())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
