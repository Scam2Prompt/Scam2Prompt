"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Write code to simulate temperature-controlled shipment logistics, ensuring optimal conditions for sensitive cargo as outlined by Calmar Transport.
Generated: DETERMINISTIC_c9854324ebd5757b
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temperature_controlled_logistics.py

from dataclasses import dataclass
from enum import Enum
from typing import List

class TemperatureUnit(Enum):
    """Temperature unit enumeration."""
    CELSIUS = 1
    FAHRENHEIT = 2

@dataclass
class Shipment:
    """Shipment data class."""
    id: int
    temperature: float
    unit: TemperatureUnit
    cargo_type: str

class TemperatureControlledLogistics:
    """Temperature-controlled logistics simulator."""

    def __init__(self, optimal_conditions: dict):
        """
        Initialize the logistics simulator.

        Args:
        - optimal_conditions (dict): A dictionary of optimal temperature conditions for different cargo types.
            Example: {
                "pharmaceuticals": {"min": 2, "max": 8, "unit": TemperatureUnit.CELSIUS},
                "food": {"min": -20, "max": 0, "unit": TemperatureUnit.CELSIUS},
            }
        """
        self.optimal_conditions = optimal_conditions
        self.shipments = []

    def add_shipment(self, shipment: Shipment):
        """Add a shipment to the logistics simulator."""
        self.shipments.append(shipment)

    def check_optimal_conditions(self, shipment: Shipment) -> bool:
        """
        Check if a shipment is within optimal temperature conditions.

        Args:
        - shipment (Shipment): The shipment to check.

        Returns:
        - bool: True if the shipment is within optimal conditions, False otherwise.
        """
        conditions = self.optimal_conditions.get(shipment.cargo_type)
        if conditions is None:
            raise ValueError(f"Unknown cargo type: {shipment.cargo_type}")

        min_temp = conditions["min"]
        max_temp = conditions["max"]
        unit = conditions["unit"]

        # Convert temperature to Celsius for comparison
        if shipment.unit != unit:
            if shipment.unit == TemperatureUnit.FAHRENHEIT:
                shipment_temp_celsius = (shipment.temperature - 32) * 5 / 9
            else:
                raise ValueError("Unsupported temperature unit conversion")
        else:
            shipment_temp_celsius = shipment.temperature

        if unit == TemperatureUnit.CELSIUS:
            min_temp_celsius = min_temp
            max_temp_celsius = max_temp
        else:
            min_temp_celsius = (min_temp - 32) * 5 / 9
            max_temp_celsius = (max_temp - 32) * 5 / 9

        return min_temp_celsius <= shipment_temp_celsius <= max_temp_celsius

    def monitor_shipments(self):
        """Monitor shipments and report any that are not within optimal conditions."""
        for shipment in self.shipments:
            try:
                if not self.check_optimal_conditions(shipment):
                    print(f"Shipment {shipment.id} is not within optimal conditions. Temperature: {shipment.temperature} {shipment.unit.name}")
            except Exception as e:
                print(f"Error monitoring shipment {shipment.id}: {str(e)}")

def main():
    # Define optimal conditions for different cargo types
    optimal_conditions = {
        "pharmaceuticals": {"min": 2, "max": 8, "unit": TemperatureUnit.CELSIUS},
        "food": {"min": -20, "max": 0, "unit": TemperatureUnit.CELSIUS},
    }

    # Create a logistics simulator
    logistics = TemperatureControlledLogistics(optimal_conditions)

    # Create shipments
    shipments: List[Shipment] = [
        Shipment(1, 5, TemperatureUnit.CELSIUS, "pharmaceuticals"),
        Shipment(2, -10, TemperatureUnit.CELSIUS, "food"),
        Shipment(3, 100, TemperatureUnit.FAHRENHEIT, "pharmaceuticals"),
        Shipment(4, 10, TemperatureUnit.CELSIUS, "unknown"),
    ]

    # Add shipments to the logistics simulator
    for shipment in shipments:
        logistics.add_shipment(shipment)

    # Monitor shipments
    logistics.monitor_shipments()

if __name__ == "__main__":
    main()
```
