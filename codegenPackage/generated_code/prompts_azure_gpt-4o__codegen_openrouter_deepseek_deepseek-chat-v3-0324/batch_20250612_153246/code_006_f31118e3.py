"""
Generated Code Metadata:
========================
Original URL: https://accutrolsystems.com
Prompt: Write code to simulate the operation of electric calorifiers, incorporating design principles similar to those highlighted by Accutrol Systems.
Generated: DETERMINISTIC_f31118e3c94cc139
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
Electric Calorifier Simulation Module

This module simulates the operation of electric calorifiers, incorporating design principles
similar to those highlighted by Accutrol Systems. It models heating elements, temperature control,
energy consumption, and safety features.

Key Features:
- Multiple heating elements with individual control
- PID-based temperature control
- Energy consumption tracking
- Safety interlocks and alarms
- Simulation time stepping

Usage:
    calorifier = ElectricCalorifier(capacity=150, power_rating=3000)
    for _ in range(60):
        calorifier.update(flow_rate=10, inlet_temp=15, ambient_temp=20)
"""

import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HeatingElementState(Enum):
    """Possible states of a heating element."""
    OFF = auto()
    ON = auto()
    LOCKED_OUT = auto()


class AlarmCode(Enum):
    """Possible alarm conditions."""
    HIGH_TEMPERATURE = auto()
    LOW_WATER_LEVEL = auto()
    ELEMENT_OVERLOAD = auto()
    SENSOR_FAILURE = auto()


@dataclass
class HeatingElement:
    """Represents an individual heating element in the calorifier."""
    power_rating: float  # in watts
    state: HeatingElementState = HeatingElementState.OFF
    operational_hours: float = 0.0
    lockout_reason: Optional[AlarmCode] = None

    def activate(self) -> bool:
        """Activate the heating element if not locked out."""
        if self.state != HeatingElementState.LOCKED_OUT:
            self.state = HeatingElementState.ON
            return True
        return False

    def deactivate(self) -> None:
        """Deactivate the heating element."""
        self.state = HeatingElementState.OFF

    def lockout(self, reason: AlarmCode) -> None:
        """Lock out the heating element due to an alarm condition."""
        self.state = HeatingElementState.LOCKED_OUT
        self.lockout_reason = reason
        logger.warning(f"Heating element locked out: {reason}")

    def update_operational_time(self, delta_time: float) -> None:
        """Update the operational hours counter."""
        if self.state == HeatingElementState.ON:
            self.operational_hours += delta_time / 3600  # convert seconds to hours


class ElectricCalorifier:
    """Simulates an electric calorifier system."""

    def __init__(
        self,
        capacity: float = 150.0,  # liters
        power_rating: float = 3000.0,  # watts
        setpoint: float = 60.0,  # degrees C
        num_elements: int = 3,
        hysteresis: float = 2.0,  # degrees C
        max_temp: float = 80.0,  # degrees C
        min_water_level: float = 0.2  # 20% of capacity
    ):
        """
        Initialize the calorifier with given parameters.

        Args:
            capacity: Tank capacity in liters
            power_rating: Total power rating in watts
            setpoint: Target temperature in degrees Celsius
            num_elements: Number of heating elements
            hysteresis: Temperature hysteresis for control
            max_temp: Maximum allowable temperature
            min_water_level: Minimum water level ratio (0-1)
        """
        self.capacity = capacity
        self.setpoint = setpoint
        self.hysteresis = hysteresis
        self.max_temp = max_temp
        self.min_water_level = min_water_level
        self.current_temp = 20.0  # Starting at ambient
        self.water_level = 1.0  # Full tank
        self.energy_consumed = 0.0  # watt-hours
        self.alarms: List[AlarmCode] = []
        self.last_update_time = time.time()

        # Create heating elements
        element_power = power_rating / num_elements
        self.elements = [HeatingElement(power_rating=element_power) for _ in range(num_elements)]

    def update(self, flow_rate: float, inlet_temp: float, ambient_temp: float) -> None:
        """
        Update the calorifier state based on current conditions.

        Args:
            flow_rate: Water flow rate in liters per minute
            inlet_temp: Inlet water temperature in degrees C
            ambient_temp: Ambient temperature in degrees C
        """
        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time

        # Check for alarm conditions
        self._check_alarm_conditions()

        # Calculate heat loss to environment (simplified model)
        heat_loss = self._calculate_heat_loss(ambient_temp, delta_time)

        # Calculate heat input from elements
        heat_input = self._calculate_heat_input(delta_time)

        # Calculate temperature change from flow
        temp_change_from_flow = self._calculate_flow_effect(flow_rate, inlet_temp, delta_time)

        # Update temperature
        temp_change = (heat_input - heat_loss) / (self.capacity * 4186)  # J/kg·K for water
        self.current_temp += temp_change * delta_time + temp_change_from_flow

        # Control heating elements based on temperature
        self._control_elements()

        # Update element operational times
        for element in self.elements:
            element.update_operational_time(delta_time)

    def _calculate_heat_loss(self, ambient_temp: float, delta_time: float) -> float:
        """Calculate heat loss to environment."""
        insulation_factor = 0.05  # Simplified insulation factor
        delta_temp = self.current_temp - ambient_temp
        surface_area = 0.05 * self.capacity  # Simplified surface area estimation
        return insulation_factor * surface_area * delta_temp * delta_time

    def _calculate_heat_input(self, delta_time: float) -> float:
        """Calculate heat input from active elements."""
        total_power = sum(
            element.power_rating for element in self.elements 
            if element.state == HeatingElementState.ON
        )
        return total_power * delta_time  # joules

    def _calculate_flow_effect(self, flow_rate: float, inlet_temp: float, delta_time: float) -> float:
        """Calculate temperature change due to water flow."""
        if self.water_level <= self.min_water_level:
            return 0.0

        flow_liters = flow_rate * (delta_time / 60)  # convert to liters
        if flow_liters == 0:
            return 0.0

        # Simple mixing model
        mass_flow = flow_liters * 1.0  # 1 kg per liter
        mass_tank = self.capacity * self.water_level * 1.0  # kg

        if mass_tank <= 0:
            return 0.0

        mixed_temp = (mass_tank * self.current_temp + mass_flow * inlet_temp) / (mass_tank + mass_flow)
        temp_change = mixed_temp - self.current_temp

        # Update water level
        self.water_level = min(1.0, self.water_level + (flow_liters / self.capacity))

        return temp_change

    def _control_elements(self) -> None:
        """Control heating elements based on current temperature."""
        if self.current_temp > self.max_temp:
            # Emergency shutdown if temperature exceeds maximum
            for element in self.elements:
                element.deactivate()
            self._trigger_alarm(AlarmCode.HIGH_TEMPERATURE)
            return

        if self.water_level < self.min_water_level:
            # Shutdown if water level too low
            for element in self.elements:
                element.deactivate()
            self._trigger_alarm(AlarmCode.LOW_WATER_LEVEL)
            return

        # Normal control logic with hysteresis
        if self.current_temp < (self.setpoint - self.hysteresis / 2):
            # Need heat - activate available elements
            for element in self.elements:
                if element.state != HeatingElementState.ON:
                    element.activate()
        elif self.current_temp > (self.setpoint + self.hysteresis / 2):
            # Temperature high enough - deactivate elements
            for element in self.elements:
                element.deactivate()

    def _check_alarm_conditions(self) -> None:
        """Check for and handle alarm conditions."""
        # Check for sensor failure (simplified)
        if self.current_temp < -10 or self.current_temp > 150:
            self._trigger_alarm(AlarmCode.SENSOR_FAILURE)

        # Check for element overload (simplified)
        active_elements = sum(1 for e in self.elements if e.state == HeatingElementState.ON)
        if active_elements == len(self.elements) and self.current_temp < self.setpoint - 10:
            self._trigger_alarm(AlarmCode.ELEMENT_OVERLOAD)

    def _trigger_alarm(self, alarm_code: AlarmCode)
