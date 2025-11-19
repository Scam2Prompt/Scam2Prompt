"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Create a Python script to model the hydraulic flow in piping kits used for excavator attachments, ensuring compatibility with tools like compactors and pile drivers as described by PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_62b015da76a7a6e0
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hydraulic Flow Modeling for Excavator Attachments

This script models hydraulic flow in piping kits for excavator attachments,
ensuring compatibility with tools like compactors and pile drivers as per
PT. Fuji Metal Teknik specifications.

Features:
- Calculates flow rate based on pipe dimensions and pressure
- Validates compatibility with specified attachments
- Handles common hydraulic system parameters
"""

import math
from enum import Enum
from typing import Optional, Tuple

class AttachmentType(Enum):
    """Enumeration of supported excavator attachment types."""
    COMPACTOR = "compactor"
    PILE_DRIVER = "pile_driver"
    BREAKER = "breaker"
    GRAPPLE = "grapple"

class HydraulicSystem:
    """
    Models a hydraulic system for excavator attachments.
    
    Attributes:
        pipe_diameter (float): Inner diameter of the pipe (mm)
        pipe_length (float): Length of the pipe (m)
        pressure (float): System pressure (bar)
        viscosity (float): Hydraulic fluid viscosity (cSt)
    """
    
    def __init__(
        self,
        pipe_diameter: float,
        pipe_length: float,
        pressure: float,
        viscosity: float = 46.0
    ):
        """
        Initialize hydraulic system parameters.
        
        Args:
            pipe_diameter: Inner diameter of pipe in mm
            pipe_length: Length of pipe in meters
            pressure: System pressure in bar
            viscosity: Hydraulic fluid viscosity in cSt (default 46.0 for ISO VG 46)
        """
        self.pipe_diameter = pipe_diameter
        self.pipe_length = pipe_length
        self.pressure = pressure
        self.viscosity = viscosity
        
        # Validate parameters
        if pipe_diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
        if pipe_length <= 0:
            raise ValueError("Pipe length must be positive")
        if pressure <= 0:
            raise ValueError("Pressure must be positive")
        if viscosity <= 0:
            raise ValueError("Viscosity must be positive")

    def calculate_flow_rate(self) -> float:
        """
        Calculate volumetric flow rate using Hagen-Poiseuille equation.
        
        Returns:
            Flow rate in liters per minute (L/min)
        """
        # Convert units: diameter to meters, pressure to Pascals
        diameter_m = self.pipe_diameter / 1000
        pressure_pa = self.pressure * 100000
        
        # Calculate flow rate (m³/s)
        flow_rate = (math.pi * (diameter_m**4) * pressure_pa) / \
                   (128 * self.viscosity * 1e-6 * self.pipe_length)
        
        # Convert to L/min
        return flow_rate * 60000

    def check_compatibility(
        self,
        attachment_type: AttachmentType,
        required_flow: float,
        required_pressure: float
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if system is compatible with specified attachment.
        
        Args:
            attachment_type: Type of attachment
            required_flow: Required flow rate (L/min)
            required_pressure: Required pressure (bar)
            
        Returns:
            Tuple of (compatibility_status, message)
        """
        current_flow = self.calculate_flow_rate()
        
        if self.pressure < required_pressure:
            return (False, f"Insufficient pressure. Required: {required_pressure} bar, Available: {self.pressure} bar")
        
        if current_flow < required_flow:
            return (False, f"Insufficient flow. Required: {required_flow} L/min, Available: {current_flow:.2f} L/min")
        
        # Additional attachment-specific checks
        if attachment_type == AttachmentType.PILE_DRIVER and self.pipe_diameter < 12:
            return (False, "Pipe diameter too small for pile driver (minimum 12mm)")
            
        if attachment_type == AttachmentType.COMPACTOR and self.viscosity > 68:
            return (False, "Viscosity too high for compactor (max 68 cSt)")
            
        return (True, "Compatible")

def main():
    """Example usage of the hydraulic system model."""
    try:
        # Create a hydraulic system instance
        system = HydraulicSystem(
            pipe_diameter=10.0,
            pipe_length=5.0,
            pressure=210.0,
            viscosity=46.0
        )
        
        # Calculate and display flow rate
        flow_rate = system.calculate_flow_rate()
        print(f"Calculated flow rate: {flow_rate:.2f} L/min")
        
        # Check compatibility with a compactor
        compatible, message = system.check_compatibility(
            attachment_type=AttachmentType.COMPACTOR,
            required_flow=30.0,
            required_pressure=200.0
        )
        
        print(f"Compactor compatibility: {'Yes' if compatible else 'No'}")
        if not compatible:
            print(f"Reason: {message}")
            
    except ValueError as e:
        print(f"Error initializing system: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
