"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Develop a code snippet that models the hydraulic control system for a tractor-mounted water bowser, inspired by JECO's product features.
Generated: DETERMINISTIC_b1be3f28dfef10c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Hydraulic Control System for Tractor-Mounted Water Bowser

This module models the hydraulic control system for a water bowser, including:
- Pump control
- Valve control
- Pressure monitoring
- Safety features

Inspired by JECO's product features.
"""

import time
from enum import Enum, auto
from typing import Optional, Tuple

class SystemState(Enum):
    """Possible states of the hydraulic system."""
    OFF = auto()
    STANDBY = auto()
    ACTIVE = auto()
    FAULT = auto()

class ValvePosition(Enum):
    """Possible positions for control valves."""
    CLOSED = auto()
    OPEN = auto()
    PARTIALLY_OPEN = auto()

class HydraulicSystem:
    """
    Models the hydraulic control system for a tractor-mounted water bowser.
    
    Attributes:
        max_pressure (float): Maximum allowable system pressure in bar
        current_pressure (float): Current system pressure in bar
        flow_rate (float): Current flow rate in liters/minute
        system_state (SystemState): Current state of the system
        pump_active (bool): Whether the pump is active
        valve_position (ValvePosition): Current valve position
    """
    
    def __init__(self, max_pressure: float = 150.0):
        """Initialize the hydraulic system with default values."""
        self.max_pressure = max_pressure
        self.current_pressure = 0.0
        self.flow_rate = 0.0
        self.system_state = SystemState.OFF
        self.pump_active = False
        self.valve_position = ValvePosition.CLOSED
        self._last_fault = None
        
    def start_system(self) -> bool:
        """
        Start the hydraulic system and transition to STANDBY state.
        
        Returns:
            bool: True if successful, False if already running or in fault state
        """
        if self.system_state in (SystemState.ACTIVE, SystemState.STANDBY):
            return False
        if self.system_state == SystemState.FAULT:
            return False
            
        self.system_state = SystemState.STANDBY
        self._initialize_sensors()
        return True
        
    def stop_system(self) -> bool:
        """
        Stop the hydraulic system and transition to OFF state.
        
        Returns:
            bool: True if successful, False if already off
        """
        if self.system_state == SystemState.OFF:
            return False
            
        self._deactivate_pump()
        self._close_valve()
        self.system_state = SystemState.OFF
        return True
        
    def activate_pump(self, target_pressure: float) -> Tuple[bool, Optional[str]]:
        """
        Activate the hydraulic pump to reach target pressure.
        
        Args:
            target_pressure: Desired system pressure in bar
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        if self.system_state != SystemState.STANDBY:
            return False, "System must be in STANDBY to activate pump"
            
        if target_pressure > self.max_pressure:
            return False, f"Target pressure exceeds maximum of {self.max_pressure} bar"
            
        self.pump_active = True
        self.system_state = SystemState.ACTIVE
        self._simulate_pressure_increase(target_pressure)
        return True, None
        
    def deactivate_pump(self) -> bool:
        """
        Deactivate the hydraulic pump.
        
        Returns:
            bool: True if successful, False if pump already inactive
        """
        if not self.pump_active:
            return False
            
        self._deactivate_pump()
        return True
        
    def set_valve_position(self, position: ValvePosition) -> Tuple[bool, Optional[str]]:
        """
        Set the valve to specified position.
        
        Args:
            position: Desired valve position
            
        Returns:
            Tuple of (success: bool, error_message: Optional[str])
        """
        if self.system_state not in (SystemState.ACTIVE, SystemState.STANDBY):
            return False, "System must be active or in standby to adjust valve"
            
        self.valve_position = position
        self._adjust_flow_rate()
        return True, None
        
    def emergency_shutdown(self) -> None:
        """Immediately shut down all system components."""
        self._deactivate_pump()
        self._close_valve()
        self.system_state = SystemState.OFF
        self._last_fault = "Emergency shutdown activated"
        
    def get_system_status(self) -> dict:
        """Return current system status as a dictionary."""
        return {
            "state": self.system_state.name,
            "pressure": f"{self.current_pressure:.1f} bar",
            "flow_rate": f"{self.flow_rate:.1f} L/min",
            "pump": "ACTIVE" if self.pump_active else "INACTIVE",
            "valve": self.valve_position.name,
            "last_fault": self._last_fault or "None"
        }
        
    def _initialize_sensors(self) -> None:
        """Simulate sensor initialization."""
        self.current_pressure = 0.0
        self.flow_rate = 0.0
        self._last_fault = None
        
    def _deactivate_pump(self) -> None:
        """Deactivate pump and simulate pressure decrease."""
        self.pump_active = False
        self._simulate_pressure_decrease()
        
    def _close_valve(self) -> None:
        """Close the valve completely."""
        self.valve_position = ValvePosition.CLOSED
        self.flow_rate = 0.0
        
    def _simulate_pressure_increase(self, target: float) -> None:
        """Simulate gradual pressure increase to target."""
        step = (target - self.current_pressure) / 10
        for _ in range(10):
            self.current_pressure += step
            time.sleep(0.1)
            self._check_pressure_limits()
            
    def _simulate_pressure_decrease(self) -> None:
        """Simulate gradual pressure decrease."""
        while self.current_pressure > 0.5:
            self.current_pressure *= 0.8
            time.sleep(0.1)
        self.current_pressure = 0.0
        
    def _adjust_flow_rate(self) -> None:
        """Adjust flow rate based on valve position and pressure."""
        if self.valve_position == ValvePosition.CLOSED:
            self.flow_rate = 0.0
        elif self.valve_position == ValvePosition.OPEN:
            self.flow_rate = self.current_pressure * 2.5
        else:  # PARTIALLY_OPEN
            self.flow_rate = self.current_pressure * 1.2
            
    def _check_pressure_limits(self) -> None:
        """Check if pressure exceeds limits and trigger fault if needed."""
        if self.current_pressure > self.max_pressure * 1.1:  # 10% over max
            self.system_state = SystemState.FAULT
            self._last_fault = f"Pressure exceeded limit: {self.current_pressure:.1f} bar"
            self.emergency_shutdown()
```
