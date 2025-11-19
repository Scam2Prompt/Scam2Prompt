"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write Python code to simulate the operation of a CHP (Combined Heat and Power) system, including energy generation and distribution, as described by پایش نیرو's services.
Generated: DETERMINISTIC_dc279688f22aeeaf
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import Tuple, Dict, Optional

class CHPSystem:
    """
    Simulates a Combined Heat and Power (CHP) system for energy generation and distribution.
    
    Attributes:
        max_electrical_output (float): Maximum electrical output in kW
        max_thermal_output (float): Maximum thermal output in kW
        electrical_efficiency (float): Electrical efficiency (0-1)
        thermal_efficiency (float): Thermal efficiency (0-1)
        fuel_energy_content (float): Energy content of fuel in kWh/m^3
        min_load (float): Minimum operational load as fraction (0-1)
    """
    
    def __init__(
        self,
        max_electrical_output: float = 1000,  # kW
        max_thermal_output: float = 1200,     # kW
        electrical_efficiency: float = 0.35,  # 35%
        thermal_efficiency: float = 0.45,     # 45%
        fuel_energy_content: float = 10.0,    # kWh/m^3
        min_load: float = 0.3                 # 30%
    ):
        """Initialize the CHP system with given parameters."""
        self.max_electrical_output = max_electrical_output
        self.max_thermal_output = max_thermal_output
        self.electrical_efficiency = electrical_efficiency
        self.thermal_efficiency = thermal_efficiency
        self.fuel_energy_content = fuel_energy_content
        self.min_load = min_load
        
        # Validate parameters
        self._validate_parameters()
        
    def _validate_parameters(self) -> None:
        """Validate system parameters."""
        if not (0 < self.electrical_efficiency < 1):
            raise ValueError("Electrical efficiency must be between 0 and 1")
        if not (0 < self.thermal_efficiency < 1):
            raise ValueError("Thermal efficiency must be between 0 and 1")
        if (self.electrical_efficiency + self.thermal_efficiency) > 1:
            raise ValueError("Sum of efficiencies cannot exceed 1")
        if not (0 < self.min_load <= 1):
            raise ValueError("Minimum load must be between 0 and 1")
        if self.fuel_energy_content <= 0:
            raise ValueError("Fuel energy content must be positive")
            
    def calculate_outputs(
        self,
        load_factor: float,
        fuel_flow_rate: Optional[float] = None
    ) -> Tuple[float, float, float]:
        """
        Calculate electrical and thermal outputs based on load factor or fuel input.
        
        Args:
            load_factor: Operational load factor (0-1)
            fuel_flow_rate: Optional fuel flow rate in m^3/h
            
        Returns:
            Tuple of (electrical_output, thermal_output, fuel_consumption)
            
        Raises:
            ValueError: If load factor is out of bounds
        """
        if not (0 <= load_factor <= 1):
            raise ValueError("Load factor must be between 0 and 1")
            
        if load_factor < self.min_load and load_factor > 0:
            raise ValueError(f"Load factor cannot be below minimum load of {self.min_load}")
            
        if fuel_flow_rate is not None:
            if fuel_flow_rate <= 0:
                raise ValueError("Fuel flow rate must be positive")
            return self._calculate_from_fuel(fuel_flow_rate)
        else:
            return self._calculate_from_load(load_factor)
            
    def _calculate_from_load(self, load_factor: float) -> Tuple[float, float, float]:
        """Calculate outputs based on load factor."""
        electrical_output = self.max_electrical_output * load_factor
        thermal_output = self.max_thermal_output * load_factor
        
        # Calculate required fuel input
        total_energy_output = electrical_output / self.electrical_efficiency
        fuel_consumption = total_energy_output / self.fuel_energy_content
        
        return electrical_output, thermal_output, fuel_consumption
        
    def _calculate_from_fuel(self, fuel_flow_rate: float) -> Tuple[float, float, float]:
        """Calculate outputs based on fuel input."""
        total_energy_input = fuel_flow_rate * self.fuel_energy_content
        electrical_output = total_energy_input * self.electrical_efficiency
        thermal_output = total_energy_input * self.thermal_efficiency
        
        # Calculate load factor
        load_factor = electrical_output / self.max_electrical_output
        
        if load_factor < self.min_load:
            raise ValueError(f"Resulting load factor {load_factor} is below minimum {self.min_load}")
            
        return electrical_output, thermal_output, fuel_flow_rate
        
    def optimize_operation(
        self,
        electrical_demand: float,
        thermal_demand: float,
        max_iterations: int = 100,
        tolerance: float = 1e-3
    ) -> Dict[str, float]:
        """
        Optimize CHP operation to meet demands while minimizing fuel consumption.
        
        Args:
            electrical_demand: Required electrical output in kW
            thermal_demand: Required thermal output in kW
            max_iterations: Maximum optimization iterations
            tolerance: Convergence tolerance
            
        Returns:
            Dictionary with operation parameters
        """
        if electrical_demand < 0 or thermal_demand < 0:
            raise ValueError("Demands cannot be negative")
            
        # Initialize variables
        best_load = 0.0
        best_fuel = float('inf')
        results = {
            'electrical_output': 0,
            'thermal_output': 0,
            'fuel_consumption': 0,
            'load_factor': 0,
            'meets_demand': False
        }
        
        # Binary search for optimal load factor
        low = self.min_load
        high = 1.0
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            try:
                elec, therm, fuel = self.calculate_outputs(mid)
                
                # Check if demands are met
                meets_elec = elec >= electrical_demand * (1 - tolerance)
                meets_therm = therm >= thermal_demand * (1 - tolerance)
                
                if meets_elec and meets_therm:
                    if fuel < best_fuel:
                        best_fuel = fuel
                        best_load = mid
                        results.update({
                            'electrical_output': elec,
                            'thermal_output': therm,
                            'fuel_consumption': fuel,
                            'load_factor': mid,
                            'meets_demand': True
                        })
                    high = mid
                else:
                    low = mid
            except ValueError:
                high = mid
                
            if (high - low) < tolerance:
                break
                
        return results
        
    def economic_analysis(
        self,
        electricity_price: float,
        heat_price: float,
        fuel_price: float,
        operational_hours: float = 8000
    ) -> Dict[str, float]:
        """
        Perform simple economic analysis of CHP operation.
        
        Args:
            electricity_price: Price per kWh of electricity
            heat_price: Price per kWh of heat
            fuel_price: Price per m^3 of fuel
            operational_hours: Annual operational hours
            
        Returns:
            Dictionary with economic metrics
        """
        if any(price < 0 for price in [electricity_price, heat_price, fuel_price]):
            raise ValueError("Prices cannot be negative")
            
        # Calculate at full load
        elec, therm, fuel = self.calculate_outputs(1.0)
        
        annual_revenue = (elec * electricity_price + therm * heat_price) * operational_hours
        annual_cost = fuel * fuel_price * operational_hours
        annual_profit = annual_revenue - annual_cost
        
        return {
            'annual_revenue': annual_revenue,
            'annual_cost': annual_cost,
            'annual_profit': annual_profit,
            'payback_period': None,  # Would require capital cost input
            'roi': None              # Would require capital cost input
        }


def simulate_chp_operation():
    """Demonstrate CHP system operation."""
    try:
        # Initialize CHP system
        chp = CHPSystem()
        
        # Example 1: Calculate outputs at 80% load
        elec, therm, fuel = chp.calculate_outputs(0.8)
        print(f"At 80% load: Electrical={elec:.2f} kW, Thermal={therm:.2f} kW, Fuel={fuel:.2f} m³/h")
        
        # Example 2: Optimize operation for given demands
        demands = chp.optimize_operation(700, 850)
        print("\nOptimized operation for demands (700 kW elec, 850 kW therm):")
        for k, v in demands.items():
            print(f"{k.replace('_', ' ').title()}: {v:.2f}" if isinstance(v, float) else f"{k.replace('_', ' ').title()}: {v}")
        
        # Example 3: Economic analysis
        economics = chp.economic_analysis(0.15, 0.08, 0.30)
        print("\
