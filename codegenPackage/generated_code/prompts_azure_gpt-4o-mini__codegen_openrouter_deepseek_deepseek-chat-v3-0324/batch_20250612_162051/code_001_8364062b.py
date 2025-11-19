"""
Generated Code Metadata:
========================
Original URL: https://vinaroy.com.vn
Prompt: Generate a code snippet that demonstrates how to use VinaRoy's air blower models in a system for transporting bulk materials.
Generated: DETERMINISTIC_8364062bdd98fa27
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import time
from enum import Enum
from typing import Optional, Tuple

# Define custom exceptions for error handling
class BlowerError(Exception):
    """Base exception for blower-related errors."""
    pass

class BlowerNotInitializedError(BlowerError):
    """Raised when blower is not properly initialized."""
    pass

class BlowerOverloadError(BlowerError):
    """Raised when blower is overloaded."""
    pass

class BlowerModel(Enum):
    """Enumeration of available VinaRoy blower models."""
    VR_250 = "VR-250"
    VR_500 = "VR-500"
    VR_1000 = "VR-1000"
    VR_2000 = "VR-2000"

class MaterialType(Enum):
    """Enumeration of supported bulk material types."""
    GRAIN = "Grain"
    POWDER = "Powder"
    PELLETS = "Pellets"
    SAND = "Sand"

class VinaRoyBlower:
    """
    A class to control VinaRoy air blowers for bulk material transport.
    
    Attributes:
        model: The blower model being used
        is_initialized: Whether the blower is properly initialized
        current_power: Current power level (0-100)
        material_type: Type of material being transported
        transport_rate: Current material transport rate in kg/hour
    """
    
    def __init__(self, model: BlowerModel):
        """Initialize the blower with specified model."""
        self.model = model
        self.is_initialized = False
        self.current_power = 0
        self.material_type: Optional[MaterialType] = None
        self.transport_rate = 0.0
        
    def initialize(self) -> None:
        """Initialize the blower system."""
        # Simulate initialization process
        time.sleep(1)  # Simulate hardware initialization delay
        self.is_initialized = True
        
    def set_material(self, material: MaterialType) -> None:
        """Set the material type for transport."""
        if not self.is_initialized:
            raise BlowerNotInitializedError("Blower must be initialized first")
        self.material_type = material
        
    def set_power(self, power_level: int) -> None:
        """
        Set the blower power level.
        
        Args:
            power_level: Desired power level (0-100)
            
        Raises:
            BlowerNotInitializedError: If blower is not initialized
            ValueError: If power level is out of range
            BlowerOverloadError: If power level exceeds model capacity
        """
        if not self.is_initialized:
            raise BlowerNotInitializedError("Blower must be initialized first")
        if not 0 <= power_level <= 100:
            raise ValueError("Power level must be between 0 and 100")
            
        # Model-specific power limits
        max_power = {
            BlowerModel.VR_250: 80,
            BlowerModel.VR_500: 90,
            BlowerModel.VR_1000: 100,
            BlowerModel.VR_2000: 100
        }
        
        if power_level > max_power[self.model]:
            raise BlowerOverloadError(
                f"Power level {power_level} exceeds maximum for {self.model.value}"
            )
            
        self.current_power = power_level
        self._calculate_transport_rate()
        
    def _calculate_transport_rate(self) -> None:
        """Calculate transport rate based on current settings."""
        if not self.material_type:
            self.transport_rate = 0.0
            return
            
        # Base rates for each model at 100% power (kg/hour)
        base_rates = {
            BlowerModel.VR_250: 250,
            BlowerModel.VR_500: 500,
            BlowerModel.VR_1000: 1000,
            BlowerModel.VR_2000: 2000
        }
        
        # Material density factors
        density_factors = {
            MaterialType.GRAIN: 1.0,
            MaterialType.POWDER: 0.8,
            MaterialType.PELLETS: 1.2,
            MaterialType.SAND: 1.5
        }
        
        base_rate = base_rates[self.model]
        density_factor = density_factors[self.material_type]
        power_factor = self.current_power / 100.0
        
        self.transport_rate = base_rate * density_factor * power_factor
        
    def get_status(self) -> Tuple[int, float, Optional[MaterialType]]:
        """
        Get current blower status.
        
        Returns:
            Tuple containing (power_level, transport_rate, material_type)
        """
        return (self.current_power, self.transport_rate, self.material_type)
        
    def emergency_stop(self) -> None:
        """Immediately stop the blower."""
        self.current_power = 0
        self.transport_rate = 0.0

# Example usage
if __name__ == "__main__":
    try:
        # Initialize a VR-1000 blower
        blower = VinaRoyBlower(BlowerModel.VR_1000)
        blower.initialize()
        
        # Set material to transport
        blower.set_material(MaterialType.GRAIN)
        
        # Set power level
        blower.set_power(75)
        
        # Get current status
        power, rate, material = blower.get_status()
        print(f"Blower status - Power: {power}%, Transport Rate: {rate:.2f} kg/h, Material: {material.value}")
        
    except BlowerError as e:
        print(f"Blower error occurred: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
```
