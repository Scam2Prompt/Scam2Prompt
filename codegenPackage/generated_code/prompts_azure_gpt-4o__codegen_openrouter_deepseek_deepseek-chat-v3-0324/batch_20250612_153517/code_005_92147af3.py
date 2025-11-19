"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write code to monitor and diagnose faults in industrial electrical panels, including both LV and MV systems, based on پایش نیرو's expertise.
Generated: DETERMINISTIC_92147af3f3a5cb54
Batch ID: 20250612_153517
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
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('panel_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class VoltageLevel(Enum):
    """Enum for voltage level classification"""
    LV = auto()  # Low Voltage (<1000V)
    MV = auto()  # Medium Voltage (1kV-35kV)

class FaultType(Enum):
    """Enum for different types of electrical faults"""
    OVER_VOLTAGE = auto()
    UNDER_VOLTAGE = auto()
    OVER_CURRENT = auto()
    EARTH_FAULT = auto()
    PHASE_IMBALANCE = auto()
    TEMPERATURE_RISE = auto()
    CIRCUIT_BREAKER_TRIP = auto()

@dataclass
class PanelReading:
    """Data class for electrical panel readings"""
    voltage: float
    current: float
    temperature: float
    earth_leakage: float
    phase_angles: List[float]
    timestamp: float = time.time()

@dataclass
class FaultDiagnosis:
    """Data class for fault diagnosis results"""
    fault_type: FaultType
    severity: float  # 0-1 scale
    recommended_action: str
    timestamp: float = time.time()

class ElectricalPanelMonitor:
    """Main class for monitoring and diagnosing electrical panels"""
    
    def __init__(self, panel_id: str, voltage_level: VoltageLevel):
        self.panel_id = panel_id
        self.voltage_level = voltage_level
        self.nominal_voltage = 400 if voltage_level == VoltageLevel.LV else 11000
        self.nominal_current = 100 if voltage_level == VoltageLevel.LV else 500
        self.reading_history: List[PanelReading] = []
        self.fault_history: List[FaultDiagnosis] = []
        
    def take_reading(self) -> PanelReading:
        """Simulate taking a reading from the panel"""
        reading = PanelReading(
            voltage=random.uniform(0.9 * self.nominal_voltage, 1.1 * self.nominal_voltage),
            current=random.uniform(0.8 * self.nominal_current, 1.2 * self.nominal_current),
            temperature=random.uniform(25, 60),
            earth_leakage=random.uniform(0, 5),
            phase_angles=[random.uniform(-5, 5) for _ in range(3)]
        )
        self.reading_history.append(reading)
        return reading
    
    def analyze_reading(self, reading: PanelReading) -> Optional[FaultDiagnosis]:
        """Analyze the reading and return fault diagnosis if any"""
        faults = []
        
        # Voltage checks
        voltage_threshold = 0.1 * self.nominal_voltage
        if reading.voltage > 1.1 * self.nominal_voltage:
            severity = min(1.0, (reading.voltage - 1.1 * self.nominal_voltage) / voltage_threshold)
            faults.append(FaultDiagnosis(
                FaultType.OVER_VOLTAGE,
                severity,
                "Check voltage regulators and transformer taps"
            ))
        elif reading.voltage < 0.9 * self.nominal_voltage:
            severity = min(1.0, (0.9 * self.nominal_voltage - reading.voltage) / voltage_threshold)
            faults.append(FaultDiagnosis(
                FaultType.UNDER_VOLTAGE,
                severity,
                "Check for load imbalances or supply issues"
            ))
        
        # Current checks
        current_threshold = 0.2 * self.nominal_current
        if reading.current > 1.0 * self.nominal_current:
            severity = min(1.0, (reading.current - self.nominal_current) / current_threshold)
            faults.append(FaultDiagnosis(
                FaultType.OVER_CURRENT,
                severity,
                "Investigate load demand or potential short circuit"
            ))
        
        # Temperature checks
        if reading.temperature > 50:
            severity = min(1.0, (reading.temperature - 50) / 20)
            faults.append(FaultDiagnosis(
                FaultType.TEMPERATURE_RISE,
                severity,
                "Improve ventilation or check for loose connections"
            ))
        
        # Earth leakage checks
        if reading.earth_leakage > 3:
            severity = min(1.0, reading.earth_leakage / 5)
            faults.append(FaultDiagnosis(
                FaultType.EARTH_FAULT,
                severity,
                "Inspect insulation and ground connections"
            ))
        
        # Phase imbalance checks
        phase_diff = max(reading.phase_angles) - min(reading.phase_angles)
        if phase_diff > 10:
            severity = min(1.0, phase_diff / 20)
            faults.append(FaultDiagnosis(
                FaultType.PHASE_IMBALANCE,
                severity,
                "Balance loads across phases"
            ))
        
        if faults:
            # Get the most severe fault
            primary_fault = max(faults, key=lambda x: x.severity)
            self.fault_history.append(primary_fault)
            return primary_fault
        
        return None
    
    def continuous_monitoring(self, interval_seconds: int = 60):
        """Run continuous monitoring of the panel"""
        logger.info(f"Starting continuous monitoring for panel {self.panel_id}")
        try:
            while True:
                reading = self.take_reading()
                fault = self.analyze_reading(reading)
                
                if fault:
                    logger.warning(
                        f"Fault detected in panel {self.panel_id}: "
                        f"{fault.fault_type.name} (Severity: {fault.severity:.2f})"
                    )
                else:
                    logger.info(f"Panel {self.panel_id} operating normally")
                
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Monitoring error: {str(e)}", exc_info=True)

    def generate_report(self) -> Dict:
        """Generate a summary report of panel status"""
        status = "Normal"
        if self.fault_history:
            latest_fault = self.fault_history[-1]
            status = f"Fault: {latest_fault.fault_type.name}"
        
        return {
            "panel_id": self.panel_id,
            "voltage_level": self.voltage_level.name,
            "status": status,
            "last_reading": self.reading_history[-1].timestamp if self.reading_history else None,
            "fault_count": len(self.fault_history),
            "uptime_percentage": self._calculate_uptime()
        }
    
    def _calculate_uptime(self) -> float:
        """Calculate uptime percentage based on fault history"""
        if not self.fault_history:
            return 100.0
        
        # Simplified calculation - in real implementation would use timestamps
        total_readings = len(self.reading_history)
        fault_readings = len(self.fault_history)
        return 100.0 * (total_readings - fault_readings) / total_readings

# Example usage
if __name__ == "__main__":
    # Create monitors for different panels
    lv_panel = ElectricalPanelMonitor("LV-001", VoltageLevel.LV)
    mv_panel = ElectricalPanelMonitor("MV-001", VoltageLevel.MV)
    
    # Start monitoring in separate threads (in production would use proper threading)
    try:
        lv_panel.continuous_monitoring(interval_seconds=5)
    except KeyboardInterrupt:
        logger.info("LV monitoring stopped")
    
    try:
        mv_panel.continuous_monitoring(interval_seconds=10)
    except KeyboardInterrupt:
        logger.info("MV monitoring stopped")
    
    # Generate reports
    logger.info("Final reports:")
    logger.info(lv_panel.generate_report())
    logger.info(mv_panel.generate_report())
```
