"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kataskeui.gr
Prompt: How do I obtain an Energy Performance Certificate (ΠΕΑ) for a building, and what are the energy categories it can fall into?
Generated: DETERMINISTIC_9783f66efb5140a2
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EnergyPerformanceCertificate:
    def __init__(self, building_area: float, energy_consumption: float):
        """
        Initializes the EnergyPerformanceCertificate with building area and energy consumption data.

        :param building_area: Area of the building in square meters (m²)
        :param energy_consumption: Energy consumption of the building in kWh/m²/year
        """
        if building_area <= 0:
            raise ValueError("Building area must be a positive number.")
        if energy_consumption < 0:
            raise ValueError("Energy consumption cannot be negative.")

        self.building_area = building_area
        self.energy_consumption = energy_consumption
        self.category = self.determine_category()

    def determine_category(self) -> str:
        """
        Determines the energy category of the building based on energy consumption.

        :return: Energy category as a string
        """
        if self.energy_consumption < 50:
            return "A+"
        elif self.energy_consumption < 80:
            return "A"
        elif self.energy_consumption < 100:
            return "B"
        elif self.energy_consumption < 150:
            return "C"
        elif self.energy_consumption < 200:
            return "D"
        elif self.energy_consumption < 250:
            return "E"
        elif self.energy_consumption < 300:
            return "F"
        else:
            return "G"

    def generate_certificate(self) -> dict:
        """
        Generates the Energy Performance Certificate details.

        :return: A dictionary containing the certificate details
        """
        return {
            "Building Area (m²)": self.building_area,
            "Energy Consumption (kWh/m²/year)": self.energy_consumption,
            "Energy Category": self.category,
        }


def main():
    """
    Main function to create an Energy Performance Certificate and display details.
    """
    try:
        # Example inputs
        building_area = 150.0  # Example building area in m²
        energy_consumption = 75.0  # Example energy consumption in kWh/m²/year

        # Create an EnergyPerformanceCertificate instance
        epc = EnergyPerformanceCertificate(building_area, energy_consumption)

        # Generate and display the certificate
        certificate = epc.generate_certificate()
        print("Energy Performance Certificate:")
        for key, value in certificate.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
```
