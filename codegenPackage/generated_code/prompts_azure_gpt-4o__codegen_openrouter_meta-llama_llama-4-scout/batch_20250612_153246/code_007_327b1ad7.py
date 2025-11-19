"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Write code to simulate bulk chiller transport logistics, including handling large shipments and maintaining temperature control, inspired by the solutions on RefrigeratorTransport.com.
Generated: DETERMINISTIC_327b1ad732aa9f28
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TemperatureUnit(Enum):
    """Temperature unit enumeration"""
    CELSIUS = 1
    FAHRENHEIT = 2

@dataclass
class Shipment:
    """Shipment data class"""
    id: int
    temperature: float
    temperature_unit: TemperatureUnit
    weight: float  # in kilograms
    volume: float  # in cubic meters

class RefrigeratedTruck:
    """Refrigerated truck class"""
    def __init__(self, capacity_weight: float, capacity_volume: float, min_temperature: float, max_temperature: float, temperature_unit: TemperatureUnit):
        """
        Initialize refrigerated truck

        Args:
        - capacity_weight (float): Maximum weight capacity in kilograms
        - capacity_volume (float): Maximum volume capacity in cubic meters
        - min_temperature (float): Minimum temperature in specified unit
        - max_temperature (float): Maximum temperature in specified unit
        - temperature_unit (TemperatureUnit): Temperature unit
        """
        self.capacity_weight = capacity_weight
        self.capacity_volume = capacity_volume
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
        self.temperature_unit = temperature_unit
        self.current_weight = 0.0
        self.current_volume = 0.0
        self.current_temperature = min_temperature
        self.shipments = []

    def add_shipment(self, shipment: Shipment):
        """
        Add shipment to truck

        Args:
        - shipment (Shipment): Shipment to add

        Raises:
        - ValueError: If shipment exceeds capacity or temperature range
        """
        if self.current_weight + shipment.weight > self.capacity_weight:
            raise ValueError("Shipment exceeds weight capacity")
        if self.current_volume + shipment.volume > self.capacity_volume:
            raise ValueError("Shipment exceeds volume capacity")
        if shipment.temperature < self.min_temperature or shipment.temperature > self.max_temperature:
            raise ValueError("Shipment temperature out of range")

        self.current_weight += shipment.weight
        self.current_volume += shipment.volume
        self.shipments.append(shipment)

        # Update current temperature to average of all shipments
        total_temperature = sum(s.temperature for s in self.shipments)
        self.current_temperature = total_temperature / len(self.shipments)

    def remove_shipment(self, shipment_id: int):
        """
        Remove shipment from truck

        Args:
        - shipment_id (int): ID of shipment to remove

        Raises:
        - ValueError: If shipment not found
        """
        shipment_to_remove = next((s for s in self.shipments if s.id == shipment_id), None)
        if shipment_to_remove is None:
            raise ValueError("Shipment not found")

        self.current_weight -= shipment_to_remove.weight
        self.current_volume -= shipment_to_remove.volume
        self.shipments.remove(shipment_to_remove)

        # Update current temperature to average of remaining shipments
        if self.shipments:
            total_temperature = sum(s.temperature for s in self.shipments)
            self.current_temperature = total_temperature / len(self.shipments)
        else:
            self.current_temperature = self.min_temperature

    def __str__(self):
        return f"Refrigerated Truck - Current Weight: {self.current_weight} kg, Current Volume: {self.current_volume} m^3, Current Temperature: {self.current_temperature} {'°C' if self.temperature_unit == TemperatureUnit.CELSIUS else '°F'}"

def main():
    try:
        # Create refrigerated truck with capacity and temperature range
        truck = RefrigeratedTruck(
            capacity_weight=10000.0,
            capacity_volume=50.0,
            min_temperature=-20.0,
            max_temperature=10.0,
            temperature_unit=TemperatureUnit.CELSIUS
        )

        # Create shipments
        shipments: List[Shipment] = [
            Shipment(1, -10.0, TemperatureUnit.CELSIUS, 2000.0, 10.0),
            Shipment(2, 0.0, TemperatureUnit.CELSIUS, 3000.0, 15.0),
            Shipment(3, 5.0, TemperatureUnit.CELSIUS, 4000.0, 20.0),
        ]

        # Add shipments to truck
        for shipment in shipments:
            truck.add_shipment(shipment)
            logging.info(f"Added shipment {shipment.id} to truck")

        # Log truck status
        logging.info(truck)

        # Remove shipment from truck
        truck.remove_shipment(2)
        logging.info(f"Removed shipment 2 from truck")

        # Log truck status after removal
        logging.info(truck)

    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
