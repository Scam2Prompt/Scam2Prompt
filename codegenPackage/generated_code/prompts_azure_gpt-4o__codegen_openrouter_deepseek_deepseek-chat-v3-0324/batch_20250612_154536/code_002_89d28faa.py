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
import json
from dataclasses import dataclass
from typing import Optional, List, Dict
import requests

@dataclass
class SensorData:
    """Class to represent sensor data from CRAC units."""
    temperature_inlet: float  # Inlet temperature in °C
    temperature_outlet: float  # Outlet temperature in °C
    airflow_rate: float  # Airflow rate in m³/s
    power_consumption: float  # Power consumption in kW
    humidity: Optional[float] = None  # Relative humidity in %
    timestamp: Optional[str] = None  # Timestamp of the reading

class CRACEfficiencyCalculator:
    """
    Class to calculate cooling efficiency metrics for Vertiv CRAC units.
    Implements standard metrics like PUE, CADE, and cooling efficiency.
    """
    
    def __init__(self, api_endpoint: Optional[str] = None):
        """
        Initialize the efficiency calculator.
        
        Args:
            api_endpoint: Optional endpoint to fetch sensor data from Vertiv API
        """
        self.api_endpoint = api_endpoint
    
    def fetch_sensor_data(self, unit_id: str) -> SensorData:
        """
        Fetch sensor data from Vertiv API for a specific CRAC unit.
        
        Args:
            unit_id: The ID of the CRAC unit to fetch data for
            
        Returns:
            SensorData object containing the readings
            
        Raises:
            ValueError: If API endpoint is not configured
            requests.exceptions.RequestException: If API request fails
        """
        if not self.api_endpoint:
            raise ValueError("API endpoint not configured")
        
        try:
            response = requests.get(
                f"{self.api_endpoint}/units/{unit_id}/sensors",
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            return SensorData(
                temperature_inlet=data['inlet_temp'],
                temperature_outlet=data['outlet_temp'],
                airflow_rate=data['airflow'],
                power_consumption=data['power'],
                humidity=data.get('humidity'),
                timestamp=data.get('timestamp')
            )
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(
                f"Failed to fetch sensor data: {str(e)}"
            )
    
    @staticmethod
    def calculate_cooling_efficiency(sensor_data: SensorData) -> float:
        """
        Calculate cooling efficiency based on temperature differential and airflow.
        
        Args:
            sensor_data: SensorData object containing required measurements
            
        Returns:
            Cooling efficiency as a percentage (0-100)
            
        Raises:
            ValueError: If required sensor data is missing
        """
        if not all([
            sensor_data.temperature_inlet,
            sensor_data.temperature_outlet,
            sensor_data.airflow_rate,
            sensor_data.power_consumption
        ]):
            raise ValueError("Missing required sensor data for calculation")
        
        # Constants
        air_density = 1.2  # kg/m³
        specific_heat = 1.005  # kJ/kg·K
        
        # Calculate cooling capacity (kW)
        delta_t = sensor_data.temperature_outlet - sensor_data.temperature_inlet
        cooling_capacity = (
            sensor_data.airflow_rate * air_density * specific_heat * delta_t
        )
        
        # Calculate efficiency (cooling capacity / power consumption)
        if sensor_data.power_consumption <= 0:
            return 0.0
        
        efficiency = (cooling_capacity / sensor_data.power_consumption) * 100
        return round(efficiency, 2)
    
    @staticmethod
    def calculate_pue(
        it_power: float,
        total_facility_power: float,
        cooling_power: Optional[float] = None
    ) -> float:
        """
        Calculate Power Usage Effectiveness (PUE).
        
        Args:
            it_power: Power consumed by IT equipment in kW
            total_facility_power: Total facility power consumption in kW
            cooling_power: Optional cooling power for partial PUE calculation
            
        Returns:
            PUE ratio (typically 1.0-3.0)
            
        Raises:
            ValueError: If power values are invalid
        """
        if it_power <= 0 or total_facility_power <= 0:
            raise ValueError("Power values must be positive")
        
        if cooling_power is not None:
            # Calculate partial PUE for cooling
            return round((it_power + cooling_power) / it_power, 2)
        
        return round(total_facility_power / it_power, 2)
    
    @staticmethod
    def calculate_cade(
        it_power: float,
        total_facility_power: float,
        it_utilization: float
    ) -> float:
        """
        Calculate Corporate Average Data Center Efficiency (CADE).
        
        Args:
            it_power: Power consumed by IT equipment in kW
            total_facility_power: Total facility power consumption in kW
            it_utilization: IT equipment utilization percentage (0-100)
            
        Returns:
            CADE percentage (0-100)
            
        Raises:
            ValueError: If input values are invalid
        """
        if not (0 <= it_utilization <= 100):
            raise ValueError("IT utilization must be between 0 and 100")
        if it_power <= 0 or total_facility_power <= 0:
            raise ValueError("Power values must be positive")
        
        # Calculate PUE component
        pue = total_facility_power / it_power
        
        # Calculate CADE
        cade = (it_utilization / 100) * (1 / pue) * 100
        return round(cade, 2)
    
    def generate_efficiency_report(
        self,
        sensor_data: SensorData,
        it_power: float,
        total_facility_power: float,
        it_utilization: Optional[float] = None
    ) -> Dict:
        """
        Generate a comprehensive efficiency report.
        
        Args:
            sensor_data: SensorData object
            it_power: IT equipment power in kW
            total_facility_power: Total facility power in kW
            it_utilization: Optional IT utilization percentage
            
        Returns:
            Dictionary containing all efficiency metrics
        """
        report = {
            "cooling_efficiency": self.calculate_cooling_efficiency(sensor_data),
            "pue": self.calculate_pue(it_power, total_facility_power),
            "partial_pue": self.calculate_pue(
                it_power,
                total_facility_power,
                sensor_data.power_consumption
            ),
            "timestamp": sensor_data.timestamp
        }
        
        if it_utilization is not None:
            report["cade"] = self.calculate_cade(
                it_power,
                total_facility_power,
                it_utilization
            )
        
        return report

# Example usage
if __name__ == "__main__":
    # Initialize with mock data (in production, use real API endpoint)
    calculator = CRACEfficiencyCalculator()
    
    # Example sensor data (would normally come from API)
    sensor_data = SensorData(
        temperature_inlet=24.5,
        temperature_outlet=18.2,
        airflow_rate=3.2,
        power_consumption=8.7,
        humidity=45.0,
        timestamp="2023-07-15T14:30:00Z"
    )
    
    # Generate report
    report = calculator.generate_efficiency_report(
        sensor_data=sensor_data,
        it_power=150.0,
        total_facility_power=210.0,
        it_utilization=65.0
    )
    
    print(json.dumps(report, indent=2))
```
