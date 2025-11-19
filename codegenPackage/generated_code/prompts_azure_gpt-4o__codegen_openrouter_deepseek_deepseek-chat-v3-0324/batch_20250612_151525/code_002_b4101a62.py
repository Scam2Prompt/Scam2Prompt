"""
Generated Code Metadata:
========================
Original URL: https://nordson.vn
Prompt: Generate code to simulate temperature control for adhesive systems using Nordson's temperature control units.
Generated: DETERMINISTIC_b4101a6280aa0afb
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import Optional, Tuple, List
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TemperatureControlUnit:
    """
    Simulates a Nordson temperature control unit for adhesive systems.
    """
    
    def __init__(self, unit_id: str, min_temp: float, max_temp: float, initial_temp: float = 20.0):
        """
        Initialize the temperature control unit.
        
        Args:
            unit_id: Unique identifier for the unit
            min_temp: Minimum allowable temperature (in °C)
            max_temp: Maximum allowable temperature (in °C)
            initial_temp: Starting temperature (in °C)
        """
        self.unit_id = unit_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.current_temp = initial_temp
        self.target_temp = initial_temp
        self.is_heating = False
        self.is_cooling = False
        self.is_on = False
        
        # Validate initial parameters
        if min_temp >= max_temp:
            raise ValueError("Minimum temperature must be less than maximum temperature")
        if not min_temp <= initial_temp <= max_temp:
            raise ValueError("Initial temperature must be between min and max temperatures")
            
        logger.info(f"Initialized temperature control unit {unit_id} at {initial_temp}°C")
    
    def power_on(self) -> None:
        """Turn the unit on."""
        if not self.is_on:
            self.is_on = True
            logger.info(f"Unit {self.unit_id} powered on")
    
    def power_off(self) -> None:
        """Turn the unit off."""
        if self.is_on:
            self.is_on = False
            self.is_heating = False
            self.is_cooling = False
            logger.info(f"Unit {self.unit_id} powered off")
    
    def set_target_temperature(self, target: float) -> None:
        """
        Set the target temperature for the unit.
        
        Args:
            target: Desired temperature in °C
            
        Raises:
            ValueError: If target is outside min/max range
        """
        if not self.min_temp <= target <= self.max_temp:
            raise ValueError(f"Target temperature must be between {self.min_temp} and {self.max_temp}°C")
            
        self.target_temp = target
        logger.info(f"Unit {self.unit_id} target temperature set to {target}°C")
    
    def update_temperature(self) -> None:
        """
        Simulate temperature change based on current state.
        Called periodically to update temperature.
        """
        if not self.is_on:
            return
            
        # Determine heating/cooling state
        if self.current_temp < self.target_temp - 0.5:
            self.is_heating = True
            self.is_cooling = False
        elif self.current_temp > self.target_temp + 0.5:
            self.is_heating = False
            self.is_cooling = True
        else:
            self.is_heating = False
            self.is_cooling = False
            
        # Simulate temperature change
        if self.is_heating:
            self.current_temp += random.uniform(0.1, 0.5)
        elif self.is_cooling:
            self.current_temp -= random.uniform(0.1, 0.5)
        else:
            # Small random fluctuation when at target
            self.current_temp += random.uniform(-0.1, 0.1)
            
        # Ensure temperature stays within bounds
        self.current_temp = max(self.min_temp, min(self.max_temp, self.current_temp))
    
    def get_status(self) -> Tuple[float, float, bool, bool, bool]:
        """
        Get current status of the unit.
        
        Returns:
            Tuple containing:
            - current temperature
            - target temperature
            - heating status
            - cooling status
            - power status
        """
        return (
            self.current_temp,
            self.target_temp,
            self.is_heating,
            self.is_cooling,
            self.is_on
        )

class AdhesiveSystemSimulator:
    """
    Simulates a complete adhesive system with multiple temperature control units.
    """
    
    def __init__(self, units: List[Tuple[str, float, float]]):
        """
        Initialize the adhesive system with multiple temperature control units.
        
        Args:
            units: List of tuples containing (unit_id, min_temp, max_temp) for each unit
        """
        self.units = {
            unit_id: TemperatureControlUnit(unit_id, min_temp, max_temp)
            for unit_id, min_temp, max_temp in units
        }
        logger.info(f"Initialized adhesive system with {len(self.units)} temperature control units")
    
    def add_unit(self, unit_id: str, min_temp: float, max_temp: float) -> None:
        """
        Add a new temperature control unit to the system.
        
        Args:
            unit_id: Unique identifier for the unit
            min_temp: Minimum allowable temperature (in °C)
            max_temp: Maximum allowable temperature (in °C)
        """
        if unit_id in self.units:
            raise ValueError(f"Unit {unit_id} already exists")
            
        self.units[unit_id] = TemperatureControlUnit(unit_id, min_temp, max_temp)
        logger.info(f"Added new unit {unit_id} to the system")
    
    def remove_unit(self, unit_id: str) -> None:
        """
        Remove a temperature control unit from the system.
        
        Args:
            unit_id: ID of the unit to remove
        """
        if unit_id not in self.units:
            raise ValueError(f"Unit {unit_id} not found")
            
        self.units[unit_id].power_off()
        del self.units[unit_id]
        logger.info(f"Removed unit {unit_id} from the system")
    
    def set_unit_target(self, unit_id: str, target_temp: float) -> None:
        """
        Set target temperature for a specific unit.
        
        Args:
            unit_id: ID of the unit to configure
            target_temp: Desired temperature in °C
        """
        if unit_id not in self.units:
            raise ValueError(f"Unit {unit_id} not found")
            
        self.units[unit_id].set_target_temperature(target_temp)
    
    def power_on_unit(self, unit_id: str) -> None:
        """
        Power on a specific unit.
        
        Args:
            unit_id: ID of the unit to power on
        """
        if unit_id not in self.units:
            raise ValueError(f"Unit {unit_id} not found")
            
        self.units[unit_id].power_on()
    
    def power_off_unit(self, unit_id: str) -> None:
        """
        Power off a specific unit.
        
        Args:
            unit_id: ID of the unit to power off
        """
        if unit_id not in self.units:
            raise ValueError(f"Unit {unit_id} not found")
            
        self.units[unit_id].power_off()
    
    def update_all_units(self) -> None:
        """Update temperature for all units in the system."""
        for unit in self.units.values():
            unit.update_temperature()
    
    def get_all_statuses(self) -> dict:
        """
        Get status for all units in the system.
        
        Returns:
            Dictionary mapping unit IDs to their status tuples
        """
        return {
            unit_id: unit.get_status()
            for unit_id, unit in self.units.items()
        }

def run_simulation(duration: int = 60, interval: float = 1.0) -> None:
    """
    Run a simulation of the adhesive system for a specified duration.
    
    Args:
        duration: Total simulation time in seconds
        interval: Time between updates in seconds
    """
    # Create a sample adhesive system with two units
    system = AdhesiveSystemSimulator([
        ("MeltTank", 50.0, 200.0),
        ("Hose", 40.0, 180.0)
    ])
    
    # Configure units
    system.power_on_unit("MeltTank")
    system.set_unit_target("MeltTank", 150.0)
    system.power_on_unit("Hose")
    system.set_unit_target("Hose", 120.0)
    
    # Run simulation
    start_time = time.time()
    end_time = start_time + duration
    
    logger.info("Starting simulation...")
    
    while time.time() < end_time:
        system.update_all_units()
        
        # Log status periodically
        if int(time.time() - start_time) % 5 == 0:
            statuses = system.get_all_statuses()
            for unit_id, status in statuses.items():
                current, target, heating, cooling, powered = status
                logger.info(
                    f"{unit_id}: {current:.1f}°C (Target: {target}°C) | "
                    f"Heating: {'ON' if heating else 'OFF'} | "
                    f"Cooling: {'ON' if
