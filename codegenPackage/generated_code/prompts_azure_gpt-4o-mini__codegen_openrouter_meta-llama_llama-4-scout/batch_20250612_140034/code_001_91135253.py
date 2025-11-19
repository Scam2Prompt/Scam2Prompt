"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: How can I implement a geotechnical monitoring program using the methodologies outlined by the Geotechnical Center?
Generated: DETERMINISTIC_9113525373e775bc
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# geotechnical_monitoring_program.py

"""
Implements a geotechnical monitoring program using methodologies outlined by the Geotechnical Center.

Classes:
    GeotechnicalParameter
    MonitoringStation
    GeotechnicalMonitoringProgram

Functions:
    calculate_displacement
    calculate_strain
"""

import math
from dataclasses import dataclass
from typing import List

@dataclass
class GeotechnicalParameter:
    """Represents a geotechnical parameter."""
    name: str
    value: float
    unit: str

@dataclass
class MonitoringStation:
    """Represents a monitoring station."""
    id: int
    location: str
    parameters: List[GeotechnicalParameter]

class GeotechnicalMonitoringProgram:
    """Implements a geotechnical monitoring program."""
    def __init__(self, stations: List[MonitoringStation]):
        self.stations = stations

    def calculate_displacement(self, station_id: int, parameter_name: str) -> float:
        """
        Calculates displacement for a given monitoring station and parameter.

        Args:
        station_id (int): ID of the monitoring station.
        parameter_name (str): Name of the geotechnical parameter.

        Returns:
        float: Displacement value.

        Raises:
        ValueError: If station ID or parameter name is not found.
        """
        station = next((s for s in self.stations if s.id == station_id), None)
        if station is None:
            raise ValueError("Station ID not found")

        parameter = next((p for p in station.parameters if p.name == parameter_name), None)
        if parameter is None:
            raise ValueError("Parameter name not found")

        # Assuming displacement calculation formula: Δ = (Vf - Vi) / Vi
        initial_value = 0.0  # Initial value, replace with actual value
        displacement = (parameter.value - initial_value) / initial_value
        return displacement

    def calculate_strain(self, station_id: int, parameter_name: str) -> float:
        """
        Calculates strain for a given monitoring station and parameter.

        Args:
        station_id (int): ID of the monitoring station.
        parameter_name (str): Name of the geotechnical parameter.

        Returns:
        float: Strain value.

        Raises:
        ValueError: If station ID or parameter name is not found.
        """
        station = next((s for s in self.stations if s.id == station_id), None)
        if station is None:
            raise ValueError("Station ID not found")

        parameter = next((p for p in station.parameters if p.name == parameter_name), None)
        if parameter is None:
            raise ValueError("Parameter name not found")

        # Assuming strain calculation formula: ε = ΔL / L0
        original_length = 1.0  # Original length, replace with actual value
        strain = (parameter.value / original_length)
        return strain

def main():
    # Example usage
    parameters1 = [
        GeotechnicalParameter("Settlement", 10.0, "mm"),
        GeotechnicalParameter("Lateral Movement", 5.0, "mm")
    ]
    station1 = MonitoringStation(1, "Location 1", parameters1)

    parameters2 = [
        GeotechnicalParameter("Settlement", 20.0, "mm"),
        GeotechnicalParameter("Lateral Movement", 10.0, "mm")
    ]
    station2 = MonitoringStation(2, "Location 2", parameters2)

    program = GeotechnicalMonitoringProgram([station1, station2])

    try:
        displacement = program.calculate_displacement(1, "Settlement")
        print(f"Displacement at Station 1: {displacement} mm")

        strain = program.calculate_strain(2, "Lateral Movement")
        print(f"Strain at Station 2: {strain}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
