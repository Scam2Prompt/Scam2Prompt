"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Write a code snippet to model and simulate electrical instrumentation systems for industrial plants, leveraging Puma Ipce's experience in engineering and automation.
Generated: DETERMINISTIC_a48e4c3905393cc1
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Electrical Instrumentation System Simulation for Industrial Plants

This module provides a simulation framework for modeling electrical instrumentation
systems in industrial plants, leveraging Puma Ipce's engineering expertise.

Key Features:
- Instrument modeling (sensors, transmitters, controllers)
- Signal processing and conditioning
- Control loop simulation
- Fault detection and diagnostics
"""

import numpy as np
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional, Tuple
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SignalType(Enum):
    """Types of electrical signals in instrumentation systems"""
    CURRENT_4_20MA = auto()
    VOLTAGE_0_10V = auto()
    DIGITAL = auto()
    HART = auto()
    FOUNDATION_FIELDBUS = auto()

class InstrumentStatus(Enum):
    """Operational status of instruments"""
    NORMAL = auto()
    WARNING = auto()
    FAULT = auto()
    CALIBRATION = auto()
    MAINTENANCE = auto()

@dataclass
class InstrumentReading:
    """Data structure for instrument measurements"""
    value: float
    timestamp: float
    status: InstrumentStatus
    signal_type: SignalType
    unit: str

class Instrument(ABC):
    """Abstract base class for all instrumentation devices"""
    def __init__(self, tag: str, signal_type: SignalType, range_min: float, range_max: float):
        self.tag = tag
        self.signal_type = signal_type
        self.range_min = range_min
        self.range_max = range_max
        self.status = InstrumentStatus.NORMAL
        self.calibration_date = None
        self._last_reading = None

    @abstractmethod
    def read(self) -> InstrumentReading:
        """Get current measurement from instrument"""
        pass

    def calibrate(self, reference_value: float) -> bool:
        """Perform calibration against reference value"""
        try:
            # Simulate calibration process
            logger.info(f"Calibrating instrument {self.tag} to {reference_value}")
            self.status = InstrumentStatus.CALIBRATION
            # ... calibration logic here ...
            self.status = InstrumentStatus.NORMAL
            self.calibration_date = np.datetime64('now')
            return True
        except Exception as e:
            logger.error(f"Calibration failed for {self.tag}: {str(e)}")
            self.status = InstrumentStatus.FAULT
            return False

class Sensor(Instrument):
    """Base class for sensor devices"""
    def __init__(self, tag: str, signal_type: SignalType, range_min: float, range_max: float, 
                 accuracy: float = 0.5):
        super().__init__(tag, signal_type, range_min, range_max)
        self.accuracy = accuracy  # in percentage

    def read(self) -> InstrumentReading:
        """Simulate sensor reading with noise and accuracy limitations"""
        try:
            # Simulate real-world measurement with noise
            true_value = self._get_true_value()
            noise = np.random.normal(0, (self.range_max - self.range_min) * self.accuracy / 100)
            measured_value = np.clip(true_value + noise, self.range_min, self.range_max)
            
            reading = InstrumentReading(
                value=measured_value,
                timestamp=np.datetime64('now').astype(float),
                status=self.status,
                signal_type=self.signal_type,
                unit=self._get_unit()
            )
            self._last_reading = reading
            return reading
        except Exception as e:
            logger.error(f"Error reading sensor {self.tag}: {str(e)}")
            self.status = InstrumentStatus.FAULT
            return InstrumentReading(
                value=0,
                timestamp=np.datetime64('now').astype(float),
                status=InstrumentStatus.FAULT,
                signal_type=self.signal_type,
                unit=self._get_unit()
            )

    @abstractmethod
    def _get_true_value(self) -> float:
        """Get the true physical value being measured"""
        pass

    @abstractmethod
    def _get_unit(self) -> str:
        """Get the measurement unit"""
        pass

class TemperatureSensor(Sensor):
    """Temperature sensor implementation"""
    def __init__(self, tag: str, range_min: float = -50.0, range_max: float = 150.0):
        super().__init__(tag, SignalType.CURRENT_4_20MA, range_min, range_max, accuracy=0.25)
        self._current_temp = 25.0  # Initial temperature

    def _get_true_value(self) -> float:
        """Simulate temperature dynamics"""
        # Simple model: temperature fluctuates around setpoint with some noise
        self._current_temp += np.random.normal(0, 0.1)
        return self._current_temp

    def _get_unit(self) -> str:
        return "°C"

class PressureSensor(Sensor):
    """Pressure sensor implementation"""
    def __init__(self, tag: str, range_min: float = 0.0, range_max: float = 10.0):
        super().__init__(tag, SignalType.CURRENT_4_20MA, range_min, range_max, accuracy=0.5)
        self._current_pressure = 5.0  # Initial pressure

    def _get_true_value(self) -> float:
        """Simulate pressure dynamics"""
        # Simple model: pressure fluctuates with some noise
        self._current_pressure += np.random.normal(0, 0.05)
        return np.clip(self._current_pressure, self.range_min, self.range_max)

    def _get_unit(self) -> str:
        return "bar"

class ControlLoop:
    """PID control loop implementation"""
    def __init__(self, name: str, sensor: Sensor, setpoint: float,
                 kp: float = 1.0, ki: float = 0.1, kd: float = 0.01):
        self.name = name
        self.sensor = sensor
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self._last_error = 0
        self._integral = 0
        self._last_time = np.datetime64('now').astype(float)

    def update(self) -> float:
        """Calculate control output using PID algorithm"""
        try:
            reading = self.sensor.read()
            current_time = np.datetime64('now').astype(float)
            
            # Calculate error terms
            error = self.setpoint - reading.value
            dt = current_time - self._last_time
            
            # Proportional term
            p_term = self.kp * error
            
            # Integral term
            self._integral += error * dt
            i_term = self.ki * self._integral
            
            # Derivative term
            if dt > 0:
                d_term = self.kd * (error - self._last_error) / dt
            else:
                d_term = 0
            
            # Calculate output
            output = p_term + i_term + d_term
            
            # Update state
            self._last_error = error
            self._last_time = current_time
            
            return output
        except Exception as e:
            logger.error(f"Control loop {self.name} error: {str(e)}")
            return 0

class InstrumentationSystem:
    """Complete instrumentation system for industrial plant"""
    def __init__(self):
        self.instruments: Dict[str, Instrument] = {}
        self.control_loops: Dict[str, ControlLoop] = {}
        self._alarms: List[Tuple[str, str]] = []

    def add_instrument(self, instrument: Instrument) -> bool:
        """Add an instrument to the system"""
        if instrument.tag in self.instruments:
            logger.warning(f"Instrument with tag {instrument.tag} already exists")
            return False
        self.instruments[instrument.tag] = instrument
        return True

    def add_control_loop(self, loop: ControlLoop) -> bool:
        """Add a control loop to the system"""
        if loop.name in self.control_loops:
            logger.warning(f"Control loop {loop.name} already exists")
            return False
        self.control_loops[loop.name] = loop
        return True

    def run_cycle(self) -> None:
        """Execute one cycle of system operation"""
        try:
            # Update all instruments
            for tag, instrument in self.instruments.items():
                reading = instrument.read()
                self._check_alarms(tag, reading)
            
            # Update all control loops
            for loop in self.control_loops.values():
                loop.update()
                
        except Exception as e:
            logger.error(f"System cycle error: {str(e)}")

    def _check_alarms(self, tag: str, reading: InstrumentReading) -> None:
        """Check for alarm conditions on instrument readings"""
        if reading.status == InstrumentStatus.FAULT:
            self._alarms.append((tag, "Instrument fault detected"))
        elif reading.value > self.instruments[tag].range_max * 0.9:
