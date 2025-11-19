"""
Generated Code Metadata:
========================
Original URL: https://www.sardiniameetsazores.eu
Prompt: Develop a program to model the drying and grinding process of "مراوح متحركة" using the technical details outlined on the Sardinia Meets Azores webpage.
Generated: DETERMINISTIC_b85d14b05af655e9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Model for drying and grinding process of 'مراوح متحركة' (moving fans) based on technical details.
This program simulates the drying and grinding stages with configurable parameters.
"""

import numpy as np
from typing import Tuple, Dict, Optional

class DryingGrindingModel:
    """
    A class to model the drying and grinding process of moving fans.
    
    Attributes:
        drying_time (float): Time duration for drying process (hours)
        grinding_time (float): Time duration for grinding process (hours)
        temperature (float): Operating temperature (°C)
        humidity (float): Relative humidity (%)
        fan_speed (float): Fan speed (RPM)
        material_moisture (float): Initial moisture content (%)
    """
    
    def __init__(
        self,
        drying_time: float = 2.5,
        grinding_time: float = 1.0,
        temperature: float = 80.0,
        humidity: float = 15.0,
        fan_speed: float = 1500.0,
        material_moisture: float = 30.0
    ):
        """
        Initialize the drying and grinding model with default or provided parameters.
        
        Args:
            drying_time: Time for drying process in hours (default: 2.5)
            grinding_time: Time for grinding process in hours (default: 1.0)
            temperature: Operating temperature in °C (default: 80.0)
            humidity: Relative humidity in % (default: 15.0)
            fan_speed: Fan speed in RPM (default: 1500.0)
            material_moisture: Initial moisture content in % (default: 30.0)
        """
        self.drying_time = drying_time
        self.grinding_time = grinding_time
        self.temperature = temperature
        self.humidity = humidity
        self.fan_speed = fan_speed
        self.material_moisture = material_moisture
        
        # Validate parameters
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate model parameters to ensure they are within acceptable ranges."""
        if self.drying_time <= 0:
            raise ValueError("Drying time must be positive")
        if self.grinding_time <= 0:
            raise ValueError("Grinding time must be positive")
        if not (50 <= self.temperature <= 120):
            raise ValueError("Temperature must be between 50°C and 120°C")
        if not (0 <= self.humidity <= 100):
            raise ValueError("Humidity must be between 0% and 100%")
        if self.fan_speed <= 0:
            raise ValueError("Fan speed must be positive")
        if not (0 <= self.material_moisture <= 100):
            raise ValueError("Material moisture must be between 0% and 100%")
    
    def drying_process(self) -> Tuple[float, Dict[str, float]]:
        """
        Simulate the drying process.
        
        Returns:
            Tuple containing:
                - final_moisture: Final moisture content after drying (%)
                - process_stats: Dictionary of process statistics
        """
        try:
            # Calculate drying rate based on parameters
            drying_rate = (0.5 * self.fan_speed / 1000) * (self.temperature / 80) * (1 - self.humidity / 100)
            
            # Calculate moisture reduction
            moisture_reduction = drying_rate * self.drying_time
            
            # Ensure moisture doesn't go below 0
            final_moisture = max(0, self.material_moisture - moisture_reduction)
            
            # Calculate energy consumption (kWh)
            energy = 1.2 * self.drying_time * (self.fan_speed / 1000) * (self.temperature / 80)
            
            process_stats = {
                'drying_rate': drying_rate,
                'moisture_reduction': moisture_reduction,
                'final_moisture': final_moisture,
                'energy_consumption': energy,
                'efficiency': min(100, moisture_reduction / self.material_moisture * 100)
            }
            
            return final_moisture, process_stats
            
        except Exception as e:
            raise RuntimeError(f"Error in drying process simulation: {str(e)}")
    
    def grinding_process(self, input_moisture: float) -> Tuple[float, Dict[str, float]]:
        """
        Simulate the grinding process.
        
        Args:
            input_moisture: Moisture content of material entering grinding (%)
            
        Returns:
            Tuple containing:
                - final_fineness: Final particle size after grinding (microns)
                - process_stats: Dictionary of process statistics
        """
        try:
            if not (0 <= input_moisture <= 100):
                raise ValueError("Input moisture must be between 0% and 100%")
            
            # Calculate grinding efficiency based on moisture
            moisture_factor = 1 - (input_moisture / 100) * 0.5
            
            # Calculate final particle size (microns)
            base_fineness = 100.0  # microns
            final_fineness = base_fineness * (1 / (self.grinding_time * moisture_factor * (self.fan_speed / 1000)))
            
            # Ensure particle size doesn't go below 1 micron
            final_fineness = max(1.0, final_fineness)
            
            # Calculate energy consumption (kWh)
            energy = 0.8 * self.grinding_time * (self.fan_speed / 1000) * (100 / (input_moisture + 1))
            
            process_stats = {
                'final_fineness': final_fineness,
                'grinding_efficiency': moisture_factor * 100,
                'energy_consumption': energy,
                'throughput': 1000 / (self.grinding_time * (input_moisture / 10 + 1))
            }
            
            return final_fineness, process_stats
            
        except Exception as e:
            raise RuntimeError(f"Error in grinding process simulation: {str(e)}")
    
    def full_process(self) -> Dict[str, any]:
        """
        Run the complete drying and grinding process simulation.
        
        Returns:
            Dictionary containing complete process results and statistics
        """
        try:
            # Run drying process
            final_moisture, drying_stats = self.drying_process()
            
            # Run grinding process with dried material
            final_fineness, grinding_stats = self.grinding_process(final_moisture)
            
            # Calculate total energy consumption
            total_energy = drying_stats['energy_consumption'] + grinding_stats['energy_consumption']
            
            return {
                'drying': drying_stats,
                'grinding': grinding_stats,
                'final_moisture': final_moisture,
                'final_fineness': final_fineness,
                'total_energy': total_energy,
                'overall_efficiency': (drying_stats['efficiency'] + grinding_stats['grinding_efficiency']) / 2
            }
            
        except Exception as e:
            raise RuntimeError(f"Error in full process simulation: {str(e)}")


def run_simulation(params: Optional[Dict[str, float]] = None) -> Dict[str, any]:
    """
    Run a simulation with optional custom parameters.
    
    Args:
        params: Dictionary of optional parameters to override defaults
        
    Returns:
        Dictionary containing simulation results
    """
    try:
        # Create model instance with default or provided parameters
        if params:
            model = DryingGrindingModel(**params)
        else:
            model = DryingGrindingModel()
        
        # Run full process
        results = model.full_process()
        
        return results
        
    except Exception as e:
        raise RuntimeError(f"Simulation failed: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        # Run with default parameters
        default_results = run_simulation()
        print("Default simulation results:")
        print(default_results)
        
        # Run with custom parameters
        custom_params = {
            'drying_time': 3.0,
            'grinding_time': 1.5,
            'temperature': 90.0,
            'fan_speed': 1800.0,
            'material_moisture': 35.0
        }
        custom_results = run_simulation(custom_params)
        print("\nCustom simulation results:")
        print(custom_results)
        
    except Exception as e:
        print(f"Error during simulation: {str(e)}")
```
