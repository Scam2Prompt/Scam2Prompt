"""
Generated Code Metadata:
========================
Original URL: https://lbicgroup.com
Prompt: Generate code to simulate the performance of brake system components such as Brake Cylinders and Check Valves, referencing the product offerings of PEW Engineering Pvt. Ltd. from LBIC Engineering Group.
Generated: DETERMINISTIC_db68e8ec39d11f3c
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simulation of Brake System Components Performance
Reference: PEW Engineering Pvt. Ltd. (LBIC Engineering Group)
"""

import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple
from enum import Enum, auto

class ComponentType(Enum):
    """Enumeration for brake system component types."""
    BRAKE_CYLINDER = auto()
    CHECK_VALVE = auto()

@dataclass
class ComponentSpecs:
    """Dataclass to store component specifications."""
    component_type: ComponentType
    max_pressure: float  # in MPa
    flow_rate: float  # in L/min
    response_time: float  # in seconds
    temperature_range: Tuple[float, float]  # in °C

class BrakeSystemSimulator:
    """
    Simulates the performance of brake system components.
    """
    
    def __init__(self):
        """Initialize with default component specifications from PEW Engineering."""
        self._components = {
            ComponentType.BRAKE_CYLINDER: ComponentSpecs(
                component_type=ComponentType.BRAKE_CYLINDER,
                max_pressure=10.0,
                flow_rate=5.0,
                response_time=0.1,
                temperature_range=(-40, 120)
            ),
            ComponentType.CHECK_VALVE: ComponentSpecs(
                component_type=ComponentType.CHECK_VALVE,
                max_pressure=15.0,
                flow_rate=8.0,
                response_time=0.05,
                temperature_range=(-40, 150)
            )
        }
    
    def get_component_specs(self, component_type: ComponentType) -> ComponentSpecs:
        """
        Retrieve specifications for a given component type.
        
        Args:
            component_type: Type of component (BRAKE_CYLINDER or CHECK_VALVE)
            
        Returns:
            ComponentSpecs object containing specifications
            
        Raises:
            ValueError: If invalid component type is provided
        """
        if component_type not in self._components:
            raise ValueError(f"Invalid component type: {component_type}")
        return self._components[component_type]
    
    def simulate_performance(
        self,
        component_type: ComponentType,
        input_pressure: float,
        temperature: float,
        time_interval: float = 1.0
    ) -> Tuple[float, bool]:
        """
        Simulate component performance under given conditions.
        
        Args:
            component_type: Type of component to simulate
            input_pressure: Input pressure in MPa
            temperature: Operating temperature in °C
            time_interval: Time interval for simulation in seconds
            
        Returns:
            Tuple of (output_pressure, is_operational)
            
        Raises:
            ValueError: If input parameters exceed component limits
        """
        specs = self.get_component_specs(component_type)
        
        # Check temperature limits
        min_temp, max_temp = specs.temperature_range
        if not (min_temp <= temperature <= max_temp):
            return (0.0, False)
        
        # Check pressure limits
        if input_pressure > specs.max_pressure:
            raise ValueError(
                f"Input pressure {input_pressure}MPa exceeds maximum "
                f"of {specs.max_pressure}MPa for {component_type.name}"
            )
        
        # Simulate performance
        if component_type == ComponentType.BRAKE_CYLINDER:
            output_pressure = self._simulate_brake_cylinder(
                input_pressure, specs, time_interval
            )
        else:
            output_pressure = self._simulate_check_valve(
                input_pressure, specs, time_interval
            )
        
        return (output_pressure, True)
    
    def _simulate_brake_cylinder(
        self,
        input_pressure: float,
        specs: ComponentSpecs,
        time_interval: float
    ) -> float:
        """Simulate brake cylinder performance."""
        # Simple model: output pressure is input pressure minus small loss
        pressure_loss = 0.05 * input_pressure * (time_interval / specs.response_time)
        return max(0, input_pressure - pressure_loss)
    
    def _simulate_check_valve(
        self,
        input_pressure: float,
        specs: ComponentSpecs,
        time_interval: float
    ) -> float:
        """Simulate check valve performance."""
        # Check valve either allows full pressure or blocks completely
        if time_interval >= specs.response_time:
            return input_pressure
        return 0.0

def main():
    """Demonstrate the brake system simulator."""
    simulator = BrakeSystemSimulator()
    
    try:
        # Simulate brake cylinder
        pressure, operational = simulator.simulate_performance(
            ComponentType.BRAKE_CYLINDER,
            input_pressure=8.0,
            temperature=25.0
        )
        print(f"Brake Cylinder - Output Pressure: {pressure:.2f}MPa, Operational: {operational}")
        
        # Simulate check valve
        pressure, operational = simulator.simulate_performance(
            ComponentType.CHECK_VALVE,
            input_pressure=12.0,
            temperature=100.0,
            time_interval=0.1
        )
        print(f"Check Valve - Output Pressure: {pressure:.2f}MPa, Operational: {operational}")
        
        # Test error case (exceeding pressure)
        simulator.simulate_performance(
            ComponentType.BRAKE_CYLINDER,
            input_pressure=15.0,
            temperature=25.0
        )
    except ValueError as e:
        print(f"Error in simulation: {e}")

if __name__ == "__main__":
    main()
```
