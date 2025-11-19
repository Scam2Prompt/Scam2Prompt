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
from enum import Enum
from typing import Dict

class EnergyCategory(Enum):
    """Energy categories for a building's Energy Performance Certificate (ΠΕΑ)"""
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"

class EnergyPerformanceCertificate:
    """Represents an Energy Performance Certificate (ΠΕΑ) for a building"""

    def __init__(self, building_name: str, energy_consumption: float, energy_category: EnergyCategory):
        """
        Initializes an EnergyPerformanceCertificate object.

        Args:
        - building_name (str): The name of the building.
        - energy_consumption (float): The energy consumption of the building in kWh/m²/year.
        - energy_category (EnergyCategory): The energy category of the building.

        Raises:
        - ValueError: If energy_consumption is not a positive number.
        """
        if energy_consumption <= 0:
            raise ValueError("Energy consumption must be a positive number")

        self.building_name = building_name
        self.energy_consumption = energy_consumption
        self.energy_category = energy_category

    def __str__(self):
        return f"Energy Performance Certificate for {self.building_name}: {self.energy_category.value} ({self.energy_consumption} kWh/m²/year)"

def get_energy_category(energy_consumption: float) -> EnergyCategory:
    """
    Determines the energy category of a building based on its energy consumption.

    Args:
    - energy_consumption (float): The energy consumption of the building in kWh/m²/year.

    Returns:
    - EnergyCategory: The energy category of the building.

    Raises:
    - ValueError: If energy_consumption is not a positive number.
    """
    if energy_consumption <= 0:
        raise ValueError("Energy consumption must be a positive number")

    # Assuming the following energy consumption ranges for each category (in kWh/m²/year)
    # These ranges may vary depending on the country's regulations
    if energy_consumption <= 20:
        return EnergyCategory.A_PLUS
    elif energy_consumption <= 40:
        return EnergyCategory.A
    elif energy_consumption <= 60:
        return EnergyCategory.B
    elif energy_consumption <= 80:
        return EnergyCategory.C
    elif energy_consumption <= 120:
        return EnergyCategory.D
    elif energy_consumption <= 160:
        return EnergyCategory.E
    elif energy_consumption <= 200:
        return EnergyCategory.F
    else:
        return EnergyCategory.G

def obtain_energia_performance_certificate(building_name: str, energy_consumption: float) -> EnergyPerformanceCertificate:
    """
    Obtains an Energy Performance Certificate (ΠΕΑ) for a building.

    Args:
    - building_name (str): The name of the building.
    - energy_consumption (float): The energy consumption of the building in kWh/m²/year.

    Returns:
    - EnergyPerformanceCertificate: The Energy Performance Certificate object.

    Raises:
    - ValueError: If energy_consumption is not a positive number.
    """
    energy_category = get_energy_category(energy_consumption)
    return EnergyPerformanceCertificate(building_name, energy_consumption, energy_category)

def main():
    try:
        building_name = "Example Building"
        energy_consumption = 50.0  # in kWh/m²/year
        certificate = obtain_energia_performance_certificate(building_name, energy_consumption)
        print(certificate)
        print("Energy categories:")
        for category in EnergyCategory:
            print(category.value)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
