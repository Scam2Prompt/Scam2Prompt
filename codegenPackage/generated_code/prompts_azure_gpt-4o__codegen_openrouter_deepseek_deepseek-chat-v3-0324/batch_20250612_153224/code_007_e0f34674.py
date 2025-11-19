"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: Create a Python program to calculate the mass or volume flow rate of a two-phase fluid in a dynamic metering system, ensuring compliance with petrochemical industry standards.
Generated: DETERMINISTIC_e0f34674019c22bc
Batch ID: 20250612_153224
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
from typing import Optional, Tuple

class Phase(Enum):
    """Enumeration for fluid phases."""
    LIQUID = 1
    GAS = 2
    TWO_PHASE = 3

class FluidProperties:
    """Class to store and calculate fluid properties."""
    
    def __init__(
        self,
        liquid_density: float,
        gas_density: float,
        liquid_viscosity: float,
        gas_viscosity: float,
        surface_tension: float,
    ):
        """
        Initialize fluid properties.
        
        Args:
            liquid_density: Density of liquid phase (kg/m³)
            gas_density: Density of gas phase (kg/m³)
            liquid_viscosity: Dynamic viscosity of liquid phase (Pa·s)
            gas_viscosity: Dynamic viscosity of gas phase (Pa·s)
            surface_tension: Surface tension between phases (N/m)
        """
        self.liquid_density = liquid_density
        self.gas_density = gas_density
        self.liquid_viscosity = liquid_viscosity
        self.gas_viscosity = gas_viscosity
        self.surface_tension = surface_tension

class PipeGeometry:
    """Class to store pipe geometry information."""
    
    def __init__(self, diameter: float, roughness: float, angle: float = 0.0):
        """
        Initialize pipe geometry.
        
        Args:
            diameter: Inner diameter of pipe (m)
            roughness: Pipe wall roughness (m)
            angle: Inclination angle from horizontal (degrees)
        """
        self.diameter = diameter
        self.roughness = roughness
        self.angle = angle

class FlowParameters:
    """Class to store flow measurement parameters."""
    
    def __init__(
        self,
        pressure: float,
        temperature: float,
        liquid_holdup: Optional[float] = None,
        gas_holdup: Optional[float] = None,
    ):
        """
        Initialize flow parameters.
        
        Args:
            pressure: System pressure (Pa)
            temperature: System temperature (K)
            liquid_holdup: Liquid volume fraction (0-1)
            gas_holdup: Gas volume fraction (0-1)
        """
        self.pressure = pressure
        self.temperature = temperature
        self.liquid_holdup = liquid_holdup
        self.gas_holdup = gas_holdup

class TwoPhaseFlowCalculator:
    """Class to calculate two-phase flow rates."""
    
    def __init__(
        self,
        fluid_properties: FluidProperties,
        pipe_geometry: PipeGeometry,
        flow_parameters: FlowParameters,
    ):
        """
        Initialize the calculator with fluid, pipe, and flow properties.
        
        Args:
            fluid_properties: FluidProperties object
            pipe_geometry: PipeGeometry object
            flow_parameters: FlowParameters object
        """
        self.fluid = fluid_properties
        self.pipe = pipe_geometry
        self.flow = flow_parameters
        
        # Validate inputs
        self._validate_inputs()
    
    def _validate_inputs(self):
        """Validate input parameters."""
        if self.flow.liquid_holdup is not None and not (0 <= self.flow.liquid_holdup <= 1):
            raise ValueError("Liquid holdup must be between 0 and 1")
        if self.flow.gas_holdup is not None and not (0 <= self.flow.gas_holdup <= 1):
            raise ValueError("Gas holdup must be between 0 and 1")
        if self.pipe.diameter <= 0:
            raise ValueError("Pipe diameter must be positive")
        if self.fluid.liquid_density <= 0 or self.fluid.gas_density <= 0:
            raise ValueError("Densities must be positive")
        if self.fluid.liquid_viscosity <= 0 or self.fluid.gas_viscosity <= 0:
            raise ValueError("Viscosities must be positive")
        if self.flow.pressure <= 0:
            raise ValueError("Pressure must be positive")
        if self.flow.temperature <= 0:
            raise ValueError("Temperature must be positive")
    
    def calculate_mass_flow_rate(
        self,
        pressure_drop: float,
        length: float,
        phase: Phase = Phase.TWO_PHASE,
    ) -> Tuple[float, float]:
        """
        Calculate mass flow rates for liquid and gas phases.
        
        Args:
            pressure_drop: Pressure drop over pipe length (Pa)
            length: Pipe length over which pressure drop occurs (m)
            phase: Phase of fluid (LIQUID, GAS, or TWO_PHASE)
            
        Returns:
            Tuple of (liquid_mass_flow, gas_mass_flow) in kg/s
        """
        if length <= 0:
            raise ValueError("Length must be positive")
        if pressure_drop <= 0:
            raise ValueError("Pressure drop must be positive")
        
        if phase == Phase.LIQUID:
            # Single-phase liquid flow
            liquid_flow = self._calculate_single_phase_flow(
                self.fluid.liquid_density,
                self.fluid.liquid_viscosity,
                pressure_drop,
                length,
            )
            return (liquid_flow, 0.0)
        
        elif phase == Phase.GAS:
            # Single-phase gas flow
            gas_flow = self._calculate_single_phase_flow(
                self.fluid.gas_density,
                self.fluid.gas_viscosity,
                pressure_drop,
                length,
            )
            return (0.0, gas_flow)
        
        else:
            # Two-phase flow calculation
            if self.flow.liquid_holdup is None or self.flow.gas_holdup is None:
                raise ValueError("Holdups must be specified for two-phase flow")
            
            return self._calculate_two_phase_flow(pressure_drop, length)
    
    def _calculate_single_phase_flow(
        self,
        density: float,
        viscosity: float,
        pressure_drop: float,
        length: float,
    ) -> float:
        """
        Calculate single-phase mass flow rate using Darcy-Weisbach equation.
        
        Args:
            density: Fluid density (kg/m³)
            viscosity: Fluid viscosity (Pa·s)
            pressure_drop: Pressure drop (Pa)
            length: Pipe length (m)
            
        Returns:
            Mass flow rate in kg/s
        """
        # Initial guess for friction factor (Colebrook-White)
        f = 0.02
        area = math.pi * (self.pipe.diameter / 2) ** 2
        
        # Iterative solution for friction factor
        for _ in range(10):  # Limited iterations for convergence
            velocity = math.sqrt(
                (2 * self.pipe.diameter * pressure_drop) / (f * density * length)
            )
            reynolds = (density * velocity * self.pipe.diameter) / viscosity
            
            # Colebrook-White equation for turbulent flow
            if reynolds > 4000:
                new_f = 1 / (
                    -2 * math.log10(
                        (self.pipe.roughness / (3.7 * self.pipe.diameter)) +
                        (2.51 / (reynolds * math.sqrt(f)))
                    )
                ) ** 2
            else:
                # Laminar flow friction factor
                new_f = 64 / reynolds
            
            if abs(new_f - f) < 1e-6:
                break
            f = new_f
        
        mass_flow = density * velocity * area
        return mass_flow
    
    def _calculate_two_phase_flow(
        self,
        pressure_drop: float,
        length: float,
    ) -> Tuple[float, float]:
        """
        Calculate two-phase mass flow rates using Beggs & Brill method.
        
        Args:
            pressure_drop: Pressure drop (Pa)
            length: Pipe length (m)
            
        Returns:
            Tuple of (liquid_mass_flow, gas_mass_flow) in kg/s
        """
        # Calculate no-slip holdup
        lambda_l = self.flow.liquid_holdup
        lambda_g = self.flow.gas_holdup
        
        # Calculate mixture density and viscosity
        rho_m = lambda_l * self.fluid.liquid_density + lambda_g * self.fluid.gas_density
        mu_m = lambda_l * self.fluid.liquid_viscosity + lambda_g * self.fluid.gas_viscosity
        
        # Calculate superficial velocities
        area = math.pi * (self.pipe.diameter / 2) ** 2
        v_sl = lambda_l * math.sqrt(
            (2 * self.pipe.diameter * pressure_drop) / (rho_m * length)
        )
        v_sg = lambda_g * math.sqrt(
            (2 * self.pipe.diameter * pressure_drop) / (rho_m * length)
        )
        
        # Calculate mixture velocity
        v_m = v_sl + v_sg
        
        # Calculate Reynolds number
        Re_m = (rho_m * v_m * self.pipe.diameter) / mu_m
        
        # Calculate friction
