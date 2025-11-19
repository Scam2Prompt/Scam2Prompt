"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Develop a library that helps data center managers assess the efficiency of their cooling and electrical strategies, inspired by the assessment services provided by Technical Power Service, Inc.
Generated: DETERMINISTIC_7cf144cffc6b40fc
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Data Center Efficiency Assessment Library

This library provides tools to assess the efficiency of cooling and electrical
strategies in data centers. It includes calculations for PUE, cooling efficiency,
and power usage metrics.

Inspired by Technical Power Service, Inc. assessment services.
"""

import json
from dataclasses import dataclass
from typing import Optional, Dict, List
import math

class DataCenterEfficiencyError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidInputError(DataCenterEfficiencyError):
    """Exception raised for invalid input values."""
    pass

@dataclass
class CoolingEfficiencyMetrics:
    """Dataclass to store cooling efficiency metrics."""
    cooling_load_factor: float
    cooling_capacity_factor: float
    return_temperature_index: float
    supply_temperature_index: float

@dataclass
class ElectricalEfficiencyMetrics:
    """Dataclass to store electrical efficiency metrics."""
    pue: float
    dc_power_usage: float  # in kW
    it_power_usage: float  # in kW
    non_it_power_usage: float  # in kW
    power_efficiency: float

class DataCenterEfficiencyAssessor:
    """
    Main class for assessing data center efficiency.
    
    Provides methods to calculate various efficiency metrics for both
    cooling and electrical systems in a data center.
    """
    
    def __init__(self, name: str = "Unnamed Data Center"):
        """
        Initialize the assessor with a data center name.
        
        Args:
            name: Name of the data center (default: "Unnamed Data Center")
        """
        self.name = name
        self._validate_name()
    
    def _validate_name(self) -> None:
        """Validate the data center name."""
        if not isinstance(self.name, str) or len(self.name.strip()) == 0:
            raise InvalidInputError("Data center name must be a non-empty string")
    
    def calculate_pue(self, total_power: float, it_power: float) -> float:
        """
        Calculate Power Usage Effectiveness (PUE).
        
        Args:
            total_power: Total facility power in kW
            it_power: IT equipment power in kW
            
        Returns:
            PUE ratio (float)
            
        Raises:
            InvalidInputError: If power values are invalid
        """
        if total_power <= 0 or it_power <= 0:
            raise InvalidInputError("Power values must be positive numbers")
        if it_power > total_power:
            raise InvalidInputError("IT power cannot exceed total power")
        
        return total_power / it_power
    
    def calculate_cooling_efficiency(
        self,
        cooling_load: float,
        cooling_capacity: float,
        return_temp: float,
        supply_temp: float
    ) -> CoolingEfficiencyMetrics:
        """
        Calculate cooling efficiency metrics.
        
        Args:
            cooling_load: Current cooling load in kW
            cooling_capacity: Total cooling capacity in kW
            return_temp: Return air temperature in °C
            supply_temp: Supply air temperature in °C
            
        Returns:
            CoolingEfficiencyMetrics object
            
        Raises:
            InvalidInputError: If input values are invalid
        """
        if cooling_load < 0 or cooling_capacity <= 0:
            raise InvalidInputError("Cooling values must be positive numbers")
        if cooling_load > cooling_capacity:
            raise InvalidInputError("Cooling load cannot exceed capacity")
        if return_temp <= supply_temp:
            raise InvalidInputError("Return temperature must be higher than supply temperature")
        
        cooling_load_factor = cooling_load / cooling_capacity
        cooling_capacity_factor = cooling_capacity / cooling_load if cooling_load > 0 else 0
        return_temperature_index = return_temp / supply_temp
        supply_temperature_index = supply_temp / return_temp
        
        return CoolingEfficiencyMetrics(
            cooling_load_factor=cooling_load_factor,
            cooling_capacity_factor=cooling_capacity_factor,
            return_temperature_index=return_temperature_index,
            supply_temperature_index=supply_temperature_index
        )
    
    def assess_electrical_efficiency(
        self,
        total_power: float,
        it_power: float
    ) -> ElectricalEfficiencyMetrics:
        """
        Calculate comprehensive electrical efficiency metrics.
        
        Args:
            total_power: Total facility power in kW
            it_power: IT equipment power in kW
            
        Returns:
            ElectricalEfficiencyMetrics object
            
        Raises:
            InvalidInputError: If power values are invalid
        """
        pue = self.calculate_pue(total_power, it_power)
        non_it_power = total_power - it_power
        power_efficiency = (it_power / total_power) * 100 if total_power > 0 else 0
        
        return ElectricalEfficiencyMetrics(
            pue=pue,
            dc_power_usage=total_power,
            it_power_usage=it_power,
            non_it_power_usage=non_it_power,
            power_efficiency=power_efficiency
        )
    
    def generate_efficiency_report(
        self,
        cooling_metrics: CoolingEfficiencyMetrics,
        electrical_metrics: ElectricalEfficiencyMetrics
    ) -> Dict:
        """
        Generate a comprehensive efficiency report.
        
        Args:
            cooling_metrics: CoolingEfficiencyMetrics object
            electrical_metrics: ElectricalEfficiencyMetrics object
            
        Returns:
            Dictionary containing the full efficiency report
        """
        return {
            "data_center_name": self.name,
            "electrical_efficiency": {
                "pue": electrical_metrics.pue,
                "total_power_kw": electrical_metrics.dc_power_usage,
                "it_power_kw": electrical_metrics.it_power_usage,
                "non_it_power_kw": electrical_metrics.non_it_power_usage,
                "power_efficiency_percentage": electrical_metrics.power_efficiency,
                "pue_rating": self._get_pue_rating(electrical_metrics.pue)
            },
            "cooling_efficiency": {
                "cooling_load_factor": cooling_metrics.cooling_load_factor,
                "cooling_capacity_factor": cooling_metrics.cooling_capacity_factor,
                "return_temperature_index": cooling_metrics.return_temperature_index,
                "supply_temperature_index": cooling_metrics.supply_temperature_index,
                "cooling_efficiency_rating": self._get_cooling_rating(
                    cooling_metrics.cooling_load_factor
                )
            }
        }
    
    def _get_pue_rating(self, pue: float) -> str:
        """Get a qualitative rating for PUE value."""
        if pue < 1.2:
            return "Excellent"
        elif pue < 1.5:
            return "Good"
        elif pue < 2.0:
            return "Fair"
        else:
            return "Poor"
    
    def _get_cooling_rating(self, cooling_load_factor: float) -> str:
        """Get a qualitative rating for cooling load factor."""
        if cooling_load_factor > 0.9:
            return "Overcapacity"
        elif cooling_load_factor > 0.7:
            return "Efficient"
        elif cooling_load_factor > 0.5:
            return "Adequate"
        else:
            return "Underutilized"
    
    def save_report_to_file(self, report: Dict, filename: str) -> None:
        """
        Save efficiency report to a JSON file.
        
        Args:
            report: Efficiency report dictionary
            filename: Output filename
            
        Raises:
            DataCenterEfficiencyError: If file operation fails
        """
        try:
            with open(filename, 'w') as f:
                json.dump(report, f, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            raise DataCenterEfficiencyError(f"Failed to save report: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize assessor
        assessor = DataCenterEfficiencyAssessor("Example Data Center")
        
        # Calculate electrical metrics
        electrical_metrics = assessor.assess_electrical_efficiency(
            total_power=500,  # kW
            it_power=300      # kW
        )
        
        # Calculate cooling metrics
        cooling_metrics = assessor.calculate_cooling_efficiency(
            cooling_load=200,    # kW
            cooling_capacity=300,  # kW
            return_temp=24,      # °C
            supply_temp=18       # °C
        )
        
        # Generate and save report
        report = assessor.generate_efficiency_report(cooling_metrics, electrical_metrics)
        assessor.save_report_to_file(report, "data_center_efficiency_report.json")
        
        print("Efficiency assessment completed successfully.")
        
    except DataCenterEfficiencyError as e:
        print(f"Error in efficiency assessment: {str(e)}")
```
