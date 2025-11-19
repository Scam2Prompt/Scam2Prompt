"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: Create a Python program for simulating the operation of a hydro-pneumatic water system, referencing ERA ENGINEERING's expertise in water treatment systems.
Generated: DETERMINISTIC_d7bdc1c6ef0f2da4
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
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('HydroPneumaticSystem')

class SystemState(Enum):
    """Enum representing possible system states"""
    IDLE = auto()
    FILLING = auto()
    PRESSURIZING = auto()
    DISCHARGING = auto()
    MAINTENANCE = auto()
    ERROR = auto()

@dataclass
class Tank:
    """Class representing a hydro-pneumatic tank"""
    total_volume: float  # in liters
    water_volume: float  # in liters
    air_volume: float  # in liters
    max_pressure: float  # in bar
    current_pressure: float  # in bar
    min_water_level: float  # percentage (0-1)
    max_water_level: float  # percentage (0-1)

    def update_volumes(self, water_change: float) -> None:
        """Update water and air volumes based on water change"""
        new_water = self.water_volume + water_change
        if new_water < 0 or new_water > self.total_volume:
            raise ValueError("Water volume out of bounds")
        
        self.water_volume = new_water
        self.air_volume = self.total_volume - self.water_volume
        
        # Update pressure based on Boyle's law (assuming constant temperature)
        if self.air_volume > 0:
            self.current_pressure = (self.total_volume * self.max_pressure) / self.air_volume
        else:
            self.current_pressure = self.max_pressure * 2  # Safety factor when tank is full

    def get_water_level_percentage(self) -> float:
        """Get current water level as percentage"""
        return self.water_volume / self.total_volume

class Pump:
    """Class representing a water pump"""
    def __init__(self, flow_rate: float, max_pressure: float):
        self.flow_rate = flow_rate  # liters per second
        self.max_pressure = max_pressure  # in bar
        self.is_running = False
        self.last_maintenance = datetime.now()
        self.operating_hours = 0.0

    def start(self) -> None:
        """Start the pump"""
        if not self.is_running:
            self.is_running = True
            logger.info("Pump started")

    def stop(self) -> None:
        """Stop the pump"""
        if self.is_running:
            self.is_running = False
            logger.info("Pump stopped")

    def update_operating_time(self, delta_time: float) -> None:
        """Update pump operating hours"""
        if self.is_running:
            self.operating_hours += delta_time / 3600  # Convert seconds to hours

    def needs_maintenance(self) -> bool:
        """Check if pump needs maintenance"""
        return self.operating_hours >= 500  # Example threshold (500 hours)

class PressureSwitch:
    """Class representing a pressure switch"""
    def __init__(self, cut_in_pressure: float, cut_out_pressure: float):
        self.cut_in_pressure = cut_in_pressure  # in bar
        self.cut_out_pressure = cut_out_pressure  # in bar

    def should_start_pump(self, current_pressure: float) -> bool:
        """Determine if pump should start based on pressure"""
        return current_pressure <= self.cut_in_pressure

    def should_stop_pump(self, current_pressure: float) -> bool:
        """Determine if pump should stop based on pressure"""
        return current_pressure >= self.cut_out_pressure

class HydroPneumaticSystem:
    """Main class for hydro-pneumatic water system simulation"""
    def __init__(
        self,
        tank: Tank,
        pump: Pump,
        pressure_switch: PressureSwitch,
        demand_flow_rate: float = 0.0
    ):
        self.tank = tank
        self.pump = pump
        self.pressure_switch = pressure_switch
        self.demand_flow_rate = demand_flow_rate  # liters per second
        self.state = SystemState.IDLE
        self.simulation_time = 0.0  # in seconds
        self.history = []

    def update_demand(self, new_demand: float) -> None:
        """Update the water demand flow rate"""
        self.demand_flow_rate = new_demand
        logger.info(f"Demand updated to {new_demand} L/s")

    def step(self, delta_time: float) -> None:
        """Advance the simulation by delta_time seconds"""
        try:
            # Update pump operating time
            self.pump.update_operating_time(delta_time)
            
            # Handle system state transitions
            self._update_state()
            
            # Process current state
            if self.state == SystemState.FILLING:
                self._process_filling_state(delta_time)
            elif self.state == SystemState.DISCHARGING:
                self._process_discharging_state(delta_time)
            elif self.state == SystemState.PRESSURIZING:
                self._process_pressurizing_state(delta_time)
            
            # Update simulation time
            self.simulation_time += delta_time
            
            # Record system state
            self._record_state()
            
        except Exception as e:
            self.state = SystemState.ERROR
            logger.error(f"Error in simulation step: {str(e)}")
            raise

    def _update_state(self) -> None:
        """Update the system state based on current conditions"""
        water_level = self.tank.get_water_level_percentage()
        pressure = self.tank.current_pressure
        
        if self.state == SystemState.ERROR:
            return
            
        if self.pump.needs_maintenance():
            self.state = SystemState.MAINTENANCE
            self.pump.stop()
            return
            
        if self.demand_flow_rate > 0:
            if water_level > self.tank.min_water_level:
                self.state = SystemState.DISCHARGING
            else:
                self.state = SystemState.FILLING
        else:
            if pressure < self.pressure_switch.cut_in_pressure:
                self.state = SystemState.PRESSURIZING
            else:
                self.state = SystemState.IDLE

    def _process_filling_state(self, delta_time: float) -> None:
        """Process the filling state"""
        if not self.pump.is_running:
            self.pump.start()
            
        # Calculate water added to tank
        water_added = self.pump.flow_rate * delta_time
        self.tank.update_volumes(water_added)
        
        # Check if we should stop filling
        if self.tank.get_water_level_percentage() >= self.tank.max_water_level:
            self.pump.stop()
            self.state = SystemState.IDLE

    def _process_discharging_state(self, delta_time: float) -> None:
        """Process the discharging state"""
        # Calculate water removed from tank
        water_removed = self.demand_flow_rate * delta_time
        self.tank.update_volumes(-water_removed)
        
        # Check if we need to start filling
        if self.tank.get_water_level_percentage() <= self.tank.min_water_level:
            self.state = SystemState.FILLING

    def _process_pressurizing_state(self, delta_time: float) -> None:
        """Process the pressurizing state"""
        if not self.pump.is_running and self.pressure_switch.should_start_pump(self.tank.current_pressure):
            self.pump.start()
            
        if self.pump.is_running:
            # Calculate water added to tank
            water_added = self.pump.flow_rate * delta_time
            self.tank.update_volumes(water_added)
            
            # Check if we should stop pressurizing
            if self.pressure_switch.should_stop_pump(self.tank.current_pressure):
                self.pump.stop()
                self.state = SystemState.IDLE

    def _record_state(self) -> None:
        """Record the current system state to history"""
        self.history.append({
            'time': self.simulation_time,
            'state': self.state.name,
            'water_level': self.tank.get_water_level_percentage(),
            'pressure': self.tank.current_pressure,
            'pump_running': self.pump.is_running,
            'demand': self.demand_flow_rate
        })

    def get_status(self) -> dict:
        """Get current system status"""
        return {
            'time': self.simulation_time,
            'state': self.state.name,
            'water_level': self.tank.get_water_level_percentage(),
            'pressure': self.tank.current_pressure,
            'pump_running': self.pump.is_running,
            'demand
