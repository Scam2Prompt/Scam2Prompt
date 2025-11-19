"""
Generated Code Metadata:
========================
Original URL: https://econopure.com.vn
Prompt: "Design a water filtration system for a large industrial application using NF technology, considering the benefits of low pressure and high efficiency."
Generated: DETERMINISTIC_f55f6058dc92ae03
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Optional

class Membrane:
    """Represents a nanofiltration membrane with specific characteristics."""
    def __init__(self, name: str, rejection_rate: float, flux_rate: float, max_pressure: float):
        """
        Initialize a membrane with its properties.
        
        Args:
            name: Name/identifier of the membrane
            rejection_rate: Salt rejection rate (0-1)
            flux_rate: Water flux rate (L/m²h)
            max_pressure: Maximum operating pressure (bar)
        """
        self.name = name
        self.rejection_rate = rejection_rate
        self.flux_rate = flux_rate
        self.max_pressure = max_pressure

class NFSystem:
    """Nanofiltration water treatment system for industrial applications."""
    def __init__(self, membrane: Membrane, system_area: float, feed_concentration: float):
        """
        Initialize the NF system.
        
        Args:
            membrane: Membrane to be used in the system
            system_area: Total membrane area (m²)
            feed_concentration: Feed water concentration (mg/L)
        """
        self.membrane = membrane
        self.system_area = system_area
        self.feed_concentration = feed_concentration
        self.operating_pressure = 0.0
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate system parameters."""
        if not 0 < self.membrane.rejection_rate <= 1:
            raise ValueError("Rejection rate must be between 0 and 1")
        if self.system_area <= 0:
            raise ValueError("System area must be positive")
        if self.feed_concentration < 0:
            raise ValueError("Feed concentration cannot be negative")
    
    def set_operating_pressure(self, pressure: float) -> None:
        """
        Set the operating pressure of the system.
        
        Args:
            pressure: Desired operating pressure (bar)
        
        Raises:
            ValueError: If pressure exceeds membrane's maximum
        """
        if pressure > self.membrane.max_pressure:
            raise ValueError(f"Pressure exceeds membrane maximum of {self.membrane.max_pressure} bar")
        self.operating_pressure = pressure
    
    def calculate_permeate_flow(self) -> float:
        """Calculate permeate flow rate based on current conditions."""
        return self.membrane.flux_rate * self.system_area
    
    def calculate_rejection(self) -> float:
        """Calculate actual rejection rate considering operating pressure."""
        # Simplified model where rejection improves with pressure up to a point
        pressure_factor = min(1.0, self.operating_pressure / self.membrane.max_pressure)
        return self.membrane.rejection_rate * pressure_factor
    
    def calculate_product_quality(self) -> float:
        """Calculate product water concentration."""
        rejection = self.calculate_rejection()
        return self.feed_concentration * (1 - rejection)
    
    def optimize_pressure(self, target_rejection: float) -> float:
        """
        Find optimal pressure to achieve target rejection.
        
        Args:
            target_rejection: Desired rejection rate (0-1)
        
        Returns:
            Optimal pressure (bar)
        
        Raises:
            ValueError: If target rejection is not achievable
        """
        if target_rejection > self.membrane.rejection_rate:
            raise ValueError("Target rejection exceeds membrane capability")
        
        # Simple linear approximation for optimization
        required_pressure = (target_rejection / self.membrane.rejection_rate) * self.membrane.max_pressure
        return min(required_pressure, self.membrane.max_pressure)

class NFSystemController:
    """Controller for managing multiple NF systems."""
    def __init__(self):
        self.systems: Dict[str, NFSystem] = {}
    
    def add_system(self, system_id: str, system: NFSystem) -> None:
        """Add an NF system to the controller."""
        if system_id in self.systems:
            raise ValueError(f"System with ID {system_id} already exists")
        self.systems[system_id] = system
    
    def get_system_performance(self, system_id: str) -> Dict[str, float]:
        """Get performance metrics for a specific system."""
        if system_id not in self.systems:
            raise ValueError(f"System {system_id} not found")
        
        system = self.systems[system_id]
        return {
            "permeate_flow": system.calculate_permeate_flow(),
            "rejection_rate": system.calculate_rejection(),
            "product_concentration": system.calculate_product_quality(),
            "operating_pressure": system.operating_pressure
        }
    
    def optimize_all_systems(self, target_rejection: float) -> Dict[str, float]:
        """
        Optimize pressure for all systems to achieve target rejection.
        
        Returns:
            Dictionary of system IDs and their optimized pressures
        """
        results = {}
        for system_id, system in self.systems.items():
            try:
                optimal_pressure = system.optimize_pressure(target_rejection)
                system.set_operating_pressure(optimal_pressure)
                results[system_id] = optimal_pressure
            except ValueError as e:
                results[system_id] = f"Error: {str(e)}"
        return results

# Example usage
if __name__ == "__main__":
    try:
        # Create a membrane
        nf_membrane = Membrane(
            name="NF-270",
            rejection_rate=0.95,
            flux_rate=25.0,
            max_pressure=20.0
        )
        
        # Create an NF system
        nf_system = NFSystem(
            membrane=nf_membrane,
            system_area=1000.0,
            feed_concentration=2000.0
        )
        
        # Set operating pressure
        nf_system.set_operating_pressure(12.0)
        
        # Create controller and add system
        controller = NFSystemController()
        controller.add_system("System1", nf_system)
        
        # Get performance metrics
        performance = controller.get_system_performance("System1")
        print("System Performance:", performance)
        
        # Optimize for target rejection
        optimized_pressures = controller.optimize_all_systems(0.9)
        print("Optimized Pressures:", optimized_pressures)
        
    except Exception as e:
        print(f"Error in system operation: {str(e)}")
```
