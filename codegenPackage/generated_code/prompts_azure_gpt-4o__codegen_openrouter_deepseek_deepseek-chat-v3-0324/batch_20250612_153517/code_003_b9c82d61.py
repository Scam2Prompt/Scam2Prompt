"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Create a script to model the setup and operation of a diesel or gas generator system, including integration with capacitor banks, as outlined by پایش نیرو.
Generated: DETERMINISTIC_b9c82d615b8fe110
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Generator System Simulation with Capacitor Bank Integration

This script models the setup and operation of a diesel/gas generator system
with capacitor bank integration for power stabilization.

Key components:
- Generator class (diesel/gas)
- CapacitorBank class
- PowerSystem class to manage integration
- Simulation engine for operation modeling
"""

import numpy as np
from typing import Union, Tuple, List
from enum import Enum, auto
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GeneratorType(Enum):
    DIESEL = auto()
    GAS = auto()

@dataclass
class GeneratorSpecs:
    """Specifications for generator setup"""
    rated_power_kw: float
    fuel_consumption_rate: float  # liters/kWh or m³/kWh
    min_load_percentage: float
    max_load_percentage: float
    ramp_rate_kw_per_sec: float
    maintenance_interval_hours: float

class Generator:
    """Models a diesel or gas generator"""
    
    def __init__(
        self,
        generator_type: GeneratorType,
        specs: GeneratorSpecs,
        name: str = "Generator"
    ):
        self.type = generator_type
        self.specs = specs
        self.name = name
        self.current_load_kw = 0.0
        self.operational_hours = 0.0
        self.fuel_consumed = 0.0
        self.is_running = False
        self.maintenance_required = False
        
    def start(self) -> bool:
        """Start the generator"""
        if self.is_running:
            logger.warning(f"{self.name} is already running")
            return False
            
        self.is_running = True
        self.current_load_kw = 0.0
        logger.info(f"{self.name} started successfully")
        return True
    
    def stop(self) -> bool:
        """Stop the generator"""
        if not self.is_running:
            logger.warning(f"{self.name} is already stopped")
            return False
            
        self.is_running = False
        self.current_load_kw = 0.0
        logger.info(f"{self.name} stopped successfully")
        return True
    
    def set_load(self, load_kw: float) -> bool:
        """Set generator load in kW"""
        if not self.is_running:
            logger.error(f"Cannot set load - {self.name} is not running")
            return False
            
        min_load = self.specs.min_load_percentage * self.specs.rated_power_kw / 100
        max_load = self.specs.max_load_percentage * self.specs.rated_power_kw / 100
        
        if load_kw < min_load or load_kw > max_load:
            logger.error(
                f"Load {load_kw}kW outside permissible range ({min_load}-{max_load}kW)"
            )
            return False
            
        self.current_load_kw = load_kw
        return True
    
    def update_operation(self, time_elapsed_hours: float) -> float:
        """
        Update generator state based on elapsed time
        Returns fuel consumed in this period
        """
        if not self.is_running:
            return 0.0
            
        self.operational_hours += time_elapsed_hours
        fuel_consumed = (
            self.current_load_kw * 
            time_elapsed_hours * 
            self.specs.fuel_consumption_rate
        )
        self.fuel_consumed += fuel_consumed
        
        # Check maintenance requirement
        if (self.operational_hours >= self.specs.maintenance_interval_hours and 
            not self.maintenance_required):
            self.maintenance_required = True
            logger.warning(f"{self.name} requires maintenance")
            
        return fuel_consumed

class CapacitorBank:
    """Models a capacitor bank for power factor correction"""
    
    def __init__(
        self,
        capacity_kvar: float,
        step_size_kvar: float,
        name: str = "Capacitor Bank"
    ):
        self.capacity_kvar = capacity_kvar
        self.step_size_kvar = step_size_kvar
        self.name = name
        self.current_kvar = 0.0
        
    def adjust(self, target_kvar: float) -> bool:
        """Adjust capacitor bank output"""
        if target_kvar < 0 or target_kvar > self.capacity_kvar:
            logger.error(
                f"Target kVAR {target_kvar} outside permissible range (0-{self.capacity_kvar})"
            )
            return False
            
        # Round to nearest step
        steps = round(target_kvar / self.step_size_kvar)
        new_kvar = steps * self.step_size_kvar
        
        if new_kvar != self.current_kvar:
            self.current_kvar = new_kvar
            logger.info(
                f"{self.name} adjusted to {self.current_kvar} kVAR "
                f"(target was {target_kvar} kVAR)"
            )
            
        return True
    
    def reset(self) -> None:
        """Reset capacitor bank to zero output"""
        self.current_kvar = 0.0
        logger.info(f"{self.name} reset to 0 kVAR")

class PowerSystem:
    """Manages integration of generators and capacitor banks"""
    
    def __init__(self):
        self.generators: List[Generator] = []
        self.capacitor_banks: List[CapacitorBank] = []
        self.total_power_kw = 0.0
        self.total_reactive_kvar = 0.0
        
    def add_generator(self, generator: Generator) -> None:
        """Add a generator to the system"""
        self.generators.append(generator)
        logger.info(f"Added {generator.name} to power system")
        
    def add_capacitor_bank(self, capacitor_bank: CapacitorBank) -> None:
        """Add a capacitor bank to the system"""
        self.capacitor_banks.append(capacitor_bank)
        logger.info(f"Added {capacitor_bank.name} to power system")
        
    def calculate_power_factor(self) -> float:
        """Calculate current power factor"""
        if self.total_power_kw == 0:
            return 1.0
            
        apparent_power = np.sqrt(
            self.total_power_kw**2 + self.total_reactive_kvar**2
        )
        return self.total_power_kw / apparent_power
        
    def distribute_load(
        self,
        required_power_kw: float,
        required_pf: float = 0.95
    ) -> Tuple[bool, str]:
        """
        Distribute load across generators and adjust capacitor banks
        Returns (success, message)
        """
        # Calculate required reactive power
        required_reactive_kvar = (
            required_power_kw * np.sqrt(1 - required_pf**2) / required_pf
        )
        
        # Start/stop generators as needed
        running_gens = [g for g in self.generators if g.is_running]
        
        if not running_gens and required_power_kw > 0:
            if not self.generators:
                return False, "No generators available"
                
            # Start the first generator
            if not self.generators[0].start():
                return False, f"Failed to start {self.generators[0].name}"
            running_gens = [self.generators[0]]
        
        # Distribute active power
        remaining_power = required_power_kw
        gen_loads = {}
        
        for gen in running_gens:
            max_possible = min(
                gen.specs.rated_power_kw,
                remaining_power
            )
            gen_loads[gen] = max_possible
            remaining_power -= max_possible
            
        if remaining_power > 0:
            return False, f"Insufficient generator capacity (short by {remaining_power} kW)"
            
        # Apply the loads
        for gen, load in gen_loads.items():
            if not gen.set_load(load):
                return False, f"Failed to set load on {gen.name}"
                
        # Adjust capacitor banks for reactive power
        remaining_reactive = required_reactive_kvar - self.total_reactive_kvar
        
        for bank in self.capacitor_banks:
            if remaining_reactive <= 0:
                break
                
            target = min(bank.capacity_kvar, remaining_reactive)
            if bank.adjust(target):
                remaining_reactive -= bank.current_kvar
        
        # Update system totals
        self.total_power_kw = required_power_kw
        self.total_reactive_kvar = sum(b.current_kvar for b in self.capacitor_banks)
        
        current_pf = self.calculate_power_factor()
        
        return True, (
            f"Load distribution successful. "
            f"Current PF: {current_pf:.3f} "
            f"(Target:
