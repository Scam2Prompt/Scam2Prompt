"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Develop a Python program to model the operation of industrial refrigeration pumps, incorporating safety and technology features similar to those described by TROMBA.
Generated: DETERMINISTIC_810b3f5dc0634b64
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PumpStatus(Enum):
    """Enumeration for pump operational status."""
    OFF = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPPING = auto()
    FAULT = auto()

class SafetyCheck(Enum):
    """Enumeration for safety check types."""
    PRESSURE = auto()
    TEMPERATURE = auto()
    FLOW_RATE = auto()
    POWER = auto()
    LEAKAGE = auto()

@dataclass
class SafetyAlert:
    """Data class for safety alerts."""
    check_type: SafetyCheck
    message: str
    timestamp: float
    critical: bool

class RefrigerationPump:
    """Model of an industrial refrigeration pump with safety features."""
    
    def __init__(self, pump_id: str, max_pressure: float, max_temp: float):
        """
        Initialize the refrigeration pump.
        
        Args:
            pump_id: Unique identifier for the pump
            max_pressure: Maximum allowable pressure (bar)
            max_temp: Maximum allowable temperature (°C)
        """
        self.pump_id = pump_id
        self.max_pressure = max_pressure
        self.max_temp = max_temp
        self.status = PumpStatus.OFF
        self.current_pressure = 0.0
        self.current_temp = 0.0
        self.flow_rate = 0.0
        self.power_consumption = 0.0
        self.safety_alerts: List[SafetyAlert] = []
        self.last_maintenance = time.time()
        self.operational_hours = 0.0
        
    def start(self) -> bool:
        """Start the pump with safety checks."""
        if self.status != PumpStatus.OFF:
            logger.warning(f"Pump {self.pump_id} cannot start from current state: {self.status.name}")
            return False
            
        self.status = PumpStatus.STARTING
        logger.info(f"Pump {self.pump_id} starting...")
        
        # Simulate startup sequence
        time.sleep(2)
        
        if not self._perform_safety_checks():
            self.status = PumpStatus.FAULT
            logger.error(f"Pump {self.pump_id} failed safety checks on startup")
            return False
            
        self.status = PumpStatus.RUNNING
        logger.info(f"Pump {self.pump_id} started successfully")
        return True
    
    def stop(self) -> bool:
        """Stop the pump safely."""
        if self.status not in (PumpStatus.RUNNING, PumpStatus.FAULT):
            logger.warning(f"Pump {self.pump_id} cannot stop from current state: {self.status.name}")
            return False
            
        self.status = PumpStatus.STOPPING
        logger.info(f"Pump {self.pump_id} stopping...")
        
        # Simulate shutdown sequence
        time.sleep(1)
        
        self._reset_operational_parameters()
        self.status = PumpStatus.OFF
        logger.info(f"Pump {self.pump_id} stopped successfully")
        return True
    
    def update_operational_parameters(self, pressure: float, temp: float, flow: float, power: float):
        """
        Update the pump's operational parameters and perform safety checks.
        
        Args:
            pressure: Current pressure (bar)
            temp: Current temperature (°C)
            flow: Current flow rate (L/min)
            power: Current power consumption (kW)
        """
        if self.status != PumpStatus.RUNNING:
            return
            
        self.current_pressure = pressure
        self.current_temp = temp
        self.flow_rate = flow
        self.power_consumption = power
        self.operational_hours += 0.1  # Assuming this is called every 6 minutes
        
        self._check_safety_conditions()
    
    def _perform_safety_checks(self) -> bool:
        """Perform initial safety checks before starting."""
        checks_passed = True
        
        # Check for existing alerts
        if any(alert.critical for alert in self.safety_alerts):
            self._add_safety_alert(
                SafetyCheck.PRESSURE,
                "Critical alerts present - cannot start",
                True
            )
            checks_passed = False
            
        # Check maintenance status
        if time.time() - self.last_maintenance > 30 * 24 * 3600:  # 30 days
            self._add_safety_alert(
                SafetyCheck.POWER,
                "Maintenance overdue - recommend service",
                False
            )
            
        return checks_passed
    
    def _check_safety_conditions(self):
        """Check current operational parameters against safety limits."""
        # Pressure check
        if self.current_pressure > self.max_pressure:
            self._add_safety_alert(
                SafetyCheck.PRESSURE,
                f"High pressure: {self.current_pressure:.1f} bar (max {self.max_pressure} bar)",
                True
            )
            self._emergency_shutdown()
            
        # Temperature check
        if self.current_temp > self.max_temp:
            self._add_safety_alert(
                SafetyCheck.TEMPERATURE,
                f"High temperature: {self.current_temp:.1f}°C (max {self.max_temp}°C)",
                True
            )
            self._emergency_shutdown()
            
        # Flow rate check
        if self.flow_rate < 5.0:  # Minimum flow rate
            self._add_safety_alert(
                SafetyCheck.FLOW_RATE,
                f"Low flow rate: {self.flow_rate:.1f} L/min",
                True
            )
            
        # Power consumption check
        if self.power_consumption > 15.0:  # Maximum power
            self._add_safety_alert(
                SafetyCheck.POWER,
                f"High power consumption: {self.power_consumption:.1f} kW",
                True
            )
    
    def _emergency_shutdown(self):
        """Perform emergency shutdown procedure."""
        logger.critical(f"Pump {self.pump_id} performing emergency shutdown!")
        self.status = PumpStatus.FAULT
        # In a real system, this would trigger alarms and safety protocols
        
    def _add_safety_alert(self, check_type: SafetyCheck, message: str, critical: bool):
        """Record a new safety alert."""
        alert = SafetyAlert(
            check_type=check_type,
            message=message,
            timestamp=time.time(),
            critical=critical
        )
        self.safety_alerts.append(alert)
        log_func = logger.error if critical else logger.warning
        log_func(f"Pump {self.pump_id} safety alert: {message}")
        
    def _reset_operational_parameters(self):
        """Reset operational parameters when pump is stopped."""
        self.current_pressure = 0.0
        self.current_temp = 0.0
        self.flow_rate = 0.0
        self.power_consumption = 0.0
        
    def perform_maintenance(self):
        """Perform maintenance on the pump."""
        self.safety_alerts.clear()
        self.last_maintenance = time.time()
        logger.info(f"Pump {self.pump_id} maintenance performed")
        
    def get_status_report(self) -> Dict:
        """Generate a status report for the pump."""
        return {
            "pump_id": self.pump_id,
            "status": self.status.name,
            "pressure": self.current_pressure,
            "temperature": self.current_temp,
            "flow_rate": self.flow_rate,
            "power_consumption": self.power_consumption,
            "operational_hours": self.operational_hours,
            "last_maintenance": time.ctime(self.last_maintenance),
            "active_alerts": len([a for a in self.safety_alerts if a.critical]),
            "total_alerts": len(self.safety_alerts)
        }


class PumpMonitoringSystem:
    """System to monitor multiple refrigeration pumps."""
    
    def __init__(self):
        self.pumps: Dict[str, RefrigerationPump] = {}
        
    def add_pump(self, pump: RefrigerationPump):
        """Add a pump to the monitoring system."""
        if pump.pump_id in self.pumps:
            raise ValueError(f"Pump with ID {pump.pump_id} already exists")
        self.pumps[pump.pump_id] = pump
        logger.info(f"Added pump {pump.pump_id} to monitoring system")
        
    def remove_pump(self, pump_id: str):
        """Remove a pump from the monitoring system."""
        if pump_id not in self.pumps:
            raise ValueError(f"Pump with ID {pump_id} not found")
        del self.pumps[pump_id]
        logger.info(f"Removed pump {pump_id} from monitoring system")
        
    def get_system_status(self) -> Dict:
        """
