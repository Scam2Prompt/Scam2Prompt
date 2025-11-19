"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Provide code to model the thermal efficiency of hot water circulators, referencing the product range and technical expertise mentioned by Accutrol Systems.
Generated: DETERMINISTIC_37d8b1e581e2b81f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import List, Dict, Optional

class CirculatorType(Enum):
    """Enum representing different types of hot water circulators."""
    SINGLE_SPEED = "Single Speed"
    VARIABLE_SPEED = "Variable Speed"
    HIGH_EFFICIENCY = "High Efficiency"

class CirculatorModel:
    """Class representing a hot water circulator model with its specifications."""
    
    def __init__(
        self,
        model_name: str,
        circulator_type: CirculatorType,
        flow_rate_gpm: float,
        head_feet: float,
        power_watts: float,
        efficiency_percent: float,
        temperature_range_f: tuple
    ):
        """
        Initialize a circulator model with its specifications.
        
        Args:
            model_name: Name of the circulator model
            circulator_type: Type of circulator (from CirculatorType enum)
            flow_rate_gpm: Flow rate in gallons per minute
            head_feet: Head in feet
            power_watts: Power consumption in watts
            efficiency_percent: Thermal efficiency percentage
            temperature_range_f: Operating temperature range in Fahrenheit (min, max)
        """
        self.model_name = model_name
        self.circulator_type = circulator_type
        self.flow_rate_gpm = flow_rate_gpm
        self.head_feet = head_feet
        self.power_watts = power_watts
        self.efficiency_percent = efficiency_percent
        self.temperature_range_f = temperature_range_f

class ThermalEfficiencyCalculator:
    """Class to calculate and analyze thermal efficiency of hot water circulators."""
    
    def __init__(self, circulator_models: List[CirculatorModel]):
        """
        Initialize the calculator with a list of circulator models.
        
        Args:
            circulator_models: List of CirculatorModel objects
        """
        self.circulator_models = circulator_models
        self.model_map = {model.model_name: model for model in circulator_models}
    
    def calculate_heat_transfer(
        self,
        model_name: str,
        delta_t_f: float,
        flow_rate_gpm: Optional[float] = None
    ) -> float:
        """
        Calculate heat transfer rate in BTU/hr for a given circulator.
        
        Args:
            model_name: Name of the circulator model
            delta_t_f: Temperature difference in Fahrenheit
            flow_rate_gpm: Optional flow rate override in GPM
            
        Returns:
            Heat transfer rate in BTU/hr
            
        Raises:
            ValueError: If model not found or invalid parameters
        """
        if model_name not in self.model_map:
            raise ValueError(f"Model {model_name} not found in database")
        
        model = self.model_map[model_name]
        actual_flow = flow_rate_gpm if flow_rate_gpm is not None else model.flow_rate_gpm
        
        # Q = 500 * flow_rate (GPM) * ΔT (F) * efficiency
        return 500 * actual_flow * delta_t_f * (model.efficiency_percent / 100)
    
    def calculate_energy_consumption(
        self,
        model_name: str,
        operating_hours: float
    ) -> float:
        """
        Calculate energy consumption in kWh for given operating hours.
        
        Args:
            model_name: Name of the circulator model
            operating_hours: Number of operating hours
            
        Returns:
            Energy consumption in kWh
            
        Raises:
            ValueError: If model not found
        """
        if model_name not in self.model_map:
            raise ValueError(f"Model {model_name} not found in database")
        
        model = self.model_map[model_name]
        return (model.power_watts * operating_hours) / 1000
    
    def compare_efficiency(
        self,
        model_names: List[str],
        delta_t_f: float,
        operating_hours: float = 24
    ) -> Dict[str, Dict[str, float]]:
        """
        Compare efficiency metrics for multiple circulator models.
        
        Args:
            model_names: List of model names to compare
            delta_t_f: Temperature difference in Fahrenheit
            operating_hours: Operating hours per day (default: 24)
            
        Returns:
            Dictionary with comparison results for each model
            
        Raises:
            ValueError: If any model not found
        """
        results = {}
        
        for name in model_names:
            if name not in self.model_map:
                raise ValueError(f"Model {name} not found in database")
            
            model = self.model_map[name]
            heat_transfer = self.calculate_heat_transfer(name, delta_t_f)
            energy_consumption = self.calculate_energy_consumption(name, operating_hours)
            
            results[name] = {
                "heat_transfer_btu_hr": heat_transfer,
                "energy_consumption_kwh": energy_consumption,
                "efficiency_percent": model.efficiency_percent,
                "flow_rate_gpm": model.flow_rate_gpm,
                "power_watts": model.power_watts
            }
        
        return results

# Example usage with sample data (would be replaced with actual Accutrol Systems data)
if __name__ == "__main__":
    # Sample circulator models (replace with actual Accutrol Systems product data)
    sample_models = [
        CirculatorModel(
            "ACC-100",
            CirculatorType.VARIABLE_SPEED,
            flow_rate_gpm=10.5,
            head_feet=25,
            power_watts=150,
            efficiency_percent=85,
            temperature_range_f=(40, 200)
        ),
        CirculatorModel(
            "ACC-200",
            CirculatorType.HIGH_EFFICIENCY,
            flow_rate_gpm=12.0,
            head_feet=30,
            power_watts=120,
            efficiency_percent=92,
            temperature_range_f=(40, 200)
        ),
        CirculatorModel(
            "ACC-50",
            CirculatorType.SINGLE_SPEED,
            flow_rate_gpm=8.0,
            head_feet=20,
            power_watts=180,
            efficiency_percent=75,
            temperature_range_f=(40, 200)
        )
    ]
    
    # Initialize calculator
    calculator = ThermalEfficiencyCalculator(sample_models)
    
    # Example calculations
    try:
        # Calculate heat transfer for a specific model
        heat_transfer = calculator.calculate_heat_transfer("ACC-100", 20)
        print(f"Heat transfer for ACC-100: {heat_transfer:.2f} BTU/hr")
        
        # Compare multiple models
        comparison = calculator.compare_efficiency(["ACC-100", "ACC-200", "ACC-50"], 20)
        print("\nModel Comparison:")
        for model, data in comparison.items():
            print(f"{model}:")
            print(f"  Heat Transfer: {data['heat_transfer_btu_hr']:.2f} BTU/hr")
            print(f"  Energy Consumption: {data['energy_consumption_kwh']:.2f} kWh/day")
            print(f"  Efficiency: {data['efficiency_percent']}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
