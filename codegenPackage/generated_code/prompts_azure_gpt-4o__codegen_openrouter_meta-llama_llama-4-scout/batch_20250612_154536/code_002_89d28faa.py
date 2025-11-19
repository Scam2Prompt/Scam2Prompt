"""
Generated Code Metadata:
========================
Original URL: https://vertiv.dns.cz
Prompt: Generate code to calculate cooling efficiency for a data center using Vertiv's CRAC (Computer Room Air Conditioning) solutions, incorporating sensor data.
Generated: DETERMINISTIC_89d28faa7ce9f900
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cooling_efficiency_calculator.py

import logging
from dataclasses import dataclass
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class SensorData:
    """Represents sensor data from CRAC units."""
    temperature: float  # in Celsius
    humidity: float  # in percentage
    airflow: float  # in cubic meters per second

@dataclass
class CRACUnit:
    """Represents a CRAC unit with its specifications."""
    model: str
    cooling_capacity: float  # in kilowatts
    airflow_rate: float  # in cubic meters per second

class CoolingEfficiencyCalculator:
    """Calculates cooling efficiency for a data center using Vertiv's CRAC solutions."""

    def __init__(self, crac_units: List[CRACUnit], sensor_data: List[SensorData]):
        """
        Initializes the calculator with CRAC units and sensor data.

        Args:
        - crac_units (List[CRACUnit]): List of CRAC units in the data center.
        - sensor_data (List[SensorData]): List of sensor data from CRAC units.
        """
        self.crac_units = crac_units
        self.sensor_data = sensor_data

    def calculate_cooling_efficiency(self) -> float:
        """
        Calculates the overall cooling efficiency of the data center.

        Returns:
        - float: Cooling efficiency in percentage.
        """
        try:
            total_cooling_capacity = sum(unit.cooling_capacity for unit in self.crac_units)
            total_airflow_rate = sum(unit.airflow_rate for unit in self.crac_units)

            if total_airflow_rate == 0:
                logging.warning("Total airflow rate is zero. Cooling efficiency cannot be calculated.")
                return 0.0

            total_airflow_utilization = sum(self._calculate_airflow_utilization(unit, data) for unit, data in zip(self.crac_units, self.sensor_data))

            if total_cooling_capacity == 0:
                logging.warning("Total cooling capacity is zero. Cooling efficiency cannot be calculated.")
                return 0.0

            cooling_efficiency = (total_airflow_utilization / total_airflow_rate) * (total_cooling_capacity / total_cooling_capacity)
            return cooling_efficiency * 100  # Convert to percentage

        except Exception as e:
            logging.error(f"Error calculating cooling efficiency: {str(e)}")
            return 0.0

    def _calculate_airflow_utilization(self, crac_unit: CRACUnit, sensor_data: SensorData) -> float:
        """
        Calculates airflow utilization for a single CRAC unit.

        Args:
        - crac_unit (CRACUnit): CRAC unit specifications.
        - sensor_data (SensorData): Sensor data from the CRAC unit.

        Returns:
        - float: Airflow utilization in cubic meters per second.
        """
        if crac_unit.airflow_rate == 0:
            logging.warning("CRAC unit airflow rate is zero. Airflow utilization cannot be calculated.")
            return 0.0

        # Assume airflow utilization is directly proportional to temperature and humidity
        airflow_utilization = crac_unit.airflow_rate * (sensor_data.temperature / 25) * (sensor_data.humidity / 50)
        return airflow_utilization

def main():
    # Example usage
    crac_units = [
        CRACUnit("Vertiv CRAC Unit 1", 10.0, 1000.0),
        CRACUnit("Vertiv CRAC Unit 2", 15.0, 1200.0),
    ]

    sensor_data = [
        SensorData(20.0, 40.0, 800.0),
        SensorData(22.0, 45.0, 900.0),
    ]

    calculator = CoolingEfficiencyCalculator(crac_units, sensor_data)
    cooling_efficiency = calculator.calculate_cooling_efficiency()
    logging.info(f"Cooling efficiency: {cooling_efficiency}%")

if __name__ == "__main__":
    main()
```
