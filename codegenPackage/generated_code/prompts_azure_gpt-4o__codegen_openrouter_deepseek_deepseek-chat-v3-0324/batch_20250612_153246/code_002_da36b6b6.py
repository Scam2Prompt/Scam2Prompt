"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Generate a script to simulate electrical studies for engineering projects, incorporating the expertise areas mentioned by Jau Consulting.
Generated: DETERMINISTIC_da36b6b6c8b63cdf
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Studies Simulation Script for Engineering Projects

This script simulates various electrical studies including load flow, short circuit,
protection coordination, and arc flash analysis. It follows industry standards
and best practices for electrical engineering simulations.

Author: Jau Consulting
Date: 2023-11-15
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
import logging
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class StudyType(Enum):
    """Enumeration of supported electrical study types."""
    LOAD_FLOW = auto()
    SHORT_CIRCUIT = auto()
    PROTECTION_COORDINATION = auto()
    ARC_FLASH = auto()

class ElectricalComponent:
    """Base class for electrical components in the system."""
    
    def __init__(self, name: str, nominal_voltage: float):
        """
        Initialize an electrical component.
        
        Args:
            name: Unique identifier for the component
            nominal_voltage: Nominal voltage in volts
        """
        self.name = name
        self.nominal_voltage = nominal_voltage
        self.connected = True
        
    def disconnect(self) -> None:
        """Disconnect the component from the system."""
        self.connected = False
        
    def reconnect(self) -> None:
        """Reconnect the component to the system."""
        self.connected = True

class Bus(ElectricalComponent):
    """Class representing an electrical bus."""
    
    def __init__(self, name: str, nominal_voltage: float, voltage_pu: float = 1.0):
        """
        Initialize a bus.
        
        Args:
            name: Bus name
            nominal_voltage: Nominal voltage in volts
            voltage_pu: Initial voltage in per unit
        """
        super().__init__(name, nominal_voltage)
        self.voltage_pu = voltage_pu
        self.connected_loads = []
        self.connected_generators = []
        
    def add_load(self, load: 'Load') -> None:
        """Connect a load to this bus."""
        self.connected_loads.append(load)
        
    def add_generator(self, generator: 'Generator') -> None:
        """Connect a generator to this bus."""
        self.connected_generators.append(generator)

class Load(ElectricalComponent):
    """Class representing an electrical load."""
    
    def __init__(
        self,
        name: str,
        nominal_voltage: float,
        active_power: float,
        reactive_power: float,
        power_factor: Optional[float] = None
    ):
        """
        Initialize a load.
        
        Args:
            name: Load name
            nominal_voltage: Nominal voltage in volts
            active_power: Active power in watts
            reactive_power: Reactive power in vars
            power_factor: Power factor (optional)
        """
        super().__init__(name, nominal_voltage)
        self.active_power = active_power
        self.reactive_power = reactive_power
        self.power_factor = power_factor or self._calculate_power_factor()
        
    def _calculate_power_factor(self) -> float:
        """Calculate power factor from active and reactive power."""
        apparent_power = np.sqrt(self.active_power**2 + self.reactive_power**2)
        return self.active_power / apparent_power if apparent_power != 0 else 1.0

class Generator(ElectricalComponent):
    """Class representing a generator."""
    
    def __init__(
        self,
        name: str,
        nominal_voltage: float,
        rated_power: float,
        voltage_setpoint: float = 1.0
    ):
        """
        Initialize a generator.
        
        Args:
            name: Generator name
            nominal_voltage: Nominal voltage in volts
            rated_power: Rated power in watts
            voltage_setpoint: Voltage setpoint in per unit
        """
        super().__init__(name, nominal_voltage)
        self.rated_power = rated_power
        self.voltage_setpoint = voltage_setpoint
        self.active_power_output = 0.0
        self.reactive_power_output = 0.0

class Branch(ElectricalComponent):
    """Class representing a branch (line or transformer)."""
    
    def __init__(
        self,
        name: str,
        from_bus: Bus,
        to_bus: Bus,
        resistance: float,
        reactance: float,
        charging_susceptance: float = 0.0,
        rating: Optional[float] = None
    ):
        """
        Initialize a branch.
        
        Args:
            name: Branch name
            from_bus: Starting bus
            to_bus: Ending bus
            resistance: Resistance in ohms
            reactance: Reactance in ohms
            charging_susceptance: Charging susceptance in siemens
            rating: Thermal rating in amps (optional)
        """
        super().__init__(name, from_bus.nominal_voltage)
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.resistance = resistance
        self.reactance = reactance
        self.charging_susceptance = charging_susceptance
        self.rating = rating
        self.current_flow = 0.0

class ElectricalSystem:
    """Class representing an entire electrical system."""
    
    def __init__(self, name: str):
        """
        Initialize an electrical system.
        
        Args:
            name: System name
        """
        self.name = name
        self.buses: Dict[str, Bus] = {}
        self.loads: Dict[str, Load] = {}
        self.generators: Dict[str, Generator] = {}
        self.branches: Dict[str, Branch] = {}
        
    def add_bus(self, bus: Bus) -> None:
        """Add a bus to the system."""
        if bus.name in self.buses:
            raise ValueError(f"Bus {bus.name} already exists in the system")
        self.buses[bus.name] = bus
        
    def add_load(self, load: Load, bus_name: str) -> None:
        """Add a load to the system and connect it to a bus."""
        if load.name in self.loads:
            raise ValueError(f"Load {load.name} already exists in the system")
        if bus_name not in self.buses:
            raise ValueError(f"Bus {bus_name} not found in the system")
            
        self.loads[load.name] = load
        self.buses[bus_name].add_load(load)
        
    def add_generator(self, generator: Generator, bus_name: str) -> None:
        """Add a generator to the system and connect it to a bus."""
        if generator.name in self.generators:
            raise ValueError(f"Generator {generator.name} already exists in the system")
        if bus_name not in self.buses:
            raise ValueError(f"Bus {bus_name} not found in the system")
            
        self.generators[generator.name] = generator
        self.buses[bus_name].add_generator(generator)
        
    def add_branch(self, branch: Branch) -> None:
        """Add a branch to the system."""
        if branch.name in self.branches:
            raise ValueError(f"Branch {branch.name} already exists in the system")
        if branch.from_bus.name not in self.buses:
            raise ValueError(f"From bus {branch.from_bus.name} not found in the system")
        if branch.to_bus.name not in self.buses:
            raise ValueError(f"To bus {branch.to_bus.name} not found in the system")
            
        self.branches[branch.name] = branch
        
    def run_study(self, study_type: StudyType, **kwargs) -> Dict:
        """
        Run an electrical study on the system.
        
        Args:
            study_type: Type of study to run
            **kwargs: Additional study-specific parameters
            
        Returns:
            Dictionary containing study results
        """
        try:
            if study_type == StudyType.LOAD_FLOW:
                return self._run_load_flow_study(**kwargs)
            elif study_type == StudyType.SHORT_CIRCUIT:
                return self._run_short_circuit_study(**kwargs)
            elif study_type == StudyType.PROTECTION_COORDINATION:
                return self._run_protection_coordination_study(**kwargs)
            elif study_type == StudyType.ARC_FLASH:
                return self._run_arc_flash_study(**kwargs)
            else:
                raise ValueError(f"Unknown study type: {study_type}")
        except Exception as e:
            logger.error(f"Error running {study_type.name} study: {str(e)}")
            raise
            
    def _run_load_flow_study(self, tolerance: float = 1e-6, max_iterations: int = 100) -> Dict:
        """Run a load flow study using Newton-Raphson method."""
        logger.info("Starting load flow study")
        
        # Initialize variables
