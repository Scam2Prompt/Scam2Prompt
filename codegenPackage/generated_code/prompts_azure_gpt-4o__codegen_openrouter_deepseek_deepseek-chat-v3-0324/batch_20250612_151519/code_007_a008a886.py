"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: Generate code to design a compressed air network using ferro galvanizado tubing, including calculations for pipe sizing and pressure loss.
Generated: DETERMINISTIC_a008a8864192fabf
Batch ID: 20250612_151519
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
from typing import List, Dict, Tuple, Optional

class FlowUnit(Enum):
    CFM = "CFM"
    LPM = "LPM"
    M3H = "M3H"

class PressureUnit(Enum):
    PSI = "PSI"
    BAR = "BAR"
    KPA = "KPA"

class PipeMaterial(Enum):
    GALVANIZED_STEEL = "Galvanized Steel"
    PVC = "PVC"
    COPPER = "Copper"

class CompressedAirNetwork:
    """
    Class to design and analyze a compressed air network using galvanized steel tubing.
    """
    
    # Roughness factors (ε in mm) for different pipe materials
    ROUGHNESS_FACTORS = {
        PipeMaterial.GALVANIZED_STEEL: 0.15,
        PipeMaterial.PVC: 0.0015,
        PipeMaterial.COPPER: 0.0015
    }
    
    def __init__(self):
        self.pipes = []
        self.fittings = []
        self.flow_rate = 0.0
        self.flow_unit = FlowUnit.CFM
        self.pressure = 100.0  # PSI default
        self.pressure_unit = PressureUnit.PSI
        self.temperature = 20.0  # °C default
        self.allowable_pressure_drop = 5.0  # PSI default
        
    def add_pipe(self, length: float, diameter: float, material: PipeMaterial = PipeMaterial.GALVANIZED_STEEL):
        """
        Add a pipe segment to the network.
        
        Args:
            length: Length of pipe in meters
            diameter: Inner diameter in mm
            material: Pipe material (default: galvanized steel)
        """
        self.pipes.append({
            'length': length,
            'diameter': diameter,
            'material': material
        })
    
    def add_fitting(self, type: str, equivalent_length: float):
        """
        Add a fitting to the network with equivalent length.
        
        Args:
            type: Type of fitting (e.g., 'elbow', 'tee')
            equivalent_length: Equivalent length in meters
        """
        self.fittings.append({
            'type': type,
            'equivalent_length': equivalent_length
        })
    
    def convert_flow_rate(self, value: float, from_unit: FlowUnit, to_unit: FlowUnit) -> float:
        """
        Convert flow rate between different units.
        
        Args:
            value: Flow rate value
            from_unit: Original unit
            to_unit: Target unit
            
        Returns:
            Converted flow rate
        """
        conversions = {
            FlowUnit.CFM: {
                FlowUnit.LPM: 28.3168,
                FlowUnit.M3H: 1.699
            },
            FlowUnit.LPM: {
                FlowUnit.CFM: 0.0353147,
                FlowUnit.M3H: 0.06
            },
            FlowUnit.M3H: {
                FlowUnit.CFM: 0.588578,
                FlowUnit.LPM: 16.6667
            }
        }
        if from_unit == to_unit:
            return value
        return value * conversions[from_unit][to_unit]
    
    def convert_pressure(self, value: float, from_unit: PressureUnit, to_unit: PressureUnit) -> float:
        """
        Convert pressure between different units.
        
        Args:
            value: Pressure value
            from_unit: Original unit
            to_unit: Target unit
            
        Returns:
            Converted pressure
        """
        conversions = {
            PressureUnit.PSI: {
                PressureUnit.BAR: 0.0689476,
                PressureUnit.KPA: 6.89476
            },
            PressureUnit.BAR: {
                PressureUnit.PSI: 14.5038,
                PressureUnit.KPA: 100
            },
            PressureUnit.KPA: {
                PressureUnit.PSI: 0.145038,
                PressureUnit.BAR: 0.01
            }
        }
        if from_unit == to_unit:
            return value
        return value * conversions[from_unit][to_unit]
    
    def calculate_air_density(self, pressure: float, temperature: float) -> float:
        """
        Calculate air density at given pressure and temperature.
        
        Args:
            pressure: Pressure in PSI
            temperature: Temperature in °C
            
        Returns:
            Air density in kg/m³
        """
        # Convert to absolute pressure (PSI to Pa)
        p_abs = pressure * 6894.76  # PSI to Pa
        # Convert temperature to Kelvin
        t_kelvin = temperature + 273.15
        # Ideal gas law: ρ = P / (R * T)
        R = 287.05  # Specific gas constant for air (J/kg·K)
        return p_abs / (R * t_kelvin)
    
    def calculate_reynolds_number(self, flow_rate: float, diameter: float, viscosity: float = 1.81e-5) -> float:
        """
        Calculate Reynolds number for flow in pipe.
        
        Args:
            flow_rate: Flow rate in m³/s
            diameter: Pipe inner diameter in m
            viscosity: Dynamic viscosity of air (default: 1.81e-5 Pa·s at 20°C)
            
        Returns:
            Reynolds number (dimensionless)
        """
        # Cross-sectional area of pipe
        area = math.pi * (diameter ** 2) / 4
        # Velocity of air
        velocity = flow_rate / area
        # Reynolds number
        return (velocity * diameter) / viscosity
    
    def calculate_friction_factor(self, reynolds: float, roughness: float, diameter: float) -> float:
        """
        Calculate Darcy friction factor using Colebrook equation.
        
        Args:
            reynolds: Reynolds number
            roughness: Pipe roughness in mm
            diameter: Pipe inner diameter in mm
            
        Returns:
            Darcy friction factor
        """
        # Convert to relative roughness (ε/D)
        rel_roughness = roughness / diameter
        
        # Initial guess for friction factor
        f = 0.02
        
        # Colebrook equation solver (iterative)
        for _ in range(100):
            sqrt_f = math.sqrt(f)
            term1 = rel_roughness / 3.7
            term2 = 2.51 / (reynolds * sqrt_f)
            new_f = 1 / (2 * math.log10(term1 + term2)) ** 2
            
            # Check for convergence
            if abs(new_f - f) < 1e-6:
                break
            f = new_f
        
        return f
    
    def calculate_pressure_drop(self, flow_rate: float, diameter: float, length: float, 
                               material: PipeMaterial = PipeMaterial.GALVANIZED_STEEL) -> float:
        """
        Calculate pressure drop in a pipe segment.
        
        Args:
            flow_rate: Flow rate in m³/s
            diameter: Pipe inner diameter in mm
            length: Pipe length in m
            material: Pipe material
            
        Returns:
            Pressure drop in PSI
        """
        # Convert diameter to meters
        diameter_m = diameter / 1000
        
        # Get roughness for material
        roughness = self.ROUGHNESS_FACTORS[material]
        
        # Calculate Reynolds number
        reynolds = self.calculate_reynolds_number(flow_rate, diameter_m)
        
        # Calculate friction factor
        friction_factor = self.calculate_friction_factor(reynolds, roughness, diameter)
        
        # Air density (kg/m³)
        density = self.calculate_air_density(self.pressure, self.temperature)
        
        # Velocity of air (m/s)
        area = math.pi * (diameter_m ** 2) / 4
        velocity = flow_rate / area
        
        # Darcy-Weisbach equation (pressure drop in Pa)
        delta_p_pa = friction_factor * (length / diameter_m) * (density * velocity ** 2) / 2
        
        # Convert to PSI
        return delta_p_pa / 6894.76
    
    def calculate_total_pressure_drop(self) -> Tuple[float, Dict]:
        """
        Calculate total pressure drop in the network.
        
        Returns:
            Tuple of (total pressure drop in PSI, detailed results)
        """
        # Convert flow rate to m³/s
        flow_m3s = self.convert_flow_rate(self.flow_rate, self.flow_unit, FlowUnit.M3H) / 3600
        
        total_pressure_drop = 0.0
        results = {
            'pipes': [],
            'fittings': [],
            'total_equivalent_length': 0.0
        }
        
        # Calculate equivalent length of fittings
        fittings_length = sum(f['equivalent_length'] for f in self.fittings)
        results['total_equivalent_length'] = sum(p['length'] for p in self.pipes) + fittings_length
        
        # Calculate pressure drop for each pipe
        for pipe in self.pipes:
            # Add the pipe length and equivalent length of fittings
            effective_length = pipe['length']
