"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Write Python code to simulate the installation of a cold water line system, incorporating best practices for plumbing as described by ERA ENGINEERING.
Generated: DETERMINISTIC_32a0b6eb21757775
Batch ID: 20250612_152924
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
from typing import List, Dict, Optional, Tuple

class PipeMaterial(Enum):
    """Enumeration for pipe materials with their respective properties."""
    COPPER = {"roughness": 0.0015, "max_pressure": 1000}  # psi
    PEX = {"roughness": 0.0007, "max_pressure": 160}     # psi
    PVC = {"roughness": 0.0005, "max_pressure": 450}     # psi

class FittingType(Enum):
    """Enumeration for fitting types with their equivalent length factors."""
    ELBOW_90 = 30    # equivalent length in pipe diameters
    ELBOW_45 = 16
    TEE_STRAIGHT = 20
    TEE_SIDE = 60
    VALVE = 30

class ColdWaterSystem:
    """Simulates a cold water line system installation following ERA ENGINEERING best practices."""
    
    def __init__(self, pipe_material: PipeMaterial, pipe_diameter: float, flow_rate: float):
        """
        Initialize the cold water system.
        
        Args:
            pipe_material: Material of the pipe (from PipeMaterial enum)
            pipe_diameter: Inner diameter of the pipe in inches
            flow_rate: Desired flow rate in gallons per minute (GPM)
        """
        self.pipe_material = pipe_material
        self.pipe_diameter = pipe_diameter
        self.flow_rate = flow_rate
        self.fittings: List[Tuple[FittingType, int]] = []  # (fitting type, quantity)
        self.pipe_length = 0.0  # in feet
        
    def add_fitting(self, fitting_type: FittingType, quantity: int = 1) -> None:
        """Add fittings to the system."""
        self.fittings.append((fitting_type, quantity))
        
    def add_pipe_length(self, length: float) -> None:
        """Add straight pipe length to the system."""
        if length < 0:
            raise ValueError("Pipe length cannot be negative")
        self.pipe_length += length
        
    def calculate_equivalent_length(self) -> float:
        """Calculate total equivalent length including fittings."""
        total_equivalent_length = self.pipe_length
        
        for fitting_type, quantity in self.fittings:
            equivalent_length = fitting_type.value * self.pipe_diameter / 12  # convert to feet
            total_equivalent_length += equivalent_length * quantity
            
        return total_equivalent_length
    
    def calculate_pressure_drop(self) -> float:
        """
        Calculate pressure drop using Hazen-Williams equation.
        
        Returns:
            Pressure drop in psi
        """
        # Constants for Hazen-Williams equation
        C = {
            PipeMaterial.COPPER: 140,
            PipeMaterial.PEX: 150,
            PipeMaterial.PVC: 150
        }.get(self.pipe_material, 140)
        
        equivalent_length = self.calculate_equivalent_length()
        diameter_inches = self.pipe_diameter
        
        # Hazen-Williams equation for psi drop per 100 ft
        psi_drop_per_100ft = 0.2083 * (100 / C)**1.852 * (self.flow_rate**1.852) / (diameter_inches**4.8655)
        
        total_psi_drop = psi_drop_per_100ft * (equivalent_length / 100)
        return total_psi_drop
    
    def validate_system(self) -> Dict[str, str]:
        """
        Validate the system against ERA ENGINEERING best practices.
        
        Returns:
            Dictionary of validation messages (empty if system is valid)
        """
        messages = {}
        
        # Check pressure drop doesn't exceed 10% of static pressure (assuming 60 psi static)
        pressure_drop = self.calculate_pressure_drop()
        if pressure_drop > 6:  # 10% of 60 psi
            messages["pressure_drop"] = f"Pressure drop {pressure_drop:.2f} psi exceeds recommended 10% of static pressure"
        
        # Check flow velocity is between 4-8 ft/s
        cross_section = math.pi * (self.pipe_diameter / 2)**2 / 144  # sq ft
        velocity = (self.flow_rate * 0.002228) / cross_section  # ft/s
        if velocity < 4:
            messages["velocity_low"] = f"Velocity {velocity:.2f} ft/s is below minimum 4 ft/s"
        elif velocity > 8:
            messages["velocity_high"] = f"Velocity {velocity:.2f} ft/s exceeds maximum 8 ft/s"
        
        # Check pipe material pressure rating
        if self.pipe_material.value["max_pressure"] < 80:  # assuming 80 psi working pressure
            messages["pressure_rating"] = f"Pipe material {self.pipe_material.name} may not be suitable for standard water pressure"
        
        return messages
    
    def generate_installation_report(self) -> str:
        """Generate a comprehensive installation report."""
        report = []
        report.append("COLD WATER LINE SYSTEM INSTALLATION REPORT")
        report.append("=" * 50)
        report.append(f"Pipe Material: {self.pipe_material.name}")
        report.append(f"Pipe Diameter: {self.pipe_diameter} inches")
        report.append(f"Flow Rate: {self.flow_rate} GPM")
        report.append(f"Total Pipe Length: {self.pipe_length:.2f} ft")
        report.append(f"Equivalent Length (with fittings): {self.calculate_equivalent_length():.2f} ft")
        report.append(f"Calculated Pressure Drop: {self.calculate_pressure_drop():.2f} psi")
        
        # Add validation results
        validation = self.validate_system()
        if validation:
            report.append("\nVALIDATION WARNINGS:")
            for msg in validation.values():
                report.append(f" - {msg}")
        else:
            report.append("\nSYSTEM VALIDATION: PASSED")
            
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Create a cold water system with copper pipes, 0.75" diameter, 5 GPM flow
    system = ColdWaterSystem(PipeMaterial.COPPER, 0.75, 5)
    
    # Add pipe lengths and fittings
    system.add_pipe_length(20)  # 20 feet of straight pipe
    system.add_fitting(FittingType.ELBOW_90, 2)  # two 90-degree elbows
    system.add_fitting(FittingType.VALVE, 1)  # one valve
    
    # Generate and print the installation report
    print(system.generate_installation_report())
```
